printOutput = ""

def cust_print(text):
    global printOutput
    printOutput = str(printOutput) + str(text) + "<br />\n"
    print(text)