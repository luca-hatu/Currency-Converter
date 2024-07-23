import requests
import tkinter as tk
from tkinter import ttk

API_URL = "https://api.exchangerate-api.com/v4/latest/USD"

def fetch_exchange_rates():
    response = requests.get(API_URL)
    data = response.json()
    return data['rates']

def convert_currency(amount, from_currency, to_currency, rates):
    if from_currency != "USD":
        amount = amount / rates[from_currency]
    return round(amount * rates[to_currency], 2)

def convert():
    amount = float(amount_entry.get())
    from_currency = from_currency_combobox.get()
    to_currency = to_currency_combobox.get()
    rates = fetch_exchange_rates()
    converted_amount = convert_currency(amount, from_currency, to_currency, rates)
    result_label.config(text=f"{amount} {from_currency} = {converted_amount} {to_currency}")

root = tk.Tk()
root.title("Currency Converter")

amount_label = tk.Label(root, text="Amount:")
amount_label.grid(column=0, row=0)
amount_entry = tk.Entry(root)
amount_entry.grid(column=1, row=0)

from_currency_label = tk.Label(root, text="From Currency:")
from_currency_label.grid(column=0, row=1)
from_currency_combobox = ttk.Combobox(root)
from_currency_combobox.grid(column=1, row=1)

to_currency_label = tk.Label(root, text="To Currency:")
to_currency_label.grid(column=0, row=2)
to_currency_combobox = ttk.Combobox(root)
to_currency_combobox.grid(column=1, row=2)

convert_button = tk.Button(root, text="Convert", command=convert)
convert_button.grid(column=1, row=3)

result_label = tk.Label(root, text="")
result_label.grid(column=1, row=4)

root.mainloop()

