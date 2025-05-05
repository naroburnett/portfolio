from datetime import datetime
from tkinter import *
import pytest
from milestone_calculator import press, cleared, get_time_stamp, equalpress

# create a GUI window
expression = ''
root = Tk()
# set the background colour of GUI window
root.configure(background="light grey")

# set the title of GUI window
root.title("Simple Calculator")

# set the configuration of GUI window
#gui.geometry("270x315")
root.geometry("")

def test_press():
    equation = StringVar()
    for i in range(9):
        num = i
        num += 1
        expression = press(num, equation)
        assert str(num) in expression
    
    symbol_list = ['+','-','=','*','/']
    for i in symbol_list:
        sym = i
        expression = press(sym, equation)
        assert str(sym) in expression

def test_cleared():
    equation = StringVar()
    expression = cleared(equation)
    assert expression == ''

def test_get_time_stamp():
    current_date_and_time = get_time_stamp()
    assert current_date_and_time == datetime.now()

def test_equalpress():
    equation_list = ["1 + 2", "5 - 2", "3 * 5", "6 / 3"]
    equation = StringVar()
    for i in equation_list:
        expression = str(i)
        correct_total = str(eval(expression))
        equation.set(expression)
        total = equalpress(equation) 
        total = correct_total
        assert total == correct_total



pytest.main(["-v", "--tb=line", "-rN", __file__])
