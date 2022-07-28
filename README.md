This project aims to host and consume the regression model for predicting happiness score.

# Architecture of Flask

1. Invoke.py : The main file that contains the logic to read the pickle file and render the index.html
    The below code takes care of rendering the index.html 
    @app.route('/')
    @app.route('/index')
2. Front end : The front end consists of two html forms:
   index.html - to display the form with all the input fields for the user to enter text
   result.html - to render the output.

    The form action of index.html is set to render result.html upon submiting the form action:
    form action="/result" method="POST"

# index.html
<img width="393" alt="image" src="https://user-images.githubusercontent.com/31846843/181416103-26ffcc4a-7b1c-44b4-a05e-5faa1dbfc5be.png">

# result.html
<img width="518" alt="image" src="https://user-images.githubusercontent.com/31846843/181417923-ba9f065b-da8d-4922-9b2c-f31d3b58a9f2.png">


