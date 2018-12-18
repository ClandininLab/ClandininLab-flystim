#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from flystim.screen import Screen
from flystim.stim_server import StimServer
from flystim.dlpc350 import make_dlpc350_objects
from math import pi

def main():
    # Put lightcrafter(s) in pattern mode
    dlpc350_objects = make_dlpc350_objects()
    for dlpc350_object in dlpc350_objects:
         dlpc350_object.pattern_mode(fps=115.06)
     
    # Define screen(s) for the rig
    # TODO: check perspective correction measurements
    w = 20.6e-2; h = 12.8e-2; # meters of image at projection plane

    bruker_right_screen = Screen(width=w, height=h, rotation=pi-pi/4, offset=(4.4e-2, 3.0e-2, -6.1e-2), id=2, fullscreen=True, vsync=None, square_side=3e-2, square_loc='ll')
    bruker_left_screen = Screen(width=w, height=h, rotation=pi+pi/4, offset=(-3.9e-2, 4.0e-2, -6.1e-2), id=1, fullscreen=True, vsync=None, square_side=3e-2, square_loc='lr')

    bruker_right_screen.draw()
    bruker_left_screen.draw()

    screens = [bruker_left_screen, bruker_right_screen]
    port = 60629
    host = ''
    
    manager =  StimServer(screens=screens, host=host, port=port, auto_stop=False)
    
    manager.black_corner_square()
    manager.set_idle_background(0)    
    
    manager.loop()

if __name__ == '__main__':
    main()