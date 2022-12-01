def main():
    print("StayAwake is loading...")
    import time
    import pyautogui
    import random
    print("Welcome to StayAwake")

    while True:
        x = random.randint(1, 640)
        y = random.randint(1, 480)
        time.sleep(2)
        pyautogui.moveTo(x, y, duration = 1)
if __name__ == "__main__":
    main()