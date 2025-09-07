#!/usr/bin/python

# Autor: Brayan Sanchez
# Fecha: 07/09/25
# Desarrollo del servidor
# Crea un servicio RPC que exponga una función para calcular el factorial de un 
# :: * número enviado por el cliente. 

import socket
import json 

def facto(x):
    if ( x == 0 or x == 1 ):
        return 1
    else:
        return x * facto(x - 1)

print(facto(10))

# switch 
#if __name__ == "__main__":
    
#    SERVIDOR_IP = "127.0.0.1"
#    SERVIDOR_PORT = 9200

    # CREACION DEL SOCKET 
#    servidor_base = socket.socket( socket.AF_INET, socket.SOCK_STREAM)


    

