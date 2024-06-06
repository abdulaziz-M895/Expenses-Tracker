import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
import requests

class ExpenseTracker:
  def __init__(self, root):
      self.root = root
      self.root.title("Expense Tracker")
      self.root.geometry("800x600")
      
      self.create_widgets()
      self.currency_conversion = {}
      self.get_conversion_rates()

  def create_widgets(self):
      self.amount_label = tk.Label(self.root, text="Amount")
      self.amount_label.pack()
      self.amount_entry = tk.Entry(self.root)
      self.amount_entry.pack()

      self.currency_label = tk.Label(self.root, text="Currency")
      self.currency_label.pack()
      self.currency_combo = ttk.Combobox(self.root)
      self.currency_combo.pack()

      self.category_label = tk.Label(self.root, text="Category")
      self.category_label.pack()
      self.category_combo = ttk.Combobox(self.root, values=[
          "life expenses", "electricity", "grocery", "rental", "charity", "savings", "education"])
      self.category_combo.pack()

      self.payment_label = tk.Label(self.root, text="Payment Method")
      self.payment_label.pack()
      self.payment_combo = ttk.Combobox(self.root, values=["Cash", "Card", "Credit", "Paypal"])
      self.payment_combo.pack()

      self.date_label = tk.Label(self.root, text="Date")
      self.date_label.pack()
      self.date_entry = tk.Entry(self.root)
      self.date_entry.pack()

      self.add_button = tk.Button(self.root, text="Add Expense", command=self.add_expense)
      self.add_button.pack()

      self.tree = ttk.Treeview(self.root, columns=("Amount", "Currency", "Category", "Payment Method", "Date"), show='headings')
      self.tree.heading("Amount", text="Amount")
      self.tree.heading("Currency", text="Currency")
      self.tree.heading("Category", text="Category")
      self.tree.heading("Payment Method", text="Payment Method")
      self.tree.heading("Date", text="Date")
      self.tree.pack(fill=tk.BOTH, expand=True)

      self.total_label = tk.Label(self.root, text="Total: 0 USD", bg='lightgreen')
      self.total_label.pack()

  def get_conversion_rates(self):
      url = "https://v6.exchangerate-api.com/v6/94c69aab32cac2b61e3557b1/latest/USD"
      response = requests.get(url)
      if response.status_code == 200:
          data = response.json()
          self.currency_conversion = data['conversion_rates']
          self.currency_combo['values'] = list(self.currency_conversion.keys())
      else:
          messagebox.showerror("Error", "Failed to fetch currency rates")

  def add_expense(self):
      amount = self.amount_entry.get()
      currency = self.currency_combo.get()
      category = self.category_combo.get()
      payment = self.payment_combo.get()
      date = self.date_entry.get()

      if not amount or not currency or not category or not payment or not date:
          messagebox.showerror("Error", "Please fill out all fields")
          return

      try:
          amount = float(amount)
      except ValueError:
          messagebox.showerror("Error", "Please enter a valid number for amount")
          return

      try:
          datetime.strptime(date, '%Y-%m-%d')
      except ValueError:
          messagebox.showerror("Error", "Please enter a valid date in YYYY-MM-DD format")
          return

      self.tree.insert("", tk.END, values=(amount, currency, category, payment, date))
      self.calculate_total()
      self.reset_form()

  def reset_form(self):
      self.amount_entry.delete(0, tk.END)
      self.currency_combo.set('')
      self.category_combo.set('')
      self.payment_combo.set('')
      self.date_entry.delete(0, tk.END)

  def calculate_total(self):
      total = 0
      for row in self.tree.get_children():
          amount_str, currency, *_ = self.tree.item(row)['values']
          amount = float(amount_str)
          if currency in self.currency_conversion:
              total += amount / self.currency_conversion[currency]

      self.total_label.config(text=f"Total: {round(total, 2)} USD")

if __name__ == "__main__":
  root = tk.Tk()
  app = ExpenseTracker(root)
  root.mainloop()
