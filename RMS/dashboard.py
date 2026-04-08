from tkinter import*
from PIL import Image,ImageTk #pip install pillow
from course import CourseClass
import sqlite3
from student import studentClass
from result import ResultClass
from report import reportClass
from tkinter import messagebox
import os
import sys
import subprocess

# ==================== MAIN DASHBOARD CLASS ====================
# This class creates the main application dashboard window after a user logs in.
# It shows quick-action buttons for managing courses, students, results and report views,
# and also shows counters for total courses, students, and results in the database.
class RMS:
    def __init__(self, root):
        self.root= root
        self.root.title("Student Result Managment System")
        self.root.geometry("1510x780+0+0")
        self.root.config(bg="white")

        #========icon=======
        # self.logo_dash=ImageTk.PhotoImage(file="assets/logo_p.png")  #optional
        img = Image.open("assets/logo_p.png")
        img = img.resize((65, 45),Image.LANCZOS )  # Change (65, 45) to your desired width and height
        self.logo_dash = ImageTk.PhotoImage(img)

        #=======title=======
        title=Label(self.root,text="Student Result Managment System",padx=10,compound=LEFT,image=self.logo_dash,font=("goudy old style",20,"bold"),bg="#033054",fg="white").place(x=0,y=0,relwidth=1,height=50)

      #========Menu========
        M_Frame=LabelFrame(self.root,text="Menus",font=("time new roman",15),bg="white")
        M_Frame.place(x=10,y=70,width=1405,height=80)

        bnt_course=Button(M_Frame,text="Course",font=("goldy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.add_course).place(x=30,y=5,width=200,height=40)

        bnt_student=Button(M_Frame,text="Student",font=("goldy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.add_student).place(x=260,y=5,width=200,height=40)

        bnt_result=Button(M_Frame,text="Result",font=("goldy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.add_result).place(x=490,y=5,width=200,height=40)

        bnt_viewstudentresult=Button(M_Frame,text="View Student Result",font=("goldy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.add_report).place(x=710,y=5,width=200,height=40)

        bnt_logout=Button(M_Frame,text="Logout",font=("goldy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.logout).place(x=940,y=5,width=200,height=40)

        bnt_exit=Button(M_Frame,text="Exit",font=("goldy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.exit).place(x=1170,y=5,width=200,height=40)


        #=========content_window========
        self.bg_img=Image.open("assets/student.png")
        self.bg_img=self.bg_img.resize((950,400),Image.LANCZOS)
        self.bg_img=ImageTk.PhotoImage(self.bg_img)

        self.lbl_bg=Label(self.root,image=self.bg_img).place(x=330,y=180,width=950,height=400)

        #========update_details========
        self.lbl_course=Label(self.root,text="Total Courses\n[ 0 ]",font=("goldy old style",20),bd=10,relief="ridge",bg="#e43b06",fg="white")
        self.lbl_course.place(x=330,y=580,width=300,height=100)

        self.lbl_student=Label(self.root,text="Total Student\n[ 0 ]",font=("goldy old style",20),bd=10,relief="ridge",bg="#0676ad",fg="white")
        self.lbl_student.place(x=655,y=580,width=300,height=100)

        self.lbl_result=Label(self.root,text="Total Result\n[ 0 ]",font=("goldy old style",20),bd=10,relief="ridge",bg="#038074",fg="white")
        self.lbl_result.place(x=980,y=580,width=300,height=100)


        #======footer========
        footer=Label(self.root,text="SRMS-Student Result Managment System\nContact Us for any Technical Issue: +91 9695411360",font=("goudy old style",12),bg="#262626",fg="white").pack(side=BOTTOM,fill=X)

        # Start periodic update of the counts (courses, students, results)
        self.update_details()

    # ======== periodical update of dashboard counts ========
    def update_details(self):
        """Fetches record counts from the database and updates the labels in the dashboard."""
        con=sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:
            # Count courses
            cur.execute("select * from course")
            cr=cur.fetchall()
            self.lbl_course.config(text=f"Total Courses\n[ {str(len(cr))} ]")

            # Count students
            cur.execute("select * from student")
            cr=cur.fetchall()
            self.lbl_student.config(text=f"Total Students\n[ {str(len(cr))} ]")

            # Count results
            cur.execute("select * from result")
            cr=cur.fetchall()
            self.lbl_result.config(text=f"Total Results\n[ {str(len(cr))} ]")

            # Re-run this method repeatedly every 200 milliseconds to refresh dashboard counts
            self.lbl_course.after(200,self.update_details)

        except Exception as es:
            messagebox.showerror("Error",f"Error due to {str(es)}",parent=self.root)
        finally:
            con.close()  # Always close DB connection


    # ======== Menu navigation helpers ========
    # Each button opens a child window for that module.
    def add_course(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=CourseClass(self.new_win)

    def add_student(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=studentClass(self.new_win)

    def add_result(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=ResultClass(self.new_win)

    def add_report(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=reportClass(self.new_win)

    # ======== Logout and exit actions ========
    def logout(self):
        """Log out current user and open the login window."""
        op=messagebox.askyesno("Confirm","Do you really want to logout?",parent=self.root)
        if op==True:
            self.root.destroy()
            # Open login window using the same Python interpreter and absolute path
            current_dir = os.path.dirname(os.path.abspath(__file__))
            login_path = os.path.join(current_dir, "login.py")
            subprocess.Popen([sys.executable, login_path])

    def exit(self):
        """Exit the application entirely."""
        op=messagebox.askyesno("Confirm","Do you really want to Exit?",parent=self.root)
        if op==True:
            self.root.destroy()


if __name__=="__main__":
    root=Tk()
    obj=RMS(root)
    root.mainloop()