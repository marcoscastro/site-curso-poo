from bottle import route, run
from bottle import static_file, request
from bottle import template, get, error
import os

# static routes
@get('/<filename:re:.*\.css>')
def stylesheets(filename):
	return static_file(filename, root='static/css')

@get('/<filename:re:.*\.js>')
def javascripts(filename):
	return static_file(filename, root='static/js')

@get('/<filename:re:.*\.(jpg|png|gif|ico)>')
def images(filename):
	return static_file(filename, root='static/img')

@get('/<filename:re:.*\.(eot|ttf|woff|svg)>')
def fonts(filename):
	return static_file(filename, root='static/font')

@route('/')
def index():
	return template('index')

@route('/obrigado')
def obrigado():
	return template('obrigado')

@error(404)
def error404(error):
	return template('index')

if __name__ == "__main__":
	if os.environ.get('APP_LOCATION') == 'heroku':
		run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
	else:
		run(host='localhost', port=8080, debug=True, reloader=True)