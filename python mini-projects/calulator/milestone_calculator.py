from tkinter import *
from datetime import datetime

# globally declare the expression variable
expression = ""
history_list = []

# Function to update expression
# in the text entry box
def press(num, equation):
	# point out the global expression variable
	global expression

	# concatenation of string
	expression = expression + str(num)

	# update the expression by using set method
	equation.set(expression)

	return str(expression)

def history_creation(root):
	history_frame = Frame(root, width = 275, height = 50, bd = 0, highlightbackground = "black", highlightcolor = "black", highlightthickness = 1)
	history_frame.pack()
	global expression
	# create the text entry box for
	# showing the history .
	history_field = Text(history_frame,width = 50, height = 25 )
	# grid method is used for placing
	# the widgets at respective positions
	# in table like structure .
	history_field.grid(row = 0, column = 0)
	history_field.pack()
	for x in history_list:
		history_field.insert('end', x + '\n')
	history_field.config(state='disabled')

	refresh_history = Button(history_frame, text="Remove/Update History", command=lambda: history_frame.pack_forget()).pack()
	refresh_history.grid(row=0, column=2)
	
def history_print(total):
	global history_list
	current_date_and_time = get_time_stamp()
	history_line = expression + '=' + total
	history_list.append(f"{current_date_and_time:%b %d, %I:%M-%p}  {history_line}")
	return history_list
	
def get_time_stamp():
    current_date_and_time = datetime.now()
    return current_date_and_time

# Function to evaluate the final expression
def equalpress(equation):
	# Try and except statement is used
	# for handling the errors like zero
	# division error etc.

	# Put that code inside the try block
	# which may generate the error
	try:

		global expression

		# eval function evaluate the expression
		# and str function convert the result
		# into string
		total = str(eval(expression))

		equation.set(total)
		
		history_print(total)
		# initialize the expression variable
		# by empty string
		expression = ""
		
	# if error is generate then handle
	# by the except block
	except:

		equation.set(" error ")
		expression = ""

	# Function to clear the contents
# of text entry box
def cleared(equation):
	global expression
	expression = ""
	equation.set("")
	return str(expression)

def basic_calculator_creation(root, equation):

	expression_frame = Frame(root, width = 150, height = 50, highlightbackground = "black", highlightcolor = "black", highlightthickness = 1)
	expression_frame.pack(side = TOP)

	# create the text entry box for
	# showing the expression .
	expression_field = Entry(expression_frame,  font = ('arial', 18, 'bold'), textvariable=equation,  width = 20,  bd = 0, justify = RIGHT)
	# grid method is used for placing
	# the widgets at respective positions
	# in table like structure .
	expression_field.grid(row = 0, column = 0)
	expression_field.pack(ipady = 10)

def buttons_creation(root, equation):

	btns_frame = Frame(root, width = 275, height = 272.5, bg = "grey")
	btns_frame.pack()

	#1
	button1 = Button(btns_frame, text=' 1 ', fg='black', bg='darkorange1',
					command=lambda: press(1, equation), height=2, width=7)
	button1.grid(row=2, column=0)

	#2
	button2 = Button(btns_frame, text=' 2 ', fg='black', bg='darkorange1',
					command=lambda: press(2, equation), height=2, width=7)
	button2.grid(row=2, column=1)

	#3
	button3 = Button(btns_frame, text=' 3 ', fg='black', bg='darkorange1',
					command=lambda: press(3, equation), height=2, width=7)
	button3.grid(row=2, column=2)

	#4
	button4 = Button(btns_frame, text=' 4 ', fg='black', bg='darkorange1',
					command=lambda: press(4, equation), height=2, width=7)
	button4.grid(row=3, column=0)

	#5
	button5 = Button(btns_frame, text=' 5 ', fg='black', bg='darkorange1',
					command=lambda: press(5, equation), height=2, width=7)
	button5.grid(row=3, column=1)

	#6
	button6 = Button(btns_frame, text=' 6 ', fg='black', bg='darkorange1',
					command=lambda: press(6, equation), height=2, width=7)
	button6.grid(row=3, column=2)

	#7
	button7 = Button(btns_frame, text=' 7 ', fg='black', bg='darkorange1',
					command=lambda: press(7, equation), height=2, width=7)
	button7.grid(row=4, column=0)

	#8
	button8 = Button(btns_frame, text=' 8 ', fg='black', bg='darkorange1',
					command=lambda: press(8, equation), height=2, width=7)
	button8.grid(row=4, column=1)

	#9
	button9 = Button(btns_frame, text=' 9 ', fg='black', bg='darkorange1',
					command=lambda: press(9, equation), height=2, width=7)
	button9.grid(row=4, column=2)

	#0
	button0 = Button(btns_frame, text=' 0 ', fg='black', bg='darkorange1',
					command=lambda: press(0, equation), height=2, width=7)
	button0.grid(row=5, column=1)

	#plus (+)
	plus = Button(btns_frame, text=' + ', fg='black', bg='darkorange1',
				command=lambda: press("+", equation), height=2, width=7)
	plus.grid(row=6, column=3)

	#minus (-)
	minus = Button(btns_frame, text=' - ', fg='black', bg='darkorange1',
				command=lambda: press("-", equation), height=2, width=7)
	minus.grid(row=5, column=3)

	#multiply (*)
	multiply = Button(btns_frame, text=' * ', fg='black', bg='darkorange1',
					command=lambda: press("*", equation), height=2, width=7)
	multiply.grid(row=4, column=3)

	#divide (/)
	divide = Button(btns_frame, text=' / ', fg='black', bg='darkorange1',
					command=lambda: press("/", equation), height=2, width=7)
	divide.grid(row=3, column=3)

	#equal (=)
	equal = Button(btns_frame, text=' = ', fg='black', bg='darkorange1',
				command=lambda: equalpress(equation), height=2, width=7)
	equal.grid(row=7, column=3)

	#clear("")
	clear = Button(btns_frame, text='Clear', fg='black', bg='darkorange1',
				command=lambda: cleared(equation), height=2, width=7)
	clear.grid(row=2, column='3')

	#decimal (.)
	Decimal= Button(btns_frame, text='.', fg='black', bg='darkorange1',
					command=lambda: press('.', equation), height=2, width=7)
	Decimal.grid(row=5, column=2)

	#pi (π)
	pi = Button(btns_frame, text='π', fg='black', bg='darkorange1',
					command=lambda: press('math.pi', equation), height=2, width=7)
	pi.grid(row=5, column=0)

	history= Button(btns_frame, text='History', fg='black', bg='darkorange1',
					command=lambda: history_creation(root), height=2, width=24)
	history.grid(row=6, column=0, columnspan = 3)

	
	
	return btns_frame

def main():
	
	# create a GUI window
	root = Tk()
	# set the background colour of GUI window
	root.configure(background="light grey")

	# set the title of GUI window
	root.title("Simple Calculator")

	# set the configuration of GUI window
	#gui.geometry("270x315")
	root.geometry("")

	equation = StringVar()

	basic_calculator_creation(root, equation )

	buttons_creation(root, equation)

	root.mainloop()

if __name__ == "__main__":
    main()