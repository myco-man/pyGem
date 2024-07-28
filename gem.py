#!/usr/bin/env python
import requests
import json
import argparse
import os
""" 
Features:
    Retreive APi key from bashrc
    Variable output through flag usage
    Help command - flesh out
    v2 - Format response - tabbed in + ?
    v1 - Preconfigured verbosity flags? cyclic calls to the api
    v2 - Formatting options?
"""
api_key=os.environ['gemini_api_key']


class gem:
    myArgs = ""
    finishReason = ""
    safetyRatings = ""
    usageMetadata = ""
    responseText= ""
    chatIndex = ""
    safetyRatings = dict(HARM_CATEGORY_SEXUALLY_EXPLICIT = None, HARM_CATEGORY_HATE_SPEECH = None, HARM_CATEGORY_HARASSMENT= None, HARM_CATEGORY_DANGEROUS_CONTENT = None)
    
    def __init__(self, args) -> None:
        self.myArgs =  args

    def gemCall(self,):
        url = 'https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key='+api_key
        postHeaders = {"Content-Type": "application/json"}
        postData = json.dumps({"contents":[{"parts":[{"text": self.myArgs.prompt}]}]})

        x = requests.post(url, data=postData, headers=postHeaders)
        tx = json.loads(x.text)

        self.responseText=tx["candidates"][0]["content"]["parts"][0]["text"]
        self.safetyRatings=tx["candidates"][0]["safetyRatings"]
        self.usageMetadata=tx["usageMetadata"]
        self.finishReason=tx["candidates"][0]["finishReason"]
        self.chatIndex=tx["candidates"][0]["index"]
    
    def setPrompt(self, newPrompt):
        if newPrompt == 'exit':
            return
        self.myArgs.prompt = newPrompt
       

    def printArgs(self):
        for ar in vars(self.myArgs):
            print(ar, getattr(self.myArgs, ar))
        return
    
    def printResponse(self):
        print("\n- - -      - - -      - - -      - - -")
        print(self.responseText)
        print("- - -      - - -      - - -      - - -\n")
        if self.myArgs.all:
            print("| Usage MetaData:      - - -      - - -      - - -\n")
            print(self.usageMetadata)
           
            print("| Finish Reason:      - - -      - - -      - - -\n")
            print(self.finishReason)
            
            print("| Safety Ratings:      - - -      - - -      - - -\n")
            print(self.safetyRatings)
        else:
            if self.myArgs.usageData:
                print("| Usage MetaData:      - - -      - - -      - - -\n")
                print(self.usageMetadata)
            
            if self.myArgs.finishReason:
                print("| Finish Reason:      - - -      - - -      - - -\n")
                print(self.finishReason)
            
            if self.myArgs.safetyRatings:
                print("| Safety Ratings:      - - -      - - -      - - -\n")
                print(self.safetyRatings)


