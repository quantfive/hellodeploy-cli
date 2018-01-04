import sys
import getpass
import requests

from settings import ACCEPTED_DBS, ACCEPTED_LANGS, AUTH

def login():
    data = {}
    sys.stdout.write('Please input your email: ')
    data['email'] = input()
    data['password'] = getpass.getpass(prompt='Please input your password: ')
    return requests.post('http://www.hellodeploy.com/api/auth/login/', data=data)

def signup():
    data = {}
    sys.stdout.write('Please input your email: ')
    data['email'] = input()
    sys.stdout.write('Please input your first name: ')
    data['first'] = input()
    sys.stdout.write('Please input your last name: ')
    data['last'] = input()
    data['password'] = getpass.getpass(prompt='Please input your password: ')
    return requests.post('http://www.hellodeploy.com/api/auth/register/', data=data)

def register():
    sys.stdout.write('Do you have a HelloDeploy account y/n: ')
    resp = input()
    if resp == 'y':
        resp = login()
    elif resp == 'n':
        resp = signup()
    else:
        print('Sorry, invalid input')
        return register()
    f = open('.credentials', 'w')
    f.write(resp)



def upload(token):
    data = {}
    sys.stdout.write('Please input your project name: ')
    data['proj'] = input()
    sys.stdout.write('Please input the language your app uses p2=python2, p3=python3, n=node, r=ruby, h=html: ')
    data['lang'] = input()
    if lang == 'h':
        do_stuff = 5
    elif lang in ACCEPTED_LANGS:
        sys.stdout.write('Please input the command to run the app: ')
        data['cmd'] = input()
        sys.stdout.write('Please input the port your app runs on: ')
        data['port'] = input()
        sys.stdout.write('Please input the Database your app uses n=none, p=postgres, s=sql3lite, m=mysql: ')
        data['db'] = input()
        if db == 'n':
            do_stuff = 5
        elif db in ACCEPTED_DBS:
            sys.stdout.write('Please input the port your Database uses: ')
            data['db_port'] = input()
            sys.stdout.write('Please input the name of your Database: ')
            data['db_name'] = input()
            sys.stdout.write('Please input the Database username: ')
            data['db_username'] = input()
            sys.stdout.write('Please input the Database password: ')
            data['db_password'] = input()
            sys.stdout.write('Please input the environment Variable for Database Host: ')
            data['db_env'] = input()
    #r = requests.post('http://www.hellodeploy.com/api/project/create/', data=data)
