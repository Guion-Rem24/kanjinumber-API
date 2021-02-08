"""webapp/app.py
author          : nsuhara <na010210dv@gmail.com>
date created    : 2020/9/18
python version  : 3.7.3
"""
import os

from flask import Flask, jsonify
from flask import render_template, request
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app, send_wildcard=True)
# app.config['CORS_HEADER'] = 'Content-Type'

""" 初期画面 """
"""
    Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token
"""
@app.route('/')
# @cross_origin(origins='localhost', headers=['Content-Type', 'Authorization', 'X-Amz-Date', 'X-Api-Key', 'X-Amz-Security-Token'])
def index():
    
    return render_template("index.html")

@app.route('/', methods=['GET'])
@cross_origin(origins='*', headers=['Content-Type', 'Authorization', 'X-Amz-Date', 'X-Api-Key', 'X-Amz-Security-Token'])
def number_post(context):
    print("GET")
    return jsonify({'success':context})

def main():
    """main
    """
    host = os.getenv('HOST', '0.0.0.0')
    port = int(os.getenv('PORT', '5000'))
    app.run(host=host, port=port, debug=True)


if __name__ == '__main__':
    main()
