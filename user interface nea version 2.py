import tkinter as tk
from tkinter import messagebox

#  MAIN WINDOW 
root = tk.Tk()
root.title("Study Quest 🧠✨")
root.geometry("1000x600")
root.config(bg="#f0f8ff")  # Soft blue background

#  STYLES 
button_style = {
    "font": ("Comic Sans MS", 12, "bold"),
    "bg": "#ffffff",
    "fg": "#333",
    "activebackground": "#add8e6",
    "highlightbackground": "#add8e6",
    "bd": 2,
    "relief": "groove",
    "padx": 10,
    "pady": 5
}

label_style = {
    "font": ("Verdana", 14),
    "bg": "#ffffff",
    "fg": "#333"
}

title_style = {
    "font": ("Comic Sans MS", 24, "bold"),
    "bg": "#f0f8ff",
    "fg": "#333"
}

menu_button_style = {
    "font": ("Verdana", 12),
    "bg": "#f0f8ff",
    "fg": "#333",
    "activebackground": "#add8e6",
    "bd": 0,
    "relief": "flat",
    "anchor": "w",
    "padx": 20,
    "pady": 10
}

#  FRAMES 
menu_frame = tk.Frame(root, bg="#f0f8ff", width=200)
menu_frame.pack(side="left", fill="y")

content_frame = tk.Frame(root, bg="#ffffff")
content_frame.pack(side="right", fill="both", expand=True)

#  GLOBAL STATE 
xp = 0
streak = 0
current_index = 0
selected_set = None

#  FLASHCARD SETS 
flashcard_sets = {
    "Math Basics": [
        {"question": "What is 2+2?", "answer": "4"},
        {"question": "What is 5×3?", "answer": "15"},
    ],
    "General Knowledge": [
        {"question": "Capital of France?", "answer": "Paris"},
        {"question": "Largest planet?", "answer": "Jupiter"},
    ],
    "Literature": [
        {"question": "Who wrote *Atonement*?", "answer": "Ian McEwan"},
        {"question": "Author of *1984*?", "answer": "George Orwell"},
    ]
}

#  HOME SCREEN 
def load_home():
    """Display home screen with welcome and progress."""
    for widget in content_frame.winfo_children():
        widget.destroy()

    tk.Label(content_frame, text="🎓 Study Quest Home", **title_style).pack(pady=30)
    tk.Label(content_frame, text=f"🏆 XP: {xp}", **label_style).pack(pady=5)
    tk.Label(content_frame, text=f"🔥 Streak: {streak}", **label_style).pack(pady=5)

#  FLASHCARD SET SELECTOR 
def show_flashcard_selector():
    """Display flashcard set selection screen when 'Flashcard' is clicked."""
    for widget in content_frame.winfo_children():
        widget.destroy()

    tk.Label(content_frame, text="🧠 Choose a Flashcard Set", font=("Comic Sans MS", 20, "bold"), bg="#ffffff", fg="#333").pack(pady=30)

    set_var = tk.StringVar(value="Select a set")
    set_menu = tk.OptionMenu(content_frame, set_var, *flashcard_sets.keys())
    set_menu.config(
        font=("Verdana", 12),
        bg="#ffffff",
        fg="#333",
        activebackground="#add8e6",
        highlightbackground="#add8e6",
        bd=2,
        relief="groove",
        padx=10,
        pady=5
    )
    set_menu.pack(pady=10)

    def start_selected_set():
        global selected_set, current_index
        selected_set = flashcard_sets.get(set_var.get())
        current_index = 0
        if selected_set:
            show_flashcards()
        else:
            messagebox.showwarning("No Set Selected", "Please choose a flashcard set.")

    tk.Button(content_frame, text="⚡ Start Flashcards", command=start_selected_set, **button_style).pack(pady=10)

