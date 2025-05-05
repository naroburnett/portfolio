def main():
    print('This program is an implementation of the Rosenberg Self-Esteem Scale. \n'
          'This program will show you ten statements that you could possibly \n'
          'apply to yourself. Please rate how much you agree with each of the \n'
          'statements by responding with one of these four letters: \n'
          'D means you strongly disagree with the statement. \n'
          'd means you disagree with the statement. \n'
          'a means you agree with the statement. \n'
          'A means you strongly agree with the statement.')
    awnsers = questions()
    positive, negitive = assigning_value(awnsers)
    total = calculations(positive, negitive)
    print (f"Your score is {total}.")
    print("A score below 15 may indicate problematic low self-esteem.total")
    


def questions():
    awnsers = []
    #question 1 starts at 0
    awnsers.append(input('I feel that I am a person of worth, at least on an equal plane with others.'
    '\nEnter D, d, a, or A: '))
    awnsers.append(input('I feel that I have a number of good qualities.'
    '\nEnter D, d, a, or A: '))
    awnsers.append(input('All in all, I am inclined to feel that I am a failure.'
    '\nEnter D, d, a, or A: '))
    awnsers.append(input('I am able to do things as well as most other people.'
    '\nEnter D, d, a, or A: '))
    awnsers.append(input('I feel I do not have much to be proud of.'
    '\nEnter D, d, a, or A: '))
    awnsers.append(input('I take a positive attitude toward myself.'
    '\nEnter D, d, a, or A: '))
    awnsers.append(input('On the whole, I am satisfied with myself.'
    '\nEnter D, d, a, or A: '))
    awnsers.append(input('I wish I could have more respect for mysel.'
    '\nEnter D, d, a, or A: '))
    awnsers.append(input('I certainly feel useless at times.'
    '\nEnter D, d, a, or A: '))
    awnsers.append(input('At times I think I am no good at all.'
    '\nEnter D, d, a, or A: '))
    return awnsers

    
def assigning_value(awnsers):
    i = 0
    positive = []
    negitive = []
    for i in range (10):
        #positive
        if i == 0 or  i == 1 or i == 3 or i == 5 or i == 6:
            if awnsers[i] == 'D':
               value = 0
            elif awnsers[i] == 'd':
                value = 1
            elif awnsers[i] == 'a':
                value = 2
            elif awnsers[i] == 'A':
                value = 3
            positive.append(value)
        #negitive
        elif i == 2 or i == 4 or i == 7 or i == 8 or i == 9:
            if awnsers[i] == 'D':
               value = 3
            elif awnsers[i] == 'd':
                value = 2
            elif awnsers[i] == 'a':
                value = 1
            elif awnsers[i] == 'A':
                value = 0
            negitive.append(value)
    return positive, negitive

def calculations(positive, negitive):
    pos = sum(positive)
    neg = sum(negitive)
    total = pos + neg
    return total
main()