import os
import sys
import re
from pprint import pprint
import inquirer
import itertools
from random import randint
import math

sys.path.append(os.path.realpath('.'))

questions = [
    inquirer.Text('number',
                  message="Input number",
                  validate=lambda _, x: re.match('\d+', x),
                  )
]
questions1 = [
    inquirer.Confirm('continue',
                  message="Should I continue"),
]


user_point=0
for i in itertools.count():
    print(f"Qazandiginiz xal: {user_point}")
    attemp_count=0
    my_number_generator=(randint(1,100) for i in range(5))
    guess_number=next(my_number_generator)
    print(guess_number)
    for j in range(5):
        answers = inquirer.prompt(questions)
        user_num=int(answers['number'])
        if user_num>guess_number:
            print("Daha kicik eded daxil edin")
            print(f"Sizin {4-attemp_count} cehdiniz qalib")
        elif user_num<guess_number:
            print("Daha boyuk eded daxil edin")
            print(f"Sizin {4-attemp_count} cehdiniz qalib")
        elif user_num==guess_number:
            print("Tebrikler reqem tapildi!!!")
            user_point+=1
            break
        attemp_count+=1
        if attemp_count==5:
            break   
    answers1 = inquirer.prompt(questions1)
    continue_=answers1['continue']
    if not continue_:
        break
    else:
        continue

pprint(user_num)