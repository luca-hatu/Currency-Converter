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
    try:
        amount = float(amount_entry.get())
        from_currency = from_currency_combobox.get()
        to_currency = to_currency_combobox.get()
        if not from_currency or not to_currency:
            result_label.config(text="Please select both currencies.", fg="red")
            return
        rates = fetch_exchange_rates()
        converted_amount = convert_currency(amount, from_currency, to_currency, rates)
        result_label.config(text=f"{amount} {from_currency} = {converted_amount} {to_currency}", fg="green")
    except ValueError:
        result_label.config(text="Invalid amount. Please enter a number.", fg="red")

root = tk.Tk()
root.title("Currency Converter")
root.geometry("300x200")
root.iconbitmap('exchange.ico')

amount_label = tk.Label(root, text="Amount:")
amount_label.grid(column=0, row=0, padx=10, pady=5)
amount_entry = tk.Entry(root)
amount_entry.grid(column=1, row=0, padx=10, pady=5)

from_currency_label = tk.Label(root, text="From Currency:")
from_currency_label.grid(column=0, row=1, padx=10, pady=5)
from_currency_combobox = ttk.Combobox(root, values=list(fetch_exchange_rates().keys()))
from_currency_combobox.grid(column=1, row=1, padx=10, pady=5)

to_currency_label = tk.Label(root, text="To Currency:")
to_currency_label.grid(column=0, row=2, padx=10, pady=5)
to_currency_combobox = ttk.Combobox(root, values=list(fetch_exchange_rates().keys()))
to_currency_combobox.grid(column=1, row=2, padx=10, pady=5)

convert_button = tk.Button(root, text="Convert", command=convert)
convert_button.grid(column=1, row=3, padx=10, pady=10)

result_label = tk.Label(root, text="")
result_label.grid(column=0, row=4, columnspan=2)

root.mainloop()
