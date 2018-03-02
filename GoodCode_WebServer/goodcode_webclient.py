# ----------------------------------- Import Needed Libraries ----------------------------------- #
import http.client
import logging
import socket
import sys
import time

# ----------------------------------- Set Debug Logging Level ----------------------------------- #
logging.getLogger().setLevel(logging.INFO)

def main():

    # ----------------------- Get Host from User ----------------------- #
    try:
        # --- Store the host in inputHost
        inputHost = sys.argv[1]
    except:
        # --- If there was not a host specified...
        # --- This will default to localhost (0.0.0.0 is acceptable also)
        logging.info("No host specified. Defaulting to localhost.")
        inputHost = "localhost"

    # ----------------------- Get Port from User ----------------------- #
    try:
        # --- Store the port in inputPort
        inputPort = sys.argv[2]
    except:
        # --- If there was not a port specified...
        # --- This will default to port 8080
        logging.info("No port specified. Defaulting to Port 8080.")
        inputPort = 8080

    # ----------------------- Get File from User ----------------------- #
    try:
        # --- Store the file name in inputFile
        inputFile = sys.argv[3]
    except:
        # --- If there was not a file specified...
        # --- This will default to index.html
        logging.info("No input file given. Defaulting to index.html.")
        inputFile = "index.html"

    # ---------------- Create MultiConnection to Server ---------------- #
    # --- Create 5 different connections that will talk to the server
    # --- Connection A, B, and C will connect to endpoint "/"
    # --- Connection D, E will connect to endpoint "/json"
    connectionA = http.client.HTTPConnection(inputHost, inputPort)
    connectionB = http.client.HTTPConnection(inputHost, inputPort)
    connectionC = http.client.HTTPConnection(inputHost, inputPort)
    connectionD = http.client.HTTPConnection(inputHost, inputPort)
    connectionE = http.client.HTTPConnection(inputHost, inputPort)

    # --------------------- Send Request to Server --------------------- #
    # --- 1. Log the time the signal begins to send to the server
    # --- 2. Establish the connection and request
    # --- 3. Log when the signal is received
    # --- 4. Display the round trip time

    # --- Request to GET the index HTML file
    if inputFile == "index.html":
        # --- Connection A
        requestTimeA = time.time()
        connectionA.request("GET", "/index/")
        receivedRequestTimeA = time.time()
        roundTripTimeA = str(receivedRequestTimeA - requestTimeA)

        # --- Connection B
        requestTimeB = time.time()
        connectionB.request("GET", "/index/")
        receivedRequestTimeB = time.time()
        roundTripTimeB = str(receivedRequestTimeB - requestTimeB)

        # --- Connection C
        requestTimeC = time.time()
        connectionC.request("GET", "/index/")
        receivedRequestTimeC = time.time()
        roundTripTimeC = str(receivedRequestTimeC - requestTimeC)

    # --- If the user did not want the index HTML file, redirect to "/"
    else:
        # --- Connection A
        requestTimeA = time.time()
        connectionA.request("GET", "/")
        receivedRequestTimeA = time.time()
        roundTripTimeA = str(receivedRequestTimeA - requestTimeA)

        # --- Connection B
        requestTimeB = time.time()
        connectionB.request("GET", "/")
        receivedRequestTimeB = time.time()
        roundTripTimeB = str(receivedRequestTimeB - requestTimeB)

        # --- Connection C
        requestTimeC = time.time()
        connectionC.request("GET", "/")
        receivedRequestTimeC = time.time()
        roundTripTimeC = str(receivedRequestTimeC - requestTimeC)

    # --- Request to endpoint "/json"
    # --- Connection D
    requestTimeD = time.time()
    connectionD.request("GET", "/json")
    receivedRequestTimeD = time.time()
    roundTripTimeD = str(receivedRequestTimeD - requestTimeD)

    # --- Request to endpoint "/"
    # --- Connection E
    requestTimeE = time.time()
    connectionE.request("GET", "/")
    receivedRequestTimeE = time.time()
    roundTripTimeE = str(receivedRequestTimeE - requestTimeE)

    # -------------------- Display Request Response -------------------- #
    connectionARequest = connectionA.getresponse()
    connectionBRequest = connectionB.getresponse()
    connectionCRequest = connectionC.getresponse()
    connectionDRequest = connectionD.getresponse()
    connectionERequest = connectionE.getresponse()

    # --- Display Socket Information
    socketInfo = socket.getaddrinfo(inputHost, inputPort)
    print("Displaying socket information: SocketFamily | Socket Type | Proto | Socket Address")
    for i in range(0, 4):
        print(socketInfo[i])

    # --- Display the HTTP Request information
    # --- Connection A
    print("\n")
    print("Connection A: ", connectionARequest.read(),
                            "\nRTT of Connection A: " + roundTripTimeA + " seconds",
                            "\nHost: " + connectionA.host,
                            "\nPort: " + connectionA.port,
                            "\nStatus Code: " + str(connectionARequest.status),
                            "\nHTTP Method: " + str(connectionARequest._method),
                            "\nProtocol Version: " + str(connectionARequest.version) + "\n",
                            connectionARequest.info())
    # --- Connection B
    print("Connection B: ", connectionBRequest.read(),
                            "\nRTT of Connection B: " + roundTripTimeB + " seconds",
                            "\nHost: " + connectionB.host,
                            "\nPort: " + connectionB.port,
                            "\nStatus Code: " + str(connectionBRequest.status),
                            "\nHTTP Method: " + str(connectionBRequest._method),
                            "\nProtocol Version: " + str(connectionBRequest.version) + "\n",
                            connectionBRequest.info())
    # --- Connection C
    print("Connection C: ", connectionCRequest.read(),
                            "\nRTT of Connection C: " + roundTripTimeC + " seconds",
                            "\nHost: " + connectionC.host,
                            "\nPort: " + connectionC.port,
                            "\nStatus Code: " + str(connectionCRequest.status),
                            "\nHTTP Method: " + str(connectionCRequest._method),
                            "\nProtocol Version: " + str(connectionCRequest.version) + "\n",
                            connectionCRequest.info())
    # --- Connection D
    print("Connection D: ", connectionDRequest.read(),
                            "\nRTT of Connection D: " + roundTripTimeD + " seconds",
                            "\nHost: " + connectionD.host,
                            "\nPort: " + connectionD.port,
                            "\nStatus Code: " + str(connectionDRequest.status),
                            "\nHTTP Method: " + str(connectionDRequest._method),
                            "\nProtocol Version: " + str(connectionDRequest.version) + "\n",
                            connectionDRequest.info())
    # --- Connection E
    print("Connection E: ", connectionERequest.read(),
                            "\nRTT of Connection E: " + roundTripTimeE + " seconds",
                            "\nHost: " + connectionE.host,
                            "\nPort: " + connectionE.port,
                            "\nStatus Code: " + str(connectionERequest.status),
                            "\nHTTP Method: " + str(connectionERequest._method),
                            "\nProtocol Version: " + str(connectionERequest.version) + "\n",
                            connectionERequest.info())

    # ------------------------ Close Connection ------------------------ #
    connectionA.close()
    connectionB.close()
    connectionC.close()
    connectionD.close()
    connectionE.close()

if __name__ == "__main__":
    main()

