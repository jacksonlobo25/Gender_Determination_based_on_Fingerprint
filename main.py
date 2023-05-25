import tkinter as tk
from gui import create_gui

def main():
    root = tk.Tk()
    root.geometry("980x700")
    root.title("Fingerprint Gender Predictor")
    root.configure(bg="#F8EFBA")
    create_gui(root)
    root.mainloop()

if __name__ == '__main__':
    main()
