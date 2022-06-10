# -*- coding: utf-8 -*-
"""
Created on Wed Jun  8 00:20:37 2022

@author: samue
"""

from PIL import Image, ImageDraw

def new_canvas(size_h, size_w, r=0, g=0, b=0):
    return Image.new(mode = "RGB", size = (size_h, size_w), color = (r, g, b))

def draw_line(img, x1, y1, x2, y2, r=255, g=255, b=255, w=0):
    draw_img = ImageDraw.Draw(img)
    shape = [(x1,y1), (x2,y2)]
    draw_img.line(shape, fill = (r,g,b), width = w)
    return img

def draw_circle(img, x1, y1, x2, y2, r=255, g=255, b=255):
    draw_img = ImageDraw.Draw(img)
    shape = (x1,y1,x2,y2)
    draw_img.ellipse(shape, fill = (r,g,b), outline = (r,g,b))
    return img
    
def draw_rectangle(img, x1, y1, x2, y2, r=255, g=255, b=255):
    draw_img = ImageDraw.Draw(img)
    shape = (x1,y1,x2,y2)
    draw_img.rectangle(shape, fill = (r,g,b), outline = (r,g,b))
    return img
    
def draw_polygon(img, x1, y1, x2, y2, x3, y3, r=255, g=255, b=255):
    draw_img = ImageDraw.Draw(img)
    shape = (x1,y1,x2,y2,x3,y3)
    draw_img.polygon(shape, fill = (r,g,b), outline = (r,g,b))
    return img
    
def rotate_canvas(im, angle, r, g, b):
    return im.rotate(angle, fillcolor=(r, g, b), expand=True)
    
def show_canvas(img):
    img.show()
    
def paste(imgor, imgpa, x, y):
    imgor.paste(imgpa, (x,y))
    
