# -*- coding: utf-8 -*-
"""Assignement_5.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1g2JHB3R4k5oLpC_DO2hTsYe0WfU8J097
"""

My_Dict = {
        'person_1': {'name': ' Abdul Rafay', 'age': 22, 'Interests': ['football,cricket'],
                     'amount_deposited': [24000, 26000]},
        'person_2': {'name': 'Nancy James', 'age': 23, 'Interests': ['baseball,cricket'],
                     'amount_deposited': [24000, 27000]},
        'person_3': {'name': 'Selena Gomez', 'age': 26, 'Interests': ['baseball,table tennis'],
                     'amount_deposited': [24000, 28000]}
    }

from functools import reduce
from datetime import date
import datetime

def get_alphabet_excluding_chars(tpl_chars):
    #method below is called list comprehension
    alphabets = [chr(i)  for i in range(97, 123) if i not in tpl_chars]
    return tuple(alphabets)

def get_alphabet_between(_fromChar, _toChar):
    #method below is called list comprehension
    alphabets = [chr(i)  for i in range(_fromChar, _toChar) ]
    return tuple(alphabets)

def get_persons(dict):
    persons = dict.keys()
    return persons

def get_Names(dict):
    lst_persons = get_persons(dict)
    lst_Names = []

    for person in lst_persons:
        lst_Names.append(dict[person]['name'].strip())
    return lst_Names

def process_person_name(dict):
   
    #Get the list of persons in the dictionary
    lst_persons = get_persons(dict)

    #Get list of Names from Dictionary
    lst_Names = get_Names(dict)

    #Cocatenate either Mr. or Ms. with each Name depending upon starting character of Name
    #if Start character is a-g then concatenate Mr. or Ms. otherwise
    func_concatenate = lambda x: \
        'Mr. ' + x if str(x).lower().startswith(get_alphabet_between(97, 104)) \
        else 'Ms. ' + x
    lst_Names_concatenated = list(map(func_concatenate, lst_Names))

    #Filter the names of the persons as per provided condition
    #condition is that remove the person data if his/her name starts with ’s’,’m’ or ‘k’
    tpl_characters = (107, 109, 115)  # 'k','m','s'
    func_filter = lambda x:str(x.split(' ')[1])[0].lower().startswith(get_alphabet_excluding_chars(tpl_characters))
    lst_names_filtered = list(filter(func_filter, lst_Names_concatenated))

    #Update the Names of persons in the dictionary
    intIndex = 0
    current_year = date.today().year

    for person in lst_persons:
        try:
            str_person_Name = person
            if str(dict[person]['name']).strip().split(' ')[0][0].lower() == \
                    str(lst_names_filtered[intIndex]).strip().split(' ')[1][0].lower():
                dict[person]['name'] = lst_names_filtered[intIndex]
                dict[person]['Year'] = current_year - int(dict[person]['age']) -1
                dict[person]['amount_deposited'] = reduce(lambda x,y:x+y, dict[person]['amount_deposited'])
        except Exception:
            # ret_Dict.pop(str_person_Name)
            # del ret_Dict[str_person_Name]
            dict[person]['name'] = 'REMOVE'
        intIndex +=1

    return dict

def remove_invalid_item_from_dict(_dict):
    for key, value in dict(_dict).items():
        nested_dict = value
        for nestedkey, nestedvalue in dict(value).items():
            if nestedvalue == 'REMOVE':
                del _dict[key]

    return  _dict

My_Dict
get_alphabet_excluding_chars((107, 109, 115))
get_alphabet_between(97,104)
get_persons(My_Dict)
process_person_name(My_Dict)
remove_invalid_item_from_dict(My_Dict)

dic_csv = My_Dict.copy() # copying  file 
My_Dict
#Json format data
final_dict = {}
final_dict["current_Date"] = datetime.datetime.now().strftime('%d-%b-%G')
final_dict["Data"] = My_Dict

from google.colab import drive
drive.mount('/content/drive')

with open('names.json', 'w') as fp:
    json.dump(My_Dict, fp, sort_keys=True, indent=4)


#writing CSV file...

import csv

labels = ['Name', 'Age', 'Interests','Year', 'Amount Deposited'] 
dct_arr = [
  {'Name': 'Mr. Abdul Rafay', 'Age': 22,'Interests':'baseball,cricket','Year':1997,'Amount Deposited':50000},
  {'Name': 'Ms. Nancy James', 'Age': 23,'Interests':'baseball,cricket','Year':1998,'Amount Deposited':51000}
  ]

try:
    with open('names.csv', 'w') as f:
        writer = csv.DictWriter(f, fieldnames=labels)
        writer.writeheader()
        for elem in dct_arr:
            writer.writerow(elem)
except IOError:
    print("I/O error")

#viewing csv file...

import pandas as pd
pd.read_csv('names.csv')