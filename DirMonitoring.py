import sys
import time
import logging
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler


def main():
    path = input("Dir name : >> ")
    choose = input ("Press '1' To print Logs HERE or '2' For Save To logs_file >> ")
    if choose == '1':
        logging.basicConfig(level=logging.INFO,format='%(asctime)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S') 
    elif choose=='2':
        print("Your logging saved successfully to ' ROOT Dir in logging.txt'")
        logging.basicConfig(level=logging.INFO,format='%(asctime)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S', filename=r"/root/logging.txt")

    event_handler = LoggingEventHandler() # Fo_Logs 
    observer = Observer() #For_watching 
    observer.schedule(event_handler, path, recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

    
