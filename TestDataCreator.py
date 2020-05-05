# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 10:51:00 2020

@author: Sreekesh
"""

import pandas as pd
from random import randint
from datetime import datetime

varchar_list1 = ['AAABBBB', 'BBBBCCCC','CCCCCDDDD','DDDDDEEEEE','EEEEFFFF','GGGGGHHH','HHHHHIIIIII','IIIIIJJJJJ','JJJKKKK','KKKKLLLL','LLLLLLLMM']
numcal = 123456
flag = 0
iteration = 0
listvar = []

df = pd.DataFrame()
df = pd.read_csv("E:\\PythonTestCreation\\TestCol.csv")

df_to_print = pd.DataFrame()

while iteration <= 488:
    
    listvar = []
    flag = 0
    while flag <= 30000 :
        
        if df.columns[iteration][0:10] == "Var_column":
            item = randint(0,9)
            listvar.append(df.columns[iteration] + "_" + varchar_list1[item] + str(flag))
        
        elif df.columns[iteration][0:9] == "TimeStamp" or df.columns[iteration][0:9] == "DateTime_" :
            now = datetime.now()
            
            listvar.append(now)

        elif df.columns[iteration][0:10] == "Int_column":
            
            listvar.append(numcal + randint(0,99))
            
        elif df.columns[iteration][0:7] == "Decimal":
            
            listvar.append(5000.456454)
            
        elif df.columns[iteration][0:7] == "Numeric":
            
            listvar.append(numcal/randint(1,9))
            
        elif df.columns[iteration][0:5] == "Char_":
            
            item = randint(0,9)
            listvar.append(df.columns[iteration] + "_" + varchar_list1[item] + str(flag))
        elif df.columns[iteration][0:4] == "Bit_":
            listvar.append(randint(0,1))
            
        flag+=1
    df_to_print.insert(iteration,df.columns[iteration],listvar)
    
    iteration+=1
    
df_to_print.to_csv("E:\\PythonTestCreation\\TestData.csv")
