# The Splitter

Small utility script to split a long MP3 into smaller ones following a timestamp txt file.

## Requirements

1. Python installed on your system.
2. Required Python libraries: pydub, click, os, alive_progress.
3. The audio file you want to split must be in WAV format. You can use ffmpeg to convert your audio file to WAV format. For example, if your audio file is in MP3 format, you can convert it to WAV format with the following command:

   ```
   ffmpeg -i your_audio_file.mp3 your_audio_file.wav
   ```

   Replace `your_audio_file.mp3` with the path to your audio file.

## How to use

1. **Install Required Libraries:**
   Before using the script, you need to install the required Python libraries. You can install them using pip:

   ```
   pip install -r requirements.txt
   ```

2. **Prepare Your Timestamp File:**
   Create a timestamp file that specifies when you want to split the audio. The timestamp file should have the following format:

   ```
   HH:MM:SS Title
   ```

   - `HH` represents hours (optional).
   - `MM` represents minutes.
   - `SS` represents seconds.
   - `Title` is the title for that segment (optional). If not provided, it will use a default title.

   Example timestamp file:

   ```
   00:00 Introduction
   05:30 Main Content
   15:45 Conclusion
   ```

3. **Run the Script:**
   Open a terminal or command prompt and navigate to the directory where "the_splitter.py" is located. Then, run the script with the following command:

   ```
   python the_splitter.py --file your_timestamp_file.txt --input your_audio_file.wav --output output_folder
   ```

   - `--file`: Specify the path to your timestamp file.
   - `--input`: Specify the path to your input audio file (in WAV format).
   - `--output`: Specify the output folder where the segmented audio files will be saved.

   Replace `your_timestamp_file.txt`, `your_audio_file.wav`, and `output_folder` with your actual file paths and desired output folder.

4. **Execution:**
   The script will process the audio file according to the timestamps in your timestamp file. It will split the audio into segments and save them as MP3 files in the specified output folder. Each segment will be named with a numerical prefix and the title you provided (or a default title if none was provided).

5. **Monitor Progress:**
   You will see a progress bar indicating the script's progress during execution.

6. **Completion:**
   Once the script has finished running, you will find the segmented audio files in the specified output folder.

That's it! You can now use this script to split audio files based on timestamps provided in your timestamp file.
