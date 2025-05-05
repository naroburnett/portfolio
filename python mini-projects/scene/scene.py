import tkinter as tk
import random
import math
from tkinter.constants import RADIOBUTTON
from tkinter import *

def main():
    # The width and height of the scene window.
    width = 800
    height = 500

    # Create the Tk root object.
    root = tk.Tk()
    root.geometry(f"{width}x{height}")

    # Create a Frame object.
    frame = tk.Frame(root)
    frame.master.title("Scene")
    frame.pack(fill=tk.BOTH, expand=1)

    # Create a canvas object that will draw into the frame.
    canvas = tk.Canvas(frame)
    canvas.pack(fill=tk.BOTH, expand=1)

    # Call the draw_scene function.
    draw_scene(canvas, 0, 0, width-1, height-1)

    root.mainloop()


def draw_scene(canvas, scene_left, scene_top, scene_right, scene_bottom):
    """Draw a scene in the canvas. scene_left, scene_top,
    scene_right, and scene_bottom contain the extent in
    pixels of the region where the scene should be drawn.
    Parameters
        scene_left: left side of the region; less than scene_right
        scene_top: top of the region; less than scene_bottom
        scene_right: right side of the region
        scene_bottom: bottom of the region
    Return: nothing

    If needed, the width and height of the
    region can be calculated like this:
    scene_width = scene_right - scene_left + 1
    scene_height = scene_bottom - scene_top + 1
    """
    
    draw_grid(canvas, scene_left, scene_top, scene_right, scene_bottom, 100)
    time = draw_time_of_day(canvas)
    draw_sky(canvas, time)
    if time == 'night':
        draw_stars(canvas)
    else:
        draw_clouds(canvas)
    draw_ocean_line(canvas, time)
    draw_land(canvas)
    draw_behind_leaves(canvas)
    draw_main_trunk(canvas)
    draw_branches(canvas)
    draw_swing(canvas)
    draw_leaves(canvas)
     
def draw_grid(canvas, left, top, right, bottom, grid_spacing ):
    text_horizontal_margin = 10
    text_vertical_margin = 10

   #Draw Horizontal line
    for i in range(top, bottom, grid_spacing):
        canvas.create_line(left, i, right, i)
        canvas.create_text(left + text_horizontal_margin, i + text_vertical_margin, text=f"{i}")
    #draw Vertical line
    for i in range(left, right, grid_spacing):
        canvas.create_line(i, top, i, bottom)
        canvas.create_text(i, top + text_vertical_margin, text=f"{i}")

def draw_time_of_day(canvas):
    time_clock = ['day', 'night', 'day']
    time = random.choice(time_clock)
    print(time)
    return time


def draw_ocean_line(canvas, time):
    if time == 'night':
        ocean_color = "steelblue4"
    else: 
        ocean_color = "steelblue1"
    canvas.create_polygon(1, 363, 67, 361, 175, 360, 408,
     360, 538, 361, 665, 360, 800, 363, 800, 500, 1, 500,
      fill=ocean_color) 

def draw_land(canvas):
    canvas.create_polygon(1,484,44,478,119,459,195,447,268,431,
    337,417,385,408,423,400,470,391,520,391,563,396,607,404,661,
    412,719,427,765,438,791,437,800,438,800,500,0,500,fill="green")

def draw_clouds(canvas):
    i = 0
    for i in range (random.randrange(10, 25)):
        scale = random.randrange(1,10)
        x1 = random.randrange(0,800)
        x2 = (x1 + 35) + (12 * scale)
        y1 =random.randrange(0,284)
        y2 = y1 + (10 * scale)
        canvas.create_oval(x1,y1,x2,y2,fill="white", outline='')

def draw_stars(canvas):
    star_color = ['yellow', 'ivory']
    for i in range (random.randrange(300,500)):
        x = random.randrange(0,800)
        y = random.randrange(0,284)
        b2 = random.randrange(1,4)
        c = x + b2
        d = y + b2
        
        canvas.create_oval(x,y,c,d,fill=random.choice(star_color), outline='')

