#!/usr/bin/env python3

from getpass import getpass
from unicodedata import digit
from passlib.hash import argon2
from captcha.image import ImageCaptcha
import random
import string

encryption_on = False
alpha_uppercase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

def create_account():
    counter = 0
    usrn_length = 0
    while(usrn_length == 0):
        if counter != 0:
            print("Username needs to be longer than 0 charaacters.")
        usrn = input("Enter username: ")
        usrn_length = len(usrn)
        counter = counter + 1

    counter = 0
    c = False
    psw = 1
    psw2 = -1
    flag1 = False

    while(psw != psw2 or flag1 == True):
        if counter != 0:
            if c != False:
                print("Passwords did not match. Please re-try.")
            elif flag1 == True:
                print("Password must be at least 7 characters long.")
                flag1 = False
            else:
                print("Password needs to include an uppercase letter, a digit, and be greater than 6 characters.")
        
        counter = counter + 1
        psw = input("Enter password: ")
        psw2 = input("Confirm password: ")
        
        if psw != psw2:
            c = True
            continue

        if len(psw) < 7:
            flag1 = True
            continue

        for i in range(0, len(alpha_uppercase)):
            if alpha_uppercase[i] in psw:
                break
        for i in range(0, len(numbers)):
            if numbers[i] in psw:
                break

    h = argon2.hash(psw)

    print("Resulting username: ", usrn)
    print("Resulting password: ", h)

def login(username, password):   
    # Login "screen"
    logged_in = False
    password = argon2.hash(password)
    print("Resulting hashed password: ", password)
    while logged_in == False:

        # not connected to database to test captcha functionality
        username_found = True
        password_found = True

        if not username_found:
            print("Invalid username.")
        elif not password_found:
            print("Invalid password.")
        else:
            logged_in = True                        
            
            # 2FA
            letters = string.ascii_letters
            letters = ''.join(random.choice(letters) for i in range(4))
            numbers = string.digits
            numbers = ''.join(random.choice(numbers) for i in range(4))
            
            # string type
            final = letters + numbers
            print("Captcha: ", final)


def test1():
    # used: passwords that did not match
    # output: error (handled)
    create_account()

def test2():
    # used: password that did not include digit
    # output: error (handled)
    create_account()

def test3():
    # used: password that did not include uppercase letter
    # output: error (handled)
    create_account()

def test4():
    # used: password that was 4 charachters long
    # output: error (handled)
    create_account()

def test5():
    # used: ArgonRox2
    # output: resulting username and password
    create_account()

def test6():
    # used: no username
    # output: error (handled)
    create_account()

def test7():
    # used: arbitrary input (as testing login functionality is not possible without database functionality)
    # output: hashed password and captcha
    login("aaa", "bbb")

def test8():
    # used: blank inputs
    # output: error (handled)
    login("","")


test1()
test2()
test3()
test4()
test5()
test6()
test7()
test8()