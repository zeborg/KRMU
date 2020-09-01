from Screenshot import Screenshot_Clipping
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
from getpass import getpass
import os

FILE_PATH = os.path.dirname(os.path.realpath(__file__))

try:
	co = Options()
	co.add_argument('start-maximized')
	co.add_argument('headless')
	co.add_argument('--disable-dev-shm-usage')
	co.add_argument('--no-sandbox')
	co.add_experimental_option('excludeSwitches', ['enable-automation'])
	co.add_experimental_option('useAutomationExtension', False)
	print()
	usr = input('Enter your KRMU Roll No.: ')
	pwd = getpass('Enter your Unisoft Password: ')
	
	driver = webdriver.Chrome(executable_path=os.path.join(FILE_PATH,'chromedriver'),options=co)
	driver.get('http://student.krmangalam.edu.in/StudentLoginNew.aspx')

	WebDriverWait(driver,30).until(
		EC.presence_of_element_located((By.ID,'username'))
	).send_keys(usr)
	WebDriverWait(driver,30).until(
	    EC.presence_of_element_located((By.ID,'password'))
	).send_keys(pwd)
	WebDriverWait(driver,30).until(
	    EC.presence_of_element_located((By.ID,'StuLogin'))
	).click()
	WebDriverWait(driver,30).until(
	    EC.presence_of_element_located((By.LINK_TEXT,'Attendance'))
	).click()

	table_id = WebDriverWait(driver,30).until(
	    EC.presence_of_element_located((By.ID,'ContentPlaceHolder1_tbody'))
	)
	rows = table_id.find_elements(By.TAG_NAME, 'tr')

	print()
	print('--------------------------------')
	print('COURSE CODE    ATTD/TOT  ATTD %')
	print('--------------------------------')
	for row in rows:
		col = row.find_elements(By.TAG_NAME, 'td')
		for c in col:
			print(c.text,'\t',end=' ')
		print()
	print('--------------------------------')
	print('TOTAL ATTENDANCE %:\t ',end='')
	print(WebDriverWait(driver,30).until(
	    EC.presence_of_element_located((By.ID,'ContentPlaceHolder1_lblTotal'))
	).text)
	print('--------------------------------')
	print()

	SS_FOLDER = f'{FILE_PATH}/Screenshots'

	if not os.path.exists(SS_FOLDER):
		os.makedirs(SS_FOLDER)

	k = Screenshot_Clipping.Screenshot().get_element(driver,WebDriverWait(driver,30).until(
	    EC.presence_of_element_located((By.ID,'ContentPlaceHolder1_tblAttendance'))
	    ),r'./Screenshots')

	os.remove(os.path.join(SS_FOLDER,'clipping_shot.png'))
	ssname = f'{usr}_{datetime.now().strftime("%d-%m-%Y_%H%M%S")}'
	os.rename(os.path.join(SS_FOLDER,k),os.path.join(SS_FOLDER,ssname))

finally:
	driver.quit()
