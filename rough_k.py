from pyonfx import *
import math
import sys

filename = "in.ass"
if len(sys.argv) > 1:
    filename = sys.argv[1]

io = Ass(filename)
meta, styles, lines = io.get_data()


def rough_k(line, l):
    cs = Utils.all_non_empty(line.chars)

    ktime = 0
    if len(cs) > 0:
        ktime = (line.end_time-line.start_time)/len(cs)
        ktime = math.floor(ktime/10)

    l.start_time = line.start_time - line.leadin / 2
    l.end_time = line.end_time + line.leadout /2
    l.dur = l.end_time - l.start_time

    text_ked = []
    for i in range(len(cs)):
        text_ked.append("{\\K%d}" % (ktime) + cs[i].text)

    l.text = "".join(text_ked)
    io.write_line(l)

for line in lines:
    rough_k(line, line.copy())

io.save()
io.open_aegisub()
