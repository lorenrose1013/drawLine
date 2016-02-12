from display import *


def draw_line_rec( screen, x0, y0, x1, y1, color ):
    if ( abs(x0-x1) < 2 and abs(y0-y1) < 2) :
        plot(screen, color, x0, y0)
        return
    mid_x = (x0 + x1) / 2
    mid_y = (y0 + y1) / 2
    draw_line_rec(screen, x0, y0, mid_x, mid_y, color)
    draw_line_rec(screen, mid_x, mid_y, x1, y1, color)
    return

