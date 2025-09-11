#!/usr/bin/env python3
# GUI Tkinter Cliente XML-RPC para factorial

import tkinter as tk
from tkinter import messagebox
import xmlrpc.client

class FactorialGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Cliente Factorial RPC")
        self.geometry("360x180")

        tk.Label(self, text="Host:").grid(row=0, column=0, padx=8, pady=6, sticky="e")
        self.host_var = tk.StringVar(value="127.0.0.1")
        tk.Entry(self, textvariable=self.host_var, width=18).grid(row=0, column=1, padx=8, pady=6)

        tk.Label(self, text="Puerto:").grid(row=0, column=2, padx=8, pady=6, sticky="e")
        self.port_var = tk.StringVar(value="9200")
        tk.Entry(self, textvariable=self.port_var, width=8).grid(row=0, column=3, padx=8, pady=6)

        tk.Label(self, text="Número:").grid(row=1, column=0, padx=8, pady=6, sticky="e")
        self.n_var = tk.StringVar()
        tk.Entry(self, textvariable=self.n_var, width=12).grid(row=1, column=1, padx=8, pady=6)

        self.btn = tk.Button(self, text="Calcular", command=self.calcular)
        self.btn.grid(row=2, column=0, columnspan=4, padx=8, pady=10)

        self.result_var = tk.StringVar(value="Resultado: —")
        tk.Label(self, textvariable=self.result_var, font=("Segoe UI", 11, "bold")).grid(row=3, column=0, columnspan=4, pady=8)

    def calcular(self):
        try:
            host = self.host_var.get().strip() or "127.0.0.1"
            port = int(self.port_var.get())
            n = int(self.n_var.get())
            if n < 0:
                raise ValueError("El número debe ser no negativo")
            url = f"http://{host}:{port}/RPC2"
            proxy = xmlrpc.client.ServerProxy(url, allow_none=True)
            r = proxy.factorial(n)
            self.result_var.set(f"Resultado: {r}")
        except Exception as e:
            messagebox.showerror("Error", str(e))

if __name__ == "__main__":
    app = FactorialGUI()
    app.mainloop()
