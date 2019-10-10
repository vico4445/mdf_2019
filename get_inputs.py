import os
from zipfile import ZipFile
import shutil
import urllib.request
from termcolor import colored

url = 'https://questionsacm.isograd.com/codecontest/sample_input_output/sample-47ML68HAoqdSsgMCTSFoUZGUfIH0frC4KQ3K8ctDf3k.zip'
urllib.request.urlretrieve(url, 'tmp')

with ZipFile('tmp', 'r') as zipObj:
    zipObj.extractall('.')

if os.path.exists('filescoding'):
    shutil.rmtree('filescoding')

print('File {} extracted'.format(colored(url.split('/')[-1][:-4], 'green')))
shutil.move(url.split('/')[-1][:-4], 'filescoding')
os.remove('tmp')
