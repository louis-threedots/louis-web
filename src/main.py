#! /usr/bin/python3
import louis_globals as glob
from audio import Audio
from main_functions import discover, main_menu



from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("chat.html")

@app.route('/_get_data/', methods=['POST'])
def _get_data():
    main()
    returnVal = jsonify({"data": render_template('response.html', myText=glob.printOutput)})
    glob.printOutput = ""
    return returnVal

if __name__ == "__main__":
    app.run(debug=True)



def main():
    arduino, cells = discover()
    audio = Audio()
    audio.speak(text="Welcome to Louis the brailliant assistant.", name="main_welcome")
    main_menu(arduino, cells, audio)

# main()
