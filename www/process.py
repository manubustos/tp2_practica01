from database import Database
from models import Samples

import random
import time
import signal
import sys

class GracefulKiller:
  kill_now = False
  def __init__(self):
    signal.signal(signal.SIGINT, self.exit_gracefully)
    signal.signal(signal.SIGTERM, self.exit_gracefully)

  def exit_gracefully(self, signum, frame):
    self.kill_now = True


def main(muestras, session):
  killer = GracefulKiller()

  while(1):
    muestra.temperature += random.uniform(-0.5,0.5)
    muestra.humidity += random.uniform(-0.5,0.5)
    muestra.pressure += random.uniform(-0.5,0.5)
    muestra.windspeed += random.uniform(-0.5,0.5)
    session.add(muestra)
    session.commit()
    time.sleep(1)
    if killer.kill_now:
      session.close()
      break

if __name__ == '__main__':
  db = Database()
  session = db.get_session()
  muestra = session.query(Samples).first()
  main(muestra, session)
