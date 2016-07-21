#!/usr/bin/env python

keys = []
values = []
dict1 = {}
dict2 = {}
with open('config.txt','r') as archivo:
    for linea in archivo:
        keys.append(linea.split('\t')[0])
        values.append(linea.split('\t')[1][:-1])
        dict1[linea.split('\t')[0]] = linea.split('\t')[1][:-1]

print(dict1)        
print(dict1.keys())

if '3' not in dict1.keys():
    print('siiii')