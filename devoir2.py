# coding : utf-8 

#partir d'un document json pour créer un fichier csv 

import json 
import csv 

with open("lobby.json") as file 
     data = json.load(file)

fichiernom = "lobby1.csv"

with open(fichiernom, "w") as file 
     csv_file = csv.writer(file)
     csv_file.writerow["client_org_corp_num","fr_client_org_corp_nm","en_client_org_corp_nm","date_comm", "objet", "objet_autre", "institution"]
    for item in data ["resultats"]: 
        csv_file.writerow([item['client_org_corp_num'],item['fr_client_org_corp_nm'],item['en_client_org_corp_nm'],item['date_comm'],item['objet'],item['objet_autre'],item['institution']])


print(fichiernom)











    











