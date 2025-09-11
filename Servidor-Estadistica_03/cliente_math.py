#!/usr/bin/env python3
# Cliente XML-RPC para estadísticas

import argparse
import xmlrpc.client

def parse_list(s: str):
	return [float(x) for x in s.replace(",", " ").split()] if s else []

def main():
	parser = argparse.ArgumentParser(description="Cliente Estadística (mean/median/stdev)")
	parser.add_argument("--op", choices=["mean", "median", "stdev"], default="mean")
	parser.add_argument("--data", help='Lista de números, separados por espacio o coma. Ej: "1,2,3 4"')
	parser.add_argument("--host", default="127.0.0.1")
	parser.add_argument("--port", type=int, default=9202)
	args = parser.parse_args()

	url = f"http://{args.host}:{args.port}/RPC2"
	proxy = xmlrpc.client.ServerProxy(url, allow_none=True)

	data = parse_list(args.data) if args.data else parse_list(input("Datos: "))
	op = getattr(proxy, args.op)
	print(op(data))

if __name__ == "__main__":
	main()