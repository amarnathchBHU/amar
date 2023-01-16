#!/bin/python 
import json

def print_dict(k,v, sp):
    if(type(v) is dict):
        print(sp, k, "-->")
        for sk,sv in v.items():
            print_dict(sk,sv, sp+"     ")
    elif (type(v) is list):
        print(sp, k, "-->")
        for i in v:
            print_dict("",i, sp+"   ")    
    else:
        print(sp, k, "-->", v)




# some JSON:
jsonData =  '''{"menu": {
  "id": "file",
  "value": "File",
  "popup": {
    "menuitem": [
      {"value": "New", "onclick": "CreateNewDoc()"},
      {"value": "Save", "onclick": "SaveDoc()"},
      {"value": "Open", "onclick": "OpenDoc()"},
      {"value": "Close", "onclick": "CloseDoc()"},
      {"value": "Validate", "onclick": "ValidateDoc()"}
    ]
  }
}}'''

# parse JSON:
dataDict = json.loads(jsonData)

# the result is a Python dictionary:
print_dict(None,dataDict, "")

# the result is a Python dictionary:
print("----dataDict.menu-----")
print(dataDict["menu"])
print("----dataDict.menu.id-----")
print(dataDict["menu"]["id"])
print("----dataDict.menu.popup.menuitem-----")
print(len(dataDict["menu"]["popup"]["menuitem"]))
print("----dataDict.menu.popup.menuitem[1].value vs Onclick-----")
print(dataDict["menu"]["popup"]["menuitem"][1]["value"], "-->", dataDict["menu"]["popup"]["menuitem"][1]["onclick"])

