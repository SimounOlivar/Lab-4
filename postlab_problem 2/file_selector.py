import tkinter as tk
from tkinter import filedialog

def get_text_file():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(
        title="Select a text file",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if file_path:
        print("Selected file:", file_path)
    else:
        print("No file selected.")

if __name__ == "__main__":
    get_text_file()
