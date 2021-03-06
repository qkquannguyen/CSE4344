# ------------------------------------- General Information ------------------------------------- #
Student Name    : Minh-Quan H. Nguyen
Student ID      : 1001032212
Class           : CSE4344 - 001
Professor       : Sajib Datta
Assignment      : Project 1 - Building a Simple Web Client and a Multithreaded Web Server 

# ------------------------------------ Overview & Background ------------------------------------ #
This is the first project for CSE4344. The goal of this project is to build a simple web client and
multithreaded web server. With this project, the student will display understanding of the client-
server communications with sockets, exposure to the basic operation of web server and client, and
exploring the basic structures of HTTP messages.

This program is developed using Python 3.6 and utilized the Flask Microframework to help build the
web application. Along with Flask, Visual Studio Code was used to write this program.

# -------------------------------- Dependencies / Libraries Used -------------------------------- #
Dependencies that were utilized in this project were:
    -   Flask
    -   Flask-API
    -   Python 3.6 Libraries

# ---------------------------------- Steps to Run the Web App. ---------------------------------- #
Assuming Python is installed on the system, simply run the following commands to use this web
application. Be sure that Python 3.6 is installed on your system. Go to your terminal window and
use the following commands:

    -   pip3 install -r requirements.txt
    -   python3 goodcode_server.py <Insert Port #>

    +   The server should be running now on the port you specified on localhost. Simply connect to it
        on the web browser by going to:
            -   localhost:<Port>
            -   0.0.0.0:<Port>

    -   Run the web client on another terminal window with the commands below:
            - python3 goodcode_webclient.py <Hostname> <Port #> <HTML File>

# ------------------------------------- Directory Structure ------------------------------------- #

    ----- GoodCode_WebServer
            |
             ----- templates
                     |
                      ----- goodcode_homepage.html
                     |
                      ----- index.html
             ----- README.txt
             ----- goodcode_server.py
             ----- goodcode_webclient.py
             ----- requirements.txt
