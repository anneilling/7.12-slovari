from module1 import *
from keyboard import *
Countries={}     #Создаем словарь с помощью литерала
Countries=dict() #Создал пустой словарь под названием Countries
Capitals={}     #Создаем словарь с помощью литерала
Capitals=dict()     #Создал пустой словарь под названием Capitals
Countries=loe_failist_listisse("riigid.txt")
Capitals=loe_failist_listisse("pealinn.txt")

for country in Countries:
    if country in Capitals:
        print('Столица страны ' + country + ': ' + Capitals[country])
    else:
        print('В базе нет страны c названием ' + country) #Проверим, есть ли она в словаре Capitals



riigid=loe_failist_listisse("riigid.txt")
pealinn=loe_failist_listisse("pealinn.txt")
