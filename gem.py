#!/usr/bin/env python
import requests
import json
import argparse
import os
""" 
Features:
    Retreive APi key from bashrc
    Variable output through flag usage
    Help command
    v2 - Format response - tabbed in + ?
    v1 - Preconfigured verbosity flags? cyclic calls to the api
    v2 - Formatting options?
"""
api_key=os.environ['gemini_api_key']
#stets


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
    
    def printArgs(self):
        for ar in vars(self.myArgs):
            print(ar, getattr(self.myArgs, ar))
        return
    
    def printResponse(self):
        print("\n- - -      - - -      - - -      - - -")
        print(self.responseText)
        print("- - -      - - -      - - -      - - -\n")
        if self.myArgs.usageData or self.myArgs.all:
            print("| Usage MetaData:      - - -      - - -      - - -\n")
            print(self.usageMetadata)
        if self.myArgs.finishReason or self.myArgs.all:
            print("| Finish Reason:      - - -      - - -      - - -\n")
            print(self.finishReason)
        if self.myArgs.safetyRatings or self.myArgs.all:
            print("| Safety Ratings:      - - -      - - -      - - -\n")
            print(self.safetyRatings)

    def responseFormatter(self): #wip
        t = self.responseText

        print(t)
        print("##################################################")
        print(t.replace('\n',' '))

def main():
    #build parser arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('-gem', '--gemini', action='store_true')
    parser.add_argument('-sr', '--safetyRatings', action='store_true')
    parser.add_argument('-ud', '--usageData', action='store_true')
    parser.add_argument('-fr', '--finishReason', action='store_true')
    parser.add_argument('-ci', '--chatIndex', action='store_true')
    parser.add_argument('-a', '--all', action='store_true')
    parser.add_argument('prompt')
    arggs = parser.parse_args()

    #Create Gemini client instance + initiate call w/ prompt
    g = gem(arggs)
    g.gemCall()

    g.printResponse()
    # g.responseFormatter()

if __name__ == "__main__":
    main()


