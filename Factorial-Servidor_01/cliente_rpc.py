#!/usr/bin/env python3
# Cliente XML-RPC para calcular factorial

import sys, time
import xmlrpc.client


IP_SERV = "192.168.100.37"
PORT = 9200

def main():
    print("### CÁLCULO DE FACTORIAL ###")
    try:
        time.sleep(0.2)
        print("[CLIENTE] Iniciando...")
        print()
        time.sleep(0.2)
        url = f"http://{IP_SERV}:{PORT}/"
        proxy = xmlrpc.client.ServerProxy(url, allow_none=True)


        print(f"[CLIENTE] Conectado a {url}")
        n = int(input("Ingrese un numero entero: "))
        if n < 0:
            print("El número debe ser no negativo.")
            sys.exit(1)




        resultado = proxy.factorial(n)
        print(f"Factorial({n}) = {resultado}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
