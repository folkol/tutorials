"""Web Application written in Bottle.

Micro-webframeworks (such as Bottle) are all about minimizing the code
and effort required to link an application to a web server. Decorators
connect a route or path to a function. The function manages getting a
user request, calling the application, and forming the response.

Tools we will need:
    - Empty server with run()
    - Returning static content
    - Content type
"""

from bottle import *

from algebra import area_of_circle


@route('/')
def welcome():
    response.set_header('Vary', 'Accept')
    response.content_type = 'text/plain'
    if 'text/html' in request.headers.get('Accept', '*/*'):
        response.content_type = 'text/html'
        return '<h1>Howdy!</h1>'

    return 'Hello, world!'


@route('/now')
def time_service():
    response.set_header('Vary', 'Accept')
    response.content_type = 'text/plain'
    response.set_header('Cache-Control', 'max-age=1')
    return time.ctime()


@route('/upper/<word>')
def upper_case_service(word):
    response.set_header('Vary', 'Accept')
    response.content_type = 'text/plain'
    return word.upper()


secret = 'the average life expectancy of a stark of a targaryen is short'


@route('/area/circle')
def circle_area_service():
    last_visit = request.get_cookie('last-visit', 'unknown', secret=secret)
    response.set_header('Vary', 'Accept')
    response.set_cookie('last-visit', time.ctime(), secret=secret)
    print(f'Last visit: {last_visit}')
    try:
        radius = float(request.query.get('radius', '0.0'))
    except ValueError as e:
        return e.args[0]
    area = area_of_circle(radius)
    if 'text/html' in request.headers.get('Accept', '*/*'):
        response.content_type = 'text/html'
        return f'<p>The area is <em> {area} </em> </p>'
    return dict(area=area)


file_template = '''\
<h1>List of files in <em> Congress Data </em> </h1>
<hr>
<ol>
% for file in files:
    <li><a href="files/{{file}}">{{file}}</a></li>
% end
</ol>
'''


@route('/files')
def list_files():
    files = os.listdir('rhettiger/congress_data/')
    if not 'text/html' in request.headers.get('Accept', '*/*'):
        return dict(files=files)
    return template(file_template, files=files)


@route('/files/<file>')
def get_file(file):
    return static_file(file, 'rhettiger/congress_data/')


if __name__ == '__main__':
    run(host='localhost', port=8080)
