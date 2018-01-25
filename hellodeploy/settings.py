from os.path import expanduser
HOME = expanduser("~")

ACCEPTED_DBS = {
    'p': 'postgres',
    'postgres': 'postgres',
    's': 'sql3lite',
    'sql3lite': 'sql3lite',
    'm': 'mysql',
    'mysql': 'mysql',
    'z': 'none',
    'none': 'none'
}
ACCEPTED_LANGS = {
    'p2': 'python:2',
    'python2': 'python:2',
    'p3': 'python:3',
    'python3': 'python:3',
    'n': 'node:latest',
    'node': 'node:latest',
    'r': 'ruby:latest',
    'ruby': 'ruby:latest',
    'h': 'HTML',
    'html': 'HTML',
    '.': 'none',
}
BASE_URL='https://backend.hellodeploy.com/backend'

CRED_PATH = HOME + '/.hd_credentials'
OPT_PATH = '.options'
