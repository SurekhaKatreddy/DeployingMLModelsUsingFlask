This project aims to host and consume the regression model for predicting happiness score.

# Architecture of Flask
The main file Invoke.py contains the logic to read the pickle file and render the index.html

The below code takes care of rendering the index.html 
@app.route('/')
@app.route('/index')

The front end consists of two html forms:
1. index.html - to display the form with all the input fields for the user to enter text
2. result.html - to render the output.

The form action of index.html is set to render result.html upon submiting the form action:
<form action="/result" method="POST">


