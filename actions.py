import subprocess

def open_safari():
    subprocess.run(["open", "-a", "Safari"])

def speak(text):
    subprocess.run(["say", text])