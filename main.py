import os

if __name__ == '__main__':
    os.system("echo 'Welcome! I am Robo Speaker 1.0, created by Zohaib Asif.' | espeak")
    print("Welcome! I am Robo Speaker 1.0, created by Zohaib Asif.")
    print("Press \\q to exit.")
    os.system("echo 'Please type what do you want me to speak' | espeak")
    while True:
        words = input("What do you want me to speak? ")
        if words == "\q":
            os.system("echo 'Exiting Robo Speaker. Good Bye!' | espeak")
            break
        command = f"echo {words} | espeak"
        os.system(command)
