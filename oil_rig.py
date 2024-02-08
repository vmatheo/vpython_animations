from ocean import *
from OilRig import *
from rocks import *
import matplotlib.pyplot as plt
import random
from vpython import *

seafloor_width = 200
class Rocks:
    rock1 = ellipsoid(pos=vector(seafloor_width/6, 4, -seafloor_width/6),
                      width=23,
                      height=20,
                      length=30,
                      color=vector(0.55, 0.57, 0.67))
    rock_bit1 = ellipsoid(pos=vector(seafloor_width/6, 2, -seafloor_width/6),
                          width=23,
                          height=20,
                          length=30,
                          axis=vector(0, 0, 1),
                          color=vector(0.55, 0.57, 0.67))
    rock2 = ellipsoid(pos=vector(seafloor_width/3, 4, seafloor_width/3),
                      width=23,
                      height=20,
                      length=30,
                      axis=vector(0, 0, 1),
                      color=vector(0.55, 0.57, 0.67))
    rock_bit2 = ellipsoid(pos=vector(seafloor_width/3, 2, seafloor_width/3),
                          width=23,
                          height=20,
                          length=30,
                          axis=vector(1, 0, 0),
                          color=vector(0.55, 0.57, 0.67))
    rock3 = ellipsoid(pos=vector(-seafloor_width/4, 4, 0),
                      width=23,
                      height=20,
                      length=30,
                      axis=vector(0, 0, 1),
                      color=vector(0.55, 0.57, 0.67))
    rock_bit3 = ellipsoid(pos=vector(-seafloor_width/4, 2, 0),
                          width=23,
                          height=20,
                          length=30,
                          axis=vector(1, 0, 0),
                          color=vector(0.55, 0.57, 0.67))

run = 0



class OilRig:
    def __init__(self, rig_width, water_column_height):
        self.rig_width = rig_width
        self.water_column_height = water_column_height
        rig_platform_width = self.rig_width
        rig_platform_length = rig_platform_width
        rig_platform_height = rig_platform_width * 0.1
        rig_platform_color = vector(0.52, 0.52, 0.51)

        rig_buoy_color = vector(0.8, 0, 0)

        rig_structure_color = vector(0.33, 0.41, 0.47)
        rig_structure_height = 10

        rig_platform = box(width=rig_platform_width,
                           length=rig_platform_length,
                           height=rig_platform_height,
                           pos=vector(0, self.water_column_height, 0),
                           color=rig_platform_color)
        rig_structure_body = box(color=rig_structure_color,
                                 pos=vector(0, self.water_column_height+rig_structure_height/2, 0),
                                 height=rig_structure_height)
        rig_structure_leg1 = box(color=rig_structure_color,
                                 height=rig_structure_height,
                                 pos=vector(rig_platform_width / 4, self.water_column_height+(rig_structure_height / 2) - 0.5,
                                            rig_platform_width / 4))
        rig_structure_leg2 = box(color=rig_structure_color,
                                 height=rig_structure_height,
                                 pos=vector(-rig_platform_width / 4, self.water_column_height+(rig_structure_height / 2) - 0.5,
                                            rig_platform_width / 4))
        rig_structure_leg3 = box(color=rig_structure_color,
                                 height=rig_structure_height,
                                 pos=vector(rig_platform_width / 4, self.water_column_height+(rig_structure_height / 2) - 0.5,
                                            -rig_platform_width / 4))
        rig_structure_leg4 = box(color=rig_structure_color,
                                 height=rig_structure_height,
                                 pos=vector(-rig_platform_width / 4, self.water_column_height+(rig_structure_height / 2) - 0.5,
                                            -rig_platform_width / 4))
        rig_structure_roof = box(pos=vector(0, self.water_column_height + rig_structure_height, 0),
                                 color=vector(0.33, 0.41, 0.47),
                                 width=rig_platform_width / 2 + 2,
                                 height=rig_platform_height / 2,
                                 length=rig_platform_width / 2 + 2)
        rig_platform_leg1 = box(
            pos=vector((rig_platform_length / 2 - 0.5), self.water_column_height-(rig_structure_height/2), (rig_platform_length / 2 - 0.5)),
            color=rig_platform_color,
            height=rig_structure_height)
        rig_platform_leg2 = box(
            pos=vector(-(rig_platform_length / 2 - 0.5), self.water_column_height-(rig_structure_height/2), (rig_platform_length / 2 - 0.5)),
            color=rig_platform_color,
            height=rig_structure_height)
        rig_platform_leg3 = box(
            pos=vector((rig_platform_length / 2 - 0.5), self.water_column_height-(rig_structure_height/2), -(rig_platform_length / 2 - 0.5)),
            color=rig_platform_color,
            height=rig_structure_height)
        rig_platform_leg4 = box(
            pos=vector(-(rig_platform_length / 2 - 0.5), self.water_column_height-(rig_structure_height/2), -(rig_platform_length / 2 - 0.5)),
            color=rig_platform_color,
            height=rig_structure_height)
        rig_platform_buoy1 = cylinder(color=rig_buoy_color,
                                      length=rig_platform_width + 1,
                                      radius=1.5,
                                      pos=vector(-(rig_platform_length/2+0.5), self.water_column_height-rig_structure_height,
                                                 -(rig_platform_length / 2 - 0.5)))
        rig_platform_buoy2 = cylinder(color=rig_buoy_color,
                                      length=rig_platform_width + 1,
                                      radius=1.5,
                                      pos=vector(-(rig_platform_length/2+0.5), self.water_column_height-rig_structure_height,
                                                 (rig_platform_length / 2 - 0.5)))
