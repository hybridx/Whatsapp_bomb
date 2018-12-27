#use python 2.7
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

times = int(input("Enter number of times:"))
message = raw_input("Enter the text you want to send:")
driver = None

def wait(SleepTime = 3):
	time.sleep(SleepTime)


def web_driver_load():
	global driver
	driver = webdriver.Chrome(raw_input("Enter you chrome driver path:")) #Enter your path here

def web_driver_quit():
	driver.quit()
	quit()


def whatsapp_login():
	driver.get('https://web.whatsapp.com/')
	wait(20)

def sendMessage(msg='Hi!'):
	web_obj = driver.find_element_by_xpath("//div[@contenteditable='true']")
	web_obj.send_keys(msg)
	web_obj.send_keys(Keys.RETURN)


if __name__ == "__main__":
	web_driver_load()
	whatsapp_login()
	for i in range(times):
		sendMessage(message)
		#wait(1)

	print("Process complete successfully")
web_driver_quit()
