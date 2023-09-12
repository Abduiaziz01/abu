import time

class Timer:
    def __init__(self, seconds):
        self.seconds = seconds

    def get_time(self):
        return self.seconds

    def start(self):
        while self.seconds > 0:
            print(self.seconds)
            time.sleep(1)
            self.seconds -= 1
        print("Таймер завершен.")

    def resert(self):
        self.seconds = self.initial_seconds

timer = Timer(10)
timer.start()
