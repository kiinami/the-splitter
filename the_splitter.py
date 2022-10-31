"""
the_splitter.py

Package 

Author:
    kinami

Created:
    4/4/22
"""
import itertools

from pydub import AudioSegment
from pydub.silence import detect_silence
import click
import os
from alive_progress import alive_it


# Opens the fp and parses the content in this format: HH:MM Title, storing it into a list of tuples
def parse_file(file):
    with open(file, 'r') as f:
        lines = f.readlines()
        res = []
        un = 1
        for line in lines:
            ml = line.split(' ')[0].split(':')
            if len(ml) == 2:
                ml = int(ml[0]) * 60 * 1000 + int(ml[1]) * 1000
            else:
                ml = int(ml[0]) * 60 * 60 * 1000 + int(ml[1]) * 60 * 1000 + int(ml[2]) * 1000
            title = ' '.join(line.split(' ')[1:]).removesuffix('\n')
            if not title:
                title = f'Untitled Track {un}'
                un += 1
            res.append((ml, title))
    return res


def accurate_timestamps(timestamps, sound):
    for ml, title in timestamps:
        split = sound[ml - 500:ml + 500]
        silences = detect_silence(split, min_silence_len=100, silence_thresh=-50)
        if len(silences) == 0:
            continue
        else:
            timestamps[timestamps.index((ml, title))] = (ml - 500 + (silences[0][0] + silences[0][1])/2, title)
    return timestamps


@click.command()
@click.option('--file', '-f', help='The timestamp file to parse', required=True, type=click.Path(exists=True, dir_okay=False))
@click.option('--input', '-i', help='The input file', required=True, type=click.Path(exists=True, dir_okay=False))
@click.option('--output', '-o', help='The output folder', required=True, type=click.Path(file_okay=False))
def main(file, input, output):
    # Parse the file
    titles = parse_file(file)
    # Open the audio file
    sound = AudioSegment.from_wav(input)

    titles = accurate_timestamps(titles, sound)

    a, b = itertools.tee([t[0] for t in titles])
    next(b, None)
    timestamps = zip(a, b)

    os.mkdir(output) if not os.path.exists(output) else None

    for i, t in alive_it(list(enumerate(timestamps))):
        audio = sound[t[0]:t[1]]
        audio.export(f'{output}/{i + 1:03}. {titles[i][1]}.mp3', format='mp3')


if __name__ == '__main__':
    main()