from vpython import *


class Ocean:

    def __init__(self, seafloor_width=0, water_column_height=0):
        self.seafloor_width = seafloor_width
        self.water_column_height = water_column_height
        ocean_floor_color = vector(1.00, 0.90, 0.70)
        ocean_floor_width = self.seafloor_width
        ocean_floor_length = ocean_floor_width
        ocean_floor_height = ocean_floor_width/15
        ocean_floor_x = 0
        ocean_floor_y = 0
        ocean_floor_z = 0
        ocean_floor_pos = vector(ocean_floor_x, ocean_floor_y, ocean_floor_z)

        ocean_water_color = vector(0.30, 0.76, 1.00)
        ocean_water_width = ocean_floor_width
        ocean_water_length = ocean_floor_length
        ocean_water_height = self.water_column_height
        ocean_water_pos = vector(ocean_floor_x, ocean_floor_y + ocean_water_height/2, ocean_floor_z)
        ocean_water_opacity = 0.2

        ocean_floor = box(width=ocean_floor_width,
                          length=ocean_floor_length,
                          height=ocean_floor_height,
                          pos=ocean_floor_pos,
                          color=ocean_floor_color)
        ocean_water = box(width=ocean_water_width,
                          length=ocean_water_length,
                          height=ocean_water_height,
                          pos=ocean_water_pos,
                          color=ocean_water_color,
                          opacity=ocean_water_opacity)

def createPlot():
    hours = [1, 2, 3, 4, 5, 6]
    mm_barrels = [random.randint(1, 16+1) for _ in range(6)]
    plt.plot(hours, mm_barrels, color="red")
    plt.title("Millions of Barrels of Oil Recovered per hour")
    plt.xlabel("Hours")
    plt.ylabel("Barrels (in millions)")
    plt.show()



def Run(x):
    global run
    if x.checked:
        run = 1
    if not x.checked:
        run = 0

scene.width = 1200
scene.height = 800
seafloor_width = 200
water_column_height = 75
rig_width = 20

Ocean = Ocean(seafloor_width, water_column_height)
Rig = OilRig(rig_width, water_column_height+4)

wtext(text="An oil rig floating on an ocean")
scene.append_to_caption("   ")
radio(bind=Run, text="Drill for Oil")
scene.append_to_caption("     ")
button = button(bind=createPlot, text="Check Reserves")

rig_pipe_length = 3
rig_pipe_color = vector(0.12, 0.15, 0.16)
pipe = box(color=rig_pipe_color,
           height=rig_pipe_length,
           pos=vector(0, water_column_height*1.05, 0))
pipe_delta_y = 1
rocks = Rocks()
oil = ellipsoid(color=color.black,
                pos=vector(0, 3, 0),
                height=10,
                width=25,
                length=20)
oil_increment = 1

while True:
    rate(10)
    new_length = (pipe.height + pipe_delta_y)*run
    pipe.height = new_length
    pipe.pos = vector(0, water_column_height*1.04-new_length/2, 0)
    if new_length == water_column_height:
        pipe_delta_y = 0

        new_oil_width = oil.width - oil_increment
        oil.width = new_oil_width

        new_oil_length = oil.length - oil_increment
        oil.length = new_oil_length
    if oil.width <= 0 and oil.length <= 0:
        oil_increment = 0
    pass


