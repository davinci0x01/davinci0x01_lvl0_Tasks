from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time

class Handler(FileSystemEventHandler):
    def on_any_event(self, event):
        print(event.event_type, "->", event.src_path)

path = input("Enter folder path: ")

observer = Observer()
observer.schedule(Handler(), path, recursive=False)
observer.start()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()

observer.join()