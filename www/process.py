from database import Database
from models import Samples

import random
import time
import signal

def main(sample, session):
  killer = GracefulKiller()

  while(1):
    sample.temperature += random.uniform(-0.5,0.5)
    sample.humidity += random.uniform(-0.5,0.5)
    sample.pressure += random.uniform(-0.5,0.5)
    sample.windspeed += random.uniform(-0.5,0.5)
    session.add(sample)
    session.commit()
    time.sleep(1)

if __name__ == '__main__':
  db = Database()
  session = db.get_session()
  sample = session.query(Samples).first()
  main(sample, session)
