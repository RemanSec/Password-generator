
import tkinter as tk
import secrets
import string

# Main window
root = tk.Tk()
root.title("Secure Password Generator")
root.geometry("430x500")
root.resizable(False, False)
root.configure(bg="#172033")

# Generate password function
def generate_password():
    try:
        length = int(length_entry.get())

        if length < 8 or length > 128:
            result_label.config(
                text="Password length must be 8-128!",
                fg="#F87171"
            )
            return

        characters = ""

        if uppercase_var.get():
            characters += string.ascii_uppercase

        if lowercase_var.get():
            characters += string.ascii_lowercase

        if numbers_var.get():
            characters += string.digits

        if symbols_var.get():
            characters += "!@#$%^&*()-_=+?"

        if not characters:
            result_label.config(
                text="Select at least one character type!",
                fg="#F87171"
            )
            return

        password = "".join(
            secrets.choice(characters)
            for _ in range(length)
        )

        password_entry.config(state="normal")
        password_entry.delete(0, tk.END)
        password_entry.insert(0, password)
        password_entry.config(state="readonly")

        result_label.config(
            text="Strong password generated!",
            fg="#34D399"
        )

    except ValueError:
        result_label.config(
            text="Please enter a valid length!",
            fg="#F87171"
        )


# Copy password
def copy_password():
    password = password_entry.get()

    if password:
        root.clipboard_clear()
        root.clipboard_append(password)
        result_label.config(
            text="Password copied!",
            fg="#34D399"
        )


# Heading
tk.Label(
    root,
    text="🔐 PASSWORD GENERATOR",
    font=("Arial", 18, "bold"),
    bg="#172033",
    fg="#60A5FA"
).pack(pady=25)

# Password length
tk.Label(
    root,
    text="Password Length:",
    font=("Arial", 12),
    bg="#172033",
    fg="white"
).pack()

length_entry = tk.Entry(
    root,
    font=("Arial", 14),
    justify="center",
    width=10
)
length_entry.insert(0, "16")
length_entry.pack(pady=10)

# Character options
uppercase_var = tk.BooleanVar(value=True)
lowercase_var = tk.BooleanVar(value=True)
numbers_var = tk.BooleanVar(value=True)
symbols_var = tk.BooleanVar(value=True)

options = [
    ("Uppercase Letters (A-Z)", uppercase_var),
    ("Lowercase Letters (a-z)", lowercase_var),
    ("Numbers (0-9)", numbers_var),
    ("Special Characters (!@#$)", symbols_var)
]

for label, variable in options:
    tk.Checkbutton(
        root,
        text=label,
        variable=variable,
        font=("Arial", 11),
        bg="#172033",
        fg="white",
        selectcolor="#25334B",
        activebackground="#172033",
        activeforeground="white"
    ).pack(anchor="w", padx=80, pady=4)

# Generate button
tk.Button(
    root,
    text="GENERATE PASSWORD",
    font=("Arial", 12, "bold"),
    bg="#2563EB",
    fg="Red",
    relief="flat",
    command=generate_password,
    padx=15,
    pady=10
).pack(pady=20)

# Password display
password_entry = tk.Entry(
    root,
    font=("Courier", 12),
    justify="center",
    width=34,
    state="readonly"
)
password_entry.pack(pady=5)

# Copy button
tk.Button(
    root,
    text="COPY PASSWORD",
    font=("Arial", 10, "bold"),
    bg="#059669",
    fg="red",
    relief="flat",
    command=copy_password,
    padx=15,
    pady=8
).pack(pady=10)

# Status message
result_label = tk.Label(
    root,
    text="Create your secure password!",
    font=("Arial", 10),
    bg="#172033",
    fg="#94A3B8"
)
result_label.pack(pady=10)

# Footer
tk.Label(
    root,
    text="Stay Secure. Stay Protected.",
    font=("Arial", 9),
    bg="#172033",
    fg="#64748B"
).pack(side="bottom", pady=15)

root.mainloop()
