#!/usr/bin/python3

########################################################################################################
# Name: Extract_Email_CardNumber_Pancard_MobileNumber from text file
# Author: Jayvardhan Singh (singh.jayvardhan06@gmail.com )
#
# Version: 1.0
# Last Updated: 02 May 2021
#
# Description:  A python script for automating extract email, card number, pancard, mobile number.
#
# Usage: 	$ python3 extract_email_cardnumber_pancard_mobile.py file.txt
#
# Requirements: This script requires python 3 to be installed.
#
#########################################################################################################


import sys
import re

def menu():
    print("[1]. Email Id Search")
    print("[2]. Card Number Search")
    print("[3]. Pancard Number Search")
    print("[4]. Phone/Mobile Number Search")
    print("[0]. Quit")

def help():
    print(sys.argv[0] + " input_filename.txt")
    exit(1)

option=99 #define option`g

try:
    file_name = sys.argv[1]
    with open(file_name, "r") as file:
        p = file.readlines()
except:
    print("[!] Error while opening the input file")
    help()

while option !=0:

    menu()
    try:
        option = int(input("Enter your option :"))
    except:
        print("[!] Invalid option. Choose between 0-4\n")

    if option == 1:
        for line in p:
            if re.search(r"^.+@[^.].*\.[a-z]{2,10}$", line, re.IGNORECASE):
                line = line.strip()
                print(line)
                print()

    elif option == 2:
        for line in p:
            if re.search(r"^((4\d{3})|(5[1-5]\d{2})|(6011)|(34\d{1})|(37\d{1}))-?\s?\d{4}-?\s?\d{4}-?\s?\d{4}|3[4,7][\d\s-]{15}$", line, re.IGNORECASE):
                line = line.strip()
                print(line)
                print()

    elif option == 3:
        for line in p:
            if re.search(r"^[A-Z]{5}\d{4}[A-Z]$", line, re.IGNORECASE):
                line = line.strip()
                print(line)
                print()

    elif option == 4:
        for line in p:
            if re.search(r"^\s*(?:\+?(\d{1,3}))?[-. (]*(\d{3})[-. )]*(\d{3})[-. ]*(\d{4})(?: x(\d+))?\s*$", line, re.IGNORECASE):
                line = line.strip()
                print(line)
                print()

    elif option == 0:
        print("\nThank you! Good bye!\n")
        exit(1)

    else:
        print()
        print("Invalid option. Choose between 0-4\n")



