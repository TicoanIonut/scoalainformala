import datetime
import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


class LocationTest(unittest.TestCase):
	
	def setUp(self):
		self.driver = webdriver.Chrome(ChromeDriverManager().install())
		self.driver.get('http://127.0.0.1:8000')
		username = self.driver.find_element_by_name('username')
		username.send_keys('2dor')
		password = self.driver.find_element_by_name('password')
		password.send_keys('howhigh4574')
		submit = self.driver.find_element_by_class_name('btn-info')
		submit.submit()
		self.logs = open('logs.txt', mode='a')
	
	def test_form(self):
		if value := 'table' in self.driver.page_source:
			self.logs.write(f"{value}, {datetime.datetime.now()}\n")
		assert value
