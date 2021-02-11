# Sample Flask App
A simple flask app template ready to run

## Instructions

1. Clone or download the repo<br>
<code>git clone https://github.com/rizagokay/flask_template.git</code>
2. Navigate to the repo folder<br>
<code>cd flask_template</code>
3. Create a virtual environment (optional)<br>
<code>python3 -m venv venv</code>
4. Activate the virtual environment (optional)<br>
<code>source venv/bin/activate</code>
5. Install requirements<br>
<code>pip3 install -r requirements.txt</code>
6. Run <br>
<code>flask run</code>

## Notes:
- See config.py for some variables
- Manage.py can be used for database migrations
- Procfile can be used for HEROKU deployments. 
- Use gunicorn for socket.io <code>gunicorn -k gevent wsgi:app</code>
