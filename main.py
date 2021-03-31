import requests
import json
from termcolor import colored
from os import system, name 
from time import sleep 
  
def clear(): 
  system("clear")

print(colored("""██╗██████╗   """, "red"))
print(colored("""██║██╔══██╗██╗""", "yellow"))
print(colored("""██║██████╔╝╚═╝""", "green"))
print(colored("""██║██╔═══╝ ██╗""", "cyan"))
print(colored("""██║██║     ╚═╝""", "blue"))
print(colored("""╚═╝╚═╝        """, "magenta"))

ip = input("Please enter an IP: ")

response = requests.get("https://geolocation-db.com/json/" + ip + "&position=true").json()

clear()
sleep(1)

from termcolor import colored

def listToString(data):  
    str1 = ""  
     
    for ele in data:  
        str1 += ele   
    
    return str1  

string = """
██╗      ██████╗  █████╗ ██████╗ ██╗███╗   ██╗ ██████╗          
██║     ██╔═══██╗██╔══██╗██╔══██╗██║████╗  ██║██╔════╝          
██║     ██║   ██║███████║██║  ██║██║██╔██╗ ██║██║  ███╗         
██║     ██║   ██║██╔══██║██║  ██║██║██║╚██╗██║██║   ██║         
███████╗╚██████╔╝██║  ██║██████╔╝██║██║ ╚████║╚██████╔╝██╗██╗██╗
╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚═════╝ ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝╚═╝╚═╝                                 
"""

data = []

for line in string.split('\n'):
    first_part = line[0:]
    data.append([first_part])

print(colored(listToString(data[1]), "red"))
print(colored(listToString(data[2]), "yellow"))
print(colored(listToString(data[3]), "green"))
print(colored(listToString(data[4]), "cyan"))
print(colored(listToString(data[5]), "blue"))
print(colored(listToString(data[6]), "magenta"))

sleep(1)
clear()
print(colored("""██╗      ██████╗  ██████╗ █████╗ ████████╗██╗ ██████╗ ███╗   ██╗""", "red"))
print(colored("""██║     ██╔═══██╗██╔════╝██╔══██╗╚══██╔══╝██║██╔═══██╗████╗  ██║██╗""", "yellow"))
print(colored("""██║     ██║   ██║██║     ███████║   ██║   ██║██║   ██║██╔██╗ ██║╚═╝""", "green"))
print(colored("""██║     ██║   ██║██║     ██╔══██║   ██║   ██║██║   ██║██║╚██╗██║██╗""", "cyan"))
print(colored("""███████╗╚██████╔╝╚██████╗██║  ██║   ██║   ██║╚██████╔╝██║ ╚████║╚═╝""", "blue"))
print(colored("""╚══════╝ ╚═════╝  ╚═════╝╚═╝  ╚═╝   ╚═╝   ╚═╝ ╚═════╝ ╚═╝  ╚═══╝""", "magenta"))
print(response["city"]+",", response["state"]+",", response["country_name"])
print("Postal:",response["postal"]+"\n")

print(colored(""" ██████╗ ██████╗  ██████╗ ██████╗ ██████╗ ███████╗""", "red"))
print(colored("""██╔════╝██╔═══██╗██╔═══██╗██╔══██╗██╔══██╗██╔════╝██╗""", "yellow"))
print(colored("""██║     ██║   ██║██║   ██║██████╔╝██║  ██║███████╗╚═╝""", "green"))
print(colored("""██║     ██║   ██║██║   ██║██╔══██╗██║  ██║╚════██║██╗""", "cyan"))
print(colored("""╚██████╗╚██████╔╝╚██████╔╝██║  ██║██████╔╝███████║╚══╝""", "blue"))
print(colored(""" ╚═════╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚═════╝ ╚══════╝""", "magenta"))
print("("+str(response["latitude"])+",",str(response["longitude"])+") (Approximated)")
