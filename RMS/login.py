# ==================== IMPORTS ====================
from tkinter import *
from PIL import Image, ImageTk, ImageDraw   # pip install Pillow
# import pyodbc  # pip install pyodbc
import sqlite3  # Using sqlite3 for local database operations
from tkinter import messagebox,ttk  # For showing message boxes and using themed widgets
import os  # For handling file paths and system operations
import sys  # For accessing system-specific parameters and functions
import subprocess  # For running external scripts and handling system operations

# ==================== LOGIN CLASS ====================
class Login_window:
    def __init__(self,root):
        self.root=root
        self.root.title("Login System")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="#021e2f")

        #=============Background Color================
        left_lbl=Label(self.root,bg="#08A3D2",bd=0)
        left_lbl.place(x=0,y=0,relheight=1,width=600)

        right_lbl=Label(self.root,bg="#031F3C",bd=0)
        right_lbl.place(x=600,y=0,relheight=1,relwidth=1)

        #==========Frame=================
        login_frame=Frame(self.root,bg="white")
        login_frame.place(x=250,y=100,height=500,width=800)


        title=Label(login_frame,text="LOGIN HERE",font=("times new roman",30,"bold"),bg="white",fg="#08A3D2")
        title.place(x=250,y=50)

        email=Label(login_frame,text="EMAIL ADDRESS",font=("times new roman",18,"bold"),bg="white",fg="black")
        email.place(x=250,y=150)
        self.txt_email=Entry(login_frame,font=("times new roman",18),bg="lightgray")
        self.txt_email.place(x=250,y=180,width=350,height=35)

        pass_=Label(login_frame,text="PASSWORD",font=("times new roman",18,"bold"),bg="white",fg="black")
        pass_.place(x=250,y=250)
        self.txt_pass=Entry(login_frame,font=("times new roman",18),bg="lightgray")
        self.txt_pass.place(x=250,y=280,width=350,height=35)

        btn_reg=Button(login_frame,cursor="hand2",command=self.register_window,text="Register new Account?",font=("times new roman",14),bg="white",bd=0,fg="#B00857")
        btn_reg.place(x=250,y=320)

        btn_forget=Button(login_frame,cursor="hand2",command=self.forget_password_window,text="Forget Password?",font=("times new roman",14),bg="white",bd=0,fg="red")
        btn_forget.place(x=450,y=320)

        btn_login=Button(login_frame,cursor="hand2",text="Login",command=self.login,font=("times new roman",18,"bold"),bg="#B00857",fg="white")
        btn_login.place(x=250,y=370,width=180,height=40)

    # ==================== LOGIN WINDOW NAVIGATION ====================
    def register_window(self):
        self.root.destroy()  # Close the login window
        import register  # Import the register module to open the registration window

    def reset(self):
        """
        Clear all form input fields and reset to default values.
        Called after successful password reset.
        """
        self.cmb_quest.current(0)
        self.txt_new_password.delete(0, END)
        self.txt_answer.delete(0, END)
        self.txt_pass.delete(0, END)
        self.txt_email.delete(0, END)


    def forget_password(self):
        """
        Validate user input and reset password in database.
        Performs validation checks and updates password if security question and answer match.
        """
        if self.txt_email.get()=="Select" or self.txt_answer.get()=="" or self.txt_new_password.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root2)
        else:
            try:
                con=sqlite3.connect(database="rms.db")
                cursor = con.cursor()
                cursor.execute("SELECT * FROM studentresult WHERE email=? and security_question=? and security_answer=?", (self.txt_email.get(), self.cmb_quest.get(), self.txt_answer.get()))
                row = cursor.fetchone()
                if row == None:
                    messagebox.showerror("Error", "Please Select the Correct Security Question and enter the correct answer", parent=self.root2)
                else:
                    # Update the password in the database
                    cursor.execute("UPDATE studentresult SET password=? WHERE email=?", (self.txt_new_password.get(), self.txt_email.get()))
                    con.commit()
                    con.close()
                    messagebox.showinfo("Success", "Password reset successfully, Please login with your new password", parent=self.root2)
                    self.reset()  # Clear the fields after successful password reset
                    self.root2.destroy()  # Close the forget password window after successful reset
            except Exception as es:
                messagebox.showerror("Error", f"Error due to: {str(es)}", parent=self.root2)

    def forget_password_window(self):
        """
        Open forget password window if email exists in database.
        Creates a modal window for password reset with security question verification.
        """
        if self.txt_email.get()=="":
           messagebox.showerror("Error","Please enter the email address to reset password",parent=self.root)
        else:
            try:
                con=sqlite3.connect(database="rms.db")
                cursor = con.cursor()
                cursor.execute("SELECT * FROM studentresult WHERE email=?", (self.txt_email.get(),))
                row = cursor.fetchone()
                if row == None:
                    messagebox.showerror("Error", "Please enter the valid email address to reset password", parent=self.root)
                else:
                    con.close()
                    self.root2 = Toplevel()  # Create a new top-level window
                    self.root2.title("Forget Password")
                    self.root2.geometry("400x400+450+150")
                    self.root2.config(bg="white")
                    self.root2.focus_force()  # Set focus to the new window
                    self.root2.grab_set()  # Make the new window modal 

                    t=Label(self.root2, text="Forget Password", font=("times new roman", 20, "bold"), bg="white", fg="#B00857")
                    t.place(x=0, y=10, relwidth=1)

                    #====== Forget Password Window ======
                    question=Label(self.root2,text="Select Security Question",font=("times new roman", 15, "bold"),bg="white",fg="black").place(x=50,y=80)

                    self.cmb_quest=ttk.Combobox(self.root2,font=("times new roman", 15),state="readonly",justify=CENTER)
                    self.cmb_quest['values']=("Select","Your Birth Place","Your Bestfriend Name","Your Pet Name")
                    self.cmb_quest.place(x=50,y=110,width=250) 
                    self.cmb_quest.current(0)

                    answer=Label(self.root2,text="Answer",font=("times new roman", 15, "bold"),bg="white",fg="black").place(x=50,y=150)
                    self.txt_answer=Entry(self.root2,font=("times new roman", 15),bg="lightgray")
                    self.txt_answer.place(x=50,y=180,width=250)

                    new_password=Label(self.root2,text="New Password",font=("times new roman", 15, "bold"),bg="white",fg="black").place(x=50,y=220)
                    self.txt_new_password=Entry(self.root2,font=("times new roman", 15),bg="lightgray")
                    self.txt_new_password.place(x=50,y=250,width=250)

                    btn_change_password=Button(self.root2,cursor="hand2",text="Reset Password",command=self.forget_password,font=("times new roman", 15, "bold"),bg="green",fg="white").place(x=90,y=300)

            except Exception as es:
                messagebox.showerror("Error",f"Error due to: {str(es)}",parent=self.root)

    
    def login(self):
        """
        Validate user credentials and log in if valid.
        Checks email and password against database records.
        """
        if self.txt_email.get()=="" or self.txt_pass.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                con=sqlite3.connect(database="rms.db")
                cursor = con.cursor()
                cursor.execute("SELECT * FROM studentresult WHERE email=? AND password=?", (self.txt_email.get(), self.txt_pass.get()))
                row = cursor.fetchone()
                if row == None:
                    messagebox.showerror("Error", "Invalid Username & Password", parent=self.root)
                else:
                    messagebox.showinfo("Success", f"Welcome:{self.txt_email.get()}", parent=self.root)
                    self.root.destroy()  # Close the login window
                    # Get the directory where this script is located and construct full path to dashboard.py
                    current_dir = os.path.dirname(os.path.abspath(__file__))
                    dashboard_path = os.path.join(current_dir, "dashboard.py")
                    subprocess.Popen([sys.executable, dashboard_path])
                    con.close()               
            except Exception as es:
                messagebox.showerror("Error",f"Error due to: {str(es)}",parent=self.root)





# ==================== APPLICATION ENTRY POINT ====================
# Create Tkinter root window
root = Tk()

# Initialize the Login_window class with the root window
obj = Login_window(root)

# Start the Tkinter event loop (keeps window open until closed)
root.mainloop()
        