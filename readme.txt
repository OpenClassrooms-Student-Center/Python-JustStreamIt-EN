JustStreamIt - application README

The project file is organized in this way:
- server.py > The file to launch the server with Flask
- requestsAPI.py > A file you can use to request the API
- templates:
    - index.html > The HTML file of the project. It is in the template folder (the MVC model view) as Flask asks for it.
- static:
    - style.css > The CSS file of the project. It is in the static folder as Flask asks for it.
        
To start the project you need to install: 
- Python (version 3)
- Flask > pip install flask 

(see https://flask.palletsprojects.com/en/1.1.x/installation/)
    
To start the server:
- Run the server.py file.
- Then go to your web browser at the URL indicated by the command line, in general http://127.0.0.1:5000/.

Every modification you make in the HTML or CSS file will be visible after reloading the page. You must make sure that the server is still running, and restart it if necessary.

To display Python variables in the HTML page, you have to pass them as a render_template parameter in this way:
render_template("index.html", text = messageWelcome, message = objective)

"messageWelcome" and "objective" are variables that are in the server.py file. Local variables, here text and message, must be created within the render_template function and assigned variable values, here the variables messageWelcome and objective. These are the variables created locally in the render_template function, which will then be displayed in the index.html file using a syntax with double braces: {{ variable_to_display }}

The value in the double braces will be converted to HTML by Flask. You can change its style by pointing to the tag in which it is located.

Here there are 2 variables, but you can put as many variables as you want in the render_template parameters, and use them in the template (here index.html). You can 
name them whatever you want, as long as they respect Python naming conventions.
