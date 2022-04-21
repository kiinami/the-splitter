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


if __name__ == '__main__':
    # Parse the file
    titles = parse_file('timestamps.txt')
    # Open the audio file
    sound = AudioSegment.from_mp3("audio.mp3")

    a, b = itertools.tee([t[0] for t in titles])
    next(b, None)
    timestamps = zip(a, b)

    for i, t in enumerate(timestamps):
        audio = sound[t[0]:t[1]]
        audio.export(f'output/{i + 1:03}. {titles[i][1]}.mp3', format='mp3')

