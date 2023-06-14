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

		# Create frames for the button widgets
		self.frame1 = tk.Frame(self)
		self.frame2 = tk.Frame(self)
		self.frame3 = tk.Frame(self)
		self.frame4 = tk.Frame(self)
		self.frame5 = tk.Frame(self)

		# Place the frames on the display
		self.frame1.grid(row=0, column=0)
		self.frame2.grid(row=1, column=0)
		self.frame3.grid(row=2, column=0)
		self.frame4.grid(row=3, column=0)
		self.frame5.grid(row=4, column=0)

		# Create the display Entry
		self.calculator_display = tk.Text(self, width=15, height=2, bg='green',fg='black', font=('courier', 21), bd=3)

		# Place the display entry onto frame1
		self.calculator_display.grid(row=0, column=0, padx=20, pady=10)
		
		
if __name__ == '__main__':
	app = MyApp()
	app.mainloop()
