from sys import *
import webbrowser
import re 
import urllib.request, urllib.parse, urllib.error

def is_connected():
    try:
        urllib.request.urlopen('http://google.com',timeout =1)
        return True
    except urllib.error.URLError as err:
        return False

def Find(string):
    url =re.findall("http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\), ]|(?:%[0-9a-fA_F][0-9afA_F]))+",string)
    return url

def webLauncher(path):
    with open(path) as fp:
        for line in fp:
            #print(line)
            url =Find(line)
            print(url)
            for str1 in url:
                webbrowser.open(str1,new =2)


def main():
    print("__________Shrigita Shinde ____________")

    print("Application Name :",argv[0])

    if(len(argv)!= 2):
        print("Invalid Argument")
        exit()
    if(argv[1] =="-h" or argv[1] == "-H"):
        print("Help :This Script to help Open URL which are written in one file")
        exit()
    if(argv[1] =="-u" or argv[1] == "-U"):
        print("Usage : Application_Name NameOfFile")
        exit()

    try:

        connected =is_connected()

        if connected:
            webLauncher(argv[1])
        else:
            print("Unabel to connect to internet .........")  
    except ValueError:
        print("Error :Invalid datatype of input ")
    except Exception as E:
        print("Error : Invalid input ",E) 




if __name__ =="__main__":
    main()