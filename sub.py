
"""
Subtitle Adder
Author: Hussein Esmail
Description: This program adds a subtitle file to a movie. Note that this can only 
    be done once to a movie (the second time would override the first). 
    
Feel free to contribute to this to make it better! 

"""

import os  # Used to change directory, list the directory, and run terminal commands
import sys # Used to exit the program
import re # Used to replace spaces in file name with "\ " for the ffmpeg command. 
# If this is not done and there are spaces in the file name, ffmpeg will think they are separate arguments

def main():
    directory = input("Directory (full path): ")
    os.chdir(directory)
    dir_items = os.listdir(directory)
    for i in range(len(dir_items)):
        print(f"{i+1}: {dir_items[i]}")
    
    movie_file = re.sub(" ", "\\ ", dir_items[int(input("Movie file (num): ")) - 1])
    subtitle_file = re.sub(" ", "\\ ", dir_items[int(input("Subtitle file (num): ")) - 1])
    output_name = re.sub(" ", "\\ ", input("Output file name (including extension): "))

    ffmpeg_command = f"ffmpeg -i {movie_file} -f {subtitle_file.split('.')[-1]} -i {subtitle_file} -map 0:0 -map 0:1 -map 1:0 -c:v copy -c:a copy -c:s mov_text {output_name}"
    os.system(ffmpeg_command)
    sys.exit()
    
if __name__ == "__main__":
    main()
