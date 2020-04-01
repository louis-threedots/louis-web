from mainApp import MainApp

run_flask = False

printOutput = ""
newInput = ""
skipMain = False

def cust_print(text):
    global printOutput
    printOutput = printOutput + str(text) + "<br />\n"
    print(text)

def cust_input():
    global newInput, skipMain, run_flask
    if run_flask:
        skipMain = True
        from main import _get_data
        import sys
        sys.exit()
        # while newInput == "":
        #     continue
        return newInput
    else:
        return input("> ")

mainApp = MainApp()