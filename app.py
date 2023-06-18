import os
from flask import Flask
from flask import render_template
import socket
import random
import datetime

app = Flask(__name__)

color_codes = {
    "red": "#e74c3c",
    "green": "#16a085",
    "blue": "#2980b9",
    "blue2": "#30336b",
    "pink": "#be2edd",
    "darkblue": "#130f40"
}

color = os.environ.get('APP_COLOR') or random.choice(["red","green","blue","blue2","darkblue","pink"])

@app.route("/")
def main():
    #return 'Hello'
    print(color)
    return render_template('hello.html', name=socket.gethostname(), color=color_codes[color])
    
@app.route('/read_file')
def read_file():
    #f = open("/service/requirements.txt", "r")
    #contents = f.read()
    #return render_template('hello.html', name=socket.gethostname(), contents=contents, color=color_codes[color])
    #return render_template('index.html', utc_dt=datetime.datetime.utcnow())
    try:
        with open ("/service/requirements.txt") as file:
            contents = file.read()
            return render_template('hello.html', name=socket.gethostname(), contents=contents, color=color_codes[color])
        

    except FileNotFoundError:
        print("File not found")    

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="8082")
