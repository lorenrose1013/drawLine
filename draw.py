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

def draw_line_o1(screen, x0, y0, x1, y1, color):
    A = y1 - y0
    B = x0 - x1
    d = 2 * A + B
    x = x0
    y = y0
    while(x < x1):
        plot(screen, color, x, y)
        if (d > 0):
            y += 1
            d += B * 2
        x += 1
        d += A * 2
    return

def draw_line_o2(screen, x0, y0, x1, y1, color):
    A = y1 - y0
    B = x0 - x1
    d = A + B * 2
    x = x0
    y = y0
    while(y < y1):
        plot(screen, color, x, y)
        if (d < 0):
            x += 1
            d += A * 2
        y += 1
        d += B * 2
    return

def draw_line_o7(screen, x0, y0, x1, y1, color):
    #not started
    A = y1 - y0
    B = x0 - x1
    d = 2 * A + B
    x = x0
    y = y0
    while(x < x1):
        plot(screen, color, x, y)
        if (d > 0):
            y += 1
            d += B * 2
        x += 1
        d += A * 2
    return

def draw_line_o8(screen, x0, y0, x1, y1, color):
    #not started
    A = y1 - y0
    B = x0 - x1
    d = 2 * A + B
    x = x0
    y = y0
    while(x < x1):
        plot(screen, color, x, y)
        if (d > 0):
            y += 1
            d += B * 2
        x += 1
        d += A * 2
    return

        
def draw_line(screen, x0, y0, x1, y1, color):
    delta_x = x1 - x0
    delta_y = y1 - y0
    if (delta_x == 0):
        #vertical
        draw_line_o2(screen, x0, y0, x1, y1, color)
        return
    if (delta_y == 0):
        #horizontal
        draw_line_o1(screen, x0, y0, x1, y1, color)
        return
    m = delta_y / delta_x
    print m
    if (m <= 1 and m > 0):
        draw_line_o1(screen, x0, y0, x1, y1, color)
    if (m >=1):
        draw_line_o2(screen, x0, y0, x1, y1, color)
    return
