import os as subroutine
import datetime
import time

appdata = "C:\\Users\\Masked Musketeer\\AppData\\Roaming"
documents = "C:\\Users\\Masked Musketeer\\Documents"
destinationFolder = "D:\\BackupTool\\files"
flagfile = "D:\\BackupTool\\FolderFlag.txt"
flagList = []

def flagRead(file,list):
    file = open(flagfile, mode = 'r', encoding = 'utf-8')
    for item in file:
        list.append(item)

def copyOver():
    