def draw_behind_leaves(canvas):
    color_list_leafs = ['darkgreen','darkolivegreen1','forestgreen','chartreuse4','olivedrab1']
    i = 0 
    for i in range (3000):
        a = random.randrange(375,625)
        b = random.randrange(61,166)
        b2 = random.randrange(1,8)
        c = a + b2
        d = b + b2
        canvas.create_oval(a,b,c,d,fill=random.choices(color_list_leafs))

def draw_main_trunk(canvas):
    canvas.create_polygon(412,404,432,390,455,374,476,353,502,321,525,
    278,528,247,531,216,516,188,495,174,481,152,463,129,452,109,470,101,
    484,122,510,147,533,168,548,180,564,183,576,181,578,168,584,154,583,
    134,580,121,592,115,604,123,617,107,631,111,647,123,656,137,663,150,
    647,179,636,200,624,232,616,254,606,297,597,322,587,349,578,378,562,
    393,537,400,520,404,502,408,485,411,467,409,450,401,434,405,418,408,
     fill="burlywood4")
def draw_branches(canvas):
    canvas.create_polygon(463,129,453,133,438,136,424,145,408,156,388,162,370,
    160,347,156,336,146,334,137,343,136,351,143,368,148,386,149,404,143,418,135,
    431,125,415,118,399,110,389,117,380,122,381,112,385,105,388,98,396,94,408,98,421,
    103,438,108,453,109,471,101,480,102,495,96,512,87,530,83,543,85,556,88,591,114,604,
    124,629,131,671,140,691,138,753,127,750,126,763,122,784,116,800,133,800,123,774,136,
    788,138,800,150,782,154,762,150,742,149,687,163,665,171,647,179,625,173,605,159,590,
    145,582,133,568,117,550,107,539,102,526,102,512,105,500,114,483,122,463,128,453,132,
     fill='burlywood4')
    canvas.create_polygon(457,123,450,112,444,101,437,90,430,85,426,73,436,68,447,75,
    460,89,476,115, fill='burlywood4')
def draw_swing(canvas):
    canvas.create_line(334,150,331,375)
    canvas.create_line(381,154,380,367)
    canvas.create_line(331,375,327,386)
    canvas.create_line(331,375,336,388)
    canvas.create_line(380,367,378,385)
    canvas.create_line(380,367,386,384)
    canvas.create_rectangle(325,386,387,385)
