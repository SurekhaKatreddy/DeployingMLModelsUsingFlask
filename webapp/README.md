# This is the root folder of flask application.

# Pickle file
This file is created by dumping the machine learning model.

# Core logic
The core logic of importing the pickle file and hosting it as service is taken care by Invoke.py
Steps to host the web application:
1. Navigate to the folder path containing the file : Invoke.py
2. Export the application using the statement: export FLASK_APP=Invoke.py 
2. Run the application: flask run

Upon doing so, the following is rendered:
<img width="592" alt="image" src="https://user-images.githubusercontent.com/31846843/181418893-faecc283-0303-469a-949f-6fa966b21027.png">

# Templates
The templates subfolder contains the necessary html pages to accept input and render output to the user.
