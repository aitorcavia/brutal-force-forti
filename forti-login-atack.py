from selenium import webdriver
import time, os

array = []

with open ("/home/kali/Documentos/dictionary/others/diccionarios/usuarios.txt", 'r') as archivo:
	array.append(archivo.read())

web = webdriver.Firefox()
web.get('https://192.168.0.2:8443')
o#s.system("firefox https://192.168.0.2:8443 &")

def login():
	user = "user"
	passw = "pass"
	inputuser = web.find_element_by_spath("//*[@id='username']")
	inputuser.send_keys(user)
	inputpass = web.find_element_by_spath("//*[@id='secretkey']")
	inputpass.send_keys(passw)
	
	loginbtn = web.find_element_by_spath("//*[@id='login_button']").click()
	
time.sleep(2)
login()

#def login():
	
