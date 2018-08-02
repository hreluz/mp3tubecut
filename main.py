#!/usr/bin/python

import sys
import subprocess

def download(url):
	basic_command = "youtube-dl --extract-audio --audio-format mp3"
	commands = [x.strip() for x in basic_command.split()]
	commands.append(url)
	subprocess.call(commands)
	
	print("Done!")


download(sys.argv[1])	