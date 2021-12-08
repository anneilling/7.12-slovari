from module1 import *
from keyboard import *
Countries={}     #Создаем словарь с помощью литерала
Countries=dict() #Создал пустой словарь под названием Countries
Capitals={}     #Создаем словарь с помощью литерала
Capitals=dict() #Создал пустой словарь под названием Capitals
Countries=loe_failist_listisse("riigid.txt") #читаем файл в список из .txt 
Capitals=loe_failist_listisse("pealinn.txt") #читаем файл в список из .txt 
country=input("Siseta riik => ")

for country in Countries:
    if country in Countries:
        print('Столица страны ' + Capitals[country])
    else:
        print('В базе нет страны c названием ' + country)




       