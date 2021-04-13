# -*- encoding: utf-8 -*-
from manim_imports_ext import *

import os
import subprocess


if __name__ == "__main__":
    dir = "videos"

    videos = ["SegmentTreeDiffScene", "SegmentTreeWhatIs", "SegmentTreeBuild", "SegmentTreeUpdate", "SegmentTreeQuery"]
    bg = "E:/Sources/acm-clan/audio/bg003.mp3"

    for k in videos:
        subprocess.call(['python3', '-m', 'manimlib', 'segmenttree.py', k, '-w'])

    os.chdir(dir)
    file_content = "\n".join(["file '"+k+".mp4'" for k in videos])

    with open("filelist.txt", "w") as text_file:
        text_file.write(file_content)
    
    subprocess.call(['ffmpeg', '-y', '-f', 'concat', '-i', 'filelist.txt', '-c', 'copy', 'output.mp4'])
    subprocess.call(['ffmpeg', '-y', '-i', 'output.mp4', '-stream_loop', '-1', '-i', bg, '-shortest', '-c:v', 'copy', '-c:a', 'aac', 'segment.mp4'])

    os.remove("output.mp4")
    os.remove("filelist.txt")

    print("merge ok.")
