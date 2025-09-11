#!/usr/bin/env python3
# Cliente CLI para multiplicación de matrices

import argparse
import xmlrpc.client

def parse_matrix(s: str):
	# Filas separadas por ';', columnas por espacios o comas
	rows = [r.strip() for r in s.split(';') if r.strip()]
	return [[float(x) for x in r.replace(',', ' ').split()] for r in rows]

def main():
	parser = argparse.ArgumentParser(description="Cliente Matmul")
	parser.add_argument("--A", help='Matriz A. Ej: "1 2;3 4"')
	parser.add_argument("--B", help='Matriz B. Ej: "5 6;7 8"')
	parser.add_argument("--host", default="127.0.0.1")
	parser.add_argument("--port", type=int, default=9204)
	args = parser.parse_args()

	url = f"http://{args.host}:{args.port}/RPC2"
	proxy = xmlrpc.client.ServerProxy(url, allow_none=True)

	A = parse_matrix(args.A) if args.A else parse_matrix(input("A (filas con ';'): "))
	B = parse_matrix(args.B) if args.B else parse_matrix(input("B (filas con ';'): "))
	C = proxy.matmul(A, B)
	for row in C:
		print(' '.join(f"{v:.2f}" for v in row))

if __name__ == "__main__":
	main()