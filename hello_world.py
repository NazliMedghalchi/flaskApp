from flask import Flask, url_for
from flask import request
app = Flask('helloworld')

@app.route('/')
def hello_world():
    # print 'this is the first app with flask'
    return 'Hello World!'

@app.route('/<name>')
def hello(name):
    return "Hello {}!".format(name)

if __name__ == '__main__':
    app.run()


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        do_the_login()
    else:
        show_all_the_login()


# def index():
#     pass
# app.add_url_rule('/', 'index', index)
#
# app.view_functions['index'] = index
