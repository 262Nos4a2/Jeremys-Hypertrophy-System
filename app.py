from database import create_database
import customtkinter as ctk

# -----------------------------
# App Configuration
# -----------------------------
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Jeremy's Hypertrophy System")
app.geometry("1200x800")
app.minsize(1000, 700)

# -----------------------------
# Title
# -----------------------------
title = ctk.CTkLabel(
    app,
    text="Jeremy's Hypertrophy System",
    font=("Segoe UI", 30, "bold")
)

title.pack(pady=(30,10))

subtitle = ctk.CTkLabel(
    app,
    text="Version 1.0.0",
    font=("Segoe UI",18)
)

subtitle.pack()

# -----------------------------
# Buttons
# -----------------------------
button_frame = ctk.CTkFrame(app)
button_frame.pack(pady=40)

buttons = [
    "Today's Workout",
    "History",
    "Progress",
    "Settings",
    "Exit"
]

for text in buttons:
    btn = ctk.CTkButton(
        button_frame,
        text=text,
        width=250,
        height=45
    )
    btn.pack(pady=10)

create_database()

app.mainloop()
