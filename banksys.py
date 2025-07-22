# Enhanced UI version of Bank Management System with PIN using Tk

import tkinter as tk
from tkinter import messagebox
import os
import json

ACCOUNTS_FILE = "accounts.json"

# Load accounts
def load_accounts():
    if os.path.exists(ACCOUNTS_FILE):
        with open(ACCOUNTS_FILE, 'r') as f:
            return json.load(f)
    return {}

# Save accounts
def save_accounts(accounts):
    with open(ACCOUNTS_FILE, 'w') as f:
        json.dump(accounts, f)

accounts = load_accounts()

# Functions
def create_account():
    acc_no = entry_acc.get()
    name = entry_name.get()
    pin = entry_pin.get()
    balance = entry_amt.get()

    if not acc_no or not name or not balance or not pin:
        messagebox.showerror("Error", "All fields are required!")
        return

    if acc_no in accounts:
        messagebox.showerror("Error", "Account already exists!")
        return

    try:
        balance = float(balance)
    except ValueError:
        messagebox.showerror("Error", "Invalid balance amount!")
        return

    accounts[acc_no] = {"name": name, "balance": balance, "pin": pin}
    save_accounts(accounts)
    messagebox.showinfo("Success", "✅ Account created successfully!")

def authenticate(acc_no, pin):
    return acc_no in accounts and accounts[acc_no]["pin"] == pin

def deposit_amount():
    acc_no = entry_acc.get()
    pin = entry_pin.get()
    amount = entry_amt.get()

    if not authenticate(acc_no, pin):
        messagebox.showerror("Error", "Invalid account number or PIN!")
        return

    try:
        amount = float(amount)
        accounts[acc_no]["balance"] += amount
        save_accounts(accounts)
        messagebox.showinfo("Success", "💰 Amount deposited!")
    except ValueError:
        messagebox.showerror("Error", "Invalid deposit amount!")

def withdraw_amount():
    acc_no = entry_acc.get()
    pin = entry_pin.get()
    amount = entry_amt.get()

    if not authenticate(acc_no, pin):
        messagebox.showerror("Error", "Invalid account number or PIN!")
        return

    try:
        amount = float(amount)
        if accounts[acc_no]["balance"] < amount:
            messagebox.showerror("Error", "❌ Insufficient balance!")
        else:
            accounts[acc_no]["balance"] -= amount
            save_accounts(accounts)
            messagebox.showinfo("Success", "💸 Withdrawal successful!")
    except ValueError:
        messagebox.showerror("Error", "Invalid withdrawal amount!")

def check_balance():
    acc_no = entry_acc.get()
    pin = entry_pin.get()

    if not authenticate(acc_no, pin):
        messagebox.showerror("Error", "Invalid account number or PIN!")
    else:
        bal = accounts[acc_no]["balance"]
        messagebox.showinfo("Balance", f"💰 Account Balance: ₹{bal:.2f}")

# GUI Design 
root = tk.Tk()
root.title("💼 Bank Management System")
root.geometry("420x450")
root.configure(bg="#eaf4f4")
root.resizable(False, False)

def label(title):
    return tk.Label(root, text=title, font=("Segoe UI", 10, "bold"), bg="#eaf4f4", anchor="w")

def entry():
    return tk.Entry(root, font=("Segoe UI", 10), bd=1, relief="solid")

label("Account Number").pack(pady=(20, 2))
entry_acc = entry(); entry_acc.pack()

label("PIN").pack(pady=(10, 2))
entry_pin = entry(); entry_pin.config(show="*"); entry_pin.pack()

label("Name (For New Account)").pack(pady=(10, 2))
entry_name = entry(); entry_name.pack()

label("Amount").pack(pady=(10, 2))
entry_amt = entry(); entry_amt.pack()

tk.Button(root, text="Create Account", command=create_account,
          font=("Segoe UI", 10, "bold"), bg="#006d77", fg="white", width=25).pack(pady=10)

tk.Button(root, text="Deposit", command=deposit_amount,
          font=("Segoe UI", 10, "bold"), bg="#00b894", fg="white", width=25).pack(pady=5)

tk.Button(root, text="Withdraw", command=withdraw_amount,
          font=("Segoe UI", 10, "bold"), bg="#fd9644", fg="white", width=25).pack(pady=5)

tk.Button(root, text="Check Balance", command=check_balance,
          font=("Segoe UI", 10, "bold"), bg="#576574", fg="white", width=25).pack(pady=5)

tk.Label(root, text="© Aman Bajpai 2025", font=("Segoe UI", 8), bg="#eaf4f4", fg="#555").pack(side="bottom", pady=5)

root.mainloop()
