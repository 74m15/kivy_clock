# -*- coding: utf-8 -*-
"""
Created on Wed May 26 15:59:01 2021

@author: CAPUANO-P
"""

import kivy

from time import localtime

from kivy.app import App
from kivy.clock import Clock

class ClockApp(App):
    
    def build(self, *args, **kwargs):
        super(ClockApp, self).build(*args, **kwargs)
        
        Clock.schedule_interval(self.on_timer, 0.05)
    
    def on_timer(self, *args):
        time = localtime()
        
        self.root.ids.hour.angle = \
            -(time.tm_hour * 3600 + time.tm_min * 60 + time.tm_sec) / 86400 * 720 + 90
        self.root.ids.minute.angle = \
            -(time.tm_min * 60 + time.tm_sec) / 3600 * 360 + 90
        self.root.ids.second.angle = \
            -(time.tm_sec) / 60 * 360 + 90
        
        return True
            
if __name__ == '__main__':
    ClockApp().run()