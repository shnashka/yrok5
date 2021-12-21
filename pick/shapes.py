# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = (700, 700)




def figure(start, angle, length):
    side = sd.get_vector(start_point=start, angle=angle, length=length, width=1)
    side.draw()
    return side.end_point


def triangle_2(_point, _angle, _len):
    next_point = _point
    for i in range(3):
        next_point = figure(start=next_point, angle=_angle + 360 / 3 * i, length=_len)




def square_2(_point, _angle, _len):
    next_point = _point
    for i in range(4):
        next_point = figure(start=next_point, angle=_angle + 360 / 4 * i, length=_len)





def pentagon_2(_point, _angle, _len):
    next_point = _point
    for i in range(5):
        next_point = figure(start=next_point, angle=_angle + 360 / 5 * i, length=_len)



def octagon_2(_point, _angle, _len):
    next_point = _point
    for i in range(6):
        next_point = figure(start=next_point, angle=_angle + 360 / 6 * i, length=_len)




# def tr_2(_point, _angle, _len):
#     next_point = _point
#     for i in range(3):
#         next_point = figure(next_point, _angle + 360 / 3 * i,_len)
#
#
# point_0 = sd.get_point(500, 400)
# tr_2(point_0, 0, 80)

#sd.pause()
