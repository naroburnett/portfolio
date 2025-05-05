import math 
"""
When you physically exercise to strengthen your heart, you
should maintain your heart rate within a range for at least 20
minutes. To find that range, subtract your age from 220. This
difference is your maximum heart rate per minute. Your heart
simply will not beat faster than this maximum (220 - age).
When exercising to strengthen your heart, you should keep your
heart rate between 65% and 85% of your heart's maximum.
"""
""" 
age = a
220 = max
220 - age = Max heart rate
"""
age = float(input("What is your age?"))
maxrate = 220 - age
lowerRate = maxrate * .65
upperRate = maxrate * .85
print (f'When you exercise to strengthen your heart, you should keep your heart rate between {lowerRate:.0f} and {upperRate:.0f} beats per minute.')


