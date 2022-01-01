
import pyttsx3
import datetime
import wikipedia
import webbrowser
import time
import subprocess
import requests
import pickle
import os
import pathlib
print('Loading .....')
f=1
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice', 'voices[0].id')


def speak(text):
    engine.say(text)
    engine.runAndWait()

def wishMe():
    hour=datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("Hello,Good Morning")
        print("Hello,Good Morning")
    elif 12 <= hour < 18:
        speak("Hello,Good Afternoon")
        print("Hello,Good Afternoon")
    else:
        speak("Hello,Good Evening")
        print("Hello,Good Evening")


speak("Loading your AI personal assistant G-One")
wishMe()


if __name__=='__main__':


    while f==1:
        speak("Tell me how can I help you now?")
        txt = "Welcome home"
        x = txt.center (20)
        print (x)
        print ("1.OPEN BANK MANAGMENT SYSTEM")
        print ("2.Open youtube")
        print ("3.Search on wikipedia")
        print ("4.Open Google")
        print ("5.Open weather")
        print ("6.Open Gmail")
        print ("7.About me")
        print ("8.open news")
        print ("9.time")
        print ("10.Exit")

        audio: str = input ()
        statement = audio

        if statement==0:

            continue
        if "bank" in statement or "account" in statement or "bank account" in statement or "1" in statement:
            class Account:
                accNo = 0
                name = ''
                deposit = 0
                type = ''

                def createAccount (self):
                    self.accNo = int (input ("Enter the account no : "))
                    self.name = input ("Enter the account holder name : ")
                    self.type = input ("Enter the type of account [C/S] : ")
                    self.deposit = int (input ("Enter The Initial amount(>=500 for Saving and >=1000 for current"))
                    print ("\n\n\nAccount Created")

                def showAccount (self):
                    print ("Account Number : ", self.accNo)
                    print ("Account Holder Name : ", self.name)
                    print ("Type of Account", self.type)
                    print ("Balance : ", self.deposit)

                def modifyAccount (self):
                    print ("Account Number : ", self.accNo)
                    self.name = input ("Modify Account Holder Name :")
                    self.type = input ("Modify type of Account :")
                    self.deposit = int (input ("Modify Balance :"))

                def depositAmount (self, amount):
                    self.deposit += amount

                def withdrawAmount (self, amount):
                    self.deposit -= amount

                def report(self):
                    print (self.accNo, " ", self.name, " ", self.type, " ", self.deposit)

                def getAccountNo (self):
                    return self.accNo

                def getAcccountHolderName (self):
                    return self.name

                def getAccountType (self):
                    return self.type

                def getDeposit (self):
                    return self.deposit


            def intro ():
                print ("\t\t\t\t**********************")
                print ("\t\t\t\tBANK MANAGEMENT SYSTEM")
                print ("\t\t\t\t**********************")

            def writeAccount ():
                account = Account ()
                account.createAccount ()
                writeAccountsFile (account)


            def displayAll ():
                file = pathlib.Path ("accounts.data")
                if file.exists ():
                    infile = open ('accounts.data', 'rb')
                    mylist = pickle.load (infile)
                    for item in mylist:
                        print (item.accNo, " ", item.name, " ", item.type, " ", item.deposit)
                    infile.close ()
                else:
                    print ("No records to display")


            def displaySp (num):
                file = pathlib.Path ("accounts.data")
                if file.exists ():
                    infile = open ('accounts.data', 'rb')
                    mylist = pickle.load (infile)
                    infile.close ()
                    found = False
                    for item in mylist:
                        if item.accNo == num:
                            print ("Your account Balance is = ", item.deposit)
                            found = True
                else:
                    print ("No records to Search")
                if not found:
                    print ("No existing record with this number")


            def depositAndWithdraw (num1, num2):
                file = pathlib.Path ("accounts.data")
                if file.exists ():
                    infile = open ('accounts.data', 'rb')
                    mylist = pickle.load (infile)
                    infile.close ()
                    os.remove ('accounts.data')
                    for item in mylist:
                        if item.accNo == num1:
                            if num2 == 1:
                                amount = int (input ("Enter the amount to deposit : "))
                                item.deposit += amount
                                print ("Your account is updted")
                            elif num2 == 2:
                                amount = int (input ("Enter the amount to withdraw : "))
                                if amount <= item.deposit:
                                    item.deposit -= amount
                                else:
                                    print ("You cannot withdraw larger amount")

                else:
                    print ("No records to Search")
                outfile = open ('newaccounts.data', 'wb')
                pickle.dump (mylist, outfile)
                outfile.close ()
                os.rename ('newaccounts.data', 'accounts.data')


            def deleteAccount (num):
                file = pathlib.Path ("accounts.data")
                if file.exists ():
                    infile = open ('accounts.data', 'rb')
                    oldlist = pickle.load (infile)
                    infile.close ()
                    newlist = []
                    for item in oldlist:
                        if item.accNo != num:
                            newlist.append (item)
                    os.remove ('accounts.data')
                    outfile = open ('newaccounts.data', 'wb')
                    pickle.dump (newlist, outfile)
                    outfile.close ()
                    os.rename ('newaccounts.data', 'accounts.data')


            def modifyAccount (num):
                file = pathlib.Path ("accounts.data")
                if file.exists ():
                    infile = open ('accounts.data', 'rb')
                    oldlist = pickle.load (infile)
                    infile.close ()
                    os.remove ('accounts.data')
                    for item in oldlist:
                        if item.accNo == num:
                            item.name = input ("Enter the account holder name : ")
                            item.type = input ("Enter the account Type : ")
                            item.deposit = int (input ("Enter the Amount : "))

                    outfile = open ('newaccounts.data', 'wb')
                    pickle.dump (oldlist, outfile)
                    outfile.close ()
                    os.rename ('newaccounts.data', 'accounts.data')


            def writeAccountsFile (account):

                file = pathlib.Path ("accounts.data")
                if file.exists ():
                    infile = open ('accounts.data', 'rb')
                    oldlist = pickle.load (infile)
                    oldlist.append (account)
                    infile.close ()
                    os.remove ('accounts.data')
                else:
                    oldlist = [account]
                outfile = open ('newaccounts.data', 'wb')
                pickle.dump (oldlist, outfile)
                outfile.close ()
                os.rename ('newaccounts.data', 'accounts.data')

            ch = ''
            num = 0
            intro ()

            while ch != 8:
                # system("cls");
                print ("\tMAIN MENU")
                print ("\t1. NEW ACCOUNT")
                print ("\t2. DEPOSIT AMOUNT")
                print ("\t3. WITHDRAW AMOUNT")
                print ("\t4. BALANCE ENQUIRY")
                print ("\t5. ALL ACCOUNT HOLDER LIST")
                print ("\t6. CLOSE AN ACCOUNT")
                print ("\t7. MODIFY AN ACCOUNT")
                print ("\t8. EXIT")
                print ("\tSelect Your Option (1-8) ")
                ch = input ()

                if ch == '1':
                    writeAccount ()
                elif ch == '2':
                    num = int (input ("\tEnter The account No. : "))
                    depositAndWithdraw (num, 1)
                elif ch == '3':
                    num = int (input ("\tEnter The account No. : "))
                    depositAndWithdraw (num, 2)
                elif ch == '4':
                    num = int (input ("\tEnter The account No. : "))
                    displaySp (num)
                elif ch == '5':
                    displayAll ()
                elif ch == '6':
                    num = int (input ("\tEnter The account No. : "))
                    deleteAccount (num)
                elif ch == '7':
                    num = int (input ("\tEnter The account No. : "))
                    modifyAccount (num)
                elif ch == '8':
                    print ("\tThanks for using bank managemnt system")
                    break
                else:
                    print ("Invalid choice")

                ch = input ("Enter your choice : ")

        if "good bye" in statement or "ok bye" in statement or "stop" in statement or "exit" in statement:
            speak('shutting down,Good bye')
            print('shutting down,Good bye')
            break



        if 'wikipedia' in statement or "3" in statement:
            speak('Searching Wikipedia...')
            statement =statement.replace("wikipedia", "")
            results = wikipedia.summary(statement, sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'youtube' in statement or "2" in statement:
            webbrowser.open_new_tab("https://www.youtube.com")
            speak("youtube is open now")
            time.sleep(5)

        elif 'google' in statement or '4' in statement:
            webbrowser.open_new_tab("https://www.google.com")
            speak("Google chrome is open now")
            time.sleep(5)

        elif 'gmail' in statement or '6' in statement:
            webbrowser.open_new_tab("gmail.com")
            speak("Google Mail open now")
            time.sleep(5)

        elif "weather" in statement or "5" in statement:
            api_key="8ef61edcf1c576d65d836254e11ea420"
            base_url="https://api.openweathermap.org/data/2.5/weather?"
            speak("whats the city name")
            city_name=audio
            complete_url=base_url+"appid="+api_key+"&q="+city_name
            response = requests.get(complete_url)
            x=response.json()
            if x["cod"]!="404":
                y=x["main"]
                current_temperature = y["temp"]
                current_humidiy = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                speak(" Temperature in kelvin unit is " +
                      str(current_temperature) +
                      "\n humidity in percentage is " +
                      str(current_humidiy) +
                      "\n description  " +
                      str(weather_description))
                print(" Temperature in kelvin unit = " +
                      str(current_temperature) +
                      "\n humidity (in percentage) = " +
                      str(current_humidiy) +
                      "\n description = " +
                      str(weather_description))

            else:
                speak(" City Not Found ")



        elif 'time' in statement or '9' in statement:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {strTime}")

        elif 'who are you' in statement or 'what can you do' in statement or '7' in statement:
            speak('.I am programmed to perform minor tasks like'
                  'opening youtube,google chrome,gmail and stackoverflow ,predict time,'
                  'take a photo,search wikipedia,predict weather' 
                  'in different cities , get top headline news from times of india!')
            print(' I am programmed to perform minor tasks like\n'
                  'opening youtube,google chrome,gmail'
                  ' and stackoverflow ,predict time,search wikipedia,\npredict weather' 
                  'in different cities\n , get top headline news from times of india!')
        elif "who made you" in statement or "who created you" in statement or "who discovered you" in statement:
            speak("I was built by Aditya kumar yadav")
            print("I was built by Aditya kumar yadav")

        elif 'news' in statement or '8' in statement:
            news = webbrowser.open_new_tab("https://timesofindia.indiatimes.com/home/headlines")
            speak('Here are some headlines from the Times of India,Happy reading')
            time.sleep(6)



        elif 'search' in statement:
            statement = statement.replace("search", "")
            webbrowser.open_new_tab(statement)
            time.sleep(5)


        elif "log off" in statement or "sign out" in statement:
            speak("Ok , your pc will log off in 10 sec make sure you exit from all applications")
            subprocess.call(["shutdown", "/l"])

time.sleep(3)
