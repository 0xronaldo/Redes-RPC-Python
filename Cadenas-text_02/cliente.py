#!/usr/bin/env python3
# autor: Brayan Ronaldo
# Fecha: 10/09/25
# enenciado : Implementa un servidor RPC que permita convertir cadenas de texto en 
# mayúsculas o minúsculas según la elección del cliente. 
# Cliente XML-RPC para cadenas: mayus/minus

import xmlrpc.client
import time
IP_SRV = "192.168.100.37"
PORT = 9200
def servidor_cadenas():
	url = f"http://{IP_SRV}:{PORT}/"
	proxy = xmlrpc.client.ServerProxy(url, allow_none=True)
	time.sleep(0.2)
	print(f"[CLIENTE] conectado a {url}")
	mensaje = input("Ingrese texto: ")
	mode = input("Elija modo ('1 mayuscula' o '2 minuscula'): ")

	if mode == "1":
		print(proxy.func_mayusculas(mensaje))
	elif mode == "2":
		print(proxy.func_minusculas(mensaje))
	else:
		print("Modo no válido. Use 'mayuscula' o 'minuscula'.")

if __name__ == "__main__":
	servidor_cadenas()
