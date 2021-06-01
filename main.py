# -*- coding: utf-8 -*-
"""
Created on Wed May 26 15:59:01 2021

@author: CAPUANO-P
"""

import kivy

from time import localtime

from kivy.app import App
from kivy.clock import Clock
from kivy.properties import BooleanProperty
from kivy.uix.relativelayout import RelativeLayout

class AnalogClock(RelativeLayout):
    
    started = BooleanProperty(False)
    
    def __init__(self, *args, **kwargs):
        super(AnalogClock, self).__init__(*args, **kwargs)
                
        self.clock_event = None
    
    def on_started(self, *args):
        if self.started:
            self.clock_event = Clock.schedule_interval(self.on_timer, 0.05)
        else:
            self.clock_event.cancel()
        
        return True
    
    def on_timer(self, *args):
        time = localtime()
        
        self.ids.hour.angle = \
            -(time.tm_hour * 3600 + time.tm_min * 60 + time.tm_sec) / 86400 * 720 + 90
        self.ids.minute.angle = \
            -(time.tm_min * 60 + time.tm_sec) / 3600 * 360 + 90
        self.ids.second.angle = \
            -(time.tm_sec) / 60 * 360 + 90
    
        return True

class ClockApp(App):
    
    def build(self, *args, **kwargs):
        super(ClockApp, self).build(*args, **kwargs)
    
    def on_start(self, *args):
        self.root.ids.clock.started = True
        
        return super(ClockApp, self).on_start(*args)
                
if __name__ == '__main__':
    ClockApp().run()