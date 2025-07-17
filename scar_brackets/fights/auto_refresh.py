import threading
import time
from django.core.management import call_command
import schedule

def job_runner(interval=1):
    cease_continuous_run = threading.Event()

    class ScheduleThread(threading.Thread):
        @classmethod
        def run(cls):
            while not cease_continuous_run.is_set():
                schedule.run_pending()
                time.sleep(interval)

    continuous_thread = ScheduleThread()
    continuous_thread.daemon = True
    continuous_thread.start()
    return cease_continuous_run

def start_auto_refresh():
    job_runner()
    print("Started auto refresh")

def refresh():
    call_command("update_from_api")

schedule.every(30).seconds.do(refresh)
