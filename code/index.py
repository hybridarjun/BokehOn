from flask import Flask, render_template, request, url_for
import os
from model_master.research.deeplab import run_model

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route("/run", methods=['POST'])
def run():
    run_model.run_visualization()
    file_path = "static/output.png"
    return render_template('output.html',user_image = file_path)

if __name__ == '__main__':
   app.run(debug = True)
