#-*-coding:utf-8-*-

from flask import Flask, url_for
from flask import render_template

app = Flask(__name__)

# 开启debug模式，修改文件后会重新加载文件
app.debug = True

########## route begin ##########
# @app.route('/')
# def hello_world():
# 	return 'Thorn Index Page!'

# @app.route('/f')
# def hello():
# 	return 'Thorn Front Page!'

# @app.route('/user/<username>')
# def show_user_profile(username):
# 	# show the use profile for that user
# 	return 'welcome User %s' % username

# @app.route('/post/<int:post_id>')
# def show_post(post_id):
# 	# show the post with the given id, the id is an integer
# 	return 'Thorn Post %d' % post_id

# @app.route('/project/')
# def projects():
# 	return 'The project page'

# @app.route('/about')
# def about():
# 	return 'Thorn about page'
########## route end ##########

########## URL Contruct ##########
@app.route('/')
def index():
	return render_template('hello.html', name = "qunny")
	# return "Welcome To Thorn."

@app.route('/login')
def login():
	pass

@app.route('/user/<username>')
def profile(username):
	pass

# with app.test_request_context():
# 	print("hahaha")
# 	print url_for('index')
# 	print url_for('login')
# 	print url_for('login', next = '/')
# 	print url_for('profile', username='john Doe')


if __name__ == '__main__':
	app.run(host='192.168.1.5')
