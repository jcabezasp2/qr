import os
from flask import Flask, send_from_directory, render_template, redirect
from flask import request
from flask import jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://fl0user:uT0ij6KYgIom@ep-young-bread-18088134.eu-central-1.aws.neon.fl0.io:5432/qr-project?sslmode=require'
db = SQLAlchemy(app)
port = int(os.environ.get("PORT", 5000))

class Log(db.Model):
    ip = db.Column(db.String(15), nullable=False)
    agent = db.Column(db.Text, nullable=False)

@app.route('/static/<path:path>')
def serve_static(path):
    return send_from_directory('static', path)

@app.route('/')
def home():
   new_log = Log(ip = request.header.get('X-Fordwarded-For'), agent = request.header.get('User-Agent'))
   db.session.add(new_log)
   db.session.commit()
   return render_template('index.html')

@app.route("/prueba", methods=["GET"])
def prueba():
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

@app.route('/<path:path>')
def all_routes(path):
    return redirect('/')

if __name__ == "__main__":
    app.run(port=port)