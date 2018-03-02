# ----------------------------------- Import Needed Libraries ----------------------------------- #
import logging
import sys

from flask import Flask, request, redirect, render_template, jsonify
from flask_api import status

# ----------------------------------- Set Debug Logging Level ----------------------------------- #
logging.getLogger().setLevel(logging.INFO)

# ------------------------------------ Initialize Flask App. ------------------------------------ #
app = Flask(__name__)

# ------------------------------------ Web Server Controller ------------------------------------ #
'''
Endpoint    : localhost:PORT/
Purpose     : Homepage of GoodCode Redirection
'''
@app.route('/', methods=['GET'])
def homepage_redirection():

    # --- Redirect the "/" routing to the homepage
    try:
        logging.info(" Address moved, redirecting...")
        return redirect('/home/<name>')
    # --- If the route is invalid, show HTTP Error 404
    except:
        return status.HTTP_404_NOT_FOUND

'''
Endpoint    : localhost:PORT/home/<name>
Purpose     : Homepage of GoodCode
'''
@app.route('/home/', methods=['GET'])
@app.route('/home/<name>', methods=['GET'])
def homepage(name=None):

    # --- Render the Homepage HTML File
    try:
        logging.info(" Client IP Address: " + request.remote_addr)
        logging.info(request.headers)
        return render_template('goodcode_homepage.html', name=name)
    except:
        # --- If the HTML file is not found, return HTTP Code 400
        return status.HTTP_400_BAD_REQUEST

'''
Endpoint    : localhost:PORT/index/<name>
Purpose     : Index of GoodCode Website
'''
@app.route('/index/', methods=['GET'])
@app.route('/index/<name>', methods=['GET'])
def index(name=None):

    # --- Render the Index HTML File
    try:
        logging.info(" Client IP Address: " + request.remote_addr)
        logging.info(request.headers)
        return render_template('index.html', name=name)
    except:
        # --- If the HTML file is not found, return HTTP Code 400
        return status.HTTP_400_BAD_REQUEST

'''
Endpoint    : localhost:PORT/json
Purpose     : Test the browser with multiple connections concurrently
'''
@app.route('/json', methods=['GET'])
def test_json():

    # --- Return a simple JSON Message
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

    # --- Run the web server and enable multiple connections
    # --- To enable multiple connections, 'threaded' will be enabled
    # --- 'threaded' will allow for multiple connections w/ multithreading
    app.run(threaded=True, port=inputPort)