import time
import os


def loading():
    for i in range(101):
        print("Loading...")
        print(f"{i}%")
        print(i*'#')
        time.sleep(0.05)
        os.system("cls")
