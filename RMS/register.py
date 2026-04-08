# ==================== IMPORTS ====================
from tkinter import *
from tkinter import ttk, messagebox  # ttk provides advanced widgets like Combobox
from PIL import Image, ImageTk  # Python Imaging Library for handling images
# import pyodbc  # Database connectivity module for SQL Server
import sqlite3  # Using sqlite3 for local database operations
import os  # For handling file paths and system operations
import sys  # For accessing system-specific parameters and functions
import subprocess  # For running external scripts and handling system operations

# ==================== REGISTRATION CLASS ====================
class Register:
    def __init__(self, root):
        # Initialize the registration window
        self.root = root
        self.root.title("Registration Window")
        self.root.geometry("1490x780+0+0")  # Window size: 1490x780 pixels, position at (0,0)
        self.root.config(bg="white")

        # ========== SET BACKGROUND IMAGE ==========
        # Load, resize, and display the main background image
        self.bg_img = Image.open("assets/bgimg.png")
        self.bg_img = self.bg_img.resize((1290, 780), Image.LANCZOS)  # LANCZOS: high-quality resizing
        self.bg = ImageTk.PhotoImage(self.bg_img)
        bg = Label(self.root, image=self.bg).place(x=200, y=0, width=1290, height=780)

        # ========== SET SIDE IMAGE ==========
        # Load and display the decorative side image
        self.side_img = Image.open("assets/side.png")
        self.side_img = self.side_img.resize((400, 500), Image.LANCZOS)
        self.side = ImageTk.PhotoImage(self.side_img)
        side = Label(self.root, image=self.side).place(x=80, y=100, width=400, height=500)

        # ========== CREATE REGISTRATION FORM FRAME ==========
        # Main frame to hold all form elements
        frame1 = Frame(self.root, bg="white")
        frame1.place(x=480, y=100, width=700, height=500)

        # Form title label
        title = Label(frame1, text="REGISTER HERE", font=("time new roman", 20, "bold"), bg="white", fg="green").place(x=50, y=30)

        # ========== ROW 1: FIRST NAME & LAST NAME ==========
        f_name = Label(frame1, text="First Name", font=("time new roman", 15, "bold"), bg="white", fg="black").place(x=50, y=100)
        self.txt_fname = Entry(frame1, font=("time new roman", 15), bg="lightgray")
        self.txt_fname.place(x=50, y=130, width=250)

        l_name = Label(frame1, text="Last Name", font=("time new roman", 15, "bold"), bg="white", fg="black").place(x=370, y=100)
        self.txt_lname = Entry(frame1, font=("time new roman", 15), bg="lightgray")
        self.txt_lname.place(x=370, y=130, width=250)

        # ========== ROW 2: CONTACT & EMAIL ==========
        contact = Label(frame1, text="Contact No.", font=("time new roman", 15, "bold"), bg="white", fg="black").place(x=50, y=170)
        self.txt_contact = Entry(frame1, font=("time new roman", 15), bg="lightgray")
        self.txt_contact.place(x=50, y=200, width=250)

        email = Label(frame1, text="Email", font=("time new roman", 15, "bold"), bg="white", fg="black").place(x=370, y=170)
        self.txt_email = Entry(frame1, font=("time new roman", 15), bg="lightgray")
        self.txt_email.place(x=370, y=200, width=250)

        # ========== ROW 3: SECURITY QUESTION & ANSWER ==========
        # Security question combobox with predefined options
        question = Label(frame1, text="Security Question", font=("time new roman", 15, "bold"), bg="white", fg="black").place(x=50, y=240)

        self.cmb_quest = ttk.Combobox(frame1, font=("time new roman", 13, "bold"), state='readonly', justify=CENTER)
        self.cmb_quest['values'] = ("Select", "Your Birth Place", "Your Best Friend Name", "Your Pet Name")
        self.cmb_quest.place(x=50, y=270, width=250)
        self.cmb_quest.current(0)  # Set default selection to "Select"

        answer = Label(frame1, text="Answer", font=("time new roman", 15, "bold"), bg="white", fg="black").place(x=370, y=240)
        self.txt_answer = Entry(frame1, font=("time new roman", 15), bg="lightgray")
        self.txt_answer.place(x=370, y=270, width=250)

        # ========== ROW 4: PASSWORD & CONFIRM PASSWORD ==========
        password = Label(frame1, text="Password", font=("time new roman", 15, "bold"), bg="white", fg="black").place(x=50, y=310)
        self.txt_password = Entry(frame1, font=("time new roman", 15), bg="lightgray")
        self.txt_password.place(x=50, y=340, width=250)

        cpassword = Label(frame1, text="Confirm Password", font=("time new roman", 15, "bold"), bg="white", fg="black").place(x=370, y=310)
        self.txt_cpassword = Entry(frame1, font=("time new roman", 15), bg="lightgray")
        self.txt_cpassword.place(x=370, y=340, width=250)

        # ========== TERMS & CONDITIONS CHECKBOX ==========
        # Checkbox to verify user agreement with Terms & Conditions
        self.var_chk = IntVar()
        chk = Checkbutton(frame1, text="I Agree The Terms & Conditions", variable=self.var_chk, onvalue=1, offvalue=0, font=("time new roman", 12), bg="white", fg="black").place(x=50, y=380)

        # ========== BUTTONS ==========
        # Register button - triggers register_data() function
        btn_register = Button(frame1, text="Register Now", font=("time new roman", 15, "bold"), bg="green", activebackground="green", bd=0, cursor="hand2", command=self.register_data).place(x=50, y=420, width=250, height=40)

        # Sign In button - placeholder for login navigation
        btn_login = Button(self.root, text="Sign In", font=("time new roman", 15, "bold"), bg="white", activebackground="white", bd=0, cursor="hand2", command=self.login_window).place(x=200, y=460, width=180, height=40)

    # ==================== LOGIN WINDOW NAVIGATION & FORM CLEARING ====================
    def login_window(self):
        self.root.destroy()  # Close the registration window
        # Get the directory where this script is located and construct full path to login.py
        current_dir = os.path.dirname(os.path.abspath(__file__))
        login_path = os.path.join(current_dir, "login.py")
        subprocess.Popen([sys.executable, login_path])

    def clear(self):
        """
        Clear all form input fields and reset to default values.
        Called after successful registration.
        """
        self.txt_fname.delete(0, END)
        self.txt_lname.delete(0, END)
        self.txt_contact.delete(0, END)
        self.txt_email.delete(0, END)
        self.txt_answer.delete(0, END)
        self.txt_password.delete(0, END)
        self.txt_cpassword.delete(0, END)
        self.cmb_quest.current(0)  # Reset combobox to "Select"
        self.var_chk.set(0)  # Uncheck the Terms & Conditions checkbox

    def register_data(self):
        """
        Validate user input and register new user in database.
        Performs validation checks and inserts data into SQL Server database.
        """
        # ========== VALIDATION: Check if all fields are filled ==========
        if (self.txt_fname.get() == "" or self.txt_contact.get() == "" or 
            self.txt_email.get() == "" or self.cmb_quest.get() == "Select" or 
            self.txt_answer.get() == "" or self.txt_password.get() == "" or 
            self.txt_cpassword.get() == ""):
            messagebox.showerror("Error", "All Fields Are Required", parent=self.root)
        
        # ========== VALIDATION: Check if passwords match ==========
        elif self.txt_password.get() != self.txt_cpassword.get():
            messagebox.showerror("Error", "Password & Confirm Password Should Be Same", parent=self.root)
        
        # ========== VALIDATION: Check if Terms & Conditions is accepted ==========
        elif self.var_chk.get() == 0:
            messagebox.showerror("Error", "Please Agree Our Terms & Conditions", parent=self.root)
        
        # ========== DATABASE OPERATION: Register user ==========
        else:
            try:
                # Connect to SQL Server database
                con=sqlite3.connect(database="rms.db")
                cursor = con.cursor()
                
                # Check if email already exists in database
                cursor.execute("SELECT * FROM studentresult WHERE email=?", (self.txt_email.get(),))
                row = cursor.fetchone()
                
                # If email already exists, show error
                if row != None:
                    messagebox.showerror("Error", "User Already Exist, Please Try With Another Email", parent=self.root)
                
                # Email is new, proceed with registration
                else:
                    # Insert user data into studentresult table
                    cursor.execute(
                        "INSERT INTO studentresult (first_name, last_name, contact, email, security_question, security_answer, password) VALUES (?, ?, ?, ?, ?, ?, ?)",
                        (
                            self.txt_fname.get(),
                            self.txt_lname.get(),
                            self.txt_contact.get(),
                            self.txt_email.get(),
                            self.cmb_quest.get(),
                            self.txt_answer.get(),
                            self.txt_password.get()
                        )
                    )
                    con.commit()  # Save changes to database
                    con.close()  # Close database connection
                    
                    # Show success message and clear form
                    messagebox.showinfo("Success", "Registration Successful", parent=self.root)
                    self.clear()
                    self.login_window()  # Navigate to login window after successful registration
            
            # ========== ERROR HANDLING: Catch any database exceptions ==========
            except Exception as es:
                messagebox.showerror("Error", f"Error Due To: {str(es)}", parent=self.root)


# ==================== APPLICATION ENTRY POINT ====================
# Create Tkinter root window
root = Tk()

# Initialize the Register class with the root window
obj = Register(root)

# Start the Tkinter event loop (keeps window open until closed)
root.mainloop()