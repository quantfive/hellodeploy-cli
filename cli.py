import os.path
from utils import register, upload

exists = os.path.exists('.credentials')

if exists:
    f = open('.credentials', 'r')
    token = f.read()
    if token[-1] == '\n':
        token = token[:-1]
    upload(token)
else:
    token = register()
    if token[-1] == '\n':
        token = token[:-1]
    upload(token)
