#!/usr/bin/env python3

import tkinter as tk
import mainscreen as ms
import os
import sys
from custom_profile import Profile
import random
import socket
from pathlib import Path
from getpass import getpass
import geocoder
from timezonefinder import TimezoneFinder
import cryptography
from cryptography.fernet import Fernet
from passlib.hash import argon2

path = os.path.dirname(os.path.realpath(__file__))
script_location = Path(__file__).absolute().parent
user_location = script_location / 'users.txt'
key_location = script_location / 'filekey.key'

encryption_on = False

class Location():
    def __init__(self):
        self.timezoneFinder = TimezoneFinder()
        g = self.get_current_latlng()
        self.latitude = float(g[0])
        self.longitude = float(g[1])
        self.timezone = self.timezoneFinder.certain_timezone_at(lat=self.latitude, lng=self.longitude)
    
    def get_current_latlng(self):
        g = geocoder.ip('me')
        return g.latlng

def main():   
    file = open("users.txt", "r")

    # Login "screen"
    login = True
    user_profile = None
    if login:
        creatingaccount = None
        while creatingaccount == None:
            creatingaccount = input("Creating an account? (0/1): ")
        
        if encryption_on:
            try:
                # opening the key
                with open(key_location, 'rb') as filekey:
                    key = filekey.read()
            except:
                # key generation
                key = Fernet.generate_key()
                
                # string the key in a file
                with open(key_location, 'wb') as filekey:
                    filekey.write(key)
            # using the key
            fernet = Fernet(key)

            with open(user_location, 'rb') as user_file:
                encrypted = user_file.read()
            
            decrypted = fernet.decrypt(encrypted)

            with open(user_location, 'wb') as user_file:
                user_file.write(decrypted)
                        

        # TODO: Change all terminal inputs to GUI inputs
        if creatingaccount == '1':
            print("You have enter Account Creation!")
            usrn = input("Enter username: ")
            c = False
            psw = 1
            psw2 = -1
            while(psw != psw2):
                if c != False:
                    print("Passwords did not match. Please re-try.")
                psw = input("Enter password: ")
                psw2 = input("Confirm password: ")
                c = True
            lic = input("Enter plate information (eg. ABC-123): ")
            st = input("Enter state of plates: ")
            em = input("Enter email: ")

            h = argon2.hash(psw)

            ss = usrn + ',' + h + ',' + lic + ',' + st + ',' + em
            with open(user_location, "a") as fs:
                fs.write("\n" + ss)
            
            user_profile = Profile(usrn, h, [lic, st], em)
            
        else:
            logginin = None
            while logginin == None:
                logginin = input("Logging in? (0/1): ")
            if logginin == '0':
                sys.exit(1) # What are you doing here?
            else:
                logged_in = False
                indx = None
                while logged_in == False:
                    username = None
                    passw = None
                    username = input("Enter username: ")
                    passw = getpass("Enter password: ")

                    username_found = False
                    password_found = False
                    users = file.readlines()

                    ##
                    # checking pass with hash
                    for i in range(0, len(users)):
                        if username_found == True and password_found == True: break
                        for j in range(0, len(users[i])):
                            if users[i][j] == ',':
                                #print("user found: ", users[i][0:j])
                                if users[i][0:j] == username:
                                    username_found = True
                                else:
                                    break
                                cc = 0
                                for k in range(j+1, len(users[i])):
                                    if users[i][k] == ',' and cc != 3:
                                        cc = cc + 1
                                    if users[i][k] == ',' and cc == 3:
                                        #print("hash h type: ", users[i][j+1:k])
                                        #print("password type: ", passw)
                                        if argon2.verify(passw, users[i][j+1:k]):
                                            password_found = True
                                            current_user = users[i]
                                            indx = k + 1
                                            break
                                        else:
                                            continue
                    ##
                    if not username_found:
                        print("Invalid username.")
                    elif not password_found:
                        print("Invalid password.")
                    else:
                        logged_in = True
                        lis = None
                        state = None
                        email = None
                        cc = 0
                        for i in range(indx, len(current_user)):
                            if current_user[i] == ',' and cc == 0:
                                cc = 1
                                lis = current_user[indx:i]
                                indx = i+1
                                continue
                            if current_user[i] == ',' and cc == 1:
                                state = current_user[indx:i]
                                cc = 2                            
                                email = current_user[i+1:]
                                break
                        
                        #print("final username: ", username)
                        #print("final password: ", passw)
                        #print("final lis: ", lis)
                        #print("final state: ", state)
                        #print("final email: ", email)

                        # 2FA
                        import smtplib, ssl

                        loc = Location()
                        sender_email = "rrgusa.dev@gmail.com"
                        port = 465  # For SSL
                        password = getpass("Type your dev email password: ") # TODO: keep this stored in an encrypted file
                        receiver_email = email
                        otp = random.randint(1000000, 9999999)
                        
                        message = """\
                        Subject: Messaging App 2FA
                        
                        Hey """ + username + """

                        Your access code is: """ + str(otp) + """

                        Login Information:
                        Host Name: """ + str(socket.gethostname()) + """
                        IP Address: """ + str(socket.gethostbyname(socket.gethostname())) + """
                        Latitude: """ + str(loc.latitude) + """
                        Longitude: """ + str(loc.longitude) + """
                        Timezone: """ + str(loc.timezone) + """

                        If you are not trying to access your account, please change your password immediately.
                        Disclaimer:
                        This message is sent from Python. Please do not reply."""

                        # Create a secure SSL context
                        context = ssl.create_default_context()
                        with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
                            server.login("rrgusa.dev@gmail.com", password)
                            server.sendmail(sender_email, receiver_email, message)
                        
                        gg = input("Enter your access code: ")
                        if gg != str(otp):
                            print("You are a puny hacker and I am the boogeyman. Good Luck!")
                            sys.exit(1)
                        #######
                        
                        #print("username: ", username)
                        # TODO: Set the user profile with provided information

        if encryption_on:
            with open(user_location, 'rb') as user_file:
                original = user_file.read()
            
            encrypted = fernet.encrypt(original)

            with open(user_location, 'wb') as user_file:
                user_file.write(encrypted)

    # TODO: Connect to main menu

if __name__ == '__main__':
    main()
