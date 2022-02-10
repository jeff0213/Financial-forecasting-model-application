import sqlite3

from flask import Flask, render_template, request, redirect, url_for, send_from_directory,session
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__,static_url_path='')
app.debug = False
# app.config['SQLALCHEMY_DATABASE_URI'] ="mysql://root:123456@127.0.0.1/model_db"
app.config['SQLALCHEMY_DATABASE_URI'] ="sqlite:///.//db//mm.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] =True
app.config['SQLALCHEMY_ECHO'] =True
app.config['SECRET_KEY'] = '123456'



db = SQLAlchemy(app)


from mm.views import use
from model.views import model
from interface.views import interface
app.register_blueprint(use,url_prefix = "/admin")
app.register_blueprint(model,url_prefix = "/model")
app.register_blueprint(interface,url_prefix="/interface")

@app.route('/admin/')
def admin_index():
    return render_template('admin/layout.html')


@app.route('/login/',methods = ['GET','POST'])
def login():
    if request.method =='POST':
        conn = sqlite3.connect(r'.\db\mm.db')
        c = conn.cursor()

        username = request.form.get('login_name')
        pwd = request.form.get('login_pwd')
        sql = 'select count(*) from user WHERE login_name=? and login_pwd=?'
        result = c.execute(sql,(username,pwd)).fetchall()
        if result[0][0] != 0:
            session['admin'] = username
            return redirect(url_for('admin_index',username = username))
        else:
            pass
        c.close()
        conn.close()


        return render_template('login.html')
    elif request.method =='GET':
        return render_template('login.html')

@app.route('/logout/')
def logout():
    session.pop('admin')
    return redirect(url_for('login'))

#
# @app.route('/profile/<filename>')
# def render_file(filename):
#
#
#
#
#     return send_from_directory(UPLOAD_FOLDER,filename)





if __name__ == '__main__':
    app.run(host='0.0.0.0')
