__author__ = 'Konstantin'
import collections
import urllib.request
import urllib
import json
import json
import re
import requests

def read():
    file = open('spent.txt', 'r')
    str = file.readlines()
    Dict  = {'0':0}

    print("1", str[5])
    for i in range(2, len(str),4):
        print(i)
        date = (str[i-2])
        dat = date[0:5]
        spent = (str[i-1])
        spend = float(spent[7:11])
        Dict[dat] = spend

        print(dat, spend,"\n", Dict,"\nTotal",sum(Dict.values()))

test = 'test'

name = "{'mainPerson':{'contains':'рибак олександр'}}"
address = "09100+Київська обл.+місто Біла Церква+ВУЛ. ФАСТІВСЬКА+будинок 21-Б"

def ValisName(name):
    print(name)
    adress = name.replace("'", '"')
    print("replaced", adress)
    url = 'http://edr.data-gov-ua.org/api/companies?where='+adress
    print("url", url)
    url = url.replace(" ", "%20")
    print(url)
    print(url)
    print("name", name.split("'")[5])
    getcompany(url)

def ValidAdress(adress):
    print(adress)
    adress = adress.replace(", ", "+")
    print(adress)
    url = 'https://maps.googleapis.com/maps/api/geocode/json?address='+adress
    print("url", url)
    url = url.replace(" ", "%20")
    print(url)
    getadress(url)
    #getinfo(url)


def getcompany(adress):
    r = requests.get(adress)
    print("r", r.json())
    r = r.json()
    companies = []
    adresses = []
    for line in r:
        #print(line)
        print(line["name"])
        comp = line["name"]
        comp = comp.replace('"', "")
        comp = comp.replace("\'", "")
        companies.append(comp)
        adresses.append(line["address"])
    print(companies)
    print(adresses)


def getadress(address):
    mass = []
    r = requests.get(address)
    r = r.json()
    print (">>>>>", r["results"])
    print ("+++", r["results"][0]["geometry"]["location"])


a = 128
b = 128
a = "123"
b = "123"
result = a == b

print(result)
def list():
    a = [1,2,3,4,5]
    for x in a[:]:
        print(x)
list()
# ValidAdress(address)
# ValisName(name)