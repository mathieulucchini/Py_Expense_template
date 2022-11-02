from ast import Str
from cmath import exp
import csv
from random import choices
from secrets import choice
from PyInquirer import prompt

expense_questions = [
    {
        "type":"input",
        "name":"amount",
        "message":"New Expense - Amount: ",
    },
    {
        "type":"input",
        "name":"label",
        "message":"New Expense - Label: ",
    },
    {
        "type":"list",
        "name":"spender",
        "message":"New Expense - Spender: ",
        "choices": []
    },
    {
        "type":"checkbox",
        "name":"concerned_users",
        "message":"Who is concerned by this expense ?",
        "choices": [],
    },
]



def new_expense(*args):

    """Récupération de la liste des users pour choisir le spender"""
    data = []
    with open('users.csv', newline='') as f:
        reader = csv.reader(f)
        data = list(reader)
    user_list = []
    for user in data:
        user_list.append(user[0])
    expense_questions[2]['choices'] = user_list

    for user in user_list :
        expense_questions[3]['choices'].append({"name" : user})

    infos = prompt(expense_questions)

    """On vérifie que le spender fait partie des utilisateurs concernés"""
    isSpenderInvolved = False
    for user in infos['concerned_users']:
        if user == infos['spender']:
            isSpenderInvolved = True
    if  not isSpenderInvolved:
        infos['concerned_users'].append(infos['spender'])

    """ On ecrit les données dans le csv"""
    f = open('expense_report.csv', 'a')
    line = infos['amount'] + ',' + infos['label'] + ',' + infos['spender'] + ','


    """On ecrit les participants dans le csv"""
    for user in infos['concerned_users']:
        line += user + ','
    line = line[:-1]
    line += '\n'
    f.write(line)
    
    f.close
    print("Expense Added !")
    return True


