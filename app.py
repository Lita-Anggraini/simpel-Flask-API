#import library Flask
from flask import Flask

#Inisialisasi variabel app sebagai Flask
app = Flask(__name__)

#Routing untuk URL / maka akan memunculkan pesen Hello World
@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

#Routing untuk URL /lita maka akan memunculkan pesan Lita Anggraini
@app.route("/lita")
def lita():
    return "<h1>Lita Anggraini</h1>"
