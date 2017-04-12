#!/usr/bin/env python3

import time
from datetime import datetime
import tkinter as tk
import random

class Component():
    def draw(self):
        raise NotImplementedError("Should have implemented this")

class Clock(Component):
    def __init__(self, container):
        self.clock = tk.Label(container)
        self.clock['background'] = 'black'
        self.clock['foreground'] = 'white'
        self.clock['pady'] = 50
        self.clock['font'] = ("Linux Biolinum O", 72)
        self.clock.pack()

    def draw(self):
        self.clock['text'] = time.strftime("%H:%M:%S", time.localtime())
        self.clock.after(500, self.draw)

class Temperature(Component):
    def __init__(self, container):
        self.temperature = tk.Label(container)
        self.temperature['background'] = 'black'
        self.temperature['foreground'] = 'white'
        self.temperature['pady'] = 50
        self.temperature['font'] = ("Linux Biolinum O", 72)
        self.temperature.pack()

    def getTemperature(self):
        #TODO: külső komponens implementációja
        return random.randint(0,30)

    def draw(self):
        self.temperature['text'] =  str(self.getTemperature()) + ' °C'
        self.temperature.after(10000, self.draw)


class GUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.attributes('-fullscreen', True)
        self.window.title('Kutya')
        self.window['background'] = 'black'

        self.components = (Clock(self.window), Temperature(self.window))
        for component in self.components:
            component.draw()

    def start(self):
        self.window.mainloop()

    def stop(self):
        pass

gui = GUI()
gui.start()
