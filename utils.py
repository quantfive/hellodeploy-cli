import sys
import getpass
import requests
import json
import os

from settings import ACCEPTED_DBS, ACCEPTED_LANGS

def login():
    data = {}
    sys.stdout.write('Please input your email: ')
    data['email'] = input()
    data['password'] = getpass.getpass(prompt='Please input your password: ')
    data['password1'] = data['password']
    data['password2'] = data['password']
    return requests.post('https://backend.hellodeploy.com/backend/api/auth/login/', data=data)

def signup():
    data = {}
    sys.stdout.write('Please input your email: ')
    data['email'] = input()
    sys.stdout.write('Please input your first name: ')
    data['first_name'] = input()
    sys.stdout.write('Please input your last name: ')
    data['last_name'] = input()
    data['password'] = getpass.getpass(prompt='Please input your password: ')
    data['password1'] = data['password']
    data['password2'] = data['password']
    return requests.post('https://backend.hellodeploy.com/backend/api/auth/register/', data=data)

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
    key = json.loads(resp.content)['key']
    f = open('.credentials', 'w')
    f.write(key)


def upload(token):
    data = {}
    sys.stdout.write('Please input the path of the project zip file: ')
    zip_file = input()
    if not os.path.isfile(zip_file):
        print('Sorry that file does not exist')
        return upload(token)
    data['files'] = open(zip_file, 'rb')
    sys.stdout.write('Please input your project name: ')
    data['name'] = input()
    sys.stdout.write('Please input the language your app uses p2=python2, p3=python3, n=node, r=ruby, h=html: ')
    data['lang'] = input()
    data['lang'] = ACCEPTED_LANGS[data['lang']]
    if data['lang'] == 'HTML':
        do_stuff = 5
    elif data['lang'] in ACCEPTED_LANGS:
        sys.stdout.write('Please input the command to run the app: ')
        data['cmd'] = input()
        sys.stdout.write('Please input the port your app runs on: ')
        data['port'] = input()
        sys.stdout.write('Please input the Database your app uses .=none, n=node, p=postgres, s=sql3lite, m=mysql: ')
        data['db'] = input()
        data['db'] = ACCEPTED_DBS[data['db']]
        if db == 'none':
            do_stuff = 5
        elif data['db'] in ACCEPTED_DBS:
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
    headers = {'authorization': 'Token ' + token}
    r = requests.post('https://backend.hellodeploy.com/backend/api/upload/', data=data, headers=headers)
    print(r)
    print(r.content)
