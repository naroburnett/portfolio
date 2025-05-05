from tkinter import *
import math
from datetime import datetime
import pprint

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

def history(expression, total):
    global history_list
    current_date_and_time = get_time_stamp()
    history_line = expression + '=' + total
    history_list.append(f"{current_date_and_time}  {history_line}")
    print(history_list)

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

        history(expression, total)

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

def basic_calculator_creation(gui):
    equation = StringVar()
    # create the text entry box for
	# showing the expression .
    expression_field = Entry(gui, textvariable=equation)
    # grid method is used for placing
    # the widgets at respective positions
    # in table like structure .
    expression_field.grid(columnspan=4, ipadx=70, ipady=20)

    #history_field = Entry(gui, textvariable=print(history_list))
    #history_field.grid(row=5, ipadx=70, ipady=20)

    #1
    button1 = Button(gui, text=' 1 ', fg='black', bg='darkorange1',
                    command=lambda: press(1, equation), height=2, width=7)
    button1.grid(row=2, column=0)

    #2
    button2 = Button(gui, text=' 2 ', fg='black', bg='darkorange1',
                    command=lambda: press(2, equation), height=2, width=7)
    button2.grid(row=2, column=1)

    #3
    button3 = Button(gui, text=' 3 ', fg='black', bg='darkorange1',
                    command=lambda: press(3, equation), height=2, width=7)
    button3.grid(row=2, column=2)

    #4
    button4 = Button(gui, text=' 4 ', fg='black', bg='darkorange1',
                    command=lambda: press(4, equation), height=2, width=7)
    button4.grid(row=3, column=0)

    #5
    button5 = Button(gui, text=' 5 ', fg='black', bg='darkorange1',
                    command=lambda: press(5, equation), height=2, width=7)
    button5.grid(row=3, column=1)

    #6
    button6 = Button(gui, text=' 6 ', fg='black', bg='darkorange1',
                    command=lambda: press(6, equation), height=2, width=7)
    button6.grid(row=3, column=2)

    #7
    button7 = Button(gui, text=' 7 ', fg='black', bg='darkorange1',
                    command=lambda: press(7, equation), height=2, width=7)
    button7.grid(row=4, column=0)

    #8
    button8 = Button(gui, text=' 8 ', fg='black', bg='darkorange1',
                    command=lambda: press(8, equation), height=2, width=7)
    button8.grid(row=4, column=1)

    #9
    button9 = Button(gui, text=' 9 ', fg='black', bg='darkorange1',
                    command=lambda: press(9, equation), height=2, width=7)
    button9.grid(row=4, column=2)

    #0
    button0 = Button(gui, text=' 0 ', fg='black', bg='darkorange1',
                    command=lambda: press(0, equation), height=2, width=7)
    button0.grid(row=5, column=1)

    #plus (+)
    plus = Button(gui, text=' + ', fg='black', bg='darkorange1',
                command=lambda: press("+", equation), height=2, width=7)
    plus.grid(row=6, column=3)

    #minus (-)
    minus = Button(gui, text=' - ', fg='black', bg='darkorange1',
                command=lambda: press("-", equation), height=2, width=7)
    minus.grid(row=5, column=3)

    #multiply (*)
    multiply = Button(gui, text=' * ', fg='black', bg='darkorange1',
                    command=lambda: press("*", equation), height=2, width=7)
    multiply.grid(row=4, column=3)

    #divide (/)
    divide = Button(gui, text=' / ', fg='black', bg='darkorange1',
                    command=lambda: press("/", equation), height=2, width=7)
    divide.grid(row=3, column=3)

    #equal (=)
    equal = Button(gui, text=' = ', fg='black', bg='darkorange1',
                command=lambda: equalpress(equation), height=2, width=7)
    equal.grid(row=7, column=3)

    #clear("")
    clear = Button(gui, text='Clear', fg='black', bg='darkorange1',
                command=lambda: cleared(equation), height=2, width=7)
    clear.grid(row=2, column='3')

    #decimal (.)
    Decimal= Button(gui, text='.', fg='black', bg='darkorange1',
                    command=lambda: press('.'), height=2, width=7)
    Decimal.grid(row=5, column=2)

    #pi (π)
    pi = Button(gui, text='π', fg='black', bg='darkorange1',
                    command=lambda: press('math.pi', equation), height=2, width=7)
    pi.grid(row=5, column=0)



def main():
    # create a GUI window
    gui = Tk()

    # set the background colour of GUI window
    gui.configure(background="light grey")

    # set the title of GUI window
    gui.title("Simple Calculator")

    # set the configuration of GUI window
    #gui.geometry("270x315")
    gui.geometry("270x315")

    basic_calculator_creation(gui)


    gui.mainloop()

if __name__ == "__main__":
    main()