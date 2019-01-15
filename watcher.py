import time
import sys
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler # PatternMatchingEventHandler

from app import helper as h
from app import constant as c
from app import helper as h
import main


class Watcher:

    def __init__(self, DIRECTORY_TO_WATCH):
        self.DIRECTORY_TO_WATCH = DIRECTORY_TO_WATCH
        self.observer = Observer()

    def run(self):
        event_handler = Handler()
        h.logger(f"Watcher has started")
        self.observer.schedule(event_handler, self.DIRECTORY_TO_WATCH, recursive=True)
        self.observer.start()
        try:
            while True:
                time.sleep(1)
        except:
            self.observer.stop()
            h.logger(f"File watcher has been finalized")

        self.observer.join()


class Handler( FileSystemEventHandler ): #PatternMatchingEventHandler ):
    #patterns = c.EXT_ALLOWED_INPUT
    @staticmethod
    def on_any_event(event):
      try:
        if event.event_type == 'created' and not event.is_directory:
          pathAndFilename = event.src_path
          h.logger(f"File {h.removePath( pathAndFilename )} has been added.")
          main.run( pathAndFilename )
      except Exception as e:
        h.logger(f"Something wrong on watcher. Erro: {str(e)}") 

if __name__ == '__main__':
  args = sys.argv[1:] # get params
  w = Watcher( DIRECTORY_TO_WATCH=args[0] if args else '.' )
  w.run()