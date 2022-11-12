from microdot_asyncio import Microdot, Response
from microdot_utemplate import render_template
from index import html_table
app = Microdot()
Response.default_content_type = 'text/html'
js_headers = {
    'Content-Encoding': 'gzip'
}
@app.route('/')
async def hello(request):
    return render_template('index.html',table = html_table)

@app.put('/query')
def query(request):
    pass

@app.route('/assets/<object>')
async def staticfiles(request, object):
    # try:
    with open('assets/{}.gz'.format(object),'rb') as fn:
        r = Response(fn.read(),200)
        r.headers = js_headers
        if object[-2:] == 'js':
            r.default_content_type = 'text/javascript'
        elif object[-3:] == 'css':
            r.default_content_type= 'text/css'
        return r
    # except:
    #     return Response('File not found',404)

@app.route('/shutdown')
def shutdown(request):
    request.app.shutdown()
    return 'The server is shutting down...'


if __name__ == '__main__':
    app.run(debug=True)