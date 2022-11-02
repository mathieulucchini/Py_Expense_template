from ast import Str
from asyncore import read
from csv import reader
from PyInquirer import prompt

def show_status():
    """On récupère les users et on les met dans une liste de dico"""
    status = []
    f = open('users.csv', 'r')
    f_reader = reader(f)
    for row in f_reader:
        status.append({"name": row[0], "debt": 0, "to": ""}) 
    f.close

    """On affecte les dettes"""
    file = open('expense_report.csv', 'r')
    file_reader = reader(file)
    for row in file_reader:
        val = row[0]
        spender = row[2]
        participants = []
        for i in range (2, len(row) - 1):
            participants.append(row[i])
        for participant in participants:
            if participant != spender:
                for sta in status:
                    if sta["name"] == participant and sta["name"] != spender:
                        sta["debt"] += (int(val) / len(participants))

            else:
                for st in status:
                    if st["name"] == participant:
                        st["debt"] -= (int(val) - (int(val) / len(participants)))

        """On associe les débiteurs a la personne qu'ils doivent rembourser"""
        in_negativ = ""
        for statut in status:
            if statut["debt"] < 0:
                in_negativ = statut["name"]
        
        for statut in status:
            if statut["debt"] > 0 and statut["name"] != in_negativ:
                statut["to"] = in_negativ
    
        """Si une personne a une dette négative, on lui doit de l'argent, on met sa dette à 0"""
        for statut in status:
            if statut["debt"] < 0:
                statut["debt"] = 0


    """On print le résultat"""    
    for statut in status:
        if statut['debt'] == 0:
            print(statut['name'] + " owes nothing")
        else :    
            print(statut['name'] + " owes " + str(statut['debt']) + " to " + statut['to'])
    