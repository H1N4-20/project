import tkinter as tk
from tkinter import messagebox, PhotoImage

# -------------------- MAIN WINDOW --------------------
root = tk.Tk()
root.title("Study Quest 🧠✨")
root.geometry("900x600")
root.config(bg="#f0f8ff")  # Soft blue background for motivation
"""This is the main application window setup."""

# -------------------- STYLES --------------------
# Button styling dictionary for consistent look across UI
button_style = {
    "font": ("Comic Sans MS", 12, "bold"),
    "bg": "#ffcccb",  # Light coral background
    "fg": "#333",     # Dark text color
    "activebackground": "#ff9999",  # Slightly darker coral when clicked
    "bd": 0,
    "relief": "flat",
    "padx": 10,
    "pady": 5
}

# Label styling dictionary for consistent look across UI
label_style = {
    "font": ("Verdana", 14),
    "bg": "#ffffff",
    "fg": "#333"
}

# -------------------- FRAMES --------------------
# Left-side menu frame
menu_frame = tk.Frame(root, bg="#add8e6", width=200)
menu_frame.pack(side="left", fill="y")

# Right-side content frame (main display area)
wacontent_frame = tk.Frame(root, bg="#ffffff")
content_frame.pack(side="right", fill="both", expand=True)

# -------------------- DEFAULT WELCOME SCREEN --------------------
def load_welcome():
    """
    Display the default welcome screen in the content frame.
    Clears any existing widgets and shows a greeting message
    with instructions for the user.
    """
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
    """
    Display the flashcard module.
    Shows a question and allows the user to flip the card
    to reveal the answer.
    """
    # Clear previous content
    for widget in content_frame.winfo_children():
        widget.destroy()

    # Question label
    question_label = tk.Label(content_frame, text="🧩 Question: What is 2+2?", **label_style)
    question_label.pack(pady=20)

    # Answer label (hidden initially)
    answer_label = tk.Label(content_frame, text="🎯 Answer: 4", **label_style)
    answer_label.pack(pady=20)
    answer_label.pack_forget()  # Hide answer initially

    def flip_card():
        """Reveal the answer when the button is clicked."""
        answer_label.pack()

    # Flip card button
    tk.Button(content_frame, text="🔄 Flip Card", command=flip_card, **button_style).pack()

# -------------------- PROGRESS MODULE --------------------
def show_progress():
    """
    Display the progress tracking module.
    Includes a progress bar, XP counter, and streak counter.
    Allows user to update stats when answering correctly.
    """
    # Clear previous content
    for widget in content_frame.winfo_children():
        widget.destroy()

    # Progress bar variable
    progress_var = tk.DoubleVar()

    # Progress bar widget
    progress_bar = tk.Scale(content_frame, variable=progress_var, from_=0, to=100,
                            orient="horizontal", label="📊 Progress", font=("Arial", 12),
                            bg="#ffffff", fg="#333", troughcolor="#add8e6", sliderrelief="flat")
    progress_bar.pack(pady=20)

    # XP and streak counters
    xp = 0
    streak = 0

    # Labels for XP and streak
    xp_label = tk.Label(content_frame, text=f"🏆 XP: {xp}", **label_style)
    streak_label = tk.Label(content_frame, text=f"🔥 Streak: {streak}", **label_style)
    xp_label.pack()
    streak_label.pack()

    def update_stats():
        """
        Update XP and streak counters when the user
        clicks 'Correct Answer'.
        """
        nonlocal xp, streak
        xp += 10
        streak += 1
        xp_label.config(text=f"🏆 XP: {xp}")
        streak_label.config(text=f"🔥 Streak: {streak}")

    # Button to simulate correct answer
    tk.Button(content_frame, text="✅ Correct Answer", command=update_stats, **button_style).pack(pady=10)

# -------------------- NAVIGATION --------------------
# Menu title
tk.Label(menu_frame, text="📚 Menu", font=("Arial", 16, "bold"), bg="#add8e6").pack(pady=20)

# Navigation buttons
tk.Button(menu_frame, text="🧠 Flashcards", command=show_flashcards, **button_style).pack(pady=10)
tk.Button(menu_frame, text="📈 Progress", command=show_progress, **button_style).pack(pady=10)

# -------------------- INITIALIZE --------------------
load_welcome()  # Load welcome screen on startup

# -------------------- MAIN LOOP --------------------
root.mainloop()

Hashing Algorithm
