from random import *
def loe_failist_listisse(file:str)->list:
    """Loeme tekst failist ja salvesta järjendisse
    :rtype: list:
    """
    file=open(file,"r")
    list_=[]
    for stroka in file:
        list_.append(stroka.strip())
    file.close()
    return list_
