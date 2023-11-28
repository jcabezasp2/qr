import os
from flask import Flask, send_from_directory, render_template, redirect
from flask import request
from flask import jsonify

app = Flask(__name__)

port = int(os.environ.get("PORT", 5000))

@app.route('/static/<path:path>')
def serve_static(path):
    return send_from_directory('static', path)

@app.route('/')
def home():
   return render_template('index.html')

@app.route("/prueba", methods=["GET"])
def prueba():
    data = {
        "method": request.method,
        "args": request.args,
        "data": request.data,
        "cookies": request.cookies,
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