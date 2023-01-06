# -*- coding: utf-8 -*-
"""
Created on Tue Jan  3 10:03:49 2023

@author: @N$#!T
"""

import pickle
import json
import datetime
import os
import pandas

def Choose():
    Choice = int(input('Enter 1 if you want to search an item (sales_id). \nEnter 2 if you want to insert a new record. \n\nPlease enter your choice: '))
    if Choice == 1:
        FetchRecords()
    elif Choice == 2:
        InsertRecords()
    else:
        print("try again")
        
def WriteToFile(DataToWrite):
    FilePath = CheckForFile()
    with open(FilePath, 'wb') as File:   
        pickle.dump(DataToWrite, File)

def ReadFile():
    FilePath = CheckForFile()
    if os.path.getsize(FilePath) == 0:
        print('Empty')
        return None
    else:
        print("Not Empty")
        with open(FilePath, 'rb') as File:
            ReadOnlyFileData = pickle.load(File)
        return ReadOnlyFileData

def CheckForFile():
    FolderPath = './'
    FileName = ('sales3.txt')
    FilePath = FolderPath + FileName
    FileStatus = os.path.exists(FilePath)
    if FileStatus:
        return FilePath
    else:
        with open(FilePath, 'w') as File:
            pass
        return FilePath

def TotalDataToWrite(DataToEnter):
    FilePath = CheckForFile()
    if os.path.getsize(FilePath) == 0:
        AllRecords = []
        AllRecords.append(DataToEnter)
    else:
        AllRecords = ReadFile()
        AllRecords.append(DataToEnter)
    WriteToFile(AllRecords)
    
def DisplayAllRecords():
    ReadOnlyFileData = ReadFile()
    if ReadOnlyFileData == None:
        print('File is empty')
    else:
        print(type(ReadOnlyFileData))
        print(ReadOnlyFileData)
    
def FetchRecords():
    SalesIdToFetch = input("Enter the sales id to fetch: ")
    ReadOnlyFileData = ReadFile()
    if ReadOnlyFileData == None:
        print('File is empty')
    else:
        for Row in ReadOnlyFileData:
            if str(Row['sales_id'])==str(SalesIdToFetch):
                print(Row)

def InsertRecords():
    NewRecord={}
    OldRecords = ReadFile()
    if OldRecords == None:
        NewRecord['sales_id'] = 'ARX' + datetime.date.today().strftime('%d%m%y' + 'YN') + (str(1).zfill(5))
    else:
        NewRecord['sales_id'] = 'ARX' + datetime.date.today().strftime('%d%m%y' + 'YN') + (str(len(OldRecords)+1).zfill(5))
    NewRecord['product_name'] = input("Enter the product name: ")
    NewRecord['Price'] = int(input("Enter the price of individual product: "))
    NewRecord['Qty'] = int(input("Enter the no. of products: "))
    NewRecord['Total_Sales'] = NewRecord['Price'] * NewRecord['Qty']
    NewRecord['Date'] = datetime.date.today().strftime('%d-%m-%Y')
    
    if NewRecord['Price']*NewRecord['Qty'] == NewRecord['Total_Sales']:
        TotalDataToWrite(NewRecord)
    else:
        NewRecord['Total_Sales'] = NewRecord['Price']*NewRecord['Qty']
        TotalDataToWrite(NewRecord)
        
# def ArchiveFile():
#     AllRecords = ReadFile()
#     if AllRecords:
#         AllRecords = pandas.DataFrame(AllRecords)
#         AllRecords.to_parquet('df.parquet.gzip',compression = 'gzip', partition_cols = 'Date')
#         pandas.read_parquet('df.parquet.gzip')
#     else:
#         print('No data to archive. File Empty.')
        
    
# ArchiveFile()
Choose()
DisplayAllRecords()