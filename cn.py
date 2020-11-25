from pyonfx import *
import sys
filename = "in.ass"
if len(sys.argv) > 1:
    filename = sys.argv[1]

io = Ass(filename)
meta, styles, lines = io.get_data()


def cn(line, l):
    for char in Utils.all_non_empty(line.chars):
        # Leadin Effect
        l.layer = 0

        l.start_time = line.start_time + char.start_time/3.5
        l.end_time = line.end_time
        l.dur = l.end_time - l.start_time

        l.text =(
            "{\\an5\\pos(%.3f,%.3f)"
            "\org(%.3f,%.3f)\\frz180\\alpha&FF&\\t(0,%d,1.5,\\frz0\\alpha&00&)} %s"
            % (
                char.center * 2/3 + line.center/3,
                char.middle * 2/3 + line.center/3,
				char.center * 2/3 + line.center/3,
                char.middle * 2/3 + line.center/3,
                200,
                char.text,
            )
        )

        io.write_line(l)

def jp(line, l):
    for char in Utils.all_non_empty(line.chars):
        # Leadin Effect
        l.layer = 1

        l.start_time = line.start_time + char.start_time
        l.end_time = line.end_time
        l.dur = l.end_time - l.start_time

        l.text =(
            "{\\an5\\pos(%.3f,%.3f)"
            "\\fscx300\\fscy300\\alpha&FF&\\3a\\t(0,%d,\\fscx100\\fscy100\\alpha&00&)} %s"
            % (
                char.center * 7/8 + line.center* 1/8,
                char.middle * 7/8 + line.center* 1/8 - 100,
                char.duration,
                char.text,
            )
        )

        io.write_line(l)

        l_border = l.copy()
        l_border.layer = 0
        l_border.start_time = line.start_time + char.start_time
        l_border.end_time = line.end_time
        l_border.dur = l_border.end_time - l_border.start_time
        #白色border渐入缩小
        l_border.text =(
            "{\\an5\\pos(%.3f,%.3f)"
            "\\3c&FFFFFF&\\1a&FF&\\4a&FF&\\3a&40&\\fscx700\\fscy700\\t(0,%d,\\fscx100\\fscy100)} %s"
		    % (
                char.center * 7/8 + line.center* 1/8,
                char.middle * 7/8 + line.center* 1/8 - 100,
                char.duration,
                char.text,
            )
		)
        io.write_line(l_border)



for line in lines:
	if line.styleref.alignment <= 3:
		cn(line,line.copy())
	elif line.styleref.alignment >= 7:
		jp(line,line.copy())
io.save()
io.open_aegisub()
