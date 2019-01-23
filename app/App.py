from flask import Flask, render_template
from flask import request
app=Flask(__name__)
@app.route('/')
def index():
    #return '<h1>Hello World!</h1>'
    return render_template('index.html')
@app.route('/user/<string:name>')
def user(name):
    return '<h1>Hello, %s!</h1>' % name
@app.route('/param')
def param():
    param=request.args.get('param')
    return 'El parametro proporcionado es: %s'%param
@app.route('/login',methods=['GET', 'POST'])
def login():
    user=request.form['user']
    pwd=request.form['pwd']
    return '<h1>Usuario: %s , Password:%s </h1>'%(user,pwd)




if __name__ == '__main__':
    app.run(debug=True, port=8000, host='0.0.0.0')