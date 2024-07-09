import re
import tkinter as tk
from tkinter import StringVar

def assess_password_strength(password):
    criteria = {
        "length": len(password) >= 8,
        "uppercase": bool(re.search(r'[A-Z]', password)),
        "lowercase": bool(re.search(r'[a-z]', password)),
        "digits": bool(re.search(r'\d', password)),
        "special_characters": bool(re.search(r'[\W_]', password))
    }
    
    score = sum(criteria.values())
    
    feedback = []
    
    if criteria["length"]:
        feedback.append("✔️ Password length is sufficient.")
    else:
        feedback.append("❌ Password should be at least 8 characters long.")
    
    if criteria["uppercase"]:
        feedback.append("✔️ Password contains uppercase letters.")
    else:
        feedback.append("❌ Password should contain at least one uppercase letter.")
    
    if criteria["lowercase"]:
        feedback.append("✔️ Password contains lowercase letters.")
    else:
        feedback.append("❌ Password should contain at least one lowercase letter.")
    
    if criteria["digits"]:
        feedback.append("✔️ Password contains digits.")
    else:
        feedback.append("❌ Password should contain at least one digit.")
    
    if criteria["special_characters"]:
        feedback.append("✔️ Password contains special characters.")
    else:
        feedback.append("❌ Password should contain at least one special character.")
    
    strength = "Very Weak"
    if score == 5:
        strength = "Very Strong"
    elif score == 4:
        strength = "Strong"
    elif score == 3:
        strength = "Medium"
    elif score == 2:
        strength = "Weak"
    
    feedback_str = "\n".join(feedback)
    
    return strength, feedback_str

def on_key_release(*args):
    password = password_var.get()
    strength, feedback = assess_password_strength(password)
    strength_var.set(f"Password Strength: {strength}")
    feedback_var.set(feedback)

# Set up the GUI
root = tk.Tk()
root.title("Password Strength Checker")

password_var = StringVar()
strength_var = StringVar()
feedback_var = StringVar()

tk.Label(root, text="Enter Password:").grid(row=0, column=0, padx=10, pady=10)
tk.Entry(root, textvariable=password_var, show='*').grid(row=0, column=1, padx=10, pady=10)
tk.Label(root, textvariable=strength_var).grid(row=1, column=0, columnspan=2, padx=10, pady=10)
tk.Label(root, textvariable=feedback_var, justify="left").grid(row=2, column=0, columnspan=2, padx=10, pady=10)

password_var.trace_add("write", on_key_release)

root.mainloop()