#  FLASHCARD MODULE 
def show_flashcards():
    """Display flashcards from selected set with card-style UI and XP tracking."""
    for widget in content_frame.winfo_children():
        widget.destroy()

    global xp, streak, selected_set, current_index

    card = selected_set[current_index]

    # --- Flashcard Frame (styled like a card) ---
    card_frame = tk.Frame(content_frame, bg="#ffffff", highlightbackground="#add8e6",
                          highlightthickness=2, bd=0, relief="ridge")
    card_frame.pack(pady=40, ipadx=20, ipady=20)

    # Question label inside card
    question_label = tk.Label(card_frame, text=f"🧩 {card['question']}",
                              font=("Comic Sans MS", 16, "bold"), bg="#ffffff", fg="#333")
    question_label.pack(pady=15)

    # Answer label inside card (hidden initially)
    answer_label = tk.Label(card_frame, text=f"🎯 {card['answer']}",
                            font=("Verdana", 14), bg="#ffffff", fg="#555")
    answer_label.pack(pady=15)
    answer_label.pack_forget()

    # --- XP and Streak Display ---
    xp_label = tk.Label(content_frame, text=f"🏆 XP: {xp}", **label_style)
    streak_label = tk.Label(content_frame, text=f"🔥 Streak: {streak}", **label_style)
    xp_label.pack()
    streak_label.pack()

    # --- Button Functions ---
    def flip_card():
        answer_label.pack()

    def correct_answer():
        global xp, streak
        xp += 10
        streak += 1
        xp_label.config(text=f"🏆 XP: {xp}")
        streak_label.config(text=f"🔥 Streak: {streak}")
        messagebox.showinfo("Correct!", f"🎉 Correct! +10 XP\nTotal XP: {xp}")

    def next_card():
        global current_index
        if current_index < len(selected_set) - 1:
            current_index += 1
            show_flashcards()
        else:
            messagebox.showinfo("End", "You've completed this flashcard set!")

    def prev_card():
        global current_index
        if current_index > 0:
            current_index -= 1
            show_flashcards()
        else:
            messagebox.showinfo("Start", "You're at the first flashcard!")

    # --- Control Buttons ---
    tk.Button(content_frame, text="🔄 Flip", command=flip_card, **button_style).pack(pady=5)
    tk.Button(content_frame, text="✅ Correct", command=correct_answer, **button_style).pack(pady=5)
    tk.Button(content_frame, text="⬅ Previous", command=prev_card, **button_style).pack(side="left", padx=20, pady=20)
    tk.Button(content_frame, text="➡ Next", command=next_card, **button_style).pack(side="right", padx=20, pady=20)

#  PROGRESS MODULE 
def show_progress():
    """Display XP and streak progress."""
    for widget in content_frame.winfo_children():
        widget.destroy()

    tk.Label(content_frame, text="📈 Your Progress", **title_style).pack(pady=30)
    tk.Label(content_frame, text=f"🏆 XP: {xp}", **label_style).pack(pady=10)
    tk.Label(content_frame, text=f"🔥 Streak: {streak}", **label_style).pack(pady=10)

#  FEEDBACK MODULE 
def show_feedback():
    """Display feedback form placeholder."""
    for widget in content_frame.winfo_children():
        widget.destroy()

    tk.Label(content_frame, text="💬 Feedback", **title_style).pack(pady=30)
    tk.Label(content_frame, text="Let us know what you think!", **label_style).pack(pady=10)

#  PROFILE MODULE 
def show_profile():
    """Display profile placeholder."""
    for widget in content_frame.winfo_children():
        widget.destroy()

    tk.Label(content_frame, text="👤 Profile", **title_style).pack(pady=30)
    tk.Label(content_frame, text="User: Hina", **label_style).pack(pady=10)
    tk.Label(content_frame, text=f"XP: {xp} | Streak: {streak}", **label_style).pack(pady=10)

# MENU BAR
tk.Label(menu_frame, text="📚 Menu", font=("Verdana", 16, "bold"), bg="#f0f8ff").pack(pady=20)

tk.Button(menu_frame, text="👤 Profile", command=show_profile, **menu_button_style).pack(fill="x")
tk.Button(menu_frame, text="🧠 Flashcard", command=show_flashcard_selector, **menu_button_style).pack(fill="x")
tk.Button(menu_frame, text="📈 Progress", command=show_progress, **menu_button_style).pack(fill="x")
tk.Button(menu_frame, text="💬 Feedback", command=show_feedback, **menu_button_style).pack(fill="x")
tk.Button(menu_frame, text="🏠 Home", command=load_home, **menu_button_style).pack(fill="x")

# INITIALIZE 
load_home()
root.mainloop()
