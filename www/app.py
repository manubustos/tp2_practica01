# Imports
from aux_pro import Process
from database import Database
from flask import Flask
from flask import jsonify
from flask import render_template
from flask import request
from models import Samples

import random

app = Flask(__name__)
db = Database()
pro = Process()

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/samples', methods = ["POST"])
def init_samples():
  # If there is a process running, return to index()
  #if pro.is_running():
  #  return index()
  d_s = {}
  d_s["temperatura"] = random.randint(10,30)
  d_s["humedad"] = random.randint(0,100)
  d_s["presion"] = random.randint(1000, 1020)
  d_s["viento"] = random.randint(10, 30)
  id_sample = db.init_sample(d_s)
  #data = request.form
  #periodo_muestreo = data["periodo"]
  pro.start_process(id_sample)
  #return render_template('index.html', temperatura=samples["temperatura"], humedad=samples["humedad"], presion=samples["presion"], viento=samples["viento"], periodo=periodo_muestreo)
  #return render_template('samples.html', temperatura=samples["temperatura"], humedad=samples["humedad"], presion=samples["presion"], viento=samples["viento"])
  return render_template('samples.html', id_sample=id_sample)


@app.route('/samples/<id_sample>', methods = ["GET"])
def get_sample(id_sample):
  sample = db.get_sample(id_sample)
  return jsonify(sample)

if __name__ == "__main__":
  app.run(host='0.0.0.0', port=8888)

