from flask import Flask,request,render_template,url_for,redirect,abort
import config

app = Flask(__name__)
app.config.from_object(config)


@app.route('/')
def hello_world():
    return render_template('index.html',name='hello kavi')

@app.route('/lz/<id>')
def getlz(id):
    return render_template('index.html', name=id)

if __name__ == '__main__':
    app.debug=True
    app.run()
