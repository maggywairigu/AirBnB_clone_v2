from flask import flask
app = flask(__name__)

@app.route('/')
@app.route('/hello')
def Helloworld():
    return "Hello World"

if __name__ == '__main__';
    app.debug = True
    app.run(host = '0.0.0.0', port = 5000)

