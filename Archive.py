# -*- coding: utf-8 -*-
"""
Created on Fri Jan  6 10:19:06 2023

@author: ANSHIT
"""

import pickle
import json
import datetime
import os
import pandas

def ArchiveFile():
    AllRecords = ReadFile()
    if AllRecords:
        AllRecords = pandas.DataFrame(AllRecords)
        AllRecords.to_parquet('ArchiveData.parquet.gzip',compression = 'gzip', partition_cols = 'Date')
        pandas.read_parquet('ArchiveData.parquet.gzip')
        os.remove('./sales3.txt')
    else:
        print('No data to archive. File Empty.')

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
    
ArchiveFile()