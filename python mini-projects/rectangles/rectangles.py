import math 

def get_user_input():
  num_rec = int(input('How many rectengles will you be working with today?'))
  return num_rec

def rec_area_loop(num_rec):
    i = 0
    while i < num_rec:
        length = int(input('What is the length: '))
        width = int(input('What is the width: '))
        area = length * width
        print('The area of your rectangle is' + str(area))
        i += 1

def main():
  num_rec = get_user_input()
  rec_area_loop(num_rec)

main()