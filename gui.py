import tkinter as tk
from GenderPredictor.predict_gender import predict_gender
from DataHandler.login_check import check_credentials
from User.logout import logout
from ImageHandler.predict_and_display import predict_and_display
import json

def create_gui(root):

    header_label = tk.Label(root, text="Fingerprint Gender Predictor", bg="#F8EFBA", font=("Helvetica", 24, "bold"))
    header_label.pack(pady=20)

    register_frame = tk.Frame(root, bg="#F8EFBA")
    register_frame.pack(pady=20)

    register_username_label = tk.Label(register_frame, text="Username:", bg="#F8EFBA", font=("Helvetica", 18))
    register_username_label.grid(row=0, column=0, pady=10)

    register_username_entry = tk.Entry(register_frame, font=("Helvetica", 18))
    register_username_entry.grid(row=0, column=1, pady=10)

    register_password_label = tk.Label(register_frame, text="Password:", bg="#F8EFBA", font=("Helvetica", 18))
    register_password_label.grid(row=1, column=0, pady=10)

    register_password_entry = tk.Entry(register_frame, show="*",font=("Helvetica", 18))
    register_password_entry.grid(row=1, column=1, pady=10)

    confirm_password_label = tk.Label(register_frame, text="Confirm Password:", bg="#F8EFBA", font=("Helvetica", 18))
    confirm_password_label.grid(row=2, column=0, pady=10)

    confirm_password_entry = tk.Entry(register_frame, show="*",font=("Helvetica", 18))
    confirm_password_entry.grid(row=2, column=1, pady=10)

    register_button = tk.Button(register_frame, text="Register", command=lambda: register(register_username_entry.get(), register_password_entry.get(), confirm_password_entry.get(), register_frame, login_frame, error_label_register), bg="#3498DB", fg="#FFFFFF", font=("Helvetica", 18))
    register_button.grid(row=3, column=1, pady=10)

    login_button_reg = tk.Button(register_frame, text="Login", command=lambda: show_login_frame(register_frame, login_frame), bg="#3498DB", fg="#FFFFFF", font=("Helvetica", 18))
    login_button_reg.grid(row=4, column=1, pady=10)
    
    error_label_register = tk.Label(register_frame, text="", fg="#C0392B", bg="#F8EFBA")
    error_label_register.grid(row=5, column=1, pady=10)

    login_frame = tk.Frame(root, bg="#F8EFBA")

    username_label = tk.Label(login_frame, text="Username:", bg="#F8EFBA", font=("Helvetica", 18))
    username_label.grid(row=0, column=0, pady=10)

    username_entry = tk.Entry(login_frame, font=("Helvetica", 18))
    username_entry.grid(row=0, column=1, pady=10)

    password_label = tk.Label(login_frame, text="Password:", bg="#F8EFBA", font=("Helvetica", 18))
    password_label.grid(row=1, column=0, pady=10)

    password_entry = tk.Entry(login_frame, show="*",font=("Helvetica", 18))
    password_entry.grid(row=1, column=1, pady=10)

    login_button = tk.Button(login_frame, text="Login", command=lambda: login(username_entry.get(), password_entry.get(), login_frame, upload_frame, error_label), bg="#3498DB", fg="#FFFFFF", font=("Helvetica", 18))
    login_button.grid(row=2, column=1, pady=10)

    register_button_on_login = tk.Button(login_frame, text="Register", command=lambda: show_register_frame(login_frame,register_frame), bg="#3498DB", fg="#FFFFFF", font=("Helvetica", 18))
    register_button_on_login.grid(row=3, column=1, pady=10)
    
    error_label = tk.Label(login_frame, text="", fg="#C0392B", bg="#F8EFBA")
    error_label.grid(row=4, column=1, pady=10)

    upload_frame = tk.Frame(root, bg="#F8EFBA")

    upload_button = tk.Button(upload_frame, text="Upload Image", command=lambda: predict_and_display_result(image_label,gender_label,logout_button), bg="#3498DB", fg="#FFFFFF", font=("Helvetica", 18))
    upload_button.pack(pady=20)

    image_label = tk.Label(upload_frame, bg="#F8EFBA")
    image_label.pack(pady=10)

    gender_label = tk.Label(upload_frame, bg="#F8EFBA")
    gender_label.pack(pady=10)

    logout_button = tk.Button(upload_frame, text="Logout", command=lambda: logouting(upload_frame, login_frame), bg="#C0392B", fg="#FFFFFF", font=("Helvetica", 18))
    logout_button.pack(pady=10)
    
def show_login_frame(register_frame,login_frame):
    register_frame.pack_forget()
    login_frame.pack(pady=20)

def show_register_frame(login_frame,register_frame):
    login_frame.pack_forget()
    register_frame.pack(pady=20)

def register(username, password, confirm_password, register_frame, login_frame, error_label):
    if not username or not password or not confirm_password:
        error_label.config(text="Please fill in all fields")
    elif password != confirm_password:
        error_label.config(text="Passwords do not match")
    else:
        with open('User/login.json', 'r') as f:
            users = json.load(f)
        N = len(users['users'])
        names = []
        for i in range(N):    
            names.append(users['users'][i]['username'])        
        if username in names:
            error_label.config(text="Username already exists")
        else:
            new_user = {
                "username": username,
                "password": password
            }
            users["users"].append(new_user)
            with open('User/login.json', 'w') as f:
                json.dump(users, f)
            register_frame.pack_forget()
            login_frame.pack(pady=20)
    
def login(username, password, login_frame, upload_frame, error_label):
    if check_credentials(username, password):
        login_frame.pack_forget()
        upload_frame.pack(pady=20)
    else:
        error_label.config(text="Incorrect username or password")

def predict_and_display_result(image_label, gender_label,logout_button):
    return predict_and_display(image_label,gender_label,logout_button)

def logouting(upload_frame,login_frame):
    return logout(upload_frame,login_frame)