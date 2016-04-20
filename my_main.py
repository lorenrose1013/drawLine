from display import *
from draw import *
from datetime import datetime


screen = new_screen()
color = [ 0, 255, 213 ]


new_start = datetime.now().microsecond
draw_line_rec(screen, 0, 0, 320, 540, color)
end_rec = datetime.now().microsecond
print "recursively only took %d micro seconds" % (end_rec - new_start)

color = [ 255, 0, 100 ]

start_time = datetime.now().microsecond
draw_line(screen, 0, 0, 320, 540, color)
post_dw = datetime.now().microsecond
print "dw algo took %d micro seconds" % (post_dw - start_time)






display(screen)
