#
#
#

import tkinter as tk
import tkinter.ttk as ttk
from string import punctuation

class MyApp(tk.Tk):
	def __init__(self):
		super().__init__()

		# Some Variables to use
		button_padding = 8
		button_width = 6
		equal_button_width = 17

		# Restrict window size from being changed
		self.resizable(False, False)
		# Set The Title
		self.title('Calculator')
		# Set the window size
		self.geometry('300x380')

		self.variable_check = False # To check if there are characters so as to append updated ones

		# Create frames for the button widgets
		self.frame1 = tk.Frame(self)
		self.frame2 = tk.Frame(self)
		self.frame3 = tk.Frame(self)
		self.frame4 = tk.Frame(self)
		self.frame5 = tk.Frame(self)
		self.frame6 = tk.Frame(self)

		# Place the frames on the display
		self.frame1.grid(row=0, column=0, padx=20,pady=(15, 40))
		self.frame2.grid(row=1, column=0, pady=(0,10))
		self.frame3.grid(row=2, column=0, pady=(0,10))
		self.frame4.grid(row=3, column=0, pady=(0,10))
		self.frame5.grid(row=4, column=0, pady=(0,10))
		self.frame6.grid(row=5, column=0, pady=(0,10))

		# Create the display Entry
		self.calculator_display = tk.Text(self.frame1, width=23, height=3, bg='green',fg='black', font=('verdana', 13), bd=4)

		# Place the display entry onto frame1
		self.calculator_display.grid(row=0, column=0, sticky='n')

		# Define the first row buttons
		self.ACbutton = ttk.Button(self.frame2, text="AC", width=button_width, padding=button_padding, command=self.clear_screen)
		self.MODbutton = ttk.Button(self.frame2, text="%", width=button_width, padding=button_padding)
		self.PIbutton = ttk.Button(self.frame2, text="PI", width=button_width, padding=button_padding)
		self.DIVIDEbutton = ttk.Button(self.frame2, text="/", width=button_width, padding=button_padding)

		# Place the first row buttons
		self.ACbutton.grid(row=0, column=0, padx=4)
		self.MODbutton.grid(row=0, column=1, padx=4)
		self.PIbutton.grid(row=0, column=2, padx=4)
		self.DIVIDEbutton.grid(row=0, column=3, padx=4)

		# Define the second row buttons
		self.button7 = ttk.Button(self.frame3, text="7", width=button_width, padding=button_padding, command=lambda:self.button_clicks("7"))
		self.button8 = ttk.Button(self.frame3, text="8", width=button_width, padding=button_padding, command=lambda:self.button_clicks("8"))
		self.button9 = ttk.Button(self.frame3, text="9", width=button_width, padding=button_padding, command=lambda:self.button_clicks("9"))
		self.ADDbutton = ttk.Button(self.frame3, text="+", width=button_width, padding=button_padding, command=lambda:self.calculate_method('+'))

		# Place the second row buttons
		self.button7.grid(row=0, column=0, padx=4)
		self.button8.grid(row=0, column=1, padx=4)
		self.button9.grid(row=0, column=2, padx=4)
		self.ADDbutton.grid(row=0, column=3, padx=4)


		# Define the third row buttons
		self.button4 = ttk.Button(self.frame4, text="4", width=button_width, padding=button_padding, command=lambda:self.button_clicks("4"))
		self.button5 = ttk.Button(self.frame4, text="5", width=button_width, padding=button_padding, command=lambda:self.button_clicks("5"))
		self.button6 = ttk.Button(self.frame4, text="6", width=button_width, padding=button_padding, command=lambda:self.button_clicks("6"))
		self.MINUSbutton = ttk.Button(self.frame4, text="-", width=button_width, padding=button_padding, command=lambda:self.calculate_method('-'))

		# Place the third row buttons
		self.button4.grid(row=0, column=0, padx=4)
		self.button5.grid(row=0, column=1, padx=4)
		self.button6.grid(row=0, column=2, padx=4)
		self.MINUSbutton.grid(row=0, column=3, padx=4)

		# Define the fourth row buttons
		self.button1 = ttk.Button(self.frame5, text="1", width=button_width, padding=button_padding, command=lambda:self.button_clicks("1"))
		self.button2 = ttk.Button(self.frame5, text="2", width=button_width, padding=button_padding, command=lambda:self.button_clicks("2"))
		self.button3 = ttk.Button(self.frame5, text="3", width=button_width, padding=button_padding, command=lambda:self.button_clicks("3"))
		self.MULTbutton = ttk.Button(self.frame5, text="*", width=button_width, padding=button_padding)

		# Place the fourth row buttons
		self.button1.grid(row=0, column=0, padx=4)
		self.button2.grid(row=0, column=1, padx=4)
		self.button3.grid(row=0, column=2, padx=4)
		self.MULTbutton.grid(row=0, column=3, padx=4)

		# Define the fifth row buttons
		self.DOTbutton = ttk.Button(self.frame6, text=".", width=button_width, padding=button_padding, command=lambda:self.button_clicks("."))
		self.button0 = ttk.Button(self.frame6, text="0", width=button_width, padding=button_padding, command=lambda:self.button_clicks("0"))
		self.EQUALbutton = ttk.Button(self.frame6, text="=", width=equal_button_width, padding=button_padding, command=self.calculate_output)

		# Place the fifth row buttons
		self.DOTbutton.grid(row=0, column=0, padx=4)
		self.button0.grid(row=0, column=1, padx=4)
		self.EQUALbutton.grid(row=0, column=3, columnspan=2, padx=4)
    
		# METHODS
		# Make the buttons interact with the display window
		# Remove white space and punctuations and convert to number
	def remove_punc_return_int(self):
		self.num1 = self.calculator_display.get('1.0', tk.END)

		# Prevent empty input
		
		for i in self.num1:
			if i in punctuation or i == '\n':
				self.first_number = self.num1.replace(i,'')
				self.calculator_display.delete('1.0', 'end') # Clear the display
		return float(self.first_number) # Return a floating-point


	def button_clicks(self, num):
	# Avoid duplicated decimal places
#######################################################################################
		display_input = self.calculator_display.get("1.0", "end")

		if num == '.' and '.' in display_input:
			return
#######################################################################################

		if self.variable_check:
			self.calculator_display.delete('1.0', 'end') # Clear screen
			self.variable_check = False # Return to false so as to append
		self.num = num
		self.calculator_display.insert(tk.INSERT, self.num) # Append the value of the clicked button to the display


	def clear_screen(self):
		self.calculator_display.delete('1.0', 'end')

	def calculate_method(self, char_x):
		self.char_x = char_x
		self.input1 = self.remove_punc_return_int() # Get the first number
		print('First number is:', self.input1)

		#print(self.first_number, 'button Clicked')

	# Calculate output of the calculation
	def calculate_output(self):
		if self.num1 != '':
			self.input2 = self.remove_punc_return_int()

		# Addition feature
		if self.char_x == '+':
			#print('First number selected')
			self.summation = self.input1 + self.input2
			#print('Second Number:', self.input2)

		# Subtraction feature
		if self.char_x == '-':
			#print('Subtraction selected')
			self.summation = self.input1 - self.input2
			#print('Second Number:', self.input2)

		self.calculator_display.insert(tk.INSERT, self.summation)
		print('Total:', self.summation)

if __name__ == '__main__':
	app = MyApp()
	app.mainloop()
