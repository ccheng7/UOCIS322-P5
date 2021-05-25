# UOCIS322 - Project 5 #
Brevet time calculator with AJAX and MongoDB!

## Overview

Store control times from Project 4 in a MongoDB database.

### What is in this repository

You have a minimal example of `docker-compose` in `DockerMongo`, using which you can connect a Flask app to MongoDB (as demonstrated in class). Refer to the lecture slides for more details on MongoDB and `docker-compose`. Solved `acp_times.py` file will be made available on Canvas under Files after the project due date.

## How to Run

1. get into the folder path and make sure the path have Dockerfile

2. config ur Dockerfile and docker-compose.yml to make sure everything is correct

3. use command 'docker-compose build', wait for completion

4. use command 'docker-compose up', wait for all process up('web_1    | INFO: * Running on http://172.20.0.3:5000/ (Press CTRL+C to quit)')

5. open the browser then enter "localhost:5000", the port was defined in yml file

6. use command 'docker-compose rm' to remove the images if you need
ccheng7@uoregon.edu
cheng cheng