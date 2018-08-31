from database import Database
from models import Samples

import random
import time
import signal
import sys

db = Database()

class GracefulKiller:
    kill_now = False
    def __init__(self):
        signal.signal(signal.SIGINT, self.exit_gracefully)
        signal.signal(signal.SIGTERM, self.exit_gracefully)

    def exit_gracefully(self, signum, frame):
        self.kill_now = True


def main(sample):
    killer = GracefulKiller()
    while(1):
        sample.temperature += random.randint(-1,1)
        sample.humidity += random.randint(-1,1)
        sample.pressure += random.randint(-1,1)
        sample.windspeed += random.randint(-1,1)
        db.add_sample(sample)
        time.sleep(1)
        if killer.kill_now:
            session.close()
            break


if __name__ == '__main__':
    if (len(sys.argv) != 2):
        sys.exit("Usage: python process.py id_sample")
    id_sample = int(sys.argv[1])
    session = db.get_session()
    sample = session.query(Samples).filter_by(id=id_sample).first()
    session.close()
    main(sample)
    