from pyonfx import *

io = Ass("in.ass")
meta, styles, lines = io.get_data()


def dup_rota(line, l):
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

for line in lines:
	if line.layer == 1:
		dup_rota(line, line.copy())

io.save()
io.open_aegisub()
