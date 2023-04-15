import os
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
   return 'Hello, World!'

os.system("git clone -b dev https://github.com/TeamUltroid/Ultroid ok && cd ok && pip3 install -U -r requirements.txt && pip3 install --no-cache-dir -r re*/st*/op*.txt && python3 -m pyUltroid ")
