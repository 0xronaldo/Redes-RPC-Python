#!/usr/bin/env python3
# GUI Tkinter para cadenas upper/lower

import tkinter as tk
from tkinter import ttk
import xmlrpc.client

class CadenasGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Cliente Cadenas RPC")
        self.geometry("480x200")

        self.host_var = tk.StringVar(value="192.168.100.37")
        self.port_var = tk.StringVar(value="9200")
        self.mode_var = tk.StringVar(value="upper")
        self.input_var = tk.StringVar()
        self.output_var = tk.StringVar(value="→ Resultado aquí")

        row = 0
        tk.Label(self, text="Host:").grid(row=row, column=0, padx=8, pady=6, sticky="e")
        tk.Entry(self, textvariable=self.host_var, width=16).grid(row=row, column=1, padx=8, pady=6)
        tk.Label(self, text="Puerto:").grid(row=row, column=2, padx=8, pady=6, sticky="e")
        tk.Entry(self, textvariable=self.port_var, width=8).grid(row=row, column=3, padx=8, pady=6)

        row += 1
        ttk.Combobox(self, textvariable=self.mode_var, values=["upper", "lower"], width=12).grid(row=row, column=0, columnspan=2, padx=8, pady=6)
        tk.Entry(self, textvariable=self.input_var, width=30).grid(row=row, column=2, columnspan=2, padx=8, pady=6)

        row += 1
        tk.Button(self, text="Transformar", command=self.transformar).grid(row=row, column=0, columnspan=4, pady=10)

        row += 1
        tk.Label(self, textvariable=self.output_var, font=("Segoe UI", 11, "bold")).grid(row=row, column=0, columnspan=4, pady=8)

    def transformar(self):
        IP_SERVER = self.host_var.get().strip()
        PORT = int(self.port_var.get())
        url = f"http://{IP_SERVER}:{PORT}"
        proxy = xmlrpc.client.ServerProxy(url, allow_none=True)
        text = self.input_var.get()
        mode = self.mode_var.get()
        if mode == "mayus":
            res = proxy.func_mayusculas(text)
        else:
            res = proxy.func_minusculas(text)
        self.output_var.set(res)

if __name__ == "__main__":
    CadenasGUI().mainloop()
