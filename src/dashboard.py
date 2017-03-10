#!/usr/bin/env python3
import time
import tkinter as tk


class GUI:
	def __init__(self):
		self.window = tk.Tk()
		self.window.attributes('-fullscreen', True)
		self.window['background'] = 'black'

	def start(self):
		self.window.mainloop()

if __name__ == '__main__':
	app = GUI()
	app.start()
