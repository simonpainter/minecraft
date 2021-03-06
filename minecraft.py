

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
		input=self.browser.find_element_by_name("email")
		input.send_keys(self.user)
		input=self.browser.find_element_by_id("password-input")
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
	def fill(self,x_start, y_start, z_start, x_end, y_end, z_end, block_name):
		command = "fill " + str(x_start) + " " + str(y_start) + " " + str(z_start) + " " + str(x_end) + " " + str(y_end) + " " + str(z_end) + " " + block_name
		self.sendCommand(command)

	def close(self):
		self.browser.close()
