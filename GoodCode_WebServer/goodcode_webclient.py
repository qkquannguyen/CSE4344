import http.client
import logging
import sys

logging.getLogger().setLevel(logging.INFO)

def main():

    try:
        inputHost = sys.argv[1]
        inputPort = sys.argv[2]
    except:
        logging.info("No port specified. Defaulting to Port 8080.")
        inputPort = 8080

    firstConnection = http.client.HTTPConnection(inputHost, inputPort)
    secondConnection = http.client.HTTPConnection(inputHost, inputPort)

    firstConnection.request("GET", "/json")
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