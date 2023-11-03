from flask import render_template, request, Blueprint

import socket

core = Blueprint('core', __name__)

@core.route('/')
def index():
    '''
    This is the home page view. Notice how it uses pagination to show a limited
    number of posts by limiting its query size and then calling paginate.
    '''
    hostname = socket.gethostname()
    host_ip = socket.gethostbyname(hostname)
    return render_template('index.html', HOSTNAME=hostname, IP=host_ip)

@core.route('/info')
def info():
    '''
    Example view of any other "core" page. Such as a info page, about page,
    contact page. Any page that doesn't really sync with one of the models.
    '''
    return render_template('info.html')