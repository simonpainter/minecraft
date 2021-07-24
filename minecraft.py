

class empower_server:
	from selenium import webdriver
	from selenium.webdriver.common.by import By
	from selenium.webdriver.common.keys import Keys
	import time

	def __init__(self,server, user, password):
		self.server =server
		self.user = user
		self.password = password
		self.browser=self.webdriver.Safari()
		self.browser.get("https://control.empowerservers.com/server/" + self.server + "/console")
		input=self.browser.find_element_by_name("user")
		input.send_keys(self.user)
		input=self.browser.find_element_by_name("password")
		input.send_keys(self.password)
		input.send_keys(self.Keys.ENTER)
		self.time.sleep(3)
	def sendCommand(self,command_string):
		input=self.browser.find_element_by_tag_name("input")
		input.send_keys(command_string)
		input.send_keys(self.Keys.ENTER)
	def setBlock(self,x,y,z,block_name):
		command = "setblock " + str(x) + " " + str(y) + " " + str(z) +  " " + block_name
		self.sendCommand(command)