def draw_leaves(canvas):
    color_list_leafs = ['darkgreen','darkolivegreen1','forestgreen','chartreuse4','olivedrab1']
    #1
    i = 0 
    for i in range (1000):
        a = random.randrange(204,289)
        b = random.randrange(195,219)
        b2 = random.randrange(1,8)
        c = a + b2
        d = b + b2
        canvas.create_oval(a,b,c,d,fill=random.choices(color_list_leafs))
    #2    
    i = 0 
    for i in range (1000):
        a = random.randrange(173,284)
        b = random.randrange(166,202)
        b2 = random.randrange(1,8)
        c = a + b2
        d = b + b2
        canvas.create_oval(a,b,c,d,fill=random.choices(color_list_leafs))
    #3
    i = 0 
    for i in range (1000):
        a = random.randrange(141,300)
        b = random.randrange(154,174)
        b2 = random.randrange(1,8)
        c = a + b2
        d = b + b2
        canvas.create_oval(a,b,c,d,fill=random.choices(color_list_leafs))
    #4
    i = 0 
    for i in range (1000):
        a = random.randrange(175,343)
        b = random.randrange(134,161)
        b2 = random.randrange(1,8)
        c = a + b2
        d = b + b2
        canvas.create_oval(a,b,c,d,fill=random.choices(color_list_leafs))
    #5
    i = 0 
    for i in range (1000):
        a = random.randrange(181,366)
        b = random.randrange(107,141)
        b2 = random.randrange(1,8)
        c = a + b2
        d = b + b2
        canvas.create_oval(a,b,c,d,fill=random.choices(color_list_leafs))
    #6
    i = 0 
    for i in range (1000):
        a = random.randrange(239,395)
        b = random.randrange(68,116)
        b2 = random.randrange(1,8)
        c = a + b2
        d = b + b2
        canvas.create_oval(a,b,c,d,fill=random.choices(color_list_leafs))
    #7
    i = 0 
    for i in range (1000):
        a = random.randrange(244,438)
        b = random.randrange(21,77)
        b2 = random.randrange(1,8)
        c = a + b2
        d = b + b2
        canvas.create_oval(a,b,c,d,fill=random.choices(color_list_leafs))
    #8
    i = 0 
    for i in range (3000):
        a = random.randrange(244,800)
        b = random.randrange(0,47)
        b2 = random.randrange(1,8)
        c = a + b2
        d = b + b2
        canvas.create_oval(a,b,c,d,fill=random.choices(color_list_leafs))
    #9
    i = 0 
    for i in range (1500):
        a = random.randrange(468,797)
        b = random.randrange(36,85)
        b2 = random.randrange(1,8)
        c = a + b2
        d = b + b2
        canvas.create_oval(a,b,c,d,fill=random.choices(color_list_leafs))
    #10
    i = 0 
    for i in range (1500):
        a = random.randrange(556,631)
        b = random.randrange(76,116)
        b2 = random.randrange(1,8)
        c = a + b2
        d = b + b2
        canvas.create_oval(a,b,c,d,fill=random.choices(color_list_leafs))
    
    i = 0 
    for i in range (1500):
        a = random.randrange(623,739)
        b = random.randrange(99,183)
        b2 = random.randrange(1,8)
        c = a + b2
        d = b + b2
        canvas.create_oval(a,b,c,d,fill=random.choices(color_list_leafs))

    i = 0 
    for i in range (500):
        a = random.randrange(631,795)
        b = random.randrange(75,116)
        b2 = random.randrange(1,8)
        c = a + b2
        d = b + b2
        canvas.create_oval(a,b,c,d,fill=random.choices(color_list_leafs))

    i = 0 
    for i in range (750):
        a = random.randrange(725,764)
        b = random.randrange(147,216)
        b2 = random.randrange(1,8)
        c = a + b2
        d = b + b2
        canvas.create_oval(a,b,c,d,fill=random.choices(color_list_leafs))
    
    i = 0 
    for i in range (750):
        a = random.randrange(683,752)
        b = random.randrange(171,261)
        b2 = random.randrange(1,8)
        c = a + b2
        d = b + b2
        canvas.create_oval(a,b,c,d,fill=random.choices(color_list_leafs))
    
    i = 0 
    for i in range (725):
        a = random.randrange(579,667)
        b = random.randrange(168,214)
        b2 = random.randrange(1,8)
        c = a + b2
        d = b + b2
        canvas.create_oval(a,b,c,d,fill=random.choices(color_list_leafs))

    i = 0 
    for i in range (725):
        a = random.randrange(548,597)
        b = random.randrange(190,229)
        b2 = random.randrange(1,8)
        c = a + b2
        d = b + b2
        canvas.create_oval(a,b,c,d,fill=random.choices(color_list_leafs))

    i = 0 
    for i in range (250):
        a = random.randrange(403,441)
        b = random.randrange(155,202)
        b2 = random.randrange(1,8)
        c = a + b2
        d = b + b2
        canvas.create_oval(a,b,c,d,fill=random.choices(color_list_leafs))
    
    i = 0 
    for i in range (250):
        a = random.randrange(435,467)
        b = random.randrange(139,183)
        b2 = random.randrange(1,8)
        c = a + b2
        d = b + b2
        canvas.create_oval(a,b,c,d,fill=random.choices(color_list_leafs))
    
    i = 0 
    for i in range (250):
        a = random.randrange(461,490)
        b = random.randrange(159,195)
        b2 = random.randrange(1,8)
        c = a + b2
        d = b + b2
        canvas.create_oval(a,b,c,d,fill=random.choices(color_list_leafs))
    i = 0 
    for i in range (1000):
        a = random.randrange(375,625)
        b = random.randrange(61,166)
        b2 = random.randrange(3,7)
        c = a + b2
        d = b + b2
        canvas.create_oval(a,b,c,d,fill=random.choices(color_list_leafs))
def draw_sky(canvas, time):
    if time == 'night':
        sky_color = "midnightblue"
    else: 
        sky_color = "skyblue3"
    canvas.create_rectangle(1,1,800,400, fill=sky_color)

# Call the main function so that
# this program will start executing.
main()