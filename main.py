"""
Program Made by :
    Sakthi Swaroopan
    Raghav Srivatsan
    Rohith Krishna

Note:
    The program doesnt't work without it's functions counterpart
"""
'''
Version 1.16
Change log:
    + Increased Storage in the Text Box within Datalocker
    + Windows are now Transient to each other;You cant interact with the root window until the child window is closed
    - This also fixes the issue of having multiple of the same window open
'''

# Change this text if program is modified or updated
version = "Encryptor v.16"

# Import Function.py and other modules
import functions as imp
import tkinter as tk
from tkinter import messagebox
from cryptography.fernet import Fernet

#Creating Missing Files
imp.initialize()


# Finish Button Command for Data Locker
def finish_button():
    txt = textbox.get('1.0',tk.END)
    imp.encrypt_and_store(txt, username)
    messagebox.showinfo('Info',"Data Saved in File! You may close the program safely now")
    
# The Data Locker Window
def Data_Locker():
    window = tk.Toplevel()
    window.title("Your Data Locker")
    window.iconbitmap(r"iconlocked.ico")
    window.resizable(0,0)
    tk.Label(window,text = "Your Data Locker",font = ('Consolas',24)).grid(row = 1,column = 0,columnspan = 2)
    
    textboxframe = tk.Frame(window)
    textboxframe.grid(row = 2)
    
    scrollbar = tk.Scrollbar(textboxframe)
    scrollbar.grid(row = 0,column = 1,sticky="ns")
    
    global textbox
    textbox = tk.Text(textboxframe,height = 10,width = 55,relief = 'ridge',bd=5)
    textbox.grid(row = 0,column = 0)
    
    textbox.config(yscrollcommand = scrollbar.set)
    scrollbar.config(command = textbox.yview)
    
    file = open(username+".dat","rb")
    raw = file.read()
    if raw != b'':
        key = imp.load_key()
        f = Fernet(key)
        decrypted = f.decrypt(raw)
        textbox.insert("1.0",decrypted.decode())
       
    tk.Button(window,text = "Finish and Save",command = finish_button,font = ('Consolas',12,'bold')).grid(row = 3,columnspan = 2)
    
    window.transient(win)
    window.grab_set()
    win.wait_window(window)

#Submit Function for Login Window
def submit_login():
    global username
    username = Username.get()
    userpass = Userpass.get()
    if imp.username_check(username):
        if imp.hash_check(username, userpass) == "Login Success":
            Data_Locker()
        else:
            messagebox.showinfo('Info',"Login Failed!"+" "+imp.hash_check(username, userpass))
    else:
        messagebox.showinfo('Info',"Login Failed! User doesn't Exist!")

#Submit Function for Register Window
def submit_register():
    preuser = username_pre.get()
    prepass = userpass_pre.get()
    chk = 0
    if prepass.lower() == prepass:
        chk+=1
    n = 0
    for i in prepass:
        if i.isdigit():
            n+=1
    if n==0:
        chk+=1
    if len(prepass) < 8:
        chk+=1
        
    chk1 = imp.username_check(preuser)
    if chk1 != True:
        if (chk == 0):
            if (preuser == "") or (" " in preuser):
                messagebox.showinfo('Info',"Username can't contain spaces!")
            else:
                imp.hash_store(preuser,imp.hash_gen(prepass))
                imp.new_user_file(preuser)
                messagebox.showinfo('Info','Account Registered Successfully!')
        else:
            messagebox.showinfo('Info',"Account wasn't Created! Password too weak!")
    else:
        messagebox.showinfo('Info',"Account wasn't Created! Username Already Exists!")

    
