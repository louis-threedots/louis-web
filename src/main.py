#! /usr/bin/python3
import louis_globals as glob

if glob.run_flask:
    from flask import Flask, render_template, jsonify

    app = Flask(__name__)

    @app.route('/')
    def index():
        return render_template("chat.html")

    @app.route('/_get_data/', methods=['POST'])
    def _get_data():
        if not glob.skipMain:
            main()
        returnVal = jsonify({"data": render_template('response.html', myText=glob.printOutput)})
        glob.printOutput = ""
        return returnVal

def main():
    glob.mainApp.on_start()


if __name__ == "__main__" and glob.run_flask:
    app.run(debug=True)

if not glob.run_flask:
    main()