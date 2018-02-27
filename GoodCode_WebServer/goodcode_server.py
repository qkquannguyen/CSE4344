# ----------------------------------- Import Needed Libraries ----------------------------------- #
import logging
import sys

from flask import Flask, render_template, jsonify

# ----------------------------------- Set Debug Logging Level ----------------------------------- #
logging.getLogger().setLevel(logging.INFO)

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

'''
Endpoint    : localhost:PORT/json
Purpose     : Test the browser with multiple connections concurrently
'''
@app.route('/json')
def test_json():
    return jsonify(success=True)


# ------------------------------------ Start Web Server App. ------------------------------------ #
if __name__ == '__main__':
    
    # ----------------- Grab Port Number from the User ----------------- #
    # --- Take the input port number and store it in a local variable
    # --- If port is not specified, default to port 80
    try:
        inputPort = sys.argv[1]
    except:
        logging.info("No port specified. Defaulting to Port 8080.")
        inputPort = 8080

    app.run(threaded=True, port=inputPort)