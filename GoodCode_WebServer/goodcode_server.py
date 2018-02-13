# ----------------------------------- Import Needed Libraries ----------------------------------- #
import sys

from flask import Flask, render_template

# ------------------------------------ Initialize Flask App. ------------------------------------ #
app = Flask(__name__)

# ------------------------------------ Web Server Controller ------------------------------------ #
'''
Endpoint    : localhost:PORT/
Purpose     : Homepage of GoodCode
'''
@app.route('/')
def homepage():
    return render_template('goodcode_homepage.html')

# ------------------------------------ Start Web Server App. ------------------------------------ #
if __name__ == '__main__':
    
    # ----------------- Grab Port Number from the User ----------------- #
    # --- Take the input port number and store it in a local variable
    # --- If port is not specified, default to port 80
    try:
        inputPort = sys.argv[1]
    except:
        print("No port specified. Defaulting to Port 80.")
        inputPort = 80

    # ----------------- Run the Web Server Application ----------------- #
    app.run(port=inputPort)