# The Login Window
def Login_func():
    global win
    win = tk.Toplevel()
    
    win.title("Login")
    win.iconbitmap(r"iconlocked.ico")
    win.resizable(0,0)
    window = tk.Frame(win, width = 50,height = 50)
    window.pack()
    tk.Label(window,text = "Login",font = ('Consolas',24)).grid(row = 1,column = 0,columnspan = 2)
    
    tk.Label(window,text = "Username:",font = ('Consolas',12,'bold')).grid(row = 2,column = 0)
    global Username
    Username = tk.StringVar()
    tk.Entry(window,textvariable = Username).grid(row = 2,column = 1)
    
    tk.Label(window,text = "Password:",font = ('Consolas',12,'bold')).grid(row = 3,column = 0)
    global Userpass
    Userpass = tk.StringVar()
    tk.Entry(window,textvariable = Userpass,show="*").grid(row = 3,column = 1)
    
    tk.Button(window,text = "Proceed",command = submit_login,font = ('Consolas',12,'bold')).grid(row = 4,column = 0,columnspan = 2)
    
    win.transient(root)
    win.grab_set()
    root.wait_window(win)

#The Register Window
def Register_func():
    window = tk.Toplevel()
    
    window.title("Register Account")
    window.iconbitmap(r"iconlocked.ico")
    window.resizable(0,0)
    tk.Label(window,text = "Register",font = ('Consolas',24)).grid(row = 1,column = 0,columnspan = 2)
    
    tk.Label(window,text = "Choose Username:",font = ('Consolas',12,'bold')).grid(row = 2,column = 0)
    global username_pre
    username_pre = tk.StringVar()
    tk.Entry(window,textvariable = username_pre).grid(row = 2,column = 1)
    
    tk.Label(window,text = "Choose Password:",font = ('Consolas',12,'bold')).grid(row = 3,column = 0)
    global userpass_pre
    userpass_pre = tk.StringVar()
    tk.Entry(window,textvariable = userpass_pre).grid(row = 3,column = 1)
        
    
    tk.Label(window,text="Please Ensure your password contains atleast",anchor = "w").grid(row = 6,column = 0, columnspan= 2,sticky = "w")
    tk.Label(window,text=" - 8 Characters",anchor = "w").grid(row = 7,column = 0, columnspan= 2,sticky = "w")
    tk.Label(window,text=" - One Uppercase Letter",anchor = "w").grid(row = 8,column = 0, columnspan= 2,sticky = "w")
    tk.Label(window,text=" - One Digit",anchor = "w").grid(row = 9,column = 0, columnspan= 2,sticky = "w")
    
    tk.Button(window,text = "Proceed",command = submit_register,font = ('Consolas',12,'bold')).grid(row = 5,column = 0,columnspan = 2)
    
    window.transient(root)
    window.grab_set()
    root.wait_window(window)

# Credits Window  
def credit():
    top = tk.Toplevel()
    top.title("Creators")
    top.iconbitmap(r"iconlocked.ico")
    tk.Label(top,text = version,font = ('Consolas',20,'bold')).grid(row = 0,column = 0)
    tk.Label(top,text = "Creators",font = ('Consolas',16)).grid(row = 1,column = 0)
    tk.Label(top,text = "Sakthi Swaroopan S",font = ('Consolas',14)).grid(row = 2,column = 0)
    tk.Label(top,text = "Raghav Srivatsan S",font = ('Consolas',14)).grid(row = 3,column = 0)
    tk.Label(top,text = "Rohith Krishna R",font = ('Consolas',14)).grid(row = 4,column = 0)
    
    top.transient(root)
    top.grab_set()
    root.wait_window(top)

# Main Window (This is the root of all windows closing this will destroy all other child windows and terminates the program)
root = tk.Tk()
root.title(version)
root.iconbitmap(r"iconlocked.ico")
root.resizable(0,0)

top = tk.Frame(root)
top.grid(row = 0,column = 0)
img = tk.PhotoImage(file = r"icon.png").subsample(4,4)
tk.Button(top,image = img,command = credit).grid(row = 0,column = 0)
tk.Label(top,text = version,font = ('Consolas',26)).grid(row = 0,column = 1)
tk.Button(root,text = "Login",command = Login_func,font = ('Consolas',18,'bold'), padx = 20).grid(row = 1,column = 0)
tk.Button(root,text = "Register",command = Register_func,font = ('Consolas',18,'bold')).grid(row = 2,column = 0)

root.mainloop()





