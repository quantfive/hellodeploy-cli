import os.path
from utils import register, upload

exists = os.path.exists('.credentials')

if exists:
    f = open('.credentials', 'r')
    token = f.read()
    upload(token[:-1])
else:
    register()
