# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 03:39:38 2021

@author: frees
"""

import requests
import sys

def main():
    url = "https://notify-api.line.me/api/notify"
    token = 'ro1pFOT1mZwssynsxRbi9UUNP7abn1sWPjIGU18JQg8'
    headers = {"Authorization" : "Bearer "+ token}

    args = sys.argv
    print(args)
    if args[0] == 1:
        message =  'finished from cmd'
    else :
        message = args[0] + 'の実行終わったよ'
    payload = {"message" :  message}
    files = {"imageFile": open("end.jpg", "rb")}

    r = requests.post(url ,headers = headers ,params=payload, files=files)

if __name__ == '__main__':
    main()