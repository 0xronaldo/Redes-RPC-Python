#!/usr/bin/env python3
# Cliente XML-RPC para calcular factorial

import argparse
import sys
import time
import xmlrpc.client

def main():
	parser = argparse.ArgumentParser(description="Cliente XML-RPC para factorial")
	parser.add_argument("n", nargs="?", type=int, help="Número entero no negativo")
	parser.add_argument("--host", default="127.0.0.1", help="Host del servidor (default: 127.0.0.1)")
	parser.add_argument("--port", type=int, default=9200, help="Puerto del servidor (default: 9200)")
	args = parser.parse_args()

	url = f"http://{args.host}:{args.port}/RPC2"
	proxy = xmlrpc.client.ServerProxy(url, allow_none=True)

	time.sleep(0.2)
	print(f"[CLIENTE] Conectado a {url}")
	print("### CÁLCULO DE FACTORIAL ###")

	try:
		n = args.n if args.n is not None else int(input("Ingrese un número entero >= 0: "))
		if n < 0:
			print("El número debe ser no negativo.")
			sys.exit(1)
		resultado = proxy.factorial(int(n))
		print(f"Factorial({n}) = {resultado}")
	except Exception as e:
		print(f"Error: {e}")

if __name__ == "__main__":
	main()
