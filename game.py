from random import choice

file = open('rating.txt')
name = input('Enter your name: ')
rating = 0
for line in file.readlines():
    if line.split()[0] == name:
        rating = int(line.split()[1])
file.close()

options = ['rock', 'paper', 'scissors']
u_options = input('Type in your options: ')
if len(u_options) > 0:
    options = u_options.split(',')
print("Okay, let's start")

while True:
    u_answer = input()
    if u_answer in options:
        new_list = []
        new_list.extend(options[options.index(u_answer)+1:])
        new_list.extend(options[:options.index(u_answer)])
    c_answer = choice(options)
    if u_answer == '!exit':
        break
    elif u_answer == '!rating':
        print(f'Your rating: {rating}')
    elif u_answer not in options:
        print('Invalid input')
    elif u_answer == c_answer:
        print(f'There is a draw {c_answer}')
        rating += 50
    elif new_list.index(c_answer) < len(new_list) / 2:
        print(f'Sorry, but computer chose {c_answer}')
    else:
        print(f'Well done. Computer chose {c_answer} and failed')
        rating += 100

print('Bye!')
