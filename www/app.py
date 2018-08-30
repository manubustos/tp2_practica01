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
  if pro.is_running():
    return index()
  d_s = {}
  d_s["temperatura"] = random.randint(10,30)
  d_s["humedad"] = random.randint(0,100)
  d_s["presion"] = random.randint(1000, 1020)
  d_s["viento"] = random.randint(10, 30)
  id_sample = db.init_sample(d_s)
  pro.start_process(id_sample)
  return render_template('index.html', id_sample=id_sample)

@app.route('/last', methods = ["GET"])
def get_last():
  sample = db.get_last_sample()
  samples = [sample.temperature, sample.humidity, sample.pressure, sample.windspeed]
  return jsonify(samples)

@app.route('/average', methods = ["GET"])
def get_average():
  samples = db.last_ten_samples();
  
  temp = 0;
  hum = 0;
  pres = 0;
  vien = 0;

  for sample in samples:
    temp = temp + sample.temperature;
    hum = hum + sample.humidity;
    pres = pres + sample.pressure;
    vien = vien + sample.windspeed;
  
  promedioTemp = temp / 10;
  promedioHum = hum / 10;
  promedioPres = pres / 10;
  promedioVien = vien / 10;

  promedio = [promedioTemp, promedioHum, promedioPres, promedioVien];

  return jsonify(promedio)

if __name__ == "__main__":
  app.run(host='0.0.0.0', port=8888)

