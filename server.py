import os
from flask import Flask, send_from_directory, render_template, redirect
from flask import request
from flask import jsonify
from flask_sqlalchemy import SQLAlchemy
from aplicacion.app import db
import psycopg2

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://fl0user:uT0ij6KYgIom@ep-young-bread-18088134.eu-central-1.aws.neon.fl0.io:5432/qr-project?sslmode=require'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_RECORD_QUERIES'] = True
app.config['DEBUG'] = True
db = SQLAlchemy(app)
port = int(os.environ.get("PORT", 5000))

class Log(db.Model):
    __tablename__ = 'logs'
    id = db.Column(db.Integer, primary_key=True)
    ip = db.Column(db.String(15), nullable=False)
    agent = db.Column(db.Text, nullable=False)

@app.route('/static/<path:path>')
def serve_static(path):
    return send_from_directory('static', path)

@app.route('/', methods=["GET"])
def home():
   return render_template('index.html')

@app.route("/prueba", methods=["GET"])
def prueba():
    db.create_all()
    new_log = Log(ip = request.headers.get('X-Fordwarded-For'), agent = request.headers.get('User-Agent'))
    db.session.add(new_log)
    db.session.commit()
    data = {
        # "method": request.method,
        # "args": request.args,
        # "form": request.form,
        # "data": request.data,
        "cookies": request.cookies,
        "headers": dict(request.headers),
        "path": request.path,
        "full_path": request.full_path,
        "script_root": request.script_root,
        "url": request.url,
        "base_url": request.base_url,
        "url_root": request.url_root,
        "host_url": request.host_url,
        "remote_addr": request.remote_addr
    }
    return jsonify(data), 200


@app.route("/prueba2", methods=["GET"])
def prueba2():
    conn = psycopg2.connect(
    dbname="qr-project",
    user="fl0user",
    password="uT0ij6KYgIom",
    host="ep-young-bread-18088134.eu-central-1.aws.neon.fl0.io",
    port="5432"
    )
    cur = conn.cursor()
    cur.execute("""
    INSERT INTO logs (ip, agent)
    VALUES (%s, %s)
    """, ('algo', 'algo2'))
    conn.commit()
    cur.close()
    conn.close()
     

@app.route('/<path:path>')
def all_routes(path):
    return redirect('/')
        
if __name__ == "__main__":
    app.run(port=port)