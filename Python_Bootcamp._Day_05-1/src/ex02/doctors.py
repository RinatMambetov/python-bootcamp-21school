import os
import threading
import time


def main():
    class Doctor:
        def __init__(self, number):
            self.number = number
            self.left_screwdriver = None
            self.right_screwdriver = threading.Lock()

        def grab_screwdrivers(self):
            # Try to grab the left screwdriver from the doctor on the left
            left_doctor = (self.number - 9 + 4) % 5 + 9
            while True:
                if doctors[left_doctor - 9].right_screwdriver.acquire(blocking=False):
                    self.left_screwdriver = doctors[left_doctor - 9].right_screwdriver
                    break

            # Try to grab the right screwdriver
            self.right_screwdriver.acquire()

        def release_screwdrivers(self):
            self.left_screwdriver.release()
            self.right_screwdriver.release()

        def blast(self):
            print(f"Doctor {self.number}: BLAST!")

    def doctor_thread(doc):
        while True:
            doc.grab_screwdrivers()
            doc.blast()
            doc.release_screwdrivers()
            time.sleep(0.1)
            os._exit(0)

    doctors = [Doctor(i) for i in range(9, 14)]

    while True:
        threads = []
        for doctor in doctors:
            t = threading.Thread(target=doctor_thread, args=(doctor,))
            threads.append(t)
            t.start()

        for t in threads:
            t.join()

        # Contain only the doctors who have a left screwdriver
        doctors = [doctor for doctor in doctors if doctor.left_screwdriver is not None]
        if len(doctors) == 0:
            break


if __name__ == '__main__':
    main()
