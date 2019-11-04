#!/usr/bin/env python

# -*- coding: utf-8 -*-

import gspread
import json

from collections import Counter
from itertools import chain
from janome.tokenizer import Tokenizer
from pprint import pprint

# Service Account Credentials
from oauth2client.service_account import ServiceAccountCredentials 

# set API(must)
scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']

# set credentials(use downloaded json file)
credentials = ServiceAccountCredentials.from_json_keyfile_name('HOGEHOGE.json', scope)

# login Google API by OAuth2
gc = gspread.authorize(credentials)

# set spreadsheet key(must modify)
SPREADSHEET_KEY = 'PIYOPIYO'

# open spread sheet(sheet1)
worksheet = gc.open_by_key(SPREADSHEET_KEY).sheet1

# read Col.A
col = 0
data = []
each_data = []
t = Tokenizer()
#for row in range(worksheet.row_count):
for row in range(7):
    val = worksheet.cell(row + 1, col + 1).value
    tokens = t.tokenize(val)
    for token in tokens:
        partOfSpeech = token.part_of_speech.split(',')[0]
        each_data.append([token.surface, token.part_of_speech])
    data.append(each_data)
    each_data = []

for row in range(len(data)):
    pprint(data[row])
    for col in range(len(data[row])):
        worksheet.update_cell(row + 1,col + 2, data[row][col][0])
