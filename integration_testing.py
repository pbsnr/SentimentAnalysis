import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class IntegrationTesting(unittest.TestCase):

	def verifySentences(self, input, output):
		self.driver = webdriver.Firefox()
		self.driver.get("http://localhost:5000")
		time.sleep(2)
		elem = self.driver.find_elements(By.XPATH, '/html/body/form/center/p[2]/textarea')
		elem[0].send_keys(input)
		time.sleep(2)
		elem = self.driver.find_elements(By.XPATH, '/html/body/form/center/p[2]/input')
		elem[0].submit()
		time.sleep(2)
		elem = self.driver.find_elements(By.XPATH, '/html/body/center/span/div')
		self.assertEqual(elem[0].text, output)
		time.sleep(2)
		self.driver.close()


	def test_verifyTemplateLoaded(self):
		self.driver = webdriver.Firefox()
		self.driver.get("http://localhost:5000")
		time.sleep(2)
		elem = self.driver.find_elements(By.XPATH, '/html/body/form/center/h1')
		self.assertEqual(elem[0].text, 'Text sentiment analysis')
		self.driver.close()

	def test_verifySentences(self):

		self.verifySentences("I love Data engineering", '😀')
		self.verifySentences("I hate Covid-19", '☹️')
		self.verifySentences("I am blue dabadee dabadaa", '😐')


if __name__ == '__main__':
	unittest.main()
