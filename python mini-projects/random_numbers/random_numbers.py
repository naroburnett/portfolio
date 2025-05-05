import random

def append_random_numbers(numbers_list, quantity = 1):
    for _ in range (quantity):
        number = round(random.uniform(0,150), 1)
        numbers_list.append(number)
    pass

def append_random_words(words_list, quantity = 1):
    for _ in range (quantity):
        dictonary = ['invite','unique','campaign','trial',
        'mask','incentive','privacy','government','jelly',
        'behave','admiration','cheek','favorable','shell','safe']
        word = random.choice(dictonary)
        words_list.append(word)
    pass

def generator_type():
   type = input('Do you want to generate random words or numbers: ').lower()
   return type

def main():
    type = generator_type()
    if type == "numbers":
        randnums = [16.2, 75.1, 52.3]
        quantity = int(input('How many numbers do you want to add to the list: '))
        append_random_numbers(randnums, quantity)
        print(randnums)
        append_random_numbers(randnums, 3)
        print(randnums)
    else:
        quantity = int(input('How many words do you want to add to the list: '))
        words_list = ['apple', "obama", 'willy']
        append_random_words(words_list, quantity)
        print(words_list)
        pass

main()