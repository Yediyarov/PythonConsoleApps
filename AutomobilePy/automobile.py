import os
import subprocess
import sys
import re
from pprint import pprint
import inquirer
import itertools
from random import randint
import math
from collections import namedtuple
from terminaltables import AsciiTable
import operator
sys.path.append(os.path.realpath('.'))

questions = [
    inquirer.Text('model',
                  message="Input car model"),
    inquirer.Text('color',
                  message="Input car color"),
    inquirer.Text('year',
                  message="Input car year",
                  validate=lambda _, x: re.match('\d+', x),
                  ),
    inquirer.Text('engine',
                  message="Input car engine",
                  validate=lambda _, x: re.match('\d+', x),
                  ),
    inquirer.Text('milage',
                  message="Input car milage",
                  validate=lambda _, x: re.match('\d+', x),
                  ),    
    inquirer.Text('price',
                  message="Input car price",
                  validate=lambda _, x: re.match('\d+', x),
                  ),

]
questions1 = [
    inquirer.Confirm('continue',
                  message="Should I continue"),
]
questions2 = [
    inquirer.List('choise',
                  message="What you want to do?",
                  choices=['Sorting','Buy','Add'],
              ),
]
questions3 = [
    inquirer.List('sort',
                  message="Sorting by what?",
                  choices=['Model','Color','Year','Engine','Milage','Price'],
              ),
]
questions4 = [
    inquirer.Text('car',
                  message="Input car name"),
    inquirer.Text('price',
                  message="Input price",
                  validate=lambda _, x: re.match('\d+', x),
                  ),
]

Car = namedtuple('Car',['model','color','year','engine','milage','price'])

table_data=[]
heading=['model','color','year','engine','milage','price']
table_data.append(heading)
count=0
while True:
    subprocess.Popen('clear')
    answers = inquirer.prompt(questions)
    table_data.append([*Car(**answers)])
    count+=1
    if count >= 10:
        answers1 = inquirer.prompt(questions1)
        continue_=answers1['continue']
        if continue_:
            continue
        else:
            break

table=AsciiTable(table_data)
print(table.table)

while True: 
    answers2 = inquirer.prompt(questions2)
    
    if answers2['choise'] == 'Sorting':
        content=table_data[1:]
        answers3=inquirer.prompt(questions3)
        if answers3['sort'] == 'Model':
            content.sort(key=operator.itemgetter(0))
        elif answers3['sort'] == 'Color':
            content.sort(key=operator.itemgetter(1)) 
        elif answers3['sort'] == 'Year':
            content.sort(key=operator.itemgetter(2))      
        elif answers3['sort'] == 'Engine':
            content.sort(key=operator.itemgetter(3))
        elif answers3['sort'] == 'Milage':
            content.sort(key=operator.itemgetter(4)) 
        elif answers3['sort'] == 'Price':
            content.sort(key=operator.itemgetter(5))
        content.insert(0,heading)
        table1=AsciiTable(content)
        print(table1.table)       
    elif answers2['choise'] == 'Buy':
        answers4 = inquirer.prompt(questions4)
        for cars in table_data[1:]:
            if cars[0] == answers4['car'] and int(cars[5]) > int(answers4['price']):
                print("You haven't enough money!")
                break
            elif cars[0] == answers4['car'] and int(cars[5]) < int(answers4['price']):
                print(f"Thanks for buying! Your cash back is { int(answers4['price']) - int(cars[5]) }")
                table_data.remove(cars)
                table2=AsciiTable(table_data)
                print(table2.table)
                break
    elif answers2['choise'] == 'Add':
        answers = inquirer.prompt(questions)
        new_car = list(answers.values())
        table_data.append(new_car)
        table3=AsciiTable(table_data)
        print(table3.table)
    
    
    answers1 = inquirer.prompt(questions1)
    continue_=answers1['continue']
    if continue_:
        continue
    else:
        break