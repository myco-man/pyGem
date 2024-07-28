#!/usr/bin/env python

import gem 
import argparse
 
helpMessage ="You have been helped!"

def main():
    #build parser arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('-gem', '--gemini', action='store_true')
    parser.add_argument('-sr', '--safetyRatings', action='store_true', help="lists the safety rating returned")
    parser.add_argument('-ud', '--usageData', action='store_true')
    parser.add_argument('-fr', '--finishReason', action='store_true')
    parser.add_argument('-ci', '--chatIndex', action='store_true')
    parser.add_argument('-a', '--all', action='store_true')
    #parser.add_argument('--help', action='store_true')
    # parser.add_argument('-h', '--help', action='help', default=argparse.SUPPRESS, help=helpMessage)
    parser.add_argument('prompt')
    arggs = parser.parse_args()
    i = ""
    while i != 'exit':
    #Create Gemini client instance + initiate call w/ prompt
        g = gem.gem(arggs)
        g.gemCall()
        g.printResponse()
        i = input().lower()
        g.setPrompt(i)
if __name__ == "__main__":
    main()