import tkinter as tk
from tkinter import ttk, messagebox

# -------------------- MAIN WINDOW --------------------
root = tk.Tk()
root.title("Study Quest 🧠✨")
root.geometry("900x600")
root.config(bg="#f0f8ff")  # Soft blue background for motivation

# -------------------- STYLES --------------------
style = ttk.Style()
style.configure("Rounded.TButton",
                font=("Comic Sans MS", 12, "bold"),
                foreground="#333",
                background="#ffcccb",
                padding=10)
style.map("Rounded.TButton",
          background=[("active", "#ff9999")])

label_style = {
    "font": ("Verdana", 14),
    "bg": "#ffffff",
    "fg": "#333"
}

# -------------------- FRAMES --------------------
menu_frame = tk.Frame(root, bg="#add8e6", width=200)
menu_frame.pack(side="left", fill="y")

content_frame = tk.Frame(root, bg="#ffffff")
content_frame.pack(side="right", fill="both", expand=True)

# -------------------- DEFAULT WELCOME SCREEN --------------------
def load_welcome():
    # Clear previous content
    for widget in content_frame.winfo_children():
        widget.destroy()

    # Welcome message
    welcome_label = tk.Label(content_frame, text="🎓 Welcome to Study Quest!",
                             font=("Comic Sans MS", 18), bg="#ffffff")
    welcome_label.pack(pady=50)

    # Instructional tip
    tip_label = tk.Label(content_frame, text="Select a module from the left to begin.",
                         font=("Verdana", 14), bg="#ffffff")
    tip_label.pack()

# -------------------- FLASHCARD MODULE --------------------
def show_flashcards():
    for widget in content_frame.winfo_children():
        widget.destroy()

    question_label = tk.Label(content_frame, text="🧩 Question: What is 2+2?", **label_style)
    question_label.pack(pady=20)

    answer_label = tk.Label(content_frame, text="🎯 Answer: 4", **label_style)
    answer_label.pack(pady=20)
    answer_label.pack_forget()  # Hide answer initially

    def flip_card():
        answer_label.pack()  # Reveal answer

    ttk.Button(content_frame, text="🔄 Flip Card", command=flip_card, style="Rounded.TButton").pack(pady=10)

# -------------------- PROGRESS MODULE --------------------
def show_progress():
    for widget in content_frame.winfo_children():
        widget.destroy()

    progress_var = tk.DoubleVar()

    progress_bar = tk.Scale(content_frame, variable=progress_var, from_=0, to=100,
                            orient="horizontal", label="📊 Progress", font=("Arial", 12),
                            bg="#ffffff", fg="#333", troughcolor="#add8e6", sliderrelief="flat")
    progress_bar.pack(pady=20)

    # XP and streak counters
    xp = 0
    streak = 0

    xp_label = tk.Label(content_frame, text=f"🏆 XP: {xp}", **label_style)
    streak_label = tk.Label(content_frame, text=f"🔥 Streak: {streak}", **label_style)
    xp_label.pack()
    streak_label.pack()

    def update_stats():
        nonlocal xp, streak
        xp += 10
        streak += 1
        xp_label.config(text=f"🏆 XP: {xp}")
        streak_label.config(text=f"🔥 Streak: {streak}")

    ttk.Button(content_frame, text="✅ Correct Answer", command=update_stats, style="Rounded.TButton").pack(pady=10)

# -------------------- NAVIGATION --------------------
tk.Label(menu_frame, text="📚 Menu", font=("Arial", 16, "bold"), bg="#add8e6").pack(pady=20)

ttk.Button(menu_frame, text="🧠 Flashcards", command=show_flashcards, style="Rounded.TButton").pack(pady=10)
ttk.Button(menu_frame, text="📈 Progress", command=show_progress, style="Rounded.TButton").pack(pady=10)

# -------------------- INITIALIZE --------------------
load_welcome()

# -------------------- MAIN LOOP --------------------
root.mainloop()
