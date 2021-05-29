# -*- coding: utf-8 -*-
"""
Created on Wed May 26 15:59:01 2021

@author: CAPUANO-P
"""

import kivy

from time import time

from kivy.app import App
from kivy.clock import Clock

class ClockApp(App):
    
    def __init__(self):
        super(ClockApp, self).__init__()
        
        self.rendering = False
    
    def get_application_config(self):
        """
            Method overriden to skip file .ini read/write (dynamic configuration))
        """
        return None
    
    def build_config(self, config):
        pass
#        config.setdefaults("mandel", { 
#                "max_iter" : 255, 
#                "min_c_real" : -2.0,
#                "min_c_imag" : -1.25,
#                "z_size" : 2.50
#            })
#        config.setdefaults("render", { 
#                "mandel_color" : "(0,0,0)", 
#                "algorithm" : "smooth"
#            })
        
    def build_settings(self, settings):
        pass
#        settings.add_json_panel("Mandel", self.config, data=\
#            """[
#                    {
#                        "type" : "title",
#                        "title" : "Mandel"
#                    },
#                    {
#                        "type" : "numeric",
#                        "title" : "Max number of iterations",
#                        "section" : "mandel",
#                        "key" : "max_iter"
#                    },
#                    {
#                        "type" : "numeric",
#                        "title" : "min(c) - real part",
#                        "section" : "mandel",
#                        "key" : "min_c_real"
#                    },
#                    {
#                        "type" : "numeric",
#                        "title" : "min(c) - imaginary part",
#                        "section" : "mandel",
#                        "key" : "min_c_imag"
#                    },
#                    {
#                        "type" : "numeric",
#                        "title" : "delta z - width of image",
#                        "section" : "mandel",
#                        "key" : "z_size"
#                    },
#                    {
#                        "type" : "title",
#                        "title" : "Render"
#                    },
#                    {
#                        "type" : "string",
#                        "title" : "RGB color of Mandelbrot set",
#                        "section" : "render",
#                        "key" : "mandel_color"
#                    },
#                    {
#                        "type" : "options",
#                        "title" : "Rendering Algorithm",
#                        "section" : "render",
#                        "key" : "algorithm",
#                        "options" : [ "smooth", "log" ]
#                    }
#                ]""")
        

if __name__ == '__main__':
    ClockApp().run()