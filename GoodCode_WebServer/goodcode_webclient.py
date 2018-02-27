# ----------------------------------- Import Needed Libraries ----------------------------------- #
import http.client
import logging
import sys

# ----------------------------------- Set Debug Logging Level ----------------------------------- #
logging.getLogger().setLevel(logging.INFO)

def main():

    try:
        inputHost = sys.argv[1]
    except:
        logging.info("No host specified. Defaulting to localhost.")
        inputHost = "localhost"

    try:
        inputPort = sys.argv[2]
    except:
        logging.info("No port specified. Defaulting to Port 8080.")
        inputPort = 8080

    firstConnection = http.client.HTTPConnection(inputHost, inputPort)
    secondConnection = http.client.HTTPConnection(inputHost, inputPort)

    firstConnection.request("GET", "/")
    secondConnection.request("GET", "/json")

    firstRequest = firstConnection.getresponse()
    secondRequest = secondConnection.getresponse()

    print(firstRequest)
    print(secondRequest)

    data = firstRequest.read()
    data2 = secondRequest.read()

    print(data)
    print(data2)

if __name__ == "__main__":
    main()