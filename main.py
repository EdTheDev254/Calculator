import tkinter as tk
import tkinter.ttk as ttk


class MyApp(tk.Tk):
	def __init__(self):
		super().__init__()
		# Restrict window size from being changed
		self.resizable(False, False)
		# Set The Title
		self.title('Calculator')
		# Set the window size
		self.geometry('300x400')


if __name__ == '__main__':
	app = MyApp()
	app.mainloop()