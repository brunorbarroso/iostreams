import time  
import sys
from watchdog.observers import Observer  
from watchdog.events import PatternMatchingEventHandler
from app import helper as h
from app import constant as c
import main

class handleWatchFileSystem( PatternMatchingEventHandler ):
    patterns = c.EXT_ALLOWED_INPUT

    def process(self, event):
        # the file will be processed there
        if event.event_type == 'created':
            h.logger(f"File {event.src_path} has been added.")  # print now only for degug
            main.run( event.src_path )

    def on_modified(self, event):
        self.process(event)

    def on_created(self, event):
        self.process(event)

if __name__ == '__main__':
  args = sys.argv[1:]
  observer = Observer()
  observer.schedule( handleWatchFileSystem(), path=args[0] if args else '.' )
  observer.start()
  h.logger(f"Watcher has started")

  try:
      while True:
          time.sleep(1)
  except KeyboardInterrupt:
      h.logger(f"File watcher has been finalized")
      observer.stop()

  observer.join()