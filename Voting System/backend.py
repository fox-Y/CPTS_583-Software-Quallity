from matplotlib.pyplot import connect
import mysql.connector
from mysql.connector import Error
import Application

#Add candidate information
def addCandidate(can_name,gender,position,party_symbol):
  try:
    #First step
    connection = mysql.connector.connect(host='localhost',
                                        database='voting',
                                        user='root',
                                        password='123456')
    #Second step
    cursor = connection.cursor()
    #Third step
    cursor.execute("insert into candidate_info(can_name,gender,position,party_symbol,no) values(%s,%s,%s,%s)",(can_name,gender,position,party_symbol))
    connection.commit()
  except Error as e:
    print("Error while connecting to mySQL", e)
  finally:
    if connection.is_connected():
      cursor.close()
      connection.close()

#Delete candidate information
def delCandidate(can_name):
  try:
    #First step
    connection = mysql.connector.connect(host='localhost',
                                        database='voting',
                                        user='root',
                                        password='123456')
    #Second step
    cursor = connection.cursor()
    #Third step
    cursor.execute("delete from candidate_info where can_name = %s", can_name)
    connection.commit()
  except Error as e:
    print("Error while connecting to mySQL", e)
  finally:
    if connection.is_connected():
      cursor.close()
      connection.close()

#Modify candidate information
def modifyCandidate():
  try:
    #First step
    connection = mysql.connector.connect(host='localhost',
                                        database='voting',
                                        user='root',
                                        password='123456')
    #Second step
    cursor = connection.cursor()
    #Third step
    cursor.execute("select database();")
    connect.commit()
  except Error as e:
    print("Error while connecting to mySQL", e)
  finally:
    if connection.is_connected():
      cursor.close()
      connection.close()

#Nominate candidate
def nominateCandidate(can_name):
  try:
    #First step
    connection = mysql.connector.connect(host='localhost',
                                        database='voting',
                                        user='root',
                                        password='123456')
    #Second step
    cursor = connection.cursor()
    #Third step
    cursor.execute("update candidate_info set nomination = 'yes' where can_name = %s", can_name)
    connection.commit()
  except Error as e:
    print("Error while connecting to mySQL", e)
  finally:
    if connection.is_connected():
      cursor.close()
      connection.close()

#Search candidate by name
def searchCandidate(can_name):
  try:
    #First step
    connection = mysql.connector.connect(host='localhost',
                                        database='voting',
                                        user='root',
                                        password='123456')
    #Second step
    cursor = connection.cursor()
    #Third step
    cursor.execute("select * from candidate_name where can_name = %s", can_name)
    connection.commit()
  except Error as e:
    print("Error while connecting to mySQL", e)
  finally:
    if connection.is_connected():
      cursor.close()
      connection.close()

#Voter register
def voterRegister(votername,gender,age,position,username,passcode):
  try:
    #First step
    connection = mysql.connector.connect(host='localhost',
                                        database='voting',
                                        user='root',
                                        password='123456')
    #Second step
    cursor = connection.cursor()
    #Third step
    cursor.execute("inter into voter_info() values(%s,%s,%s,%s,%s,%s)",(votername,gender,age,position,username,passcode))
    connect.commit()
  except Error as e:
    print("Error while connecting to mySQL", e)
  finally:
    if connection.is_connected():
      cursor.close()
      connection.close()

#Delete voter information
def delVoter(votername):
  try:
    #First step
    connection = mysql.connector.connect(host='localhost',
                                        database='voting',
                                        user='root',
                                        password='123456')
    #Second step
    cursor = connection.cursor()
    #Third step
    cursor.execute("delete from voter_info where votername = %s", votername)
    connection.commit()
  except Error as e:
    print("Error while connecting to mySQL", e)
  finally:
    if connection.is_connected():
      cursor.close()
      connection.close()

#Voter login
def voterLogin():
  try:
    #First step
    connection = mysql.connector.connect(host='localhost',
                                        database='voting',
                                        user='root',
                                        password='123456')
    #Second step
    cursor = connection.cursor()
    #Third step
    cursor.execute("select database();")
    connect.commit()
  except Error as e:
    print("Error while connecting to mySQL", e)
  finally:
    if connection.is_connected():
      cursor.close()
      connection.close()

#Administor login
def adLogin():
  try:
    #First step
    connection = mysql.connector.connect(host='localhost',
                                        database='voting',
                                        user='root',
                                        password='123456')
    #Second step
    cursor = connection.cursor()
    #Third step
    cursor.execute("select database();")
    connect.commit()
  except Error as e:
    print("Error while connecting to mySQL", e)
  finally:
    if connection.is_connected():
      cursor.close()
      connection.close()