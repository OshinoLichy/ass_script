from pyonfx import *
import sys
from random import randrange


white = "f0f0f0"
cyan = "35e9ef"
purple = "c451d4"
yellow = "e29b3f"

filename = "in.ass"
if len(sys.argv) > 1:
    filename = sys.argv[1]

io = Ass(filename)
meta, styles, lines = io.get_data()

def add_color(line, l, color):
    
    #l.start_time = line.start_time
    #l.end_time = line.end_time
    #l.dur = l.end_time - l.start_time

    l.text =("{\\c&H%s&}%s") % (color, line.raw_text)

    io.write_line(l)

for line in lines:
    color_list = [white]*6 + [cyan]*5 + [purple]*3 + [yellow]*1
    add_color(line, line.copy(), color_list[randrange(15)])
io.save()

