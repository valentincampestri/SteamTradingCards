#Github: https://github.com/valentincampestri
#Steam: https://steamcommunity.com/id/-Cosmodius-/

import webbrowser
from colorama import *
init()
import requests
from bs4 import BeautifulSoup

linkDeJuegos = input('Ingresar link del producto para buscar sus cromos. Si desea ingresar más de 1, separarlos SOLAMENTE con una coma (","):\n')
linkDeJuegos2 = linkDeJuegos.split(",")
cantidad = 0

while cantidad < len(linkDeJuegos2):

	inicio = ""
	appId = ""
	for letra in linkDeJuegos2[cantidad]:
		if letra.isnumeric() or (letra == "/" and len(appId) != 0):
			if letra != "/":
				appId += letra
			else:
				break
		else:
			inicio += letra

	linkCromosDelJuego = "https://steamcommunity.com/market/search?appid=753&category_753_Game%5B%5D=tag_app_" + appId + "&q=trading"

	if (inicio == "https://store.steampowered.com/app/") and len(appId) > 0:
		result = requests.get(linkDeJuegos2[cantidad])
		content = result.text
		soup = BeautifulSoup(content, "lxml")
		nombreJuego = soup.find("div", id="appHubAppName").get_text()
		if not "Steam Trading Cards" in content:
			print(Fore.YELLOW + "\n" + nombreJuego + " no cuenta con cromos.")
		else:
			print(Fore.GREEN + "\nCromos de " + nombreJuego + " encontrados!")
			webbrowser.open(linkCromosDelJuego)
	elif (inicio == "store.steampowered.com/app/") and len(appId) > 0:
		result = requests.get("https://" + linkDeJuegos2[cantidad])
		content = result.text
		soup = BeautifulSoup(content, "lxml")
		nombreJuego = soup.find("div", id="appHubAppName").get_text()
		if not "Steam Trading Cards" in content:
			print(Fore.YELLOW + "\n" + nombreJuego + " no cuenta con cromos.")
		else:
			print(Fore.GREEN + "\nCromos de " + nombreJuego + " encontrados!")
			webbrowser.open(linkCromosDelJuego)
	else:
		print(Fore.RED + "\nEl link N°"+ str(cantidad+1) + " que ingresó no pertenece al de un producto de Steam, compruebe que sea correcto.")

	cantidad += 1

print(Fore.RESET)
input("\nPresione enter para finalizar el programa.")