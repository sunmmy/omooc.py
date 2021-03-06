# a borad with memory

import simplegui
import math

# global variables
canvas_width = 600
canvas_height = 400
draw_list = []
draw_color = 'red'
draw_shape = 'circle'
draw_radius = 15

def click_circle():
    global draw_shape 
    draw_shape = 'circle'
    
def click_triangle():
    global draw_shape
    draw_shape = 'triangle'
    
def click_square():
    global draw_shape
    draw_shape = 'square'
    
def click_red():
    global draw_color
    draw_color = 'red'
    
def click_green():
    global draw_green 
    draw_color = 'green'
        
def click_blue():
    global draw_blue
    draw_color = 'blue'

def click(pos):
    global draw_list, draw_color, draw_shape
    x = pos[0]
    y = pos[1]
    
    if draw_shape == 'circle':
        pos = [x, y]
    elif draw_shape == "triangle":
        pos = [[x,y], [x+26, y], [x+13, y+13*math.sqrt(3)]]
    else:
        pos = [[x,y], [x+20, y], [x+20, y+20],[x, y+20]]              
    
def draw(canvas):
    for draw_pos in draw_list:
        if draw_pos[1] == 'circle':
            canvas.draw_circle(draw_pos[0],draw_radius, 1, 'black',draw_pos[2])
        else:
            canvas.draw_polygon(draw_pos[0], 1, 'black',draw_pos[2])
    
frame = simplegui.create_frame('drawing for fun', canvas_width, canvas_height)   
frame.set_canvas_background('white')
 
button_circle = frame.add_button('circle',click_circle, 100)
button_triangle = frame.add_button('triangle',click_triangle, 100)
button_square = frame.add_button('square',click_square, 100)
button_red = frame.add_button('red',click_red, 100)
button_green = frame.add_button('green',click_green, 100)
button_blue = frame.add_button('blue',click_blue, 100)

frame.set_mouseclick_handler(click)
frame.set_draw_handler(draw)

frame.start()
    

