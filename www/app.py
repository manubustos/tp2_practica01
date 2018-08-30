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
  #return render_template('index.html', temperatura=samples["temperatura"], humedad=samples["humedad"], presion=samples["presion"], viento=samples["viento"])
  return render_template('index.html', id_sample=id_sample)

@app.route('/last', methods = ["GET"])
def get_last():
  sample = db.get_last_sample()
  #samples = [sample.temperature, sample.humidity, sample.pressure, sample.windspeed]
  samples = [1,2,3,4]
  return jsonify(samples)

@app.route('/average', methods = ["GET"])
def get_average():
  sample = db.get_average()
  #sample = [1,2,3,4]
  return jsonify(sample)

if __name__ == "__main__":
  app.run(host='0.0.0.0', port=8888)

