from pprint import pprint
import json
from urllib.request import urlopen
from collections import namedtuple
from terminaltables import AsciiTable
import terminaltables
import inquirer
import operator
import re
with urlopen("https://api.coinmarketcap.com/v2/listings/") as url:
    raw_data=url.read().decode()
    info=json.loads(raw_data)

questions1 = [
    inquirer.List('choise',
                  message="What you want to do?",
                  choices=['Paging','Sort','Search'],
              ),
]
questions2 = [
    inquirer.List('choise',
                  message="Make choise",
                  choices=['Previous','Next'],
              ),
]
questions3 = [
    inquirer.Confirm('continue',
                  message="Should I continue"),
]
questions4 = [
    inquirer.List('sort',
                  message="Sorting by what?",
                  choices=['id','name','symbol','website_slug'],
              ),
]
questions5 = [
    inquirer.List('search',
                  message="Search by what?",
                  choices=['id','name','symbol','website_slug'],
              ),
]
questions6 = [
    inquirer.Text('id',
                  message="Input searching id!",
                  validate=lambda _, x: re.match('\d+', x),
                  )
]
questions7 = [
    inquirer.Text('name',
                  message="Input searching name!",
                  )
]
questions8 = [
    inquirer.Text('symbol',
                  message="Input searching symbol!",
                  )
]
questions9 = [
    inquirer.Text('website_slug',
                  message="Input searching website_slug!",
                  )
]
table_data=[]
heading=['id','name','symbol','website_slug']
list_data=info['data']
paging=0
table_data.insert(0,heading)

while True:
    table_data=[]
    table_data.insert(0,heading)
    for i in range(paging*10,(paging+1)*10):
        table_data.append(list(list_data[i].values())) 

    table1=AsciiTable(table_data)
    print(table1.table)
    answers1 = inquirer.prompt(questions1)
    if answers1['choise'] == 'Paging':
        answers2 = inquirer.prompt(questions2)
        if answers2['choise'] == 'Next':
            paging+=1
            continue
        else:
            paging-=1
            continue
    elif answers1['choise'] == 'Sort':
        content=table_data[1:]
        answers4=inquirer.prompt(questions4)
        if answers4['sort'] == 'id':
            content.sort(key=operator.itemgetter(0))
        elif answers4['sort'] == 'name':
            content.sort(key=operator.itemgetter(1)) 
        elif answers4['sort'] == 'symbol':
            content.sort(key=operator.itemgetter(2))      
        elif answers4['sort'] == 'website_slug':
            content.sort(key=operator.itemgetter(3))
        content.insert(0,heading)
        table2=AsciiTable(content)
        print(table2.table)   
    elif answers1['choise'] == 'Search':
        search_=table_data[1:]
        search_result=[]
        answers5=inquirer.prompt(questions5)
        
        if answers5['search'] == 'id':
            search_column=0
            answers6 = inquirer.prompt(questions6)
            searching_element=int(answers6['id'])
            
        elif answers5['search'] == 'name':
            search_column=1
            answers7 = inquirer.prompt(questions7)
            searching_element=answers7['name']
        elif answers5['search'] == 'symbol':
            search_column=2
            answers8 = inquirer.prompt(questions8)
            searching_element=answers8['symbol']      
        elif answers5['search'] == 'website_slug':
            search_column=3
            answers9 = inquirer.prompt(questions9)
            searching_element=answers9['website_slug']
       
        for sublist in search_:
            if sublist[search_column] == searching_element:
                search_result.append(sublist)
                search_result.insert(0,heading)
                table3=AsciiTable(search_result)
                print(table3.table)
                break

    answers3 = inquirer.prompt(questions3)
    continue_=answers3['continue']
    if continue_:
        continue
    else:
        break