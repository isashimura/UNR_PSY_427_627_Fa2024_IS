# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 14:01:35 2024

@author: isash
"""

#%% libraries

import random
from psychopy import visual, core
import os

#%% access file

fdir = r'C:\Users\isash\OneDrive - University of Nevada, Reno\Fall 2024\PSY 427 Comp App\fLoc_stimuli\fLoc_stimuli'
floc = os.listdir(fdir)

#%% sort files

child_adult = [os.path.join(fdir, f) for f in floc if 'adult' in f or 'child' in f]
house_corr = [os.path.join(fdir, f) for f in floc if 'house' in f or 'corridor' in f]
instrum_car = [os.path.join(fdir, f) for f in floc if 'instrument' in f or 'car' in f]

#%% create disp

screen_size = [600,400]
win = visual.Window(size=screen_size, 
                    color=(0.5,0.5,0.5),
                    fullscr=False, 
                    units='pix')

#%% time stuff

block_time = 20
img_time = 1
gap_time = .25

n_img_in_block = int(block_time / (img_time + gap_time))

#%%  crosshair

center = visual.ShapeStim(win, vertices = [[-0.1, 0], [0.1, 0], [0, 0], [0, -0.1], [0, 0], [0, 0.1]], lineWidth = 5, closeShape = False)


#%% disp faces L

random.shuffle(child_adult)
for i in range(min(n_img_in_block, len(child_adult))):
    img = visual.ImageStim(win, image = child_adult[i], units = 'pix', pos = (-150, 0.0), size = (200,200))
    img.draw()
    center.draw()
    win.flip()  
    core.wait(img_time)  
    win.flip()
    core.wait(gap_time)
    
core.wait(3)

#end face

#%% disp place L 

random.shuffle(house_corr)
for i in range(min(n_img_in_block, len(house_corr))):
    img = visual.ImageStim(win, image = house_corr[i], units = 'pix', pos = (-150, 0.0), size = (200,200))
    img.draw()
    center.draw()
    win.flip()  
    core.wait(img_time)  
    win.flip()
    core.wait(gap_time)
    
core.wait(3)

#end place 

#%% disp obj L

random.shuffle(instrum_car)
for i in range(min(n_img_in_block, len(instrum_car))):
    img = visual.ImageStim(win, image = instrum_car[i], units = 'pix', pos = (-150, 0.0), size = (200,200))
    img.draw()
    center.draw()
    win.flip()  
    core.wait(img_time)  
    win.flip()
    core.wait(gap_time)
    
core.wait(3)

#end obj 

#%% disp faces R

random.shuffle(child_adult)
for i in range(min(n_img_in_block, len(child_adult))):
    img = visual.ImageStim(win, image = child_adult[i], units = 'pix', pos = (150, 0.0), size = (200,200))
    img.draw()
    center.draw()
    win.flip()  
    core.wait(img_time)  
    win.flip()
    core.wait(gap_time)
    
core.wait(3)

#end face

#%% disp place R

random.shuffle(house_corr)
for i in range(min(n_img_in_block, len(house_corr))):
    img = visual.ImageStim(win, image = house_corr[i], units = 'pix', pos = (150, 0.0), size = (200,200))
    img.draw()
    center.draw()
    win.flip()  
    core.wait(img_time)  
    win.flip()
    core.wait(gap_time)
    
core.wait(3)

#end place 

#%% disp obj R

random.shuffle(instrum_car)
for i in range(min(n_img_in_block, len(instrum_car))):
    img = visual.ImageStim(win, image = instrum_car[i], units = 'pix', pos = (150, 0.0), size = (200,200))
    img.draw()
    center.draw()
    win.flip()  
    core.wait(img_time)  
    win.flip()
    core.wait(gap_time)
    
core.wait(3)

#end obj 

#%% close screen

win.close()