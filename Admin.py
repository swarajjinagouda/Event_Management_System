import tkinter.ttk
from PIL import ImageTk  # Install Pillow
from tkinter import *
import pymysql  # Install pymysql
from tkinter import messagebox
import tkinter as tk
import random


class tkinterApp(tk.Tk):
    # __init__ function for class tkinterApp
    def __init__(self, *args, **kwargs):
        # __init__ function for class Tk
        tk.Tk.__init__(self, *args, **kwargs)
        self.geometry("1920x1080")
        self.title("Event Management System")
        self.app_data = {"Username": tk.StringVar()}

        # Creating a container
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # Initializing frames to an empty array
        self.frames = {}

        # Iterating through a tuple consisting of the different page layouts
        for F in (StartPage, Admin_Login, Admin_Registration, Customer_Login, Customer_Registration, Admin_Dashboard, Admin_Theme, Admin_CreateEvent, Admin_ModifyEvent, Admin_EventList, User_Dashboard, Admin_Dashboard2, Admin_User_Feedback, Admin_Registered_Users, User_Event_Request, Admin_EventRequest, User_Dashboard2, User_EventList, User_Contact_Us):
            frame = F(container, self)

            # Initializing frame of that object from
            # StartPage, page1, page2 respectively with
            # FOR loop
            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)  # StartPage

    # To display the current frame passed as PARAMETER
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

        # ------------------- START -------------------- #


class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.controller = controller
        self.config(bg="sky blue")  # for solid bg

        frame1 = Frame(self, bg="#FEFCFF", relief="solid")
        frame1.place(x=650, y=440, width=240, height=230)

        # Background Image
        self.bg = ImageTk.PhotoImage(file="images/9.jpg")
        bg = Label(self, image=self.bg, relief="solid").place(x=250, y=50)

        login_as = Label(frame1, text="Login As", font=("Times new roman", 25, "bold"), bg="#FEFCFF", fg="black").place(
            x=55, y=30)  # x=700, y=450

        admin_login = Button(frame1, text="Admin", font=("Times new roman", 18, "bold"), relief="solid", bg="#FEFCFF",
                             fg="green", cursor="hand2", command=lambda: controller.show_frame(Admin_Login)).place(x=78,
                                                                                                                   y=85)  # x=720, y=520

        customer_login = Button(frame1, text="Customer", font=("Times new roman", 18, "bold"), relief="solid",
                                bg="#FEFCFF", fg="green", cursor="hand2",
                                command=lambda: controller.show_frame(Customer_Login)).place(x=65, y=145)  # x=708, y=580

        # ------------------- ADMIN LOGIN -------------------- #


class Admin_Login(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.controller = controller
        self.config(bg="sky blue")  # for solid bg

        login_frame = Frame(self, bg="white")
        login_frame.place(x=350, y=100, width=800, height=500)

        # Back Button
        self.bg = ImageTk.PhotoImage(file="images/back-arrow.png")
        bg = Button(login_frame, image=self.bg, command=lambda: controller.show_frame(StartPage), relief="solid").place(x=0, y=0, width=35, height=35)

        title = Label(login_frame, text="ADMIN LOGIN", font=("Times New Roman", 30, "bold"), bg="white",
                      fg="#08A3D2").place(x=250, y=50)

        username = Label(login_frame, text="Username", font=("Times New Roman", 18, "bold"), bg="white",
                         fg="#2C3539").place(x=250, y=150)
        self.txt_username = Entry(login_frame, font=("Times New Roman", 18), bg="lightgray")
        self.txt_username.place(x=250, y=180, width=350, height=35)

        pass_ = Label(login_frame, text="Password", font=("Times New Roman", 18, "bold"), bg="white",
                      fg="#2C3539").place(x=250, y=250)
        self.txt_pass_ = Entry(login_frame, font=("Times New Roman", 18), bg="lightgray", show="*")
        self.txt_pass_.place(x=250, y=280, width=350, height=35)

        btn_reg = Button(login_frame, cursor="hand2", command=lambda: controller.show_frame(Admin_Registration),
                         text="Register new Account?",
                         font=("Times New Roman", 14), bg="white", bd=0, fg="#B00857").place(x=250, y=320)

        btn_login = Button(login_frame, text="Login", command=self.login, font=("Times New Roman", 20, "bold"),
                           fg="white", bg="#B00857", cursor="hand2").place(x=250, y=380, width=180, height=40)

    def clear(self):
        self.txt_username.delete(0, END)
        self.txt_pass_.delete(0, END)

    def login(self):
        if self.txt_username.get() == "" or self.txt_pass_.get() == "":
            messagebox.showerror("Error", "All Fields are Required", parent=self)

        else:
            try:
                con = pymysql.connect(host="localhost", user="root", password="root", db="event_management", port=3307)
                cur = con.cursor()
                cur.execute("SELECT f_name FROM ADMIN WHERE USERNAME=%s", self.txt_username.get())
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror("Error", "Invalid USERNAME", parent=self)

                else:
                    # messagebox.showinfo("Success", "Welcome", parent=self)
                    self.controller.app_data["admin"] = row
                    # print(self.controller.app_data["admin"])
                con.close()

            except Exception as es:
                messagebox.showerror("Error", f"Error Due to: {str(es)}", parent=self)

            try:
                con = pymysql.connect(host="localhost", user="root", password="root", db="event_management", port=3307)
                cur = con.cursor()
                cur.execute("SELECT * FROM ADMIN WHERE USERNAME=%s and PASSWORD=%s",
                                (self.txt_username.get(), self.txt_pass_.get()))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror("Error", "Invalid USERNAME or PASSWORD", parent=self)

                else:
                    messagebox.showinfo("Success", "Welcome", parent=self)
                    self.clear()
                    self.controller.show_frame(Admin_Dashboard)
                con.close()

            except Exception as es:
                messagebox.showerror("Error", f"Error Due to: {str(es)}", parent=self)

                # ------------------- ADMIN REGISTRATION -------------------- #


class Admin_Registration(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.controller = controller
        self.config(bg="sky blue")  # for solid bg

        # Register Frame
        frame1 = Frame(self, bg="white")
        frame1.place(x=425, y=100, width=700, height=550)

        title = Label(frame1, text="ADMIN REGISTRATION", font=("Times new roman", 20, "bold"), bg="white",
                      fg="green").place(x=210, y=30)

        # First Name
        f_name = Label(frame1, text="First Name:", font=("Times new roman", 15, "bold"), bg="white", fg="black").place(x=50, y=100)
        self.txt_fname = Entry(frame1, font=("Times new roman", 15), bg="lightgray", relief="solid")
        self.txt_fname.place(x=50, y=130, width=250)

        # Last Name
        l_name = Label(frame1, text="Last Name:", font=("Times new roman", 15, "bold"), bg="white", fg="black").place(x=50, y=170)
        self.txt_lname = Entry(frame1, font=("Times new roman", 15), bg="lightgray", relief="solid")
        self.txt_lname.place(x=50, y=200, width=250)

        # Gender
        gender = Label(frame1, text="Gender:", font=("Times new roman", 15, "bold"), bg="white", fg="black").place(x=50,
                                                                                                                   y=240)
        self.gender = Entry(frame1, font=("Times new roman", 15), bg="lightgray", relief="solid")
        self.gender.place(x=50, y=270, width=250)

        # Email-ID
        email_id = Label(frame1, text="Email-ID:", font=("Times new roman", 15, "bold"), bg="white", fg="black").place(x=50, y=310)
        self.txt_emailid = Entry(frame1, font=("Times new roman", 15), bg="lightgray", relief="solid")
        self.txt_emailid.place(x=50, y=340, width=250)

        # Phone Number
        ph_no = Label(frame1, text="Phone number:", font=("Times new roman", 15, "bold"), bg="white", fg="black").place(x=50, y=380)
        self.txt_phno = Entry(frame1, font=("Times new roman", 15), bg="lightgray", relief="solid")
        self.txt_phno.place(x=50, y=410, width=250)

        # Username
        username = Label(frame1, text="Username:", font=("Times new roman", 15, "bold"), bg="white", fg="black").place(x=370, y=240)
        self.txt_username = Entry(frame1, font=("Times new roman", 15), bg="lightgray", relief="solid")
        self.txt_username.place(x=370, y=270, width=250)

        # Password
        password = Label(frame1, text="Password:", font=("Times new roman", 15, "bold"), bg="white", fg="black").place(
            x=370, y=310)
        self.txt_password = Entry(frame1, font=("Times new roman", 15), bg="lightgray", relief="solid", show="*")
        self.txt_password.place(x=370, y=340, width=250)

        # Confirm Password
        confirm_pwd = Label(frame1, text="Confirm Password:", font=("Times new roman", 15, "bold"), bg="white",
                            fg="black").place(x=370, y=380)
        self.txt_confirmpwd = Entry(frame1, font=("Times new roman", 15), bg="lightgray", relief="solid", show="*")
        self.txt_confirmpwd.place(x=370, y=410, width=250)

        # Register Button
        btn_register = Button(frame1, text="Register", font=("Times new roman", 13, "bold"), relief="solid", bg="white",
                              fg="green", cursor="hand2", command=self.register_data).place(x=300, y=460)

        # Sign In Button
        sign_in_label = Label(frame1, cursor="hand2", text="Already a User?", font=("Times New Roman", 14), bg="white",
                              fg="black").place(x=240, y=504)
        sign_in = Button(frame1, cursor="hand2", command=lambda: controller.show_frame(Admin_Login), text="Sign In",
                         relief="solid", font=("Times New Roman", 13, "bold"), bg="white", fg="green").place(x=370, y=500)

    def clear(self):
        self.txt_fname.delete(0, END)
        self.txt_lname.delete(0, END)
        self.gender.delete(0, END)
        self.txt_emailid.delete(0, END)
        self.txt_phno.delete(0, END)
        self.txt_username.delete(0, END)
        self.txt_password.delete(0, END)
        self.txt_confirmpwd.delete(0, END)

    def register_data(self):
        if self.txt_fname.get() == "" or self.txt_lname.get() == "" or self.gender.get() == "" or self.txt_emailid.get() == "" or self.txt_phno.get() == "" or self.txt_username.get() == "" or self.txt_password.get() == "" or self.txt_confirmpwd.get() == "":
            messagebox.showerror("Error", "All Fields are Required", parent=self)
        elif self.gender.get() != "Male" and self.gender.get() != "Female" and self.gender.get() != "male" and self.gender.get() != "female" and self.gender.get() != "MALE" and self.gender.get() != "FEMALE":
            messagebox.showerror("Error", "Input correct Gender", parent=self)
        elif self.txt_password.get() != self.txt_confirmpwd.get():
            messagebox.showerror("Error", "Password and Confirm Password should match", parent=self)
        elif len(self.txt_phno.get()) != 10:
            messagebox.showerror("Error", "Phone number is not valid", parent=self)
        else:
            try:
                con = pymysql.connect(host="localhost", user="root", password="root", db="event_management", port=3307)
                cur = con.cursor()
                cur.execute("select * from admin where username=%s", self.txt_username.get())
                row = cur.fetchone()
                if row != None:
                    messagebox.showerror("Error", "Username Already exists, Try Another username", parent=self)
                else:
                    cur.execute(
                        "insert into admin (f_name,l_name,gender,email_id,ph_no,username,password) values(%s,%s,%s,%s,%s,%s,%s)",
                        (
                            self.txt_fname.get(),
                            self.txt_lname.get(),
                            self.gender.get(),
                            self.txt_emailid.get(),
                            self.txt_phno.get(),
                            self.txt_username.get(),
                            self.txt_password.get()
                        ))
                    con.commit()
                    con.close()
                    messagebox.showinfo("Success", "Register Successful", parent=self)
                    self.clear()
                    self.controller.show_frame(Admin_Login)

            except Exception as es:
                messagebox.showerror("Error", f"Error due to:{str(es)}", parent=self)

                # ------------------- CUSTOMER LOGIN -------------------- #


class Customer_Login(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.controller = controller
        self.config(bg="sky blue")  # for solid bg

        login_frame = Frame(self, bg="white")
        login_frame.place(x=350, y=100, width=800, height=500)

        # Back Button
        self.bg = ImageTk.PhotoImage(file="images/back-arrow.png")
        bg = Button(login_frame, image=self.bg, command=lambda: controller.show_frame(StartPage), relief="solid").place(x=0, y=0, width=35, height=35)

        title = Label(login_frame, text="CUSTOMER LOGIN", font=("Times New Roman", 30, "bold"), bg="white",
                      fg="#08A3D2").place(x=220, y=50)

        username = Label(login_frame, text="Username", font=("Times New Roman", 18, "bold"), bg="white",
                         fg="#2C3539").place(x=250, y=150)
        self.txt_username = Entry(login_frame, font=("Times New Roman", 18), bg="lightgray")
        self.txt_username.place(x=250, y=180, width=350, height=35)

        pass_ = Label(login_frame, text="Password", font=("Times New Roman", 18, "bold"), bg="white",
                      fg="#2C3539").place(x=250, y=250)
        self.txt_pass_ = Entry(login_frame, font=("Times New Roman", 18), bg="lightgray", show="*")
        self.txt_pass_.place(x=250, y=280, width=350, height=35)

        btn_reg = Button(login_frame, cursor="hand2", command=lambda: controller.show_frame(Customer_Registration), text="Register new Account?",
                         font=("Times New Roman", 14), bg="white", bd=0, fg="#B00857").place(x=250, y=320)

        btn_login = Button(login_frame, text="Login", command=self.login, font=("Times New Roman", 20, "bold"),
                           fg="white", bg="#B00857", cursor="hand2").place(x=250, y=380, width=180, height=40)

    def clear(self):
        self.txt_username.delete(0, END)
        self.txt_pass_.delete(0, END)

    def login(self):
        if self.txt_username.get() == "" or self.txt_pass_.get() == "":
            messagebox.showerror("Error", "All Fields are Required", parent=self)
        else:
            try:
                con = pymysql.connect(host="localhost", user="root", password="root", db="event_management", port=3307)
                cur = con.cursor()
                cur.execute("SELECT * FROM CUSTOMER WHERE USERNAME=%s and PASSWORD=%s",
                            (self.txt_username.get(), self.txt_pass_.get()))
                self.controller.app_data["Username"] = self.txt_username.get()
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror("Error", "Invalid USERNAME or PASSWORD", parent=self)

                else:
                    messagebox.showinfo("Success", "Welcome", parent=self)
                    self.clear()
                    self.controller.show_frame(User_Dashboard)
                con.close()

            except Exception as es:
                messagebox.showerror("Error", f"Error Due to: {str(es)}", parent=self)

                # ------------------- CUSTOMER REGISTRATION -------------------- #


class Customer_Registration(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.controller = controller
        self.config(bg="sky blue")  # for solid bg

        # Register Frame
        frame1 = Frame(self, bg="white")
        frame1.place(x=425, y=100, width=700, height=550)

        title = Label(frame1, text="CUSTOMER REGISTRATION", font=("Times new roman", 20, "bold"), bg="white",
                      fg="green").place(x=170, y=30)

        # First Name
        f_name = Label(frame1, text="First Name:", font=("Times new roman", 15, "bold"), bg="white", fg="black").place(x=50, y=100)
        self.txt_fname = Entry(frame1, font=("Times new roman", 15), bg="lightgray", relief="solid")
        self.txt_fname.place(x=50, y=130, width=250)

        # Last Name
        l_name = Label(frame1, text="Last Name:", font=("Times new roman", 15, "bold"), bg="white", fg="black").place(
            x=50, y=170)  # x=370
        self.txt_lname = Entry(frame1, font=("Times new roman", 15), bg="lightgray", relief="solid")
        self.txt_lname.place(x=50, y=200, width=250)

        # Gender
        gender = Label(frame1, text="Gender:", font=("Times new roman", 15, "bold"), bg="white", fg="black").place(x=50,
                                                                                                                   y=240)
        self.gender = Entry(frame1, font=("Times new roman", 15), bg="lightgray", relief="solid")
        self.gender.place(x=50, y=270, width=250)

        # Email-ID
        email_id = Label(frame1, text="Email-ID:", font=("Times new roman", 15, "bold"), bg="white", fg="black").place(x=50, y=310)
        self.txt_emailid = Entry(frame1, font=("Times new roman", 15), bg="lightgray", relief="solid")
        self.txt_emailid.place(x=50, y=340, width=250)

        # Phone Number
        ph_no = Label(frame1, text="Phone number:", font=("Times new roman", 15, "bold"), bg="white", fg="black").place(x=50, y=380)
        self.txt_phno = Entry(frame1, font=("Times new roman", 15), bg="lightgray", relief="solid")
        self.txt_phno.place(x=50, y=410, width=250)

        # Username
        username = Label(frame1, text="Username:", font=("Times new roman", 15, "bold"), bg="white", fg="black").place(x=370, y=240)
        self.txt_username = Entry(frame1, font=("Times new roman", 15), bg="lightgray", relief="solid")
        self.txt_username.place(x=370, y=270, width=250)

        # Password
        password = Label(frame1, text="Password:", font=("Times new roman", 15, "bold"), bg="white", fg="black").place(x=370, y=310)
        self.txt_password = Entry(frame1, font=("Times new roman", 15), bg="lightgray", relief="solid", show="*")
        self.txt_password.place(x=370, y=340, width=250)

        # Confirm Password
        confirm_pwd = Label(frame1, text="Confirm Password:", font=("Times new roman", 15, "bold"), bg="white", fg="black").place(x=370, y=380)
        self.txt_confirmpwd = Entry(frame1, font=("Times new roman", 15), bg="lightgray", relief="solid", show="*")
        self.txt_confirmpwd.place(x=370, y=410, width=250)

        # Register Button
        btn_register = Button(frame1, text="Register", font=("Times new roman", 13, "bold"), relief="solid", bg="white",
                              fg="green", cursor="hand2", command=self.register_data).place(x=300, y=460)

        # Sign In Button
        sign_in_label = Label(frame1, cursor="hand2", text="Already a User?", font=("Times New Roman", 14), bg="white",
                              fg="black").place(x=240, y=504)
        sign_in = Button(frame1, cursor="hand2", command=lambda: controller.show_frame(Customer_Login), text="Sign In", relief="solid",
                         font=("Times New Roman", 13, "bold"), bg="white", fg="green").place(x=370, y=500)

    def clear(self):
        self.txt_fname.delete(0, END)
        self.txt_lname.delete(0, END)
        self.gender.delete(0, END)
        self.txt_emailid.delete(0, END)
        self.txt_phno.delete(0, END)
        self.txt_username.delete(0, END)
        self.txt_password.delete(0, END)
        self.txt_confirmpwd.delete(0, END)

    def register_data(self):
        if self.txt_fname.get() == "" or self.txt_lname.get() == "" or self.gender.get() == "" or self.txt_emailid.get() == "" or self.txt_phno.get() == "" or self.txt_username.get() == "" or self.txt_password.get() == "" or self.txt_confirmpwd.get() == "":
            messagebox.showerror("Error", "All Fields are Required", parent=self)
        elif self.gender.get() != "Male" and self.gender.get() != "Female" and self.gender.get() != "male" and self.gender.get() != "female" and self.gender.get() != "MALE" and self.gender.get() != "FEMALE":
            messagebox.showerror("Error", "Input correct Gender", parent=self)
        elif self.txt_password.get() != self.txt_confirmpwd.get():
            messagebox.showerror("Error", "Password and Confirm Password should match", parent=self)
        elif len(self.txt_phno.get()) != 10:
            messagebox.showerror("Error", "Phone number is not valid", parent=self)
        else:
            try:
                con = pymysql.connect(host="localhost", user="root", password="root", db="event_management", port=3307)
                cur = con.cursor()
                cur.execute("select * from customer where username=%s", self.txt_username.get())
                row = cur.fetchone()
                if row != None:
                    messagebox.showerror("Error", "Username Already exists, Try Another username", parent=self)
                else:
                    cur.execute(
                        "insert into customer (f_name,l_name,gender,email_id,ph_no,username,password) values(%s,%s,%s,%s,%s,%s,%s)",
                        (
                            self.txt_fname.get(),
                            self.txt_lname.get(),
                            self.gender.get(),
                            self.txt_emailid.get(),
                            self.txt_phno.get(),
                            self.txt_username.get(),
                            self.txt_password.get()
                        ))
                    con.commit()
                    con.close()
                    messagebox.showinfo("Success", "Register Successful", parent=self)
                    self.clear()
                    self.controller.show_frame(Customer_Login)

            except Exception as es:
                messagebox.showerror("Error", f"Error due to:{str(es)}", parent=self)

                # ------------------- ADMIN FIRST PAGE -------------------- #


class Admin_Dashboard(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.controller = controller
        self.config(bg="white")  # for solid bg

        # Blue Frame
        frame_1 = Frame(self, bg="#1589FF")
        frame_1.place(x=220, y=0, width=1920, height=40)

        # Title
        title = Label(frame_1, text="Event Management System", font=("Times New Roman", 20, "bold"), bg="#1589FF",
                      fg="white").place(x=10, y=0)

        # Refresh Button
        home = Button(frame_1, cursor="hand2", command=self.refresh, text="Refresh",
                      font=("Times New Roman", 14, "bold"), bg="#1589FF", bd=0,
                      fg="white").place(x=1125, y=3)

        # Logout Button
        logout = Button(frame_1, cursor="hand2", command=lambda: controller.show_frame(Admin_Login), text="Logout",
                        font=("Times New Roman", 14, "bold"), bg="#1589FF", bd=0, fg="white").place(x=1230, y=3)

        # Dashboard
        dashboard = Label(self, text="DASHBOARD", font=("Times New Roman", 18, "bold", "underline"), bg="white", fg="#08A3D2").place(x=795, y=50)

        # --Card 1--#
        self.card_1 = Frame(self, bg="#ef255f")
        self.card_1.place(x=280, y=120, width=350, height=250)
        lb_events = Label(self.card_1, text="Total Events", font=("Times New Roman", 20, "bold"), bg="#ef255f",
                          fg="white").place(x=100, y=200)
        try:
            con = pymysql.connect(host="localhost", user="root", password="root", db="event_management", port=3307)
            cur = con.cursor()
            cur.execute("SELECT event_id FROM event_123")
            j = 0
            row = cur.fetchall()
            if row == None:
                messagebox.showerror("Error", "No events found", parent=self)
            else:
                for i in row:
                    j += 1
            con.close()

        except Exception as es:
            messagebox.showerror("Error", f"Error Due to: {str(es)}", parent=self)

        lb_event_no = Label(self.card_1, text=j, font=("Times New Roman", 65, "bold"), bg="#ef255f",
                            fg="white").place(x=150, y=60)

        # --Card 2--#
        self.card_2 = Frame(self, bg="#FDD017")
        self.card_2.place(x=700, y=120, width=350, height=250)
        lb_events = Label(self.card_2, text="Users Registered", font=("Times New Roman", 20, "bold"), bg="#fccf4d",
                          fg="white").place(x=75, y=200)

        try:
            con = pymysql.connect(host="localhost", user="root", password="root", db="event_management", port=3307)
            cur = con.cursor()
            cur.execute("SELECT username FROM customer")
            j = 0
            row = cur.fetchall()
            if row == None:
                messagebox.showerror("Error", "No customers found", parent=self)
            else:
                for i in row:
                    j += 1
            con.close()

        except Exception as es:
            messagebox.showerror("Error", f"Error Due to: {str(es)}", parent=self)

        lb_event_no = Label(self.card_2, text=j, font=("Times New Roman", 65, "bold"), bg="#fccf4d",
                            fg="white").place(x=140, y=60)
        # --Card 3--#
        self.card_3 = Frame(self, bg="#49beb7")
        self.card_3.place(x=1120, y=120, width=350, height=250)  # x=1040, y=90
        lb_events = Label(self.card_3, text="Completed Events", font=("Times New Roman", 20, "bold"), bg="#49beb7",
                          fg="white").place(x=70, y=200)

        try:
            con = pymysql.connect(host="localhost", user="root", password="root", db="event_management", port=3307)
            cur = con.cursor()
            cur.execute("SELECT event_id FROM event_123 where event_status='Completed'")
            k = 0
            row = cur.fetchall()
            if row == None:
                messagebox.showerror("Error", "No events are completed yet", parent=self)
            else:
                for i in row:
                    k += 1
            con.close()

        except Exception as es:
            messagebox.showerror("Error", f"Error Due to: {str(es)}", parent=self)

        lb_event_no = Label(self.card_3, text=k, font=("Times New Roman", 65, "bold"), bg="#49beb7",
                            fg="white").place(x=145, y=60)

        # --Card 4--#
        self.card_4 = Frame(self, bg="light green")
        self.card_4.place(x=280, y=450, width=350, height=250)
        lb_events = Label(self.card_4, text="Themes", font=("Times New Roman", 20, "bold"), bg="light green",
                          fg="white").place(x=125, y=200)

        try:
            con = pymysql.connect(host="localhost", user="root", password="root", db="event_management", port=3307)
            cur = con.cursor()
            cur.execute("SELECT theme_name from theme")
            j = 0
            row = cur.fetchall()
            if row == None:
                messagebox.showerror("Error", "No events found", parent=self)
            else:
                for i in row:
                    j += 1
            con.close()

        except Exception as es:
            messagebox.showerror("Error", f"Error Due to: {str(es)}", parent=self)

        lb_event_no = Label(self.card_4, text=j, font=("Times New Roman", 65, "bold"), bg="light green",
                            fg="white").place(x=145, y=60)

        # --Card 5--#
        self.card_5 = Frame(self, bg="pink")
        self.card_5.place(x=700, y=450, width=350, height=250)
        lb_event_requests = Label(self.card_5, text="Event Requests", font=("Times New Roman", 20, "bold"), bg="pink",
                          fg="white").place(x=90, y=200)

        try:
            con = pymysql.connect(host="localhost", user="root", password="root", db="event_management", port=3307)
            cur = con.cursor()
            cur.execute("SELECT req_id from user_event_request")
            j = 0
            row = cur.fetchall()
            if row == None:
                messagebox.showerror("Error", "No events found", parent=self)
            else:
                for i in row:
                    j += 1
            con.close()

        except Exception as es:
            messagebox.showerror("Error", f"Error Due to: {str(es)}", parent=self)

        lb_event_requests = Label(self.card_5, text=j, font=("Times New Roman", 65, "bold"), bg="pink",
                            fg="white").place(x=145, y=60)

        # --Card 6--#
        self.card_6 = Frame(self, bg="orange")
        self.card_6.place(x=1120, y=450, width=350, height=250)
        lb_events = Label(self.card_6, text="Active Events", font=("Times New Roman", 20, "bold"), bg="orange",
                          fg="white").place(x=95, y=200)

        try:
            con = pymysql.connect(host="localhost", user="root", password="root", db="event_management", port=3307)
            cur = con.cursor()
            cur.execute("SELECT event_id FROM event_123 where event_status='Active'")
            k = 0
            row = cur.fetchall()
            if row == None:
                messagebox.showerror("Error", "No events are completed yet", parent=self)
            else:
                for i in row:
                    k += 1
            con.close()

        except Exception as es:
            messagebox.showerror("Error", f"Error Due to: {str(es)}", parent=self)

        lb_event_no = Label(self.card_6, text=k, font=("Times New Roman", 65, "bold"), bg="orange",
                            fg="white").place(x=145, y=60)

        # --GREY FRAME--#
        side_card = Frame(self, bg="#3C4248")
        side_card.place(x=0, y=0, width=225, height=1080)
        line_card = Frame(self, bg="white")
        line_card.place(x=0, y=45, width=225, height=1)

        title = Label(side_card, text="Welcome Admin", font=("Times New Roman", 20, "bold"), bg="#3C4248",
                      fg="white").place(x=10, y=0)

        # --DASHBOARD--#
        btn_dashboard = Button(side_card, text="Dashboard", command=lambda: controller.show_frame(Admin_Dashboard), font=("Helvetica", 18, "bold"),
                               bg="#3C4248", fg="white", bd=0).place(x=40, y=60)  # bg="light grey"
        self.bg4 = ImageTk.PhotoImage(file="C:/Users/Swaraj/Desktop/Icons/Icons/dashboard.png")
        events_icon4 = Label(side_card, bg="#3C4248", fg="light grey", image=self.bg4).place(x=10, y=70)

        # --EVENTS--#
        lb_events_side = Label(side_card, text="Events", font=("Helvetica", 20, "bold"), bg="#3C4248", fg="light grey").place(x=40, y=130)
        self.bg = ImageTk.PhotoImage(file="C:/Users/Swaraj/Desktop/Icons/Icons/calendar.png")
        events_icon = Label(side_card, bg="#3C4248", fg="light grey", image=self.bg).place(x=10, y=135)
        self.bg2 = ImageTk.PhotoImage(file="C:/Users/Swaraj/Desktop/Icons/Icons/right-arrow.png")
        events_icon2 = Button(side_card, bg="#3C4248", fg="light grey", bd=0, image=self.bg2, command=lambda: controller.show_frame(Admin_Dashboard2)).place(x=150, y=140)

        # --CREATE EVENT--#
        btn_events_create = Button(side_card, command=lambda: controller.show_frame(Admin_CreateEvent), text="Create Events", font=("Helvetica", 18, "bold"), bg="#3C4248",
                                   fg="white", bd=0).place(x=35, y=170)  # bg="light grey"
        self.bg3 = ImageTk.PhotoImage(file="C:/Users/Swaraj/Desktop/Icons/Icons/calendar_add.png")
        events_icon3 = Label(side_card, bg="#3C4248", fg="light grey", image=self.bg3).place(x=10, y=180)

        # --CREATE THEME--#
        btn_theme_create = Button(side_card, text="Create Theme", command=lambda: controller.show_frame(Admin_Theme),
                                  font=("Helvetica", 18, "bold"), bg="#3C4248", fg="white", bd=0).place(x=35, y=215)
        self.bg8 = ImageTk.PhotoImage(file="C:/Users/Swaraj/Desktop/Icons/Icons/12.png")
        events_icon8 = Label(side_card, bg="#3C4248", fg="light grey", image=self.bg8).place(x=10, y=225)

        # --MODIFY EVENT--#
        btn_events_mod = Button(side_card, text="Modify Event", command=lambda: controller.show_frame(Admin_ModifyEvent), font=("Helvetica", 18, "bold"),
                                bg="#3C4248", fg="white", bd=0).place(x=35, y=260)  # bg="light grey"
        self.bg5 = ImageTk.PhotoImage(file="C:/Users/Swaraj/Desktop/Icons/Icons/calendar_mod.png")
        events_icon5 = Label(side_card, bg="#3C4248", fg="light grey", image=self.bg5).place(x=10, y=270)

        # --EVENT REQUESTS--#
        btn_events_request = Button(side_card, text="Event Requests", font=("Helvetica", 18, "bold"), command=lambda: controller.show_frame(Admin_EventRequest),
                                    bg="#3C4248", fg="white", bd=0).place(x=35, y=305)  # bg="light grey"
        self.bg6 = ImageTk.PhotoImage(file="C:/Users/Swaraj/Desktop/Icons/Icons/calendar_notification.png")
        events_icon6 = Label(side_card, bg="#3C4248", fg="light grey", image=self.bg6).place(x=10, y=315)

        # --EVENT LIST--#
        btn_events_list = Button(side_card, text="Event List", font=("Helvetica", 18, "bold"), command=lambda: controller.show_frame(Admin_EventList),
                                 bg="#3C4248", fg="white", bd=0).place(x=35, y=350)  # bg="light grey"
        self.bg7 = ImageTk.PhotoImage(file="C:/Users/Swaraj/Desktop/Icons/Icons/list.png")
        events_icon7 = Label(side_card, bg="#3C4248", fg="light grey", image=self.bg7).place(x=10, y=360)

        # --User Feedback--#
        btn_user_feedback = Button(side_card, text="User Feedback", font=("Helvetica", 18, "bold"), command=lambda: controller.show_frame(Admin_User_Feedback),
                           bg="#3C4248", fg="white", bd=0).place(x=35, y=393)  # bg="light grey"
        self.bg9 = ImageTk.PhotoImage(file="C:/Users/Swaraj/Desktop/Icons/Icons/feedback.png")
        events_icon9 = Label(side_card, bg="#3C4248", fg="light grey", image=self.bg9).place(x=7, y=400)

        # --Registered Users--#
        btn_registered_user = Button(side_card, text="Reg. Users", font=("Helvetica", 18, "bold"),
                           command=lambda: controller.show_frame(Admin_Registered_Users),
                           bg="#3C4248", fg="white", bd=0).place(x=35, y=435)  # bg="light grey"
        self.bg10 = ImageTk.PhotoImage(file="C:/Users/Swaraj/Desktop/Icons/Icons/reg_users.png")
        events_icon10 = Label(side_card, bg="#3C4248", fg="light grey", image=self.bg10).place(x=9, y=442)

    def refresh(self):
        try:
            con = pymysql.connect(host="localhost", user="root", password="root", db="event_management", port=3307)
            cur = con.cursor()
            cur.execute("SELECT event_id FROM event_123")
            j = 0
            row = cur.fetchall()
            if row == None:
                messagebox.showerror("Error", "No events found", parent=self)
            else:
                for i in row:
                    j += 1
            con.close()
        except Exception as es:
            messagebox.showerror("Error", f"Error Due to: {str(es)}", parent=self)

        lb_event_no = Label(self.card_1, text=j, font=("Times New Roman", 65, "bold"), bg="#ef255f",
                            fg="white").place(x=150, y=60)

        try:
            con = pymysql.connect(host="localhost", user="root", password="root", db="event_management", port=3307)
            cur = con.cursor()
            cur.execute("SELECT username FROM customer")
            j = 0
            row = cur.fetchall()
            if row == None:
                messagebox.showerror("Error", "No customers found", parent=self)
            else:
                for i in row:
                    j += 1
            con.close()

        except Exception as es:
            messagebox.showerror("Error", f"Error Due to: {str(es)}", parent=self)

        lb_event_no = Label(self.card_2, text=j, font=("Times New Roman", 65, "bold"), bg="#fccf4d",
                            fg="white").place(x=140, y=60)

        try:
            con = pymysql.connect(host="localhost", user="root", password="root", db="event_management", port=3307)
            cur = con.cursor()
            cur.execute("SELECT event_id FROM event_123 where event_status='Completed'")
            k = 0
            row = cur.fetchall()
            if row == None:
                messagebox.showerror("Error", "No events are completed yet", parent=self)
            else:
                for i in row:
                    k += 1
            con.close()

        except Exception as es:
            messagebox.showerror("Error", f"Error Due to: {str(es)}", parent=self)

        lb_event_no = Label(self.card_3, text=k, font=("Times New Roman", 65, "bold"), bg="#49beb7",
                            fg="white").place(x=145, y=60)

        try:
            con = pymysql.connect(host="localhost", user="root", password="root", db="event_management", port=3307)
            cur = con.cursor()
            cur.execute("SELECT theme_name from theme")
            j = 0
            row = cur.fetchall()
            if row == None:
                messagebox.showerror("Error", "No events found", parent=self)
            else:
                for i in row:
                    j += 1
            con.close()

        except Exception as es:
            messagebox.showerror("Error", f"Error Due to: {str(es)}", parent=self)

        lb_event_no = Label(self.card_4, text=j, font=("Times New Roman", 65, "bold"), bg="light green",
                            fg="white").place(x=145, y=60)

        try:
            con = pymysql.connect(host="localhost", user="root", password="root", db="event_management", port=3307)
            cur = con.cursor()
            cur.execute("SELECT theme_name from theme")
            j = 0
            row = cur.fetchall()
            if row == None:
                messagebox.showerror("Error", "No events found", parent=self)
            else:
                for i in row:
                    j += 1
            con.close()

        except Exception as es:
            messagebox.showerror("Error", f"Error Due to: {str(es)}", parent=self)

        lb_event_no = Label(self.card_4, text=j, font=("Times New Roman", 65, "bold"), bg="light green",
                            fg="white").place(x=145, y=60)

        try:
            con = pymysql.connect(host="localhost", user="root", password="root", db="event_management", port=3307)
            cur = con.cursor()
            cur.execute("SELECT req_id from user_event_request")
            j = 0
            row = cur.fetchall()
            if row == None:
                messagebox.showerror("Error", "No events found", parent=self)
            else:
                for i in row:
                    j += 1
            con.close()

        except Exception as es:
            messagebox.showerror("Error", f"Error Due to: {str(es)}", parent=self)

        lb_event_requests = Label(self.card_5, text=j, font=("Times New Roman", 65, "bold"), bg="pink",
                            fg="white").place(x=145, y=60)

        try:
            con = pymysql.connect(host="localhost", user="root", password="root", db="event_management", port=3307)
            cur = con.cursor()
            cur.execute("SELECT event_id FROM event_123 where event_status='Active'")
            k = 0
            row = cur.fetchall()
            if row == None:
                messagebox.showerror("Error", "No events are completed yet", parent=self)
            else:
                for i in row:
                    k += 1
            con.close()

        except Exception as es:
            messagebox.showerror("Error", f"Error Due to: {str(es)}", parent=self)

        lb_event_no = Label(self.card_6, text=k, font=("Times New Roman", 65, "bold"), bg="orange",
                            fg="white").place(x=145, y=60)

        # ------------------- ADMIN DASHBOARD 2-------------------- #


class Admin_Dashboard2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.controller = controller
        self.config(bg="white")  # for solid bg

        # Blue Frame
        frame_1 = Frame(self, bg="#1589FF")
        frame_1.place(x=220, y=0, width=1920, height=40)

        # Title
        title = Label(frame_1, text="Event Management System", font=("Times New Roman", 20, "bold"), bg="#1589FF",
                      fg="white").place(x=10, y=0)

        # Refresh Button
        home = Button(frame_1, cursor="hand2", command=self.refresh, text="Refresh",
                      font=("Times New Roman", 14, "bold"), bg="#1589FF", bd=0,
                      fg="white").place(x=1125, y=3)

        # Logout Button
        logout = Button(frame_1, cursor="hand2", command=lambda: controller.show_frame(Admin_Login), text="Logout",
                        font=("Times New Roman", 14, "bold"), bg="#1589FF", bd=0, fg="white").place(x=1230, y=3)

        # Dashboard
        dashboard = Label(self, text="DASHBOARD", font=("Times New Roman", 18, "bold", "underline"), bg="white",
                          fg="#08A3D2").place(x=795, y=50)

        # --Card 1--#
        self.card_1 = Frame(self, bg="#ef255f")
        self.card_1.place(x=280, y=120, width=350, height=250)
        lb_events = Label(self.card_1, text="Total Events", font=("Times New Roman", 20, "bold"), bg="#ef255f",
                          fg="white").place(x=100, y=200)
        try:
            con = pymysql.connect(host="localhost", user="root", password="root", db="event_management", port=3307)
            cur = con.cursor()
            cur.execute("SELECT event_id FROM event_123")
            j = 0
            row = cur.fetchall()
            if row == None:
                messagebox.showerror("Error", "No events found", parent=self)
            else:
                for i in row:
                    j += 1
            con.close()

        except Exception as es:
            messagebox.showerror("Error", f"Error Due to: {str(es)}", parent=self)

        lb_event_no = Label(self.card_1, text=j, font=("Times New Roman", 65, "bold"), bg="#ef255f",
                            fg="white").place(x=150, y=60)

        # --Card 2--#
        self.card_2 = Frame(self, bg="#FDD017")
        self.card_2.place(x=700, y=120, width=350, height=250)
        lb_events = Label(self.card_2, text="Users Registered", font=("Times New Roman", 20, "bold"), bg="#fccf4d",
                          fg="white").place(x=75, y=200)

        try:
            con = pymysql.connect(host="localhost", user="root", password="root", db="event_management", port=3307)
            cur = con.cursor()
            cur.execute("SELECT username FROM customer")
            j = 0
            row = cur.fetchall()
            if row == None:
                messagebox.showerror("Error", "No customers found", parent=self)
            else:
                for i in row:
                    j += 1
            con.close()

        except Exception as es:
            messagebox.showerror("Error", f"Error Due to: {str(es)}", parent=self)

        lb_event_no = Label(self.card_2, text=j, font=("Times New Roman", 65, "bold"), bg="#fccf4d",
                            fg="white").place(x=140, y=60)
        # --Card 3--#
        self.card_3 = Frame(self, bg="#49beb7")
        self.card_3.place(x=1120, y=120, width=350, height=250)  # x=1040, y=90
        lb_events = Label(self.card_3, text="Completed Events", font=("Times New Roman", 20, "bold"), bg="#49beb7",
                          fg="white").place(x=70, y=200)

        try:
            con = pymysql.connect(host="localhost", user="root", password="root", db="event_management", port=3307)
            cur = con.cursor()
            cur.execute("SELECT event_id FROM event_123 where event_status='Completed'")
            k = 0
            row = cur.fetchall()
            if row == None:
                messagebox.showerror("Error", "No events are completed yet", parent=self)
            else:
                for i in row:
                    k += 1
            con.close()

        except Exception as es:
            messagebox.showerror("Error", f"Error Due to: {str(es)}", parent=self)

        lb_event_no = Label(self.card_3, text=k, font=("Times New Roman", 65, "bold"), bg="#49beb7",
                            fg="white").place(x=145, y=60)

        # --Card 4--#
        self.card_4 = Frame(self, bg="light green")
        self.card_4.place(x=280, y=450, width=350, height=250)
        lb_events = Label(self.card_4, text="Themes", font=("Times New Roman", 20, "bold"), bg="light green",
                          fg="white").place(x=130, y=200)

        try:
            con = pymysql.connect(host="localhost", user="root", password="root", db="event_management", port=3307)
            cur = con.cursor()
            cur.execute("SELECT theme_name from theme")
            j = 0
            row = cur.fetchall()
            if row == None:
                messagebox.showerror("Error", "No events found", parent=self)
            else:
                for i in row:
                    j += 1
            con.close()

        except Exception as es:
            messagebox.showerror("Error", f"Error Due to: {str(es)}", parent=self)

        lb_event_no = Label(self.card_4, text=j, font=("Times New Roman", 65, "bold"), bg="light green",
                            fg="white").place(x=145, y=60)

        # --Card 5--#
        self.card_5 = Frame(self, bg="pink")
        self.card_5.place(x=700, y=450, width=350, height=250)
        lb_event_requests = Label(self.card_5, text="Event Requests", font=("Times New Roman", 20, "bold"), bg="pink",
                                  fg="white").place(x=90, y=200)

        try:
            con = pymysql.connect(host="localhost", user="root", password="root", db="event_management", port=3307)
            cur = con.cursor()
            cur.execute("SELECT req_id from user_event_request")
            j = 0
            row = cur.fetchall()
            if row == None:
                messagebox.showerror("Error", "No events found", parent=self)
            else:
                for i in row:
                    j += 1
            con.close()

        except Exception as es:
            messagebox.showerror("Error", f"Error Due to: {str(es)}", parent=self)

        lb_event_requests = Label(self.card_5, text=j, font=("Times New Roman", 65, "bold"), bg="pink",
                                  fg="white").place(x=145, y=60)

        # --Card 6--#
        self.card_6 = Frame(self, bg="orange")
        self.card_6.place(x=1120, y=450, width=350, height=250)
        lb_events = Label(self.card_6, text="Active Events", font=("Times New Roman", 20, "bold"), bg="orange",
                          fg="white").place(x=95, y=200)

        try:
            con = pymysql.connect(host="localhost", user="root", password="root", db="event_management", port=3307)
            cur = con.cursor()
            cur.execute("SELECT event_id FROM event_123 where event_status='Active'")
            k = 0
            row = cur.fetchall()
            if row == None:
                messagebox.showerror("Error", "No events are completed yet", parent=self)
            else:
                for i in row:
                    k += 1
            con.close()

        except Exception as es:
            messagebox.showerror("Error", f"Error Due to: {str(es)}", parent=self)

        lb_event_no = Label(self.card_6, text=k, font=("Times New Roman", 65, "bold"), bg="orange",
                            fg="white").place(x=145, y=60)

        # --GREY FRAME--#
        side_card = Frame(self, bg="#3C4248")
        side_card.place(x=0, y=0, width=225, height=1080)
        line_card = Frame(self, bg="white")
        line_card.place(x=0, y=45, width=225, height=1)

        title = Label(side_card, text="Welcome Admin", font=("Times New Roman", 20, "bold"), bg="#3C4248",
                      fg="white").place(x=10, y=0)

        # --DASHBOARD--#
        btn_dashboard = Button(side_card, text="Dashboard", command=lambda: controller.show_frame(Admin_Dashboard),
                               font=("Helvetica", 18, "bold"),
                               bg="#3C4248", fg="white", bd=0).place(x=40, y=60)  # bg="light grey"
        self.bg4 = ImageTk.PhotoImage(file="C:/Users/Swaraj/Desktop/Icons/Icons/dashboard.png")
        events_icon4 = Label(side_card, bg="#3C4248", fg="light grey", image=self.bg4).place(x=10, y=70)

        # --EVENTS--#
        lb_events_side = Label(side_card, text="Events", font=("Helvetica", 20, "bold"), bg="#3C4248",
                               fg="light grey").place(x=40, y=130)
        self.bg = ImageTk.PhotoImage(file="C:/Users/Swaraj/Desktop/Icons/Icons/calendar.png")
        events_icon = Label(side_card, bg="#3C4248", fg="light grey", image=self.bg).place(x=10, y=135)
        self.bg2 = ImageTk.PhotoImage(file="C:/Users/Swaraj/Desktop/Icons/Icons/Upward.png")
        events_icon2 = Button(side_card, bg="#3C4248", fg="light grey", bd=0, image=self.bg2, command=lambda: controller.show_frame(Admin_Dashboard)).place(x=150, y=140)

    def refresh(self):
        try:
            con = pymysql.connect(host="localhost", user="root", password="root", db="event_management", port=3307)
            cur = con.cursor()
            cur.execute("SELECT event_id FROM event_123")
            j = 0
            row = cur.fetchall()
            if row == None:
                messagebox.showerror("Error", "No events found", parent=self)
            else:
                for i in row:
                    j += 1
            con.close()
        except Exception as es:
            messagebox.showerror("Error", f"Error Due to: {str(es)}", parent=self)

        lb_event_no = Label(self.card_1, text=j, font=("Times New Roman", 65, "bold"), bg="#ef255f",
                            fg="white").place(x=150, y=60)

        try:
            con = pymysql.connect(host="localhost", user="root", password="root", db="event_management", port=3307)
            cur = con.cursor()
            cur.execute("SELECT username FROM customer")
            j = 0
            row = cur.fetchall()
            if row == None:
                messagebox.showerror("Error", "No customers found", parent=self)
            else:
                for i in row:
                    j += 1
            con.close()

        except Exception as es:
            messagebox.showerror("Error", f"Error Due to: {str(es)}", parent=self)

        lb_event_no = Label(self.card_2, text=j, font=("Times New Roman", 65, "bold"), bg="#fccf4d",
                            fg="white").place(x=140, y=60)

        try:
            con = pymysql.connect(host="localhost", user="root", password="root", db="event_management", port=3307)
            cur = con.cursor()
            cur.execute("SELECT event_id FROM event_123 where event_status='Completed'")
            k = 0
            row = cur.fetchall()
            if row == None:
                messagebox.showerror("Error", "No events are completed yet", parent=self)
            else:
                for i in row:
                    k += 1
            con.close()

        except Exception as es:
            messagebox.showerror("Error", f"Error Due to: {str(es)}", parent=self)

        lb_event_no = Label(self.card_3, text=k, font=("Times New Roman", 65, "bold"), bg="#49beb7",
                            fg="white").place(x=145, y=60)

        try:
            con = pymysql.connect(host="localhost", user="root", password="root", db="event_management", port=3307)
            cur = con.cursor()
            cur.execute("SELECT theme_name from theme")
            j = 0
            row = cur.fetchall()
            if row == None:
                messagebox.showerror("Error", "No events found", parent=self)
            else:
                for i in row:
                    j += 1
            con.close()

        except Exception as es:
            messagebox.showerror("Error", f"Error Due to: {str(es)}", parent=self)

        lb_event_no = Label(self.card_4, text=j, font=("Times New Roman", 65, "bold"), bg="light green",
                            fg="white").place(x=145, y=60)

        try:
            con = pymysql.connect(host="localhost", user="root", password="root", db="event_management", port=3307)
            cur = con.cursor()
            cur.execute("SELECT req_id from user_event_request")
            j = 0
            row = cur.fetchall()
            if row == None:
                messagebox.showerror("Error", "No events found", parent=self)
            else:
                for i in row:
                    j += 1
            con.close()

        except Exception as es:
            messagebox.showerror("Error", f"Error Due to: {str(es)}", parent=self)

        lb_event_requests = Label(self.card_5, text=j, font=("Times New Roman", 65, "bold"), bg="pink",
                            fg="white").place(x=145, y=60)

        try:
            con = pymysql.connect(host="localhost", user="root", password="root", db="event_management", port=3307)
            cur = con.cursor()
            cur.execute("SELECT event_id FROM event_123 where event_status='Active'")
            k = 0
            row = cur.fetchall()
            if row == None:
                messagebox.showerror("Error", "No events are completed yet", parent=self)
            else:
                for i in row:
                    k += 1
            con.close()

        except Exception as es:
            messagebox.showerror("Error", f"Error Due to: {str(es)}", parent=self)

        lb_event_no = Label(self.card_6, text=k, font=("Times New Roman", 65, "bold"), bg="orange",
                            fg="white").place(x=145, y=60)

        # ------------------- ADMIN CREATE THEME-------------------- #


class Admin_Theme(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.controller = controller
        self.config(bg="#F6F7F7")  # for solid bg

        # Blue Frame
        frame_1 = Frame(self, bg="#1589FF")
        frame_1.place(x=220, y=0, width=1920, height=40)

        # Title
        title = Label(frame_1, text="Event Management System", font=("Times New Roman", 20, "bold"), bg="#1589FF",
                      fg="white").place(x=10, y=0)

        # Refresh Button
        home = Button(frame_1, cursor="hand2", command=self.refresh, text="Refresh",
                      font=("Times New Roman", 14, "bold"), bg="#1589FF", bd=0,
                      fg="white").place(x=1125, y=3)

        # Logout Button
        logout = Button(frame_1, cursor="hand2", command=lambda: controller.show_frame(Admin_Login), text="Logout",
                        font=("Times New Roman", 14, "bold"), bg="#1589FF", bd=0, fg="white").place(x=1230, y=3)

        # --GREY FRAME--#
        side_card = Frame(self, bg="#3C4248")
        side_card.place(x=0, y=0, width=225, height=1080)
        line_card = Frame(self, bg="white")
        line_card.place(x=0, y=45, width=225, height=1)
        title = Label(side_card, text="Welcome Admin", font=("Times New Roman", 20, "bold"), bg="#3C4248",
                      fg="white").place(x=10, y=0)

        # --DASHBOARD--#
        btn_dashboard = Button(side_card, text="Dashboard", command=lambda: controller.show_frame(Admin_Dashboard),
                               font=("Helvetica", 18, "bold"),
                               bg="#3C4248", fg="white", bd=0).place(x=40, y=60)  # bg="light grey"
        self.bg4 = ImageTk.PhotoImage(file="C:/Users/Swaraj/Desktop/Icons/Icons/dashboard.png")
        events_icon4 = Label(side_card, bg="#3C4248", fg="light grey", image=self.bg4).place(x=10, y=70)

        # --EVENTS--#
        lb_events_side = Label(side_card, text="Events", font=("Helvetica", 20, "bold"), bg="#3C4248",
                               fg="light grey").place(x=40, y=130)
        self.bg = ImageTk.PhotoImage(file="C:/Users/Swaraj/Desktop/Icons/Icons/calendar.png")
        events_icon = Label(side_card, bg="#3C4248", fg="light grey", image=self.bg).place(x=10, y=135)
        self.bg2 = ImageTk.PhotoImage(file="C:/Users/Swaraj/Desktop/Icons/Icons/right-arrow.png")
        events_icon2 = Label(side_card, bg="#3C4248", fg="light grey", image=self.bg2).place(x=150, y=140)

        # --CREATE EVENT--#
        btn_events_create = Button(side_card, text="Create Events", command=lambda: controller.show_frame(Admin_CreateEvent), font=("Helvetica", 18, "bold"), bg="#3C4248",
                                   fg="white", bd=0).place(x=35, y=170)  # bg="light grey"
        self.bg3 = ImageTk.PhotoImage(file="C:/Users/Swaraj/Desktop/Icons/Icons/calendar_add.png")
        events_icon3 = Label(side_card, bg="#3C4248", fg="light grey", image=self.bg3).place(x=10, y=180)

        # --CREATE THEME--#
        btn_theme_create = Button(side_card, text="Create Theme", command=lambda: controller.show_frame(Admin_Theme),
                                  font=("Helvetica", 18, "bold"), bg="#3C4248", fg="white", bd=0).place(x=35, y=215)
        self.bg8 = ImageTk.PhotoImage(file="C:/Users/Swaraj/Desktop/Icons/Icons/12.png")
        events_icon3 = Label(side_card, bg="#3C4248", fg="light grey", image=self.bg8).place(x=10, y=225)

        # --MODIFY EVENT--#
        btn_events_mod = Button(side_card, text="Modify Event", command=lambda: controller.show_frame(Admin_ModifyEvent), font=("Helvetica", 18, "bold"),
                                bg="#3C4248", fg="white", bd=0).place(x=35, y=260)  # bg="light grey"
        self.bg5 = ImageTk.PhotoImage(file="C:/Users/Swaraj/Desktop/Icons/Icons/calendar_mod.png")
        events_icon5 = Label(side_card, bg="#3C4248", fg="light grey", image=self.bg5).place(x=10, y=270)

        # --EVENT REQUESTS--#
        btn_events_request = Button(side_card, text="Event Requests", font=("Helvetica", 18, "bold"), command=lambda: controller.show_frame(Admin_EventRequest),
                                    bg="#3C4248", fg="white", bd=0).place(x=35, y=305)  # bg="light grey"
        self.bg6 = ImageTk.PhotoImage(file="C:/Users/Swaraj/Desktop/Icons/Icons/calendar_notification.png")
        events_icon6 = Label(side_card, bg="#3C4248", fg="light grey", image=self.bg6).place(x=10, y=315)

        # --EVENT LIST--#
        btn_events_list = Button(side_card, text="Event List", font=("Helvetica", 18, "bold"), command=lambda: controller.show_frame(Admin_EventList),
                                 bg="#3C4248", fg="white", bd=0).place(x=35, y=350)  # bg="light grey"
        self.bg7 = ImageTk.PhotoImage(file="C:/Users/Swaraj/Desktop/Icons/Icons/list.png")
        events_icon7 = Label(side_card, bg="#3C4248", fg="light grey", image=self.bg7).place(x=10, y=360)

        # --User Feedback--#
        btn_user_feedback = Button(side_card, text="User Feedback", font=("Helvetica", 18, "bold"),
                                   command=lambda: controller.show_frame(Admin_User_Feedback),
                                   bg="#3C4248", fg="white", bd=0).place(x=35, y=393)  # bg="light grey"
        self.bg9 = ImageTk.PhotoImage(file="C:/Users/Swaraj/Desktop/Icons/Icons/feedback.png")
        events_icon9 = Label(side_card, bg="#3C4248", fg="light grey", image=self.bg9).place(x=7, y=400)

        # --Registered Users--#
        btn_registered_user = Button(side_card, text="Reg. Users", font=("Helvetica", 18, "bold"),
                                     command=lambda: controller.show_frame(Admin_Registered_Users),
                                     bg="#3C4248", fg="white", bd=0).place(x=35, y=435)  # bg="light grey"
        self.bg10 = ImageTk.PhotoImage(file="C:/Users/Swaraj/Desktop/Icons/Icons/reg_users.png")
        events_icon10 = Label(side_card, bg="#3C4248", fg="light grey", image=self.bg10).place(x=9, y=442)

        # WHITE FRAME
        theme_frame = Frame(self, bg="white")
        theme_frame.place(x=475, y=150, width=800, height=500)

        # Title
        title = Label(theme_frame, text="CREATE THEME", font=("Times New Roman", 25, "bold", "underline"), bg="white",
                      fg="#08A3D2").place(x=20, y=20)

        # --NAME--#
        theme_name = Label(theme_frame, text="Name:", font=("Times New Roman", 18, "bold"), bg="white",
                         fg="#2C3539").place(x=78, y=100)
        self.txt_theme_name = Entry(theme_frame, relief="solid", font=("Times New Roman", 18), bg="lightgray")
        self.txt_theme_name.place(x=160, y=100, width=350, height=35)

        # --DESCRIPTION--#
        theme_description = Label(theme_frame, text="Description:", font=("Times New Roman", 18, "bold"), bg="white",
                      fg="#2C3539").place(x=20, y=160)
        self.theme_description = Text(theme_frame, relief="solid", font=("Times New Roman", 18), bg="lightgray")
        self.theme_description.place(x=160, y=160, width=350, height=150)

        # --CREATE BUTTON--#
        btn_create = Button(theme_frame, text="Create", command=self.theme, font=("Times New Roman", 20, "bold"),
                           fg="white", bg="#B00857", cursor="hand2").place(x=160, y=350, width=180, height=40)

    def clear(self):
        self.txt_theme_name.delete(0, END)
        self.theme_description.delete(1.0, END)

    def theme(self):
        if self.txt_theme_name.get() == "" or self.theme_description.get(1.0, END) == "":
            messagebox.showerror("Error", "All Fields are Required", parent=self)
        else:
            try:
                con = pymysql.connect(host="localhost", user="root", password="root", db="event_management",
                                      port=3307)
                cur = con.cursor()
                cur.execute(
                    "INSERT INTO THEME (theme_name,theme_description) values(%s,%s)",
                    (
                        self.txt_theme_name.get(),
                        self.theme_description.get(1.0, END)
                    ))
                con.commit()

                messagebox.showinfo("Alert", "Theme Created Successfully", parent=self)

                self.clear()
                self.controller.show_frame(Admin_Theme)
                con.close()

            except Exception as es:
                messagebox.showerror("Error", f"Error Due to: {str(es)}", parent=self)

    def refresh(self):
        self.txt_theme_name.delete(0, END)
        self.theme_description.delete(1.0, END)

        # ------------------- ADMIN CREATE THEME-------------------- #


class Admin_CreateEvent(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.controller = controller
        self.config(bg="#F6F7F7")  # for solid bg

        # Blue Frame
        frame_1 = Frame(self, bg="#1589FF")
        frame_1.place(x=220, y=0, width=1920, height=40)

        # Title
        title = Label(frame_1, text="Event Management System", font=("Times New Roman", 20, "bold"), bg="#1589FF",
                      fg="white").place(x=10, y=0)

        # Refresh Button
        home = Button(frame_1, cursor="hand2", command=self.refresh, text="Refresh",
                      font=("Times New Roman", 14, "bold"), bg="#1589FF", bd=0,
                      fg="white").place(x=1125, y=3)

        # Logout Button
        logout = Button(frame_1, cursor="hand2", command=lambda: controller.show_frame(Admin_Login), text="Logout",
                        font=("Times New Roman", 14, "bold"), bg="#1589FF", bd=0, fg="white").place(x=1230, y=3)

        # --GREY FRAME--#
        side_card = Frame(self, bg="#3C4248")
        side_card.place(x=0, y=0, width=225, height=1080)
        line_card = Frame(self, bg="white")
        line_card.place(x=0, y=45, width=225, height=1)
        title = Label(side_card, text="Welcome Admin", font=("Times New Roman", 20, "bold"), bg="#3C4248",
                      fg="white").place(x=10, y=0)

        # --DASHBOARD--#
        btn_dashboard = Button(side_card, text="Dashboard", command=lambda: controller.show_frame(Admin_Dashboard),
                               font=("Helvetica", 18, "bold"),
                               bg="#3C4248", fg="white", bd=0).place(x=40, y=60)  # bg="light grey"
        self.bg4 = ImageTk.PhotoImage(file="C:/Users/Swaraj/Desktop/Icons/Icons/dashboard.png")
        events_icon4 = Label(side_card, bg="#3C4248", fg="light grey", image=self.bg4).place(x=10, y=70)

        # --EVENTS--#
        lb_events_side = Label(side_card, text="Events", font=("Helvetica", 20, "bold"), bg="#3C4248",
                               fg="light grey").place(x=40, y=130)
        self.bg = ImageTk.PhotoImage(file="C:/Users/Swaraj/Desktop/Icons/Icons/calendar.png")
        events_icon = Label(side_card, bg="#3C4248", fg="light grey", image=self.bg).place(x=10, y=135)
        self.bg2 = ImageTk.PhotoImage(file="C:/Users/Swaraj/Desktop/Icons/Icons/right-arrow.png")
        events_icon2 = Label(side_card, bg="#3C4248", fg="light grey", image=self.bg2).place(x=150, y=140)

        # --CREATE EVENT--#
        btn_events_create = Button(side_card, text="Create Events", command=lambda: controller.show_frame(Admin_CreateEvent), font=("Helvetica", 18, "bold"), bg="#3C4248",
                                   fg="white", bd=0).place(x=35, y=170)  # bg="light grey"
        self.bg3 = ImageTk.PhotoImage(file="C:/Users/Swaraj/Desktop/Icons/Icons/calendar_add.png")
        events_icon3 = Label(side_card, bg="#3C4248", fg="light grey", image=self.bg3).place(x=10, y=180)

        # --CREATE THEME--#
        btn_theme_create = Button(side_card, text="Create Theme", command=lambda: controller.show_frame(Admin_Theme),
                                  font=("Helvetica", 18, "bold"), bg="#3C4248", fg="white", bd=0).place(x=35, y=215)
        self.bg8 = ImageTk.PhotoImage(file="C:/Users/Swaraj/Desktop/Icons/Icons/12.png")
        events_icon3 = Label(side_card, bg="#3C4248", fg="light grey", image=self.bg8).place(x=10, y=225)

        # --MODIFY EVENT--#
        btn_events_mod = Button(side_card, text="Modify Event", command=lambda: controller.show_frame(Admin_ModifyEvent), font=("Helvetica", 18, "bold"),
                                bg="#3C4248", fg="white", bd=0).place(x=35, y=260)  # bg="light grey"
        self.bg5 = ImageTk.PhotoImage(file="C:/Users/Swaraj/Desktop/Icons/Icons/calendar_mod.png")
        events_icon5 = Label(side_card, bg="#3C4248", fg="light grey", image=self.bg5).place(x=10, y=270)

        # --EVENT REQUESTS--#
        btn_events_request = Button(side_card, text="Event Requests", font=("Helvetica", 18, "bold"), command=lambda: controller.show_frame(Admin_EventRequest),
                                    bg="#3C4248", fg="white", bd=0).place(x=35, y=305)  # bg="light grey"
        self.bg6 = ImageTk.PhotoImage(file="C:/Users/Swaraj/Desktop/Icons/Icons/calendar_notification.png")
        events_icon6 = Label(side_card, bg="#3C4248", fg="light grey", image=self.bg6).place(x=10, y=315)

        # --EVENT LIST--#
        btn_events_list = Button(side_card, text="Event List", font=("Helvetica", 18, "bold"), command=lambda: controller.show_frame(Admin_EventList),
                                 bg="#3C4248", fg="white", bd=0).place(x=35, y=350)  # bg="light grey"
        self.bg7 = ImageTk.PhotoImage(file="C:/Users/Swaraj/Desktop/Icons/Icons/list.png")
        events_icon7 = Label(side_card, bg="#3C4248", fg="light grey", image=self.bg7).place(x=10, y=360)

        # --User Feedback--#
        btn_user_feedback = Button(side_card, text="User Feedback", font=("Helvetica", 18, "bold"),
                                   command=lambda: controller.show_frame(Admin_User_Feedback),
                                   bg="#3C4248", fg="white", bd=0).place(x=35, y=393)  # bg="light grey"
        self.bg9 = ImageTk.PhotoImage(file="C:/Users/Swaraj/Desktop/Icons/Icons/feedback.png")
        events_icon9 = Label(side_card, bg="#3C4248", fg="light grey", image=self.bg9).place(x=7, y=400)

        # --Registered Users--#
        btn_registered_user = Button(side_card, text="Reg. Users", font=("Helvetica", 18, "bold"),
                                     command=lambda: controller.show_frame(Admin_Registered_Users),
                                     bg="#3C4248", fg="white", bd=0).place(x=35, y=435)  # bg="light grey"
        self.bg10 = ImageTk.PhotoImage(file="C:/Users/Swaraj/Desktop/Icons/Icons/reg_users.png")
        events_icon10 = Label(side_card, bg="#3C4248", fg="light grey", image=self.bg10).place(x=9, y=442)

        # WHITE FRAME
        self.event_frame = Frame(self, bg="white")
        self.event_frame.place(x=370, y=85, width=1000, height=700)

        # Title
        title = Label(self.event_frame, text="CREATE EVENT", font=("Times New Roman", 25, "bold", "underline"), bg="white",
                      fg="#08A3D2").place(x=20, y=20)

        # Request ID
        request_id = Label(self.event_frame, text="Request ID:", font=("Times New Roman", 18, "bold"), bg="white",
                           fg="#2C3539").place(x=750, y=20)
        self.txt_request_id = Entry(self.event_frame, relief="solid", font=("Times New Roman", 18), bg="lightgray")
        self.txt_request_id.place(x=880, y=20, width=60, height=35)
        self.insert = ImageTk.PhotoImage(file="C:/Users/Swaraj/Desktop/Icons/Icons/insert.png")
        events_insert = Button(self.event_frame, command = self.insert2,bg="white", bd=0, fg="light grey", image=self.insert).place(x=950, y=20, width=25, height=30)

        # --Unique ID--#
        event_id = Label(self.event_frame, text="Event ID:", font=("Times New Roman", 18, "bold"), bg="white",
                           fg="#2C3539").place(x=63, y=100)
        self.txt_event_id = Entry(self.event_frame, relief="solid", font=("Times New Roman", 18), bg="lightgray")
        self.txt_event_id.place(x=180, y=100, width=50, height=35)

        # --Event Theme--#
        self.click = StringVar()
        try:
            con = pymysql.connect(host="localhost", user="root", password="root", db="event_management", port=3307)
            cur = con.cursor()
            cur.execute("SELECT THEME_NAME FROM THEME")
            lst = ["Select"]
            row = cur.fetchall()
            if row == None:
                messagebox.showerror("Error", "No Themes available", parent=self)

            else:
                for i in row:
                    if i not in lst:
                        lst.append(i)
            con.close()

        except Exception as es:
            messagebox.showerror("Error", f"Error Due to: {str(es)}", parent=self)

        status = Label(self.event_frame, text="Event Theme:", font=("Times New Roman", 18, "bold"), bg="white", fg = "#2C3539").place(x=525, y=100)
        self.click.set("Select")
        self.txt_theme = OptionMenu(self.event_frame, self.click, *lst)
        self.txt_theme.place(x=675, y=100, width=120, height=35)

        # --NAME--#
        event_name = Label(self.event_frame, text="Event Name:", font=("Times New Roman", 18, "bold"), bg="white", fg="#2C3539").place(x=30, y=160)
        self.txt_event_name = Entry(self.event_frame, relief="solid", font=("Times New Roman", 18), bg="lightgray")
        self.txt_event_name.place(x=180, y=160, width=320, height=35)

        # --DATE OF EVENT--#
        # --PLACEHOLDER--#
        def focus(event):
            temp3 = self.focus_get()
            widget2 = str(temp3)

            if widget2 == ".!frame.!admin_createevent.!frame4.!entry4" and self.txt_date_event.get() == "DD/MM/YYYY":
                temp3.delete(0, END)
            if widget2 != ".!frame.!admin_createevent.!frame4.!entry4" and self.txt_date_event.get() == "":
                self.txt_date_event.insert(END, "DD/MM/YYYY")
            if widget2 == ".!frame.!admin_createevent.!frame4.!entry6" and self.txt_start_time.get() == "HH:MM":
                temp3.delete(0, END)
            if widget2 != ".!frame.!admin_createevent.!frame4.!entry6" and self.txt_start_time.get() == "":
                self.txt_start_time.insert(END, "HH:MM")
            if widget2 == ".!frame.!admin_createevent.!frame4.!entry7" and self.txt_end_time.get() == "HH:MM":
                temp3.delete(0, END)
            if widget2 != ".!frame.!admin_createevent.!frame4.!entry7" and self.txt_end_time.get() == "":
                self.txt_end_time.insert(END, "HH:MM")

        # getting the field
        self.bind_all("<Button-1>", lambda k: focus(k))

        date_event = Label(self.event_frame, text="Date of Event:", font=("Times New Roman", 18, "bold"), bg="white",
                           fg="#2C3539").place(x=525, y=160)
        self.txt_date_event = Entry(self.event_frame, relief="solid", font=("Times New Roman", 18), bg="lightgray", fg="grey")
        self.txt_date_event.place(x=678, y=160, width=175, height=35)
        self.txt_date_event.insert(END, "DD/MM/YYYY")

        # --DURATION--#
        event_duration = Label(self.event_frame, text="Duration:", font=("Times New Roman", 18, "bold"), bg="white",
                           fg="#2C3539").place(x=527, y=220)
        self.txt_event_duration = Entry(self.event_frame, relief="solid", font=("Times New Roman", 18), bg="lightgray")
        self.txt_event_duration.place(x=635, y=220, width=50, height=35)
        event_duration_days = Label(self.event_frame, text="day(s)", font=("Times New Roman", 18, "bold"), bg="white",
                               fg="#2C3539").place(x=690, y=220)

        # --TIMING--#
        start_time = Label(self.event_frame, text="Timing:", font=("Times New Roman", 18, "bold"), bg="white",
                           fg="#2C3539").place(x=85, y=220)
        self.txt_start_time = Entry(self.event_frame, relief="solid", font=("Times New Roman", 18), bg="lightgray", fg="grey")
        self.txt_start_time.place(x=180, y=220, width=110, height=35)
        self.txt_start_time.insert(END, "HH:MM")

        end_time = Label(self.event_frame, text="--", font=("Times New Roman", 18, "bold"), bg="white",
                           fg="#2C3539").place(x=295, y=220)
        self.txt_end_time = Entry(self.event_frame, relief="solid", font=("Times New Roman", 18), bg="lightgray", fg="grey")
        self.txt_end_time.place(x=325, y=220, width=110, height=35)
        self.txt_end_time.insert(END, "HH:MM")

        # --Maximum Guest--#
        max_guest = Label(self.event_frame, text="Max. Guest:", font=("Times New Roman", 18, "bold"), bg="white",
                           fg="#2C3539").place(x=40, y=280)
        self.txt_max_guest = Entry(self.event_frame, relief="solid", font=("Times New Roman", 18), bg="lightgray")
        self.txt_max_guest.place(x=180, y=280, width=175, height=35)

        # --Venue--#
        venue = Label(self.event_frame, text="Venue:", font=("Times New Roman", 18, "bold"), bg="white",
                          fg="#2C3539").place(x=92, y=340)
        self.txt_venue = Entry(self.event_frame, relief="solid", font=("Times New Roman", 18), bg="lightgray")
        self.txt_venue.place(x=180, y=340, width=250, height=35)

        # --Contact No--#
        contact_no = Label(self.event_frame, text="Contact No.:", font=("Times New Roman", 18, "bold"), bg="white",
                      fg="#2C3539").place(x=33, y=400)
        self.txt_contact_no = Entry(self.event_frame, relief="solid", font=("Times New Roman", 18), bg="lightgray")
        self.txt_contact_no.place(x=180, y=400, width=150, height=35)

        # --Event Fees--#
        event_fees = Label(self.event_frame, text="Event Fees: ₹", font=("Times New Roman", 18, "bold"), bg="white",
                      fg="#2C3539").place(x=540, y=400)
        self.txt_event_fees = Entry(self.event_frame, relief="solid", font=("Times New Roman", 18), bg="lightgray")
        self.txt_event_fees.place(x=690, y=400, width=100, height=35)

        # --DESCRIPTION--#
        event_description = Label(self.event_frame, text="Description:", font=("Times New Roman", 18, "bold"), bg="white",
                                  fg="#2C3539").place(x=37, y=460)
        self.event_description = Text(self.event_frame, relief="solid", font=("Times New Roman", 18), bg="lightgray")
        self.event_description.place(x=180, y=460, width=250, height=150)

        # --Status--#
        self.clicked = StringVar()
        options = ["Select", "Pending", "Limit Reached", "Active", "Cancelled", "Completed"]
        status = Label(self.event_frame, text="Status:", font=("Times New Roman", 18, "bold"), bg="white",
                           fg="#2C3539").place(x=540, y=460)
        self.clicked.set("Select")
        self.txt_status = OptionMenu(self.event_frame, self.clicked, *options)
        self.txt_status.place(x=620, y=460, width=120, height=35)

        # --CREATE BUTTON--#
        btn_create = Button(self.event_frame, text="Create", command=self.event, font=("Times New Roman", 20, "bold"),
                            fg="white", bg="#B00857", cursor="hand2").place(x=400, y=635, width=180, height=40)

    def clear(self):
        self.txt_event_id.delete(0, END)
        self.txt_event_name.delete(0, END)
        self.txt_date_event.delete(0, END)
        self.txt_event_duration.delete(0, END)
        self.txt_start_time.delete(0, END)
        self.txt_end_time.delete(0, END)
        self.txt_max_guest.delete(0, END)
        self.txt_venue.delete(0, END)
        self.txt_contact_no.delete(0, END)
        self.event_description.delete(1.0, END)
        self.txt_event_fees.delete(0, END)
        self.clicked.set("Select")
        self.click.set("Select")

    def event(self):
        if self.txt_event_id.get() == "" or self.txt_event_name.get() == "" or self.txt_date_event.get() == "" or self.txt_event_duration.get() == "" or self.txt_start_time.get() == "" or self.txt_end_time.get() == "" or self.txt_max_guest.get() == "" or self.txt_venue.get() == "" or self.txt_contact_no.get() == "" or self.event_description.get(1.0, END) == "" or self.txt_event_fees.get() == "":
            messagebox.showerror("Error", "All Fields are Required", parent=self)

        elif self.clicked.get() == "Select":
            messagebox.showerror("Error", "Select Status field", parent=self)

        elif self.click.get() == "Select":
            messagebox.showerror("Error", "Select Theme field", parent=self)

        else:
            try:
                con = pymysql.connect(host="localhost", user="root", password="root", db="event_management", port=3307)
                cur = con.cursor()
                a = self.click.get()
                temp = a[2:-3]
                cur.execute(
                    "INSERT INTO EVENT_123 (event_id, event_name, event_date, event_duration, start_time, end_time, max_guest, venue, contact_no, event_fees, event_description, event_status, theme_name) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                    (
                        self.txt_event_id.get(),
                        self.txt_event_name.get(),
                        self.txt_date_event.get(),
                        self.txt_event_duration.get(),
                        self.txt_start_time.get(),
                        self.txt_end_time.get(),
                        self.txt_max_guest.get(),
                        self.txt_venue.get(),
                        self.txt_contact_no.get(),
                        self.txt_event_fees.get(),
                        self.event_description.get(1.0, END),
                        self.clicked.get(),
                        temp
                        ))

                con.commit()

                messagebox.showinfo("Alert", "Event Created Successfully", parent=self)

                self.clear()
                self.txt_request_id.delete(0, END)
                self.controller.show_frame(Admin_CreateEvent)
                con.close()

            except Exception as es:
                messagebox.showerror("Error", f"Error Due to: {str(es)}", parent=self)

    def insert2(self):
        #self.click = StringVar()
        try:
            con = pymysql.connect(host="localhost", user="root", password="root", db="event_management", port=3307)
            cur = con.cursor()
            cur.execute("SELECT * from user_event_request where req_id=%s",
                        (
                            self.txt_request_id.get()
                        ))
            lst = []
            row = cur.fetchall()
            if row == None:
                messagebox.showerror("Error", "Invalid USERNAME or PASSWORD", parent=self)

            else:
                for i in row:
                    lst.append(i)
                #print(lst[0])
            con.close()
            self.clear()
            self.txt_date_event.delete(0, END)
            self.txt_start_time.delete(0, END)
            self.txt_end_time.delete(0, END)
            self.txt_event_name.insert(END, lst[0][1])
            self.txt_date_event.insert(END, lst[0][2])
            self.txt_event_duration.insert(END, lst[0][5])
            self.txt_start_time.insert(END, lst[0][3])
            self.txt_end_time.insert(END, lst[0][4])
            self.txt_max_guest.insert(END, lst[0][6])
            self.txt_venue.insert(END, lst[0][7])
            self.txt_contact_no.insert(END, lst[0][8])
            self.event_description.insert(END, lst[0][9])
            self.clicked.set("Pending")

        except Exception as es:
            messagebox.showerror("Error", f"Error Due to: {str(es)}", parent=self)

    def refresh(self):
        # --Event Theme--#
        self.click = StringVar()
        try:
            con = pymysql.connect(host="localhost", user="root", password="root", db="event_management", port=3307)
            cur = con.cursor()
            cur.execute("SELECT THEME_NAME FROM THEME")
            # (self.txt_username.get(), self.txt_pass_.get()))
            lst = ["Select"]
            row = cur.fetchall()
            if row == None:
                messagebox.showerror("Error", "Invalid USERNAME or PASSWORD", parent=self)

            else:
                for i in row:
                    lst.append(i)
            con.close()

        except Exception as es:
            messagebox.showerror("Error", f"Error Due to: {str(es)}", parent=self)

        status = Label(self.event_frame, text="Event Theme:", font=("Times New Roman", 18, "bold"), bg="white",
                       fg="#2C3539").place(x=525, y=100)
        self.click.set("Select")
        self.txt_status = OptionMenu(self.event_frame, self.click, *lst)
        self.txt_status.place(x=675, y=100, width=120, height=35)

        self.txt_event_id.delete(0, END)
        self.txt_event_name.delete(0, END)
        self.txt_date_event.delete(0, END)
        self.txt_event_duration.delete(0, END)
        self.txt_start_time.delete(0, END)
        self.txt_end_time.delete(0, END)
        self.txt_max_guest.delete(0, END)
        self.txt_venue.delete(0, END)
        self.txt_contact_no.delete(0, END)
        self.event_description.delete(1.0, END)
        self.txt_event_fees.delete(0, END)
        self.txt_request_id.delete(0, END)
        self.clicked.set("Select")
        self.click.set("Select")

        self.txt_start_time.insert(END, "HH:MM")
        self.txt_end_time.insert(END, "HH:MM")
        self.txt_date_event.insert(END, "DD/MM/YYYY")

        # ------------------- ADMIN MODIFY EVENT-------------------- #


class Admin_ModifyEvent(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.controller = controller
        self.config(bg="#F6F7F7")  # for solid bg

        # Blue Frame
        frame_1 = Frame(self, bg="#1589FF")
        frame_1.place(x=220, y=0, width=1920, height=40)

        # Title
        title = Label(frame_1, text="Event Management System", font=("Times New Roman", 20, "bold"), bg="#1589FF",
                      fg="white").place(x=10, y=0)

        # Refresh Button
        home = Button(frame_1, cursor="hand2", command=self.refresh, text="Refresh",
                      font=("Times New Roman", 14, "bold"), bg="#1589FF", bd=0,
                      fg="white").place(x=1125, y=3)

        # Logout Button
        logout = Button(frame_1, cursor="hand2", command=lambda: controller.show_frame(Admin_Login), text="Logout",
                        font=("Times New Roman", 14, "bold"), bg="#1589FF", bd=0, fg="white").place(x=1230, y=3)

        # --GREY FRAME--#
        side_card = Frame(self, bg="#3C4248")
        side_card.place(x=0, y=0, width=225, height=1080)
        line_card = Frame(self, bg="white")
        line_card.place(x=0, y=45, width=225, height=1)

        title = Label(side_card, text="Welcome Admin", font=("Times New Roman", 20, "bold"), bg="#3C4248",
                      fg="white").place(x=10, y=0)

        # --DASHBOARD--#
        btn_dashboard = Button(side_card, text="Dashboard", command=lambda: controller.show_frame(Admin_Dashboard),
                               font=("Helvetica", 18, "bold"),
                               bg="#3C4248", fg="white", bd=0).place(x=40, y=60)  # bg="light grey"
        self.bg4 = ImageTk.PhotoImage(file="C:/Users/Swaraj/Desktop/Icons/Icons/dashboard.png")
        events_icon4 = Label(side_card, bg="#3C4248", fg="light grey", image=self.bg4).place(x=10, y=70)

        # --EVENTS--#
        lb_events_side = Label(side_card, text="Events", font=("Helvetica", 20, "bold"), bg="#3C4248",
                               fg="light grey").place(x=40, y=130)
        self.bg = ImageTk.PhotoImage(file="C:/Users/Swaraj/Desktop/Icons/Icons/calendar.png")
        events_icon = Label(side_card, bg="#3C4248", fg="light grey", image=self.bg).place(x=10, y=135)
        self.bg2 = ImageTk.PhotoImage(file="C:/Users/Swaraj/Desktop/Icons/Icons/right-arrow.png")
        events_icon2 = Label(side_card, bg="#3C4248", fg="light grey", image=self.bg2).place(x=150, y=140)

        # --CREATE EVENT--#
        btn_events_create = Button(side_card, text="Create Events",
                                   command=lambda: controller.show_frame(Admin_CreateEvent),
                                   font=("Helvetica", 18, "bold"), bg="#3C4248",
                                   fg="white", bd=0).place(x=35, y=170)  # bg="light grey"
        self.bg3 = ImageTk.PhotoImage(file="C:/Users/Swaraj/Desktop/Icons/Icons/calendar_add.png")
        events_icon3 = Label(side_card, bg="#3C4248", fg="light grey", image=self.bg3).place(x=10, y=180)

        # --CREATE THEME--#
        btn_theme_create = Button(side_card, text="Create Theme", command=lambda: controller.show_frame(Admin_Theme),
                                  font=("Helvetica", 18, "bold"), bg="#3C4248", fg="white", bd=0).place(x=35, y=215)
        self.bg8 = ImageTk.PhotoImage(file="C:/Users/Swaraj/Desktop/Icons/Icons/12.png")
        events_icon3 = Label(side_card, bg="#3C4248", fg="light grey", image=self.bg8).place(x=10, y=225)

        # --MODIFY EVENT--#
        btn_events_mod = Button(side_card, text="Modify Event", command=lambda: controller.show_frame(Admin_ModifyEvent), font=("Helvetica", 18, "bold"),
                                bg="#3C4248", fg="white", bd=0).place(x=35, y=260)  # bg="light grey"
        self.bg5 = ImageTk.PhotoImage(file="C:/Users/Swaraj/Desktop/Icons/Icons/calendar_mod.png")
        events_icon5 = Label(side_card, bg="#3C4248", fg="light grey", image=self.bg5).place(x=10, y=270)

        # --EVENT REQUESTS--#
        btn_events_request = Button(side_card, text="Event Requests", font=("Helvetica", 18, "bold"), command=lambda: controller.show_frame(Admin_EventRequest),
                                    bg="#3C4248", fg="white", bd=0).place(x=35, y=305)  # bg="light grey"
        self.bg6 = ImageTk.PhotoImage(file="C:/Users/Swaraj/Desktop/Icons/Icons/calendar_notification.png")
        events_icon6 = Label(side_card, bg="#3C4248", fg="light grey", image=self.bg6).place(x=10, y=315)

        # --EVENT LIST--#
        btn_events_list = Button(side_card, text="Event List", font=("Helvetica", 18, "bold"), command=lambda: controller.show_frame(Admin_EventList),
                                 bg="#3C4248", fg="white", bd=0).place(x=35, y=350)  # bg="light grey"
        self.bg7 = ImageTk.PhotoImage(file="C:/Users/Swaraj/Desktop/Icons/Icons/list.png")
        events_icon7 = Label(side_card, bg="#3C4248", fg="light grey", image=self.bg7).place(x=10, y=360)

        # --User Feedback--#
        btn_user_feedback = Button(side_card, text="User Feedback", font=("Helvetica", 18, "bold"),
                                   command=lambda: controller.show_frame(Admin_User_Feedback),
                                   bg="#3C4248", fg="white", bd=0).place(x=35, y=393)  # bg="light grey"
        self.bg9 = ImageTk.PhotoImage(file="C:/Users/Swaraj/Desktop/Icons/Icons/feedback.png")
        events_icon9 = Label(side_card, bg="#3C4248", fg="light grey", image=self.bg9).place(x=7, y=400)

        # --Registered Users--#
        btn_registered_user = Button(side_card, text="Reg. Users", font=("Helvetica", 18, "bold"),
                                     command=lambda: controller.show_frame(Admin_Registered_Users),
                                     bg="#3C4248", fg="white", bd=0).place(x=35, y=435)  # bg="light grey"
        self.bg10 = ImageTk.PhotoImage(file="C:/Users/Swaraj/Desktop/Icons/Icons/reg_users.png")
        events_icon10 = Label(side_card, bg="#3C4248", fg="light grey", image=self.bg10).place(x=9, y=442)

        # WHITE FRAME
        self.event_frame = Frame(self, bg="white")
        self.event_frame.place(x=370, y=85, width=1000, height=700)

        # Title
        title = Label(self.event_frame, text="MODIFY EVENT", font=("Times New Roman", 25, "bold", "underline"), bg="white",
                      fg="#08A3D2").place(x=20, y=20)

        # --Unique ID--#
        event_id = Label(self.event_frame, text="Event ID:", font=("Times New Roman", 18, "bold"), bg="white",
                         fg="#2C3539").place(x=63, y=100)
        self.txt_event_id = Entry(self.event_frame, relief="solid", font=("Times New Roman", 18), bg="lightgray")
        self.txt_event_id.place(x=180, y=100, width=50, height=35)

        self.search = ImageTk.PhotoImage(file="C:/Users/Swaraj/Desktop/Icons/Icons/Search.png")
        events_search = Button(self.event_frame, bg="white",bd=0, command=self.search2, fg="light grey", image=self.search).place(x=245, y=98, width=25, height=33)

        # --Event Theme--#
        self.click = StringVar()
        try:
            con = pymysql.connect(host="localhost", user="root", password="root", db="event_management", port=3307)
            cur = con.cursor()
            cur.execute("SELECT THEME_NAME FROM THEME")
            lst = ["Select"]
            row = cur.fetchall()
            if row == None:
                messagebox.showerror("Error", "No Themes available", parent=self)

            else:
                for i in row:
                    if i not in lst:
                        lst.append(i)
            con.close()

        except Exception as es:
            messagebox.showerror("Error", f"Error Due to: {str(es)}", parent=self)

        status = Label(self.event_frame, text="Event Theme:", font=("Times New Roman", 18, "bold"), bg="white",
                       fg="#2C3539").place(x=525, y=100)
        self.click.set("Select")
        self.txt_theme = OptionMenu(self.event_frame, self.click, *lst)
        self.txt_theme.place(x=675, y=100, width=120, height=35)

        # --NAME--#
        event_name = Label(self.event_frame, text="Event Name:", font=("Times New Roman", 18, "bold"), bg="white",
                           fg="#2C3539").place(x=20, y=160)
        self.txt_event_name = Entry(self.event_frame, relief="solid", font=("Times New Roman", 18), bg="lightgray")
        self.txt_event_name.place(x=180, y=160, width=320, height=35)

        # --DATE OF EVENT--#
        date_event = Label(self.event_frame, text="Date of Event:", font=("Times New Roman", 18, "bold"), bg="white",
                           fg="#2C3539").place(x=525, y=160)
        self.txt_date_event = Entry(self.event_frame, relief="solid", font=("Times New Roman", 18), bg="lightgray")
        self.txt_date_event.place(x=678, y=160, width=175, height=35)
        #self.txt_date_event.insert(END, "DD/MM/YYYY")
        # self.txt_date_event.config(state=DISABLED)
        # self.txt_date_event.bind("<Button-1>", focus)

        # --DURATION--#
        event_duration = Label(self.event_frame, text="Duration:", font=("Times New Roman", 18, "bold"), bg="white",
                               fg="#2C3539").place(x=527, y=220)
        self.txt_event_duration = Entry(self.event_frame, relief="solid", font=("Times New Roman", 18), bg="lightgray")
        self.txt_event_duration.place(x=635, y=220, width=50, height=35)
        event_duration_days = Label(self.event_frame, text="day(s)", font=("Times New Roman", 18, "bold"), bg="white",
                                    fg="#2C3539").place(x=690, y=220)

        # --TIMING--#
        start_time = Label(self.event_frame, text="Timing:", font=("Times New Roman", 18, "bold"), bg="white",
                           fg="#2C3539").place(x=85, y=220)
        self.txt_start_time = Entry(self.event_frame, relief="solid", font=("Times New Roman", 18), bg="lightgray")
        self.txt_start_time.place(x=180, y=220, width=110, height=35)
        #self.txt_start_time.insert(END, "HH:MM")

        end_time = Label(self.event_frame, text="--", font=("Times New Roman", 18, "bold"), bg="white",
                         fg="#2C3539").place(x=295, y=220)
        self.txt_end_time = Entry(self.event_frame, relief="solid", font=("Times New Roman", 18), bg="lightgray")
        self.txt_end_time.place(x=325, y=220, width=110, height=35)
        #self.txt_end_time.insert(END, "HH:MM")

        # --Maximum Guest--#
        max_guest = Label(self.event_frame, text="Max. Guest:", font=("Times New Roman", 18, "bold"), bg="white",
                          fg="#2C3539").place(x=40, y=280)
        self.txt_max_guest = Entry(self.event_frame, relief="solid", font=("Times New Roman", 18), bg="lightgray")
        self.txt_max_guest.place(x=180, y=280, width=175, height=35)

        # --Venue--#
        venue = Label(self.event_frame, text="Venue:", font=("Times New Roman", 18, "bold"), bg="white",
                      fg="#2C3539").place(x=92, y=340)
        self.txt_venue = Entry(self.event_frame, relief="solid", font=("Times New Roman", 18), bg="lightgray")
        self.txt_venue.place(x=180, y=340, width=250, height=35)

        # --Contact No--#
        contact_no = Label(self.event_frame, text="Contact No.:", font=("Times New Roman", 18, "bold"), bg="white",
                           fg="#2C3539").place(x=33, y=400)
        self.txt_contact_no = Entry(self.event_frame, relief="solid", font=("Times New Roman", 18), bg="lightgray")
        self.txt_contact_no.place(x=180, y=400, width=150, height=35)

        # --Event Fees--#
        event_fees = Label(self.event_frame, text="Event Fees: ₹", font=("Times New Roman", 18, "bold"), bg="white",
                           fg="#2C3539").place(x=540, y=400)
        self.txt_event_fees = Entry(self.event_frame, relief="solid", font=("Times New Roman", 18), bg="lightgray")
        self.txt_event_fees.place(x=690, y=400, width=100, height=35)

        # --DESCRIPTION--#
        event_description = Label(self.event_frame, text="Description:", font=("Times New Roman", 18, "bold"),
                                  bg="white",
                                  fg="#2C3539").place(x=37, y=460)
        self.event_description = Text(self.event_frame, relief="solid", font=("Times New Roman", 18), bg="lightgray")
        self.event_description.place(x=180, y=460, width=250, height=150)

        # --Status--#
        self.clicked = StringVar()
        options = ["Select", "Active", "Cancelled", "Completed"]
        status = Label(self.event_frame, text="Status:", font=("Times New Roman", 18, "bold"), bg="white",
                       fg="#2C3539").place(x=540, y=460)
        self.clicked.set("Select")
        self.txt_status = OptionMenu(self.event_frame, self.clicked, *options)
        self.txt_status.place(x=620, y=460, width=120, height=35)

        # --CREATE BUTTON--#
        btn_update = Button(self.event_frame, text="Update", command=self.update_event, font=("Times New Roman", 20, "bold"),
                            fg="white", bg="#B00857", cursor="hand2").place(x=400, y=635, width=180, height=40)

    def clear(self):
        self.txt_event_id.delete(0, END)
        self.txt_event_name.delete(0, END)
        self.txt_date_event.delete(0, END)
        self.txt_event_duration.delete(0, END)
        self.txt_start_time.delete(0, END)
        self.txt_end_time.delete(0, END)
        self.txt_max_guest.delete(0, END)
        self.txt_venue.delete(0, END)
        self.txt_contact_no.delete(0, END)
        self.event_description.delete(1.0, END)
        self.txt_event_fees.delete(0, END)
        self.clicked.set("Select")
        self.click.set("Select")

    def update_event(self):
        if self.txt_event_id.get() == "" or self.txt_event_name.get() == "" or self.txt_date_event.get() == "" or self.txt_event_duration.get() == "" or self.txt_start_time.get() == "" or self.txt_end_time.get() == "" or self.txt_max_guest.get() == "" or self.txt_venue.get() == "" or self.txt_contact_no.get() == "" or self.event_description.get(
                1.0, END) == "" or self.txt_event_fees.get() == "":
            messagebox.showerror("Error", "All Fields are Required", parent=self)

        elif self.clicked.get() == "Select":
            messagebox.showerror("Error", "Select Status field", parent=self)

        elif self.click.get() == "Select":
            messagebox.showerror("Error", "Select Theme field", parent=self)

        else:
            try:
                con = pymysql.connect(host="localhost", user="root", password="root", db="event_management", port=3307)
                cur = con.cursor()
                a = self.click.get()
                # print(a)
                if '(' in a:
                    temp = a[2:-3]
                else:
                    temp = a
                # print(temp)
                cur.execute(
                    "UPDATE EVENT_123 SET event_name=%s, event_date=%s, event_duration=%s, start_time=%s, end_time=%s, max_guest=%s, venue=%s, contact_no=%s, event_fees=%s, event_description=%s, event_status=%s, theme_name=%s where event_id=%s",
                    (
                        self.txt_event_name.get(),
                        self.txt_date_event.get(),
                        self.txt_event_duration.get(),
                        self.txt_start_time.get(),
                        self.txt_end_time.get(),
                        self.txt_max_guest.get(),
                        self.txt_venue.get(),
                        self.txt_contact_no.get(),
                        self.txt_event_fees.get(),
                        self.event_description.get(1.0, END),
                        self.clicked.get(),
                        temp,
                        self.txt_event_id.get()
                    ))

                con.commit()
                messagebox.showinfo("Alert", "Event Updated Successfully", parent=self)
                self.clear()
                self.controller.show_frame(Admin_ModifyEvent)
                con.close()

            except Exception as es:
                messagebox.showerror("Error", f"Error Due to: {str(es)}", parent=self)

    def refresh(self):
        # --Event Theme--#
        self.click = StringVar()
        try:
            con = pymysql.connect(host="localhost", user="root", password="root", db="event_management", port=3307)
            cur = con.cursor()
            cur.execute("SELECT THEME_NAME FROM THEME")
            # (self.txt_username.get(), self.txt_pass_.get()))
            lst = ["Select"]
            row = cur.fetchall()
            if row == None:
                messagebox.showerror("Error", "Invalid USERNAME or PASSWORD", parent=self)

            else:
                for i in row:
                    lst.append(i)
            con.close()

        except Exception as es:
            messagebox.showerror("Error", f"Error Due to: {str(es)}", parent=self)

        status = Label(self.event_frame, text="Event Theme:", font=("Times New Roman", 18, "bold"), bg="white",
                       fg="#2C3539").place(x=525, y=100)
        self.click.set("Select")
        self.txt_status = OptionMenu(self.event_frame, self.click, *lst)
        self.txt_status.place(x=675, y=100, width=120, height=35)

        self.txt_event_id.delete(0, END)
        self.txt_event_name.delete(0, END)
        self.txt_date_event.delete(0, END)
        self.txt_event_duration.delete(0, END)
        self.txt_start_time.delete(0, END)
        self.txt_end_time.delete(0, END)
        self.txt_max_guest.delete(0, END)
        self.txt_venue.delete(0, END)
        self.txt_contact_no.delete(0, END)
        self.event_description.delete(1.0, END)
        self.txt_event_fees.delete(0, END)
        self.clicked.set("Select")
        self.click.set("Select")

    def search2(self):
        try:
            con = pymysql.connect(host="localhost", user="root", password="root", db="event_management", port=3307)
            cur = con.cursor()

            cur.execute("SELECT * FROM EVENT_123 WHERE event_id=%s", self.txt_event_id.get())
            row2 = cur.fetchall()
            con.commit()
            con.close()
            if len(row2) == 0:
                messagebox.showerror("Error", "Invalid Event ID", parent=self)
                self.txt_event_id.delete(0, END)
                self.txt_event_name.delete(0, END)
                self.txt_date_event.delete(0, END)
                self.txt_event_duration.delete(0, END)
                self.txt_start_time.delete(0, END)
                self.txt_end_time.delete(0, END)
                self.txt_max_guest.delete(0, END)
                self.txt_venue.delete(0, END)
                self.txt_contact_no.delete(0, END)
                self.event_description.delete(1.0, END)
                self.txt_event_fees.delete(0, END)
                self.clicked.set("Select")
                self.click.set("Select")
            else:
                # self.txt_event_id.delete(0, END)
                self.txt_event_name.delete(0, END)
                self.txt_date_event.delete(0, END)
                self.txt_event_duration.delete(0, END)
                self.txt_start_time.delete(0, END)
                self.txt_end_time.delete(0, END)
                self.txt_max_guest.delete(0, END)
                self.txt_venue.delete(0, END)
                self.txt_contact_no.delete(0, END)
                self.event_description.delete(1.0, END)
                self.txt_event_fees.delete(0, END)
                self.clicked.set("Select")
                self.click.set("Select")

                self.txt_event_name.insert(END, row2[0][1])
                self.txt_date_event.insert(END, row2[0][2])
                self.txt_event_duration.insert(END, row2[0][3])
                self.txt_start_time.insert(END, row2[0][4])
                self.txt_end_time.insert(END, row2[0][5])
                self.txt_max_guest.insert(END, row2[0][6])
                self.txt_venue.insert(END, row2[0][7])
                self.txt_contact_no.insert(END, row2[0][8])
                self.event_description.insert(END, row2[0][10])
                self.txt_event_fees.insert(END, row2[0][9])
                self.clicked.set(row2[0][11])
                self.click.set(row2[0][12])

        except Exception as es:
            messagebox.showerror("Error", f"Error Due to: {str(es)}", parent=self)

            # ------------------- ADMIN EVENT LIST-------------------- #


class Admin_EventList(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.controller = controller
        self.config(bg="#F6F7F7")  # for solid bg

        # Blue Frame
        frame_1 = Frame(self, bg="#1589FF")
        frame_1.place(x=220, y=0, width=1920, height=40)

        # Title
        title = Label(frame_1, text="Event Management System", font=("Times New Roman", 20, "bold"), bg="#1589FF",
                      fg="white").place(x=10, y=0)

        # Refresh Button
        home = Button(frame_1, cursor="hand2", command=self.refresh, text="Refresh",
                      font=("Times New Roman", 14, "bold"), bg="#1589FF", bd=0,
                      fg="white").place(x=1125, y=3)

        # Logout Button
        logout = Button(frame_1, cursor="hand2", command=lambda: controller.show_frame(Admin_Login), text="Logout",
                        font=("Times New Roman", 14, "bold"), bg="#1589FF", bd=0, fg="white").place(x=1230, y=3)

        # --GREY FRAME--#
        side_card = Frame(self, bg="#3C4248")
        side_card.place(x=0, y=0, width=225, height=1080)
        line_card = Frame(self, bg="white")
        line_card.place(x=0, y=45, width=225, height=1)

        # b = self.controller.app_data["admin"].get()
        title = Label(side_card, text="Welcome Admin", font=("Times New Roman", 20, "bold"), bg="#3C4248",
                      fg="white").place(x=10, y=0)

        # --DASHBOARD--#
        btn_dashboard = Button(side_card, text="Dashboard", command=lambda: controller.show_frame(Admin_Dashboard),
                               font=("Helvetica", 18, "bold"),
                               bg="#3C4248", fg="white", bd=0).place(x=40, y=60)  # bg="light grey"
        self.bg4 = ImageTk.PhotoImage(file="C:/Users/Swaraj/Desktop/Icons/Icons/dashboard.png")
        events_icon4 = Label(side_card, bg="#3C4248", fg="light grey", image=self.bg4).place(x=10, y=70)

        # --EVENTS--#
        lb_events_side = Label(side_card, text="Events", font=("Helvetica", 20, "bold"), bg="#3C4248",
                               fg="light grey").place(x=40, y=130)
        self.bg = ImageTk.PhotoImage(file="C:/Users/Swaraj/Desktop/Icons/Icons/calendar.png")
        events_icon = Label(side_card, bg="#3C4248", fg="light grey", image=self.bg).place(x=10, y=135)
        self.bg2 = ImageTk.PhotoImage(file="C:/Users/Swaraj/Desktop/Icons/Icons/right-arrow.png")
        events_icon2 = Label(side_card, bg="#3C4248", fg="light grey", image=self.bg2).place(x=150, y=140)

        # --CREATE EVENT--#
        btn_events_create = Button(side_card, command=lambda: controller.show_frame(Admin_CreateEvent),
                                   text="Create Events", font=("Helvetica", 18, "bold"), bg="#3C4248",
                                   fg="white", bd=0).place(x=35, y=170)  # bg="light grey"
        self.bg3 = ImageTk.PhotoImage(file="C:/Users/Swaraj/Desktop/Icons/Icons/calendar_add.png")
        events_icon3 = Label(side_card, bg="#3C4248", fg="light grey", image=self.bg3).place(x=10, y=180)

        # --CREATE THEME--#
        btn_theme_create = Button(side_card, text="Create Theme", command=lambda: controller.show_frame(Admin_Theme),
                                  font=("Helvetica", 18, "bold"), bg="#3C4248", fg="white", bd=0).place(x=35, y=215)
        self.bg8 = ImageTk.PhotoImage(file="C:/Users/Swaraj/Desktop/Icons/Icons/12.png")
        events_icon3 = Label(side_card, bg="#3C4248", fg="light grey", image=self.bg8).place(x=10, y=225)

        # --MODIFY EVENT--#
        btn_events_mod = Button(side_card, text="Modify Event",
                                command=lambda: controller.show_frame(Admin_ModifyEvent),
                                font=("Helvetica", 18, "bold"),
                                bg="#3C4248", fg="white", bd=0).place(x=35, y=260)  # bg="light grey"
        self.bg5 = ImageTk.PhotoImage(file="C:/Users/Swaraj/Desktop/Icons/Icons/calendar_mod.png")
        events_icon5 = Label(side_card, bg="#3C4248", fg="light grey", image=self.bg5).place(x=10, y=270)

        # --EVENT REQUESTS--#
        btn_events_request = Button(side_card, text="Event Requests", font=("Helvetica", 18, "bold"), command=lambda: controller.show_frame(Admin_EventRequest),
                                    bg="#3C4248", fg="white", bd=0).place(x=35, y=305)  # bg="light grey"
        self.bg6 = ImageTk.PhotoImage(file="C:/Users/Swaraj/Desktop/Icons/Icons/calendar_notification.png")
        events_icon6 = Label(side_card, bg="#3C4248", fg="light grey", image=self.bg6).place(x=10, y=315)

        # --EVENT LIST--#
        btn_events_list = Button(side_card, text="Event List", font=("Helvetica", 18, "bold"), command=lambda: controller.show_frame(Admin_EventList),
                                 bg="#3C4248", fg="white", bd=0).place(x=35, y=350)  # bg="light grey"
        self.bg7 = ImageTk.PhotoImage(file="C:/Users/Swaraj/Desktop/Icons/Icons/list.png")
        events_icon7 = Label(side_card, bg="#3C4248", fg="light grey", image=self.bg7).place(x=10, y=360)

        # --User Feedback--#
        btn_user_feedback = Button(side_card, text="User Feedback", font=("Helvetica", 18, "bold"),
                                   command=lambda: controller.show_frame(Admin_User_Feedback),
                                   bg="#3C4248", fg="white", bd=0).place(x=35, y=393)  # bg="light grey"
        self.bg9 = ImageTk.PhotoImage(file="C:/Users/Swaraj/Desktop/Icons/Icons/feedback.png")
        events_icon9 = Label(side_card, bg="#3C4248", fg="light grey", image=self.bg9).place(x=7, y=400)

        # --Registered Users--#
        btn_registered_user = Button(side_card, text="Reg. Users", font=("Helvetica", 18, "bold"),
                                     command=lambda: controller.show_frame(Admin_Registered_Users),
                                     bg="#3C4248", fg="white", bd=0).place(x=35, y=435)  # bg="light grey"
        self.bg10 = ImageTk.PhotoImage(file="C:/Users/Swaraj/Desktop/Icons/Icons/reg_users.png")
        events_icon10 = Label(side_card, bg="#3C4248", fg="light grey", image=self.bg10).place(x=9, y=442)

        # WHITE FRAME

        event_list_frame = Frame(self, bg="white")
        event_list_frame.place(x=265, y=125, width=1225, height=600)
        title = Label(event_list_frame, text="EVENT LIST", font=("Times New Roman", 20, "bold", "underline"), bg="white",
                      fg="#08A3D2").place(x=520, y=20)

        columns = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12')

        self.table = tkinter.ttk.Treeview(event_list_frame, columns=columns, show="headings", selectmode='browse')
        self.table.place(x=50, y=75, width=1150, height=500)

        verscrlbar = tkinter.ttk.Scrollbar(event_list_frame, orient="horizontal", command=self.table.xview)

        # Calling pack method w.r.to verical
        # scrollbar
        verscrlbar.place(x=51, y=557, width=1148)

        # Configuring treeview
        self.table.configure(xscrollcommand=verscrlbar.set)

        style = tkinter.ttk.Style()
        style.theme_use("clam")

        # Define headings
        self.table.heading('1', text='Event ID')
        self.table.heading('2', text='Event Theme')
        self.table.heading('3', text='Event Name')
        self.table.heading('4', text='Event Date')
        self.table.heading('5', text='Event Duration')
        self.table.heading('6', text='Start Time')
        self.table.heading('7', text='End Time')
        self.table.heading('8', text='Max.Guest')
        self.table.heading('9', text='Venue')
        self.table.heading('10', text='Contact Number')
        self.table.heading('11', text='Event Fees')
        self.table.heading('12', text='Event Status')

        self.table.column("1", width=50, anchor='c')
        self.table.column("2", width=100, anchor='c')
        self.table.column("3", width=120, anchor='c')
        self.table.column("4", width=90, anchor='c')
        self.table.column("5", width=80, anchor='c')
        self.table.column("6", width=60, anchor='c')
        self.table.column("7", width=60, anchor='c')
        self.table.column("8", width=90, anchor='c')
        self.table.column("9", width=90, anchor='c')
        self.table.column("10", width=90, anchor='c')
        self.table.column("11", width=90, anchor='c')
        self.table.column("12", width=90, anchor='c')

        try:
            con = pymysql.connect(host="localhost", user="root", password="root", db="event_management", port=3307)
            cur = con.cursor()

            cur.execute("SELECT event_id, theme_name, event_name, event_date, event_duration, start_time, end_time, max_guest, venue, contact_no, event_fees, event_status FROM event_123")
            rows = cur.fetchall()
            con.commit()
            con.close()

            for i in rows:
                self.table.insert('', 'end', values=i)

        except Exception as es:
            messagebox.showerror("Error", f"Error Due to: {str(es)}", parent=self)

    def refresh(self):
        try:
            con = pymysql.connect(host="localhost", user="root", password="root", db="event_management", port=3307)
            cur = con.cursor()

            cur.execute("SELECT event_id, theme_name, event_name, event_date, event_duration, start_time, end_time, max_guest, venue, contact_no, event_fees, event_status FROM event_123")
            rows2 = cur.fetchall()
            con.commit()
            con.close()

            for i in self.table.get_children():
                self.table.delete(i)

                # if i not in rows2:
                #     self.table.insert('', 'end', values=i)

        except Exception as es:
            messagebox.showerror("Error", f"Error Due to: {str(es)}", parent=self)

        try:
            con = pymysql.connect(host="localhost", user="root", password="root", db="event_management", port=3307)
            cur = con.cursor()

            cur.execute("SELECT event_id, theme_name, event_name, event_date, event_duration, start_time, end_time, max_guest, venue, contact_no, event_fees, event_status FROM event_123")
            rows = cur.fetchall()
            con.commit()
            con.close()

            for i in rows:
                self.table.insert('', 'end', values=i)

        except Exception as es:
            messagebox.showerror("Error", f"Error Due to: {str(es)}", parent=self)

        # ------------------- CUSTOMER DASHBOARD-------------------- #


class User_Dashboard(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.controller = controller
        self.config(bg="#F6F7F7")  # for solid bg

        # Blue Frame
        frame_1 = Frame(self, bg="#1589FF")
        frame_1.place(x=220, y=0, width=1920, height=40)

        # Title
        title = Label(frame_1, text="Event Management System", font=("Times New Roman", 20, "bold"), bg="#1589FF",
                      fg="white").place(x=10, y=0)

        # Refresh Button
        home = Button(frame_1, cursor="hand2", command=self.refresh, text="Refresh",
                      font=("Times New Roman", 14, "bold"), bg="#1589FF", bd=0,
                      fg="white").place(x=1000, y=3)

        # Contact Us Button
        contact_us = Button(frame_1, cursor="hand2", text="Contact Us", font=("Times New Roman", 14, "bold"), command=lambda: controller.show_frame(User_Contact_Us),
                            bg="#1589FF", bd=0, fg="white").place(x=1100, y=3)

        # Logout Button
        logout = Button(frame_1, cursor="hand2", command=lambda: controller.show_frame(Customer_Login), text="Logout",
                        font=("Times New Roman", 14, "bold"), bg="#1589FF", bd=0, fg="white").place(x=1230, y=3)

        # --GREY FRAME--#
        side_card = Frame(self, bg="#3C4248")
        side_card.place(x=0, y=0, width=225, height=1080)
        line_card = Frame(self, bg="white")
        line_card.place(x=0, y=45, width=225, height=1)

        # b = self.controller.app_data["admin"].get()
        title = Label(side_card, text="Welcome User", font=("Times New Roman", 20, "bold"), bg="#3C4248",
                      fg="white").place(x=10, y=0)

        # --DASHBOARD--#
        btn_dashboard = Button(side_card, text="Home", command=lambda: controller.show_frame(User_Dashboard),
                               font=("Helvetica", 18, "bold"),
                               bg="#3C4248", fg="white", bd=0).place(x=40, y=60)  # bg="light grey"
        self.bg4 = ImageTk.PhotoImage(file="C:/Users/Swaraj/Desktop/Icons/Icons/dashboard.png")
        events_icon4 = Label(side_card, bg="#3C4248", fg="light grey", image=self.bg4).place(x=10, y=70)

        # --EVENTS--#
        lb_events_side = Label(side_card, text="Events", font=("Helvetica", 20, "bold"), bg="#3C4248",
                               fg="light grey").place(x=40, y=130)
        self.bg = ImageTk.PhotoImage(file="C:/Users/Swaraj/Desktop/Icons/Icons/calendar.png")
        events_icon = Label(side_card, bg="#3C4248", fg="light grey", image=self.bg).place(x=10, y=135)
        self.bg2 = ImageTk.PhotoImage(file="C:/Users/Swaraj/Desktop/Icons/Icons/right-arrow.png")
        events_icon2 = Button(side_card, bg="#3C4248", command=lambda: controller.show_frame(User_Dashboard2), bd=0, fg="light grey", image=self.bg2).place(x=150, y=140)

        # --REQUEST EVENT--#
        btn_events_create = Button(side_card, command=lambda: controller.show_frame(User_Event_Request),
                                   text="Request Events", font=("Helvetica", 18, "bold"), bg="#3C4248",
                                   fg="white", bd=0).place(x=35, y=170)  # bg="light grey"
        self.bg3 = ImageTk.PhotoImage(file="C:/Users/Swaraj/Desktop/Icons/Icons/calendar_add.png")
        events_icon3 = Label(side_card, bg="#3C4248", fg="light grey", image=self.bg3).place(x=10, y=180)

        # --EVENT LIST--#
        btn_events_list = Button(side_card, text="Event List", font=("Helvetica", 18, "bold"),
                                 command=lambda: controller.show_frame(User_EventList),
                                 bg="#3C4248", fg="white", bd=0).place(x=35, y=214)  # bg="light grey"
        self.bg7 = ImageTk.PhotoImage(file="C:/Users/Swaraj/Desktop/Icons/Icons/list.png")
        events_icon7 = Label(side_card, bg="#3C4248", fg="light grey", image=self.bg7).place(x=13, y=225)



        # WHITE FRAME
        self.event_list_frame = Frame(self, bg="white")
        self.event_list_frame.place(x=265, y=75, width=1225, height=720)


        title = Label(self.event_list_frame, text="ACTIVE EVENT LIST", font=("Times New Roman", 20, "bold", "underline"),
                      bg="white", fg="#08A3D2").place(x=490, y=20)

        columns = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12')

        self.table = tkinter.ttk.Treeview(self.event_list_frame, columns=columns, show="headings", selectmode='browse')
        self.table.place(x=50, y=75, width=1150, height=250)

        verscrlbar = tkinter.ttk.Scrollbar(self.event_list_frame, orient="horizontal", command=self.table.xview)

        # Calling pack method w.r.to verical
        # scrollbar
        verscrlbar.place(x=51, y=310, width=1148)

        # Configuring treeview
        self.table.configure(xscrollcommand=verscrlbar.set)

        style = tkinter.ttk.Style()
        style.theme_use("clam")

        # define headings
        self.table.heading('1', text='Event ID')
        self.table.heading('2', text='Event Theme')
        self.table.heading('3', text='Event Name')
        self.table.heading('4', text='Event Date')
        self.table.heading('5', text='Event Duration')
        self.table.heading('6', text='Start Time')
        self.table.heading('7', text='End Time')
        self.table.heading('8', text='Max.Guest')
        self.table.heading('9', text='Venue')
        self.table.heading('10', text='Contact Number')
        self.table.heading('11', text='Event Fees')
        self.table.heading('12', text='Event Status')

        self.table.column("1", width=50, anchor='c')
        self.table.column("2", width=100, anchor='c')
        self.table.column("3", width=120, anchor='c')
        self.table.column("4", width=90, anchor='c')
        self.table.column("5", width=80, anchor='c')
        self.table.column("6", width=60, anchor='c')
        self.table.column("7", width=60, anchor='c')
        self.table.column("8", width=90, anchor='c')
        self.table.column("9", width=90, anchor='c')
        self.table.column("10", width=90, anchor='c')
        self.table.column("11", width=90, anchor='c')
        self.table.column("12", width=90, anchor='c')

        try:
            con = pymysql.connect(host="localhost", user="root", password="root", db="event_management", port=3307)
            cur = con.cursor()

            cur.execute(
                "SELECT event_id, theme_name, event_name, event_date, event_duration, start_time, end_time, max_guest, venue, contact_no, event_fees, event_status FROM event_123 where event_status='Active'")
            rows = cur.fetchall()
            con.commit()
            con.close()

            for i in rows:
                self.table.insert('', 'end', values=i)

        except Exception as es:
            messagebox.showerror("Error", f"Error Due to: {str(es)}", parent=self)

        register_event = Label(self.event_list_frame, text="REGISTER FOR AN EVENT ", font=("Times New Roman", 20, "bold", "underline"),
                      bg="white", fg="#08A3D2").place(x=450, y=370)

        # Event ID
        event_id = Label(self.event_list_frame, text="Event ID:", font=("Times New Roman", 18, "bold"), bg="white",
                         fg="#2C3539").place(x=548, y=500)
        self.txt_event_id = Entry(self.event_list_frame, relief="solid", font=("Times New Roman", 18), bg="lightgray")
        self.txt_event_id.place(x=660, y=500, width=50, height=35)

        # Register ID
        register_id = Label(self.event_list_frame, text="Register ID:", font=("Times New Roman", 18, "bold"), bg="white",
                         fg="#2C3539").place(x=523, y=440)
        self.txt_register_id = Entry(self.event_list_frame, relief="solid", font=("Times New Roman", 18), bg="lightgray")
        self.txt_register_id.place(x=660, y=440, width=50, height=35)

        k = random.randint(0, 999)
        self.txt_register_id.insert(END, k)
        self.txt_register_id.config(state=DISABLED)

        register = Button(self.event_list_frame, text="Register", command=self.register2, font=("Times New Roman", 16, "bold"),
                            fg="white", bg="#B00857", cursor="hand2").place(x=563, y=560, width=100, height=40)

    def register2(self):
        try:
            con = pymysql.connect(host="localhost", user="root", password="root", db="event_management", port=3307)
            cur = con.cursor()

            cur.execute(
                "INSERT INTO user_register (reg_id, event_id, username)values(%s,%s,%s)",
                (
                    self.txt_register_id.get(),
                    self.txt_event_id.get(),
                    self.controller.app_data["Username"]

                ))
            # rows = cur.fetchall()
            con.commit()
            messagebox.showinfo("Alert", "Event Registration Successful", parent=self)
            con.close()

            self.txt_register_id.config(state=NORMAL)
            self.txt_register_id.delete(0, END)
            k = random.randint(0, 999)
            self.txt_register_id.insert(END, k)
            self.txt_register_id.config(state=DISABLED)
            self.txt_event_id.delete(0, END)

            self.controller.show_frame(User_Dashboard)
        except Exception as es:
            messagebox.showerror("Error", f"Error Due to: {str(es)}", parent=self)

    def refresh(self):
        for i in self.table.get_children():
            self.table.delete(i)
        try:
            con = pymysql.connect(host="localhost", user="root", password="root", db="event_management", port=3307)
            cur = con.cursor()

            cur.execute(
                "SELECT event_id, theme_name, event_name, event_date, event_duration, start_time, end_time, max_guest, venue, contact_no, event_fees, event_status FROM event_123 where event_status='Active'")
            rows = cur.fetchall()
            con.commit()
            con.close()

            for i in rows:
                self.table.insert('', 'end', values=i)

        except Exception as es:
            messagebox.showerror("Error", f"Error Due to: {str(es)}", parent=self)

        self.txt_register_id.config(state=NORMAL)
        self.txt_register_id.delete(0, END)
        k = random.randint(0, 999)
        self.txt_register_id.insert(END, k)
        self.txt_register_id.config(state=DISABLED)

    def contact_us_window(self):
        pass

        # ------------------- CUSTOMER DASHBOARD2-------------------- #


class User_Dashboard2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.controller = controller
        self.config(bg="#F6F7F7")  # for solid bg

        # Blue Frame
        frame_1 = Frame(self, bg="#1589FF")
        frame_1.place(x=220, y=0, width=1920, height=40)

        # Title
        title = Label(frame_1, text="Event Management System", font=("Times New Roman", 20, "bold"),
                      bg="#1589FF",
                      fg="white").place(x=10, y=0)

        # Refresh Button
        home = Button(frame_1, cursor="hand2", command=self.refresh, text="Refresh",
                      font=("Times New Roman", 14, "bold"), bg="#1589FF", bd=0,
                      fg="white").place(x=1000, y=3)

        # Contact Us Button
        contact_us = Button(frame_1, cursor="hand2", text="Contact Us", font=("Times New Roman", 14, "bold"),
                            bg="#1589FF", bd=0, fg="white").place(x=1100, y=3)

        # Logout Button
        logout = Button(frame_1, cursor="hand2", command=lambda: controller.show_frame(Customer_Login),
                        text="Logout",
                        font=("Times New Roman", 14, "bold"), bg="#1589FF", bd=0, fg="white").place(x=1230, y=3)

        # --GREY FRAME--#
        side_card = Frame(self, bg="#3C4248")
        side_card.place(x=0, y=0, width=225, height=1080)
        line_card = Frame(self, bg="white")
        line_card.place(x=0, y=45, width=225, height=1)

        # b = self.controller.app_data["admin"].get()
        title = Label(side_card, text="Welcome User", font=("Times New Roman", 20, "bold"), bg="#3C4248",
                      fg="white").place(x=10, y=0)

        # --DASHBOARD--#
        btn_dashboard = Button(side_card, text="Home", command=lambda: controller.show_frame(User_Dashboard),
                               font=("Helvetica", 18, "bold"),
                               bg="#3C4248", fg="white", bd=0).place(x=40, y=60)  # bg="light grey"
        self.bg4 = ImageTk.PhotoImage(file="C:/Users/Swaraj/Desktop/Icons/Icons/dashboard.png")
        events_icon4 = Label(side_card, bg="#3C4248", fg="light grey", image=self.bg4).place(x=10, y=70)



        # --EVENTS--#
        lb_events_side = Label(side_card, text="Events", font=("Helvetica", 20, "bold"), bg="#3C4248",
                               fg="light grey").place(x=40, y=130)
        self.bg = ImageTk.PhotoImage(file="C:/Users/Swaraj/Desktop/Icons/Icons/calendar.png")
        events_icon = Label(side_card, bg="#3C4248", fg="light grey", image=self.bg).place(x=10, y=135)
        self.bg2 = ImageTk.PhotoImage(file="C:/Users/Swaraj/Desktop/Icons/Icons/Upward.png")
        events_icon2 = Button(side_card, bg="#3C4248", command=lambda: controller.show_frame(User_Dashboard), bd=0, fg="light grey", image=self.bg2).place(x=150, y=140)

        self.event_list_frame = Frame(self, bg="white")
        self.event_list_frame.place(x=265, y=75, width=1225, height=720)

        # WHITE FRAME
        title = Label(self.event_list_frame, text="ACTIVE EVENT LIST",
                      font=("Times New Roman", 20, "bold", "underline"),
                      bg="white", fg="#08A3D2").place(x=490, y=20)

        columns = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12')

        self.table = tkinter.ttk.Treeview(self.event_list_frame, columns=columns, show="headings",
                                          selectmode='browse')
        self.table.place(x=50, y=75, width=1150, height=250)

        verscrlbar = tkinter.ttk.Scrollbar(self.event_list_frame, orient="horizontal", command=self.table.xview)

        # Calling pack method w.r.to verical
        # scrollbar
        verscrlbar.place(x=51, y=310, width=1148)

        # Configuring treeview
        self.table.configure(xscrollcommand=verscrlbar.set)

        style = tkinter.ttk.Style()
        style.theme_use("clam")

        # define headings
        self.table.heading('1', text='Event ID')
        self.table.heading('2', text='Event Theme')
        self.table.heading('3', text='Event Name')
        self.table.heading('4', text='Event Date')
        self.table.heading('5', text='Event Duration')
        self.table.heading('6', text='Start Time')
        self.table.heading('7', text='End Time')
        self.table.heading('8', text='Max.Guest')
        self.table.heading('9', text='Venue')
        self.table.heading('10', text='Contact Number')
        self.table.heading('11', text='Event Fees')
        self.table.heading('12', text='Event Status')

        self.table.column("1", width=50, anchor='c')
        self.table.column("2", width=100, anchor='c')
        self.table.column("3", width=120, anchor='c')
        self.table.column("4", width=90, anchor='c')
        self.table.column("5", width=80, anchor='c')
        self.table.column("6", width=60, anchor='c')
        self.table.column("7", width=60, anchor='c')
        self.table.column("8", width=90, anchor='c')
        self.table.column("9", width=90, anchor='c')
        self.table.column("10", width=90, anchor='c')
        self.table.column("11", width=90, anchor='c')
        self.table.column("12", width=90, anchor='c')

        try:
            con = pymysql.connect(host="localhost", user="root", password="root", db="event_management",
                                  port=3307)
            cur = con.cursor()

            cur.execute(
                "SELECT event_id, theme_name, event_name, event_date, event_duration, start_time, end_time, max_guest, venue, contact_no, event_fees, event_status FROM event_123 where event_status='Active'")
            rows = cur.fetchall()
            con.commit()
            con.close()

            for i in rows:
                self.table.insert('', 'end', values=i)

        except Exception as es:
            messagebox.showerror("Error", f"Error Due to: {str(es)}", parent=self)

        register_event = Label(self.event_list_frame, text="REGISTER FOR AN EVENT ",
                               font=("Times New Roman", 20, "bold", "underline"),
                               bg="white", fg="#08A3D2").place(x=450, y=370)

        # Event ID
        event_id = Label(self.event_list_frame, text="Event ID:", font=("Times New Roman", 18, "bold"),
                         bg="white",
                         fg="#2C3539").place(x=548, y=500)
        self.txt_event_id = Entry(self.event_list_frame, relief="solid", font=("Times New Roman", 18),
                                  bg="lightgray")
        self.txt_event_id.place(x=660, y=500, width=50, height=35)

        # Register ID
        register_id = Label(self.event_list_frame, text="Register ID:", font=("Times New Roman", 18, "bold"),
                            bg="white",
                            fg="#2C3539").place(x=523, y=440)
        self.txt_register_id = Entry(self.event_list_frame, relief="solid", font=("Times New Roman", 18),
                                     bg="lightgray")
        self.txt_register_id.place(x=660, y=440, width=50, height=35)

        k = random.randint(0, 999)
        self.txt_register_id.insert(END, k)
        self.txt_register_id.config(state=DISABLED)

        register = Button(self.event_list_frame, text="Register", command=self.register2,
                          font=("Times New Roman", 16, "bold"),
                          fg="white", bg="#B00857", cursor="hand2").place(x=563, y=560, width=100, height=40)

    def register2(self):
        try:
            con = pymysql.connect(host="localhost", user="root", password="root", db="event_management",
                                  port=3307)
            cur = con.cursor()

            cur.execute(
                "INSERT INTO user_register (reg_id, event_id, username)values(%s,%s,%s)",
                (
                    self.txt_register_id.get(),
                    self.txt_event_id.get(),
                    self.controller.app_data["Username"]

                ))
            # rows = cur.fetchall()
            con.commit()
            messagebox.showinfo("Alert", "Event Registration Successful", parent=self)
            con.close()

            self.txt_register_id.config(state=NORMAL)
            self.txt_register_id.delete(0, END)
            k = random.randint(0, 999)
            self.txt_register_id.insert(END, k)
            self.txt_register_id.config(state=DISABLED)
            self.txt_event_id.delete(0, END)

            self.controller.show_frame(User_Dashboard)
        except Exception as es:
            messagebox.showerror("Error", f"Error Due to: {str(es)}", parent=self)

    def refresh(self):
        for i in self.table.get_children():
            self.table.delete(i)
        try:
            con = pymysql.connect(host="localhost", user="root", password="root", db="event_management",
                                  port=3307)
            cur = con.cursor()

            cur.execute(
                "SELECT event_id, theme_name, event_name, event_date, event_duration, start_time, end_time, max_guest, venue, contact_no, event_fees, event_status FROM event_123 where event_status='Active'")
            rows = cur.fetchall()
            con.commit()
            con.close()

            for i in rows:
                self.table.insert('', 'end', values=i)

        except Exception as es:
            messagebox.showerror("Error", f"Error Due to: {str(es)}", parent=self)

        self.txt_register_id.config(state=NORMAL)
        self.txt_register_id.delete(0, END)
        k = random.randint(0, 999)
        self.txt_register_id.insert(END, k)
        self.txt_register_id.config(state=DISABLED)

        # ------------------- ADMIN VENUE-------------------- #


class Admin_User_Feedback(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.controller = controller
        self.config(bg="#F6F7F7")  # for solid bg

        # Blue Frame
        frame_1 = Frame(self, bg="#1589FF")
        frame_1.place(x=220, y=0, width=1920, height=40)

        # Title
        title = Label(frame_1, text="Event Management System", font=("Times New Roman", 20, "bold"), bg="#1589FF",
                      fg="white").place(x=10, y=0)

        # Refresh Button
        home = Button(frame_1, cursor="hand2", command=self.refresh, text="Refresh",
                      font=("Times New Roman", 14, "bold"), bg="#1589FF", bd=0,
                      fg="white").place(x=1125, y=3)

        # Logout Button
        logout = Button(frame_1, cursor="hand2", command=lambda: controller.show_frame(Admin_Login), text="Logout",
                        font=("Times New Roman", 14, "bold"), bg="#1589FF", bd=0, fg="white").place(x=1230, y=3)

        # --GREY FRAME--#
        side_card = Frame(self, bg="#3C4248")
        side_card.place(x=0, y=0, width=225, height=1080)
        line_card = Frame(self, bg="white")
        line_card.place(x=0, y=45, width=225, height=1)
        title = Label(side_card, text="Welcome Admin", font=("Times New Roman", 20, "bold"), bg="#3C4248",
                      fg="white").place(x=10, y=0)

        # --DASHBOARD--#
        btn_dashboard = Button(side_card, text="Dashboard", command=lambda: controller.show_frame(Admin_Dashboard),
                               font=("Helvetica", 18, "bold"),
                               bg="#3C4248", fg="white", bd=0).place(x=40, y=60)  # bg="light grey"
        self.bg4 = ImageTk.PhotoImage(file="C:/Users/Swaraj/Desktop/Icons/Icons/dashboard.png")
        events_icon4 = Label(side_card, bg="#3C4248", fg="light grey", image=self.bg4).place(x=10, y=70)

        # --EVENTS--#
        lb_events_side = Label(side_card, text="Events", font=("Helvetica", 20, "bold"), bg="#3C4248",
                               fg="light grey").place(x=40, y=130)
        self.bg = ImageTk.PhotoImage(file="C:/Users/Swaraj/Desktop/Icons/Icons/calendar.png")
        events_icon = Label(side_card, bg="#3C4248", fg="light grey", image=self.bg).place(x=10, y=135)
        self.bg2 = ImageTk.PhotoImage(file="C:/Users/Swaraj/Desktop/Icons/Icons/right-arrow.png")
        events_icon2 = Label(side_card, bg="#3C4248", fg="light grey", image=self.bg2).place(x=150, y=140)

        # --CREATE EVENT--#
        btn_events_create = Button(side_card, text="Create Events",
                                   command=lambda: controller.show_frame(Admin_CreateEvent),
                                   font=("Helvetica", 18, "bold"), bg="#3C4248",
                                   fg="white", bd=0).place(x=35, y=170)  # bg="light grey"
        self.bg3 = ImageTk.PhotoImage(file="C:/Users/Swaraj/Desktop/Icons/Icons/calendar_add.png")
        events_icon3 = Label(side_card, bg="#3C4248", fg="light grey", image=self.bg3).place(x=10, y=180)

        # --CREATE THEME--#
        btn_theme_create = Button(side_card, text="Create Theme", command=lambda: controller.show_frame(Admin_Theme),
                                  font=("Helvetica", 18, "bold"), bg="#3C4248", fg="white", bd=0).place(x=35, y=215)
        self.bg8 = ImageTk.PhotoImage(file="C:/Users/Swaraj/Desktop/Icons/Icons/12.png")
        events_icon3 = Label(side_card, bg="#3C4248", fg="light grey", image=self.bg8).place(x=10, y=225)

        # --MODIFY EVENT--#
        btn_events_mod = Button(side_card, text="Modify Event",
                                command=lambda: controller.show_frame(Admin_ModifyEvent),
                                font=("Helvetica", 18, "bold"),
                                bg="#3C4248", fg="white", bd=0).place(x=35, y=260)  # bg="light grey"
        self.bg5 = ImageTk.PhotoImage(file="C:/Users/Swaraj/Desktop/Icons/Icons/calendar_mod.png")
        events_icon5 = Label(side_card, bg="#3C4248", fg="light grey", image=self.bg5).place(x=10, y=270)

        # --EVENT REQUESTS--#
        btn_events_request = Button(side_card, text="Event Requests", font=("Helvetica", 18, "bold"), command=lambda: controller.show_frame(Admin_EventRequest),
                                    bg="#3C4248", fg="white", bd=0).place(x=35, y=305)  # bg="light grey"
        self.bg6 = ImageTk.PhotoImage(file="C:/Users/Swaraj/Desktop/Icons/Icons/calendar_notification.png")
        events_icon6 = Label(side_card, bg="#3C4248", fg="light grey", image=self.bg6).place(x=10, y=315)

        # --EVENT LIST--#
        btn_events_list = Button(side_card, text="Event List", font=("Helvetica", 18, "bold"),
                                 command=lambda: controller.show_frame(Admin_EventList),
                                 bg="#3C4248", fg="white", bd=0).place(x=35, y=350)  # bg="light grey"
        self.bg7 = ImageTk.PhotoImage(file="C:/Users/Swaraj/Desktop/Icons/Icons/list.png")
        events_icon7 = Label(side_card, bg="#3C4248", fg="light grey", image=self.bg7).place(x=10, y=360)

        # --User Feedback--#
        btn_user_feedback = Button(side_card, text="User Feedback", font=("Helvetica", 18, "bold"),
                                   command=lambda: controller.show_frame(Admin_User_Feedback),
                                   bg="#3C4248", fg="white", bd=0).place(x=35, y=393)  # bg="light grey"
        self.bg9 = ImageTk.PhotoImage(file="C:/Users/Swaraj/Desktop/Icons/Icons/feedback.png")
        events_icon9 = Label(side_card, bg="#3C4248", fg="light grey", image=self.bg9).place(x=7, y=400)

        # --Registered Users--#
        btn_registered_user = Button(side_card, text="Reg. Users", font=("Helvetica", 18, "bold"),
                                     command=lambda: controller.show_frame(Admin_Registered_Users),
                                     bg="#3C4248", fg="white", bd=0).place(x=35, y=435)  # bg="light grey"
        self.bg10 = ImageTk.PhotoImage(file="C:/Users/Swaraj/Desktop/Icons/Icons/reg_users.png")
        events_icon10 = Label(side_card, bg="#3C4248", fg="light grey", image=self.bg10).place(x=9, y=442)

        # WHITE FRAME
        self.event_frame = Frame(self, bg="white")
        self.event_frame.place(x=370, y=190, width=1000, height=420)

        # Title
        title = Label(self.event_frame, text="USER FEEDBACK", font=("Times New Roman", 25, "bold", "underline"), bg="white",
                      fg="#08A3D2").place(x=20, y=20)

        columns = ('1', '2')
        columns2 = ('1', '2', '3')

        self.table = tkinter.ttk.Treeview(self.event_frame, columns=columns, show="headings", selectmode='browse')
        self.table.place(x=150, y=105, width=200, height=250)

        self.table2 = tkinter.ttk.Treeview(self.event_frame, columns=columns2, show="headings", selectmode='browse')
        self.table2.place(x=350, y=105, width=500, height=250)

        style = tkinter.ttk.Style()
        style.theme_use("clam")

        # define headings
        self.table.heading('1', text='Username')
        self.table.heading('2', text='Feedback')
        self.table.column("1", width=70, anchor='c')
        self.table.column("2", width=80, anchor='c')

        self.table2.heading('1', text='First Name')
        self.table2.heading('2', text='Last Name')
        self.table2.heading('3', text='Phone Number')
        self.table2.column("1", width=80, anchor='c')
        self.table2.column("2", width=80, anchor='c')
        self.table2.column("3", width=80, anchor='c')

        try:
            con = pymysql.connect(host="localhost", user="root", password="root", db="event_management", port=3307)
            cur = con.cursor()

            cur.execute(
                "SELECT * FROM user_feedback")

            rows = cur.fetchall()
            con.commit()
            con.close()

            if len(rows) < 1:
                messagebox.showerror("Error", "No Feedback Available", parent=self)

            lst3 = []
            for j in range(0, len(rows)):
                lst3.append(rows[j][0])

            for i in rows:
                self.table.insert('', 'end', values=i)

        except Exception as es:
            messagebox.showerror("Error", f"Error Due to: {str(es)}", parent=self)

        for y in lst3:
            try:
                con = pymysql.connect(host="localhost", user="root", password="root", db="event_management", port=3307)
                cur = con.cursor()

                cur.execute(
                    "SELECT f_name,l_name,ph_no FROM customer where username=%s",
                    (
                        y
                    ))
                rows2 = cur.fetchall()
                con.commit()
                con.close()

                for i in rows2:
                    self.table2.insert('', 'end', values=i)

            except Exception as es:
                messagebox.showerror("Error", f"Error Due to: {str(es)}", parent=self)

    def refresh(self):
        for i in self.table.get_children():
            self.table.delete(i)
        for j in self.table2.get_children():
            self.table2.delete(j)
        try:
            con = pymysql.connect(host="localhost", user="root", password="root", db="event_management", port=3307)
            cur = con.cursor()

            cur.execute(
                "SELECT * FROM user_feedback")

            rows = cur.fetchall()
            con.commit()
            con.close()

            if len(rows) < 1:
                messagebox.showerror("Error", "No Feedback Available", parent=self)

            lst3 = []
            for j in range(0, len(rows)):
                lst3.append(rows[j][0])

            for i in rows:
                self.table.insert('', 'end', values=i)

        except Exception as es:
            messagebox.showerror("Error", f"Error Due to: {str(es)}", parent=self)

        for y in lst3:
            try:
                con = pymysql.connect(host="localhost", user="root", password="root", db="event_management", port=3307)
                cur = con.cursor()

                cur.execute(
                    "SELECT f_name,l_name,ph_no FROM customer where username=%s",
                    (
                        y
                    ))
                rows2 = cur.fetchall()
                con.commit()
                con.close()

                for i in rows2:
                    self.table2.insert('', 'end', values=i)

            except Exception as es:
                messagebox.showerror("Error", f"Error Due to: {str(es)}", parent=self)

        # ------------------- ADMIN REGISTERED USERS-------------------- #


class Admin_Registered_Users(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.controller = controller
        self.config(bg="#F6F7F7")  # for solid bg

        # Blue Frame
        frame_1 = Frame(self, bg="#1589FF")
        frame_1.place(x=220, y=0, width=1920, height=40)

        # Title
        title = Label(frame_1, text="Event Management System", font=("Times New Roman", 20, "bold"), bg="#1589FF",
                      fg="white").place(x=10, y=0)

        # Refresh Button
        home = Button(frame_1, cursor="hand2", command=self.refresh, text="Refresh",
                      font=("Times New Roman", 14, "bold"), bg="#1589FF", bd=0,
                      fg="white").place(x=1125, y=3)

        # Logout Button
        logout = Button(frame_1, cursor="hand2", command=lambda: controller.show_frame(Admin_Login), text="Logout",
                        font=("Times New Roman", 14, "bold"), bg="#1589FF", bd=0, fg="white").place(x=1230, y=3)

        # --GREY FRAME--#
        side_card = Frame(self, bg="#3C4248")
        side_card.place(x=0, y=0, width=225, height=1080)
        line_card = Frame(self, bg="white")
        line_card.place(x=0, y=45, width=225, height=1)
        title = Label(side_card, text="Welcome Admin", font=("Times New Roman", 20, "bold"), bg="#3C4248",
                      fg="white").place(x=10, y=0)

        # --DASHBOARD--#
        btn_dashboard = Button(side_card, text="Dashboard", command=lambda: controller.show_frame(Admin_Dashboard),
                               font=("Helvetica", 18, "bold"),
                               bg="#3C4248", fg="white", bd=0).place(x=40, y=60)  # bg="light grey"
        self.bg4 = ImageTk.PhotoImage(file="C:/Users/Swaraj/Desktop/Icons/Icons/dashboard.png")
        events_icon4 = Label(side_card, bg="#3C4248", fg="light grey", image=self.bg4).place(x=10, y=70)

        # --EVENTS--#
        lb_events_side = Label(side_card, text="Events", font=("Helvetica", 20, "bold"), bg="#3C4248",
                               fg="light grey").place(x=40, y=130)
        self.bg = ImageTk.PhotoImage(file="C:/Users/Swaraj/Desktop/Icons/Icons/calendar.png")
        events_icon = Label(side_card, bg="#3C4248", fg="light grey", image=self.bg).place(x=10, y=135)
        self.bg2 = ImageTk.PhotoImage(file="C:/Users/Swaraj/Desktop/Icons/Icons/right-arrow.png")
        events_icon2 = Label(side_card, bg="#3C4248", fg="light grey", image=self.bg2).place(x=150, y=140)

        # --CREATE EVENT--#
        btn_events_create = Button(side_card, text="Create Events",
                                   command=lambda: controller.show_frame(Admin_CreateEvent),
                                   font=("Helvetica", 18, "bold"), bg="#3C4248",
                                   fg="white", bd=0).place(x=35, y=170)  # bg="light grey"
        self.bg3 = ImageTk.PhotoImage(file="C:/Users/Swaraj/Desktop/Icons/Icons/calendar_add.png")
        events_icon3 = Label(side_card, bg="#3C4248", fg="light grey", image=self.bg3).place(x=10, y=180)

        # --CREATE THEME--#
        btn_theme_create = Button(side_card, text="Create Theme", command=lambda: controller.show_frame(Admin_Theme),
                                  font=("Helvetica", 18, "bold"), bg="#3C4248", fg="white", bd=0).place(x=35, y=215)
        self.bg8 = ImageTk.PhotoImage(file="C:/Users/Swaraj/Desktop/Icons/Icons/12.png")
        events_icon3 = Label(side_card, bg="#3C4248", fg="light grey", image=self.bg8).place(x=10, y=225)

        # --MODIFY EVENT--#
        btn_events_mod = Button(side_card, text="Modify Event",
                                command=lambda: controller.show_frame(Admin_ModifyEvent),
                                font=("Helvetica", 18, "bold"),
                                bg="#3C4248", fg="white", bd=0).place(x=35, y=260)  # bg="light grey"
        self.bg5 = ImageTk.PhotoImage(file="C:/Users/Swaraj/Desktop/Icons/Icons/calendar_mod.png")
        events_icon5 = Label(side_card, bg="#3C4248", fg="light grey", image=self.bg5).place(x=10, y=270)

        # --EVENT REQUESTS--#
        btn_events_request = Button(side_card, text="Event Requests", font=("Helvetica", 18, "bold"), command=lambda: controller.show_frame(Admin_EventRequest),
                                    bg="#3C4248", fg="white", bd=0).place(x=35, y=305)  # bg="light grey"
        self.bg6 = ImageTk.PhotoImage(file="C:/Users/Swaraj/Desktop/Icons/Icons/calendar_notification.png")
        events_icon6 = Label(side_card, bg="#3C4248", fg="light grey", image=self.bg6).place(x=10, y=315)

        # --EVENT LIST--#
        btn_events_list = Button(side_card, text="Event List", font=("Helvetica", 18, "bold"),
                                 command=lambda: controller.show_frame(Admin_EventList),
                                 bg="#3C4248", fg="white", bd=0).place(x=35, y=350)  # bg="light grey"
        self.bg7 = ImageTk.PhotoImage(file="C:/Users/Swaraj/Desktop/Icons/Icons/list.png")
        events_icon7 = Label(side_card, bg="#3C4248", fg="light grey", image=self.bg7).place(x=10, y=360)

        # --User Feedback--#
        btn_user_feedback = Button(side_card, text="User Feedback", font=("Helvetica", 18, "bold"),
                                   command=lambda: controller.show_frame(Admin_User_Feedback),
                                   bg="#3C4248", fg="white", bd=0).place(x=35, y=393)  # bg="light grey"
        self.bg9 = ImageTk.PhotoImage(file="C:/Users/Swaraj/Desktop/Icons/Icons/feedback.png")
        events_icon9 = Label(side_card, bg="#3C4248", fg="light grey", image=self.bg9).place(x=7, y=400)

        # --Registered Users--#
        btn_registered_user = Button(side_card, text="Reg. Users", font=("Helvetica", 18, "bold"),
                                     command=lambda: controller.show_frame(Admin_Registered_Users),
                                     bg="#3C4248", fg="white", bd=0).place(x=35, y=435)  # bg="light grey"
        self.bg10 = ImageTk.PhotoImage(file="C:/Users/Swaraj/Desktop/Icons/Icons/reg_users.png")
        events_icon10 = Label(side_card, bg="#3C4248", fg="light grey", image=self.bg10).place(x=9, y=442)

        # WHITE FRAME
        self.event_frame = Frame(self, bg="white")
        self.event_frame.place(x=370, y=180, width=1000, height=500)

        # Title
        title = Label(self.event_frame, text="REGISTERED USERS", font=("Times New Roman", 25, "bold", "underline"), bg="white",
                      fg="#08A3D2").place(x=20, y=20)

        # --Event ID--#
        event_id = Label(self.event_frame, text="Event ID:", font=("Times New Roman", 18, "bold"), bg="white",
                         fg="#2C3539").place(x=63, y=100)
        self.txt_event_id = Entry(self.event_frame, relief="solid", font=("Times New Roman", 18), bg="lightgray")
        self.txt_event_id.place(x=180, y=100, width=50, height=35)

        self.search = ImageTk.PhotoImage(file="C:/Users/Swaraj/Desktop/Icons/Icons/Search.png")
        events_search = Button(self.event_frame, bg="white", bd=0, fg="light grey", command=self.search2,
                               image=self.search).place(x=245, y=98, width=25, height=33)

        columns = ('1', '2')
        columns2 = ('1', '2', '3')

        self.table = tkinter.ttk.Treeview(self.event_frame, columns=columns, show="headings", selectmode='browse')
        self.table.place(x=150, y=170, width=200, height=250)

        self.table2 = tkinter.ttk.Treeview(self.event_frame, columns=columns2, show="headings", selectmode='browse')
        self.table2.place(x=350, y=170, width=500, height=250)

        style = tkinter.ttk.Style()
        style.theme_use("clam")

        # define headings
        self.table.heading('1', text='Registration ID')
        self.table.heading('2', text='Username')
        self.table.column("1", width=70, anchor='c')
        self.table.column("2", width=80, anchor='c')

        self.table2.heading('1', text='First Name')
        self.table2.heading('2', text='Last Name')
        self.table2.heading('3', text='Phone Number')
        self.table2.column("1", width=80, anchor='c')
        self.table2.column("2", width=80, anchor='c')
        self.table2.column("3", width=80, anchor='c')

        # --Count--#
        count = Label(self.event_frame, text="Count:", font=("Times New Roman", 18, "bold"), bg="white", fg="#2C3539").place(x=720, y=98)
        self.txt_count = Entry(self.event_frame, relief="solid", font=("Times New Roman", 18), bg="lightgray")
        self.txt_count.place(x=800, y=98, width=50, height=35)

    def refresh(self):
        for i in self.table.get_children():
            self.table.delete(i)
        for j in self.table2.get_children():
            self.table2.delete(j)
        try:
            con = pymysql.connect(host="localhost", user="root", password="root", db="event_management", port=3307)
            cur = con.cursor()

            cur.execute(
                "SELECT reg_id, username FROM user_register where event_id=%s",
                (
                    self.txt_event_id.get()
                ))
            rows = cur.fetchall()
            con.commit()
            con.close()

            if len(rows) < 1:
                messagebox.showerror("Error", "No Registered Users", parent=self)

            lst3 = []
            for j in range(0, len(rows)):
                lst3.append(rows[j][1])

            for i in rows:
                self.table.insert('', 'end', values=i)

        except Exception as es:
            messagebox.showerror("Error", f"Error Due to: {str(es)}", parent=self)

        for y in lst3:
            try:
                con = pymysql.connect(host="localhost", user="root", password="root", db="event_management", port=3307)
                cur = con.cursor()

                cur.execute(
                    "SELECT f_name,l_name,ph_no FROM customer where username=%s",
                    (
                        y
                    ))
                rows2 = cur.fetchall()
                con.commit()
                con.close()

                for i in rows2:
                    self.table2.insert('', 'end', values=i)

            except Exception as es:
                messagebox.showerror("Error", f"Error Due to: {str(es)}", parent=self)

        # --Count--#
        self.txt_count.config(state=NORMAL)
        self.txt_count.delete(0, END)
        self.txt_count.config(state=DISABLED)

        try:
            con = pymysql.connect(host="localhost", user="root", password="root", db="event_management", port=3307)
            cur = con.cursor()

            cur.execute(
                "SELECT count(reg_id) from user_register where event_id=%s",
                (
                    self.txt_event_id.get()
                ))
            count = cur.fetchone()
            con.commit()
            con.close()

            self.txt_count.config(state=NORMAL)
            self.txt_count.insert(END, count)
            self.txt_count.config(state=DISABLED)

        except Exception as es:
            messagebox.showerror("Error", f"Error Due to: {str(es)}", parent=self)

    def search2(self):
        for i in self.table.get_children():
            self.table.delete(i)
        for j in self.table2.get_children():
            self.table2.delete(j)
        try:
            con = pymysql.connect(host="localhost", user="root", password="root", db="event_management", port=3307)
            cur = con.cursor()

            cur.execute(
                "SELECT reg_id, username FROM user_register where event_id=%s",
                (
                    self.txt_event_id.get()
                ))
            rows = cur.fetchall()
            con.commit()
            con.close()

            if len(rows) < 1:
                messagebox.showerror("Error", "No Registered Users", parent=self)

            lst = []
            for j in range(0, len(rows)):
                lst.append(rows[j][1])

            for i in rows:
                self.table.insert('', 'end', values=i)

        except Exception as es:
            messagebox.showerror("Error", f"Error Due to: {str(es)}", parent=self)

        for y in lst:
            try:
                con = pymysql.connect(host="localhost", user="root", password="root", db="event_management", port=3307)
                cur = con.cursor()

                cur.execute(
                    "SELECT f_name,l_name,ph_no FROM customer where username=%s",
                    (
                        y
                    ))
                rows2 = cur.fetchall()
                con.commit()
                con.close()

                for i in rows2:
                    self.table2.insert('', 'end', values=i)

            except Exception as es:
                messagebox.showerror("Error", f"Error Due to: {str(es)}", parent=self)

        # --Count--#
        self.txt_count.config(state=NORMAL)
        self.txt_count.delete(0, END)
        self.txt_count.config(state=DISABLED)
        try:
            con = pymysql.connect(host="localhost", user="root", password="root", db="event_management", port=3307)
            cur = con.cursor()

            cur.execute(
                "SELECT count(reg_id) from user_register where event_id=%s",
                (
                    self.txt_event_id.get()
                ))
            print(self.txt_event_id.get())
            count = cur.fetchone()
            print(count)
            con.commit()
            con.close()

            self.txt_count.config(state=NORMAL)
            self.txt_count.insert(END, count)
            self.txt_count.config(state=DISABLED)



        except Exception as es:
            messagebox.showerror("Error", f"Error Due to: {str(es)}", parent=self)

            # ------------------- CUSTOMER EVENT REQUEST-------------------- #


class User_Event_Request(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.controller = controller
        self.config(bg="#F6F7F7")  # for solid bg

        # Blue Frame
        frame_1 = Frame(self, bg="#1589FF")
        frame_1.place(x=220, y=0, width=1920, height=40)

        # Title
        title = Label(frame_1, text="Event Management System", font=("Times New Roman", 20, "bold"), bg="#1589FF",
                      fg="white").place(x=10, y=0)

        # Refresh Button
        home = Button(frame_1, cursor="hand2", command=self.refresh, text="Refresh",
                      font=("Times New Roman", 14, "bold"), bg="#1589FF", bd=0,
                      fg="white").place(x=1000, y=3)

        # Contact Us Button
        contact_us = Button(frame_1, cursor="hand2", text="Contact Us", font=("Times New Roman", 14, "bold"), command=lambda: controller.show_frame(User_Contact_Us),
                            bg="#1589FF", bd=0, fg="white").place(x=1100, y=3)

        # Logout Button
        logout = Button(frame_1, cursor="hand2", command=lambda: controller.show_frame(Customer_Login), text="Logout",
                        font=("Times New Roman", 14, "bold"), bg="#1589FF", bd=0, fg="white").place(x=1230, y=3)

        # --GREY FRAME--#
        side_card = Frame(self, bg="#3C4248")
        side_card.place(x=0, y=0, width=225, height=1080)
        line_card = Frame(self, bg="white")
        line_card.place(x=0, y=45, width=225, height=1)

        # b = self.controller.app_data["admin"].get()
        title = Label(side_card, text="Welcome User", font=("Times New Roman", 20, "bold"), bg="#3C4248",
                      fg="white").place(x=10, y=0)

        # --DASHBOARD--#
        btn_dashboard = Button(side_card, text="Home", command=lambda: controller.show_frame(User_Dashboard),
                               font=("Helvetica", 18, "bold"),
                               bg="#3C4248", fg="white", bd=0).place(x=40, y=60)  # bg="light grey"
        self.bg4 = ImageTk.PhotoImage(file="C:/Users/Swaraj/Desktop/Icons/Icons/dashboard.png")
        events_icon4 = Label(side_card, bg="#3C4248", fg="light grey", image=self.bg4).place(x=10, y=70)

        # --EVENTS--#
        lb_events_side = Label(side_card, text="Events", font=("Helvetica", 20, "bold"), bg="#3C4248",
                               fg="light grey").place(x=40, y=130)
        self.bg = ImageTk.PhotoImage(file="C:/Users/Swaraj/Desktop/Icons/Icons/calendar.png")
        events_icon = Label(side_card, bg="#3C4248", fg="light grey", image=self.bg).place(x=10, y=135)
        self.bg2 = ImageTk.PhotoImage(file="C:/Users/Swaraj/Desktop/Icons/Icons/right-arrow.png")
        events_icon2 = Label(side_card, bg="#3C4248", fg="light grey", image=self.bg2).place(x=150, y=140)

        # --REQUEST EVENT--#
        btn_events_create = Button(side_card, command=lambda: controller.show_frame(User_Event_Request),
                                   text="Request Events", font=("Helvetica", 18, "bold"), bg="#3C4248",
                                   fg="white", bd=0).place(x=35, y=170)  # bg="light grey"
        self.bg3 = ImageTk.PhotoImage(file="C:/Users/Swaraj/Desktop/Icons/Icons/calendar_add.png")
        events_icon3 = Label(side_card, bg="#3C4248", fg="light grey", image=self.bg3).place(x=10, y=180)

        # --EVENT LIST--#
        btn_events_list = Button(side_card, text="Event List", font=("Helvetica", 18, "bold"),
                                 command=lambda: controller.show_frame(User_EventList),
                                 bg="#3C4248", fg="white", bd=0).place(x=35, y=214)  # bg="light grey"
        self.bg7 = ImageTk.PhotoImage(file="C:/Users/Swaraj/Desktop/Icons/Icons/list.png")
        events_icon7 = Label(side_card, bg="#3C4248", fg="light grey", image=self.bg7).place(x=13, y=225)

        # WHITE FRAME
        self.event_frame = Frame(self, bg="white")
        self.event_frame.place(x=265, y=75, width=1225, height=720)

        title = Label(self.event_frame, text="REQUEST FOR AN EVENT", font=("Times New Roman", 20, "bold", "underline"),
                      bg="white", fg="#08A3D2").place(x=490, y=20)

        # --Request ID--#
        request_id = Label(self.event_frame, text="Request ID:", font=("Times New Roman", 18, "bold"), bg="white",
                         fg="#2C3539").place(x=45, y=100)
        self.txt_request_id = Entry(self.event_frame, relief="solid", font=("Times New Roman", 18), bg="lightgray")
        self.txt_request_id.place(x=180, y=100, width=60, height=35)

        k = random.randint(0, 9999)
        self.txt_request_id.insert(END, k)
        self.txt_request_id.config(state=DISABLED)

        # --EVENT NAME--#
        event_name = Label(self.event_frame, text="Event Name:", font=("Times New Roman", 18, "bold"), bg="white",
                           fg="#2C3539").place(x=33, y=160)
        self.txt_event_name = Entry(self.event_frame, relief="solid", font=("Times New Roman", 18), bg="lightgray")
        self.txt_event_name.place(x=180, y=160, width=320, height=35)

        # --DATE OF EVENT--#
        date_event = Label(self.event_frame, text="Date of Event:", font=("Times New Roman", 18, "bold"), bg="white",
                           fg="#2C3539").place(x=525, y=160)
        self.txt_date_event = Entry(self.event_frame, relief="solid", font=("Times New Roman", 18), bg="lightgray",
                                    fg="black")
        self.txt_date_event.place(x=678, y=160, width=175, height=35)
        #self.txt_date_event.insert(END, "DD/MM/YYYY")
        # self.txt_date_event.config(state=DISABLED)
        # self.txt_date_event.bind("<Button-1>", focus)

        # --TIMING--#
        start_time = Label(self.event_frame, text="Timing:", font=("Times New Roman", 18, "bold"), bg="white",
                           fg="#2C3539").place(x=85, y=220)
        self.txt_start_time = Entry(self.event_frame, relief="solid", font=("Times New Roman", 18), bg="lightgray",
                                    fg="black")
        self.txt_start_time.place(x=180, y=220, width=110, height=35)
        #self.txt_start_time.insert(END, "HH:MM")

        end_time = Label(self.event_frame, text="--", font=("Times New Roman", 18, "bold"), bg="white",
                         fg="#2C3539").place(x=295, y=220)
        self.txt_end_time = Entry(self.event_frame, relief="solid", font=("Times New Roman", 18), bg="lightgray",
                                  fg="black")
        self.txt_end_time.place(x=325, y=220, width=110, height=35)
        #self.txt_end_time.insert(END, "HH:MM")

        # --DURATION--#
        event_duration = Label(self.event_frame, text="Duration:", font=("Times New Roman", 18, "bold"), bg="white",
                               fg="#2C3539").place(x=527, y=220)
        self.txt_event_duration = Entry(self.event_frame, relief="solid", font=("Times New Roman", 18), bg="lightgray")
        self.txt_event_duration.place(x=635, y=220, width=50, height=35)
        event_duration_days = Label(self.event_frame, text="day(s)", font=("Times New Roman", 18, "bold"), bg="white",
                                    fg="#2C3539").place(x=690, y=220)

        # --Maximum Guest--#
        max_guest = Label(self.event_frame, text="Max. Guest:", font=("Times New Roman", 18, "bold"), bg="white",
                          fg="#2C3539").place(x=40, y=280)
        self.txt_max_guest = Entry(self.event_frame, relief="solid", font=("Times New Roman", 18), bg="lightgray")
        self.txt_max_guest.place(x=180, y=280, width=175, height=35)

        # --Venue--#
        venue = Label(self.event_frame, text="Venue:", font=("Times New Roman", 18, "bold"), bg="white",
                      fg="#2C3539").place(x=92, y=340)
        self.txt_venue = Entry(self.event_frame, relief="solid", font=("Times New Roman", 18), bg="lightgray")
        self.txt_venue.place(x=180, y=340, width=250, height=35)

        # --Contact No--#
        contact_no = Label(self.event_frame, text="Contact No.:", font=("Times New Roman", 18, "bold"), bg="white",
                           fg="#2C3539").place(x=33, y=400)
        self.txt_contact_no = Entry(self.event_frame, relief="solid", font=("Times New Roman", 18), bg="lightgray")
        self.txt_contact_no.place(x=180, y=400, width=150, height=35)

        # --DESCRIPTION--#
        event_description = Label(self.event_frame, text="Description:", font=("Times New Roman", 18, "bold"),
                                  bg="white",
                                  fg="#2C3539").place(x=37, y=460)
        self.event_description = Text(self.event_frame, relief="solid", font=("Times New Roman", 18), bg="lightgray")
        self.event_description.place(x=180, y=460, width=250, height=150)

        # --REQUEST BUTTON--#
        btn_create = Button(self.event_frame, text="Request", command=self.event, font=("Times New Roman", 20, "bold"),
                            fg="white", bg="#B00857", cursor="hand2").place(x=400, y=635, width=180, height=40)

    def clear(self):
        # self.txt_request_id.delete(0, END)
        self.txt_event_name.delete(0, END)
        self.txt_date_event.delete(0, END)
        self.txt_event_duration.delete(0, END)
        self.txt_start_time.delete(0, END)
        self.txt_end_time.delete(0, END)
        self.txt_max_guest.delete(0, END)
        self.txt_venue.delete(0, END)
        self.txt_contact_no.delete(0, END)
        self.event_description.delete(1.0, END)

    def event(self):
        if self.txt_event_name.get() == "" or self.txt_date_event.get() == "" or self.txt_event_duration.get() == "" or self.txt_start_time.get() == "" or self.txt_end_time.get() == "" or self.txt_max_guest.get() == "" or self.txt_venue.get() == "" or self.txt_contact_no.get() == "" or self.event_description.get(1.0, END) == "" :
            messagebox.showerror("Error", "All Fields are Required", parent=self)

        else:
            try:
                con = pymysql.connect(host="localhost", user="root", password="root", db="event_management", port=3307)
                cur = con.cursor()
                cur.execute(
                    "INSERT INTO user_event_request (req_id, event_name, event_date, start_time, end_time, duration, max_guest, venue, contact_no, description) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                    (
                        self.txt_request_id.get(),
                        self.txt_event_name.get(),
                        self.txt_date_event.get(),
                        self.txt_start_time.get(),
                        self.txt_end_time.get(),
                        self.txt_event_duration.get(),
                        self.txt_max_guest.get(),
                        self.txt_venue.get(),
                        self.txt_contact_no.get(),
                        self.event_description.get(1.0, END)
                    ))
                con.commit()
                messagebox.showinfo("Alert", "Event Request Successful", parent=self)

                self.clear()
                self.controller.show_frame(User_Event_Request)
                con.close()

            except Exception as es:
                messagebox.showerror("Error", f"Error Due to: {str(es)}", parent=self)

    def refresh(self):
        self.txt_request_id.config(state=NORMAL)
        self.txt_request_id.delete(0, END)
        k = random.randint(0, 9999)
        self.txt_request_id.insert(END, k)
        self.txt_request_id.config(state=DISABLED)
        self.clear()
        # self.txt_start_time.insert(END, "HH:MM")
        # self.txt_end_time.insert(END, "HH:MM")
        # self.txt_date_event.insert(END, "DD/MM/YYYY")

        # ------------------- ADMIN EVENT REQUEST LIST-------------------- #


class Admin_EventRequest(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.controller = controller
        self.config(bg="#F6F7F7")  # for solid bg

        # Blue Frame
        frame_1 = Frame(self, bg="#1589FF")
        frame_1.place(x=220, y=0, width=1920, height=40)

        # Title
        title = Label(frame_1, text="Event Management System", font=("Times New Roman", 20, "bold"), bg="#1589FF",
                      fg="white").place(x=10, y=0)

        # Refresh Button
        home = Button(frame_1, cursor="hand2", command=self.refresh, text="Refresh",
                      font=("Times New Roman", 14, "bold"), bg="#1589FF", bd=0,
                      fg="white").place(x=1125, y=3)

        # Logout Button
        logout = Button(frame_1, cursor="hand2", command=lambda: controller.show_frame(Admin_Login), text="Logout",
                        font=("Times New Roman", 14, "bold"), bg="#1589FF", bd=0, fg="white").place(x=1230, y=3)

        # --GREY FRAME--#
        side_card = Frame(self, bg="#3C4248")
        side_card.place(x=0, y=0, width=225, height=1080)
        line_card = Frame(self, bg="white")
        line_card.place(x=0, y=45, width=225, height=1)

        # b = self.controller.app_data["admin"].get()
        title = Label(side_card, text="Welcome Admin", font=("Times New Roman", 20, "bold"), bg="#3C4248",
                      fg="white").place(x=10, y=0)

        # --DASHBOARD--#
        btn_dashboard = Button(side_card, text="Dashboard", command=lambda: controller.show_frame(Admin_Dashboard),
                               font=("Helvetica", 18, "bold"),
                               bg="#3C4248", fg="white", bd=0).place(x=40, y=60)  # bg="light grey"
        self.bg4 = ImageTk.PhotoImage(file="C:/Users/Swaraj/Desktop/Icons/Icons/dashboard.png")
        events_icon4 = Label(side_card, bg="#3C4248", fg="light grey", image=self.bg4).place(x=10, y=70)

        # --EVENTS--#
        lb_events_side = Label(side_card, text="Events", font=("Helvetica", 20, "bold"), bg="#3C4248",
                               fg="light grey").place(x=40, y=130)
        self.bg = ImageTk.PhotoImage(file="C:/Users/Swaraj/Desktop/Icons/Icons/calendar.png")
        events_icon = Label(side_card, bg="#3C4248", fg="light grey", image=self.bg).place(x=10, y=135)
        self.bg2 = ImageTk.PhotoImage(file="C:/Users/Swaraj/Desktop/Icons/Icons/right-arrow.png")
        events_icon2 = Label(side_card, bg="#3C4248", fg="light grey", image=self.bg2).place(x=150, y=140)

        # --CREATE EVENT--#
        btn_events_create = Button(side_card, command=lambda: controller.show_frame(Admin_CreateEvent),
                                   text="Create Events", font=("Helvetica", 18, "bold"), bg="#3C4248",
                                   fg="white", bd=0).place(x=35, y=170)  # bg="light grey"
        self.bg3 = ImageTk.PhotoImage(file="C:/Users/Swaraj/Desktop/Icons/Icons/calendar_add.png")
        events_icon3 = Label(side_card, bg="#3C4248", fg="light grey", image=self.bg3).place(x=10, y=180)

        # --CREATE THEME--#
        btn_theme_create = Button(side_card, text="Create Theme", command=lambda: controller.show_frame(Admin_Theme),
                                  font=("Helvetica", 18, "bold"), bg="#3C4248", fg="white", bd=0).place(x=35, y=215)
        self.bg8 = ImageTk.PhotoImage(file="C:/Users/Swaraj/Desktop/Icons/Icons/12.png")
        events_icon3 = Label(side_card, bg="#3C4248", fg="light grey", image=self.bg8).place(x=10, y=225)

        # --MODIFY EVENT--#
        btn_events_mod = Button(side_card, text="Modify Event",
                                command=lambda: controller.show_frame(Admin_ModifyEvent),
                                font=("Helvetica", 18, "bold"),
                                bg="#3C4248", fg="white", bd=0).place(x=35, y=260)  # bg="light grey"
        self.bg5 = ImageTk.PhotoImage(file="C:/Users/Swaraj/Desktop/Icons/Icons/calendar_mod.png")
        events_icon5 = Label(side_card, bg="#3C4248", fg="light grey", image=self.bg5).place(x=10, y=270)

        # --EVENT REQUESTS--#
        btn_events_request = Button(side_card, text="Event Requests", font=("Helvetica", 18, "bold"), command=lambda: controller.show_frame(Admin_EventRequest),
                                    bg="#3C4248", fg="white", bd=0).place(x=35, y=305)  # bg="light grey"
        self.bg6 = ImageTk.PhotoImage(file="C:/Users/Swaraj/Desktop/Icons/Icons/calendar_notification.png")
        events_icon6 = Label(side_card, bg="#3C4248", fg="light grey", image=self.bg6).place(x=10, y=315)

        # --EVENT LIST--#
        btn_events_list = Button(side_card, text="Event List", font=("Helvetica", 18, "bold"), command=lambda: controller.show_frame(Admin_EventList),
                                 bg="#3C4248", fg="white", bd=0).place(x=35, y=350)  # bg="light grey"
        self.bg7 = ImageTk.PhotoImage(file="C:/Users/Swaraj/Desktop/Icons/Icons/list.png")
        events_icon7 = Label(side_card, bg="#3C4248", fg="light grey", image=self.bg7).place(x=10, y=360)

        event_list_frame = Frame(self, bg="white")
        event_list_frame.place(x=265, y=125, width=1225, height=600)

        # --User Feedback--#
        btn_user_feedback = Button(side_card, text="User Feedback", font=("Helvetica", 18, "bold"),
                                   command=lambda: controller.show_frame(Admin_User_Feedback),
                                   bg="#3C4248", fg="white", bd=0).place(x=35, y=393)  # bg="light grey"
        self.bg9 = ImageTk.PhotoImage(file="C:/Users/Swaraj/Desktop/Icons/Icons/feedback.png")
        events_icon9 = Label(side_card, bg="#3C4248", fg="light grey", image=self.bg9).place(x=7, y=400)

        # --Registered Users--#
        btn_registered_user = Button(side_card, text="Reg. Users", font=("Helvetica", 18, "bold"),
                                     command=lambda: controller.show_frame(Admin_Registered_Users),
                                     bg="#3C4248", fg="white", bd=0).place(x=35, y=435)  # bg="light grey"
        self.bg10 = ImageTk.PhotoImage(file="C:/Users/Swaraj/Desktop/Icons/Icons/reg_users.png")
        events_icon10 = Label(side_card, bg="#3C4248", fg="light grey", image=self.bg10).place(x=9, y=442)

        # WHITE FRAME
        title = Label(event_list_frame, text="REQUESTED EVENTS", font=("Times New Roman", 20, "bold", "underline"), bg="white",
                      fg="#08A3D2").place(x=50, y=20)

        # Request ID
        request_id = Label(event_list_frame, text="Request ID:", font=("Times New Roman", 18, "bold"), bg="white",
                         fg="#2C3539").place(x=900, y=20)
        self.txt_request_id = Entry(event_list_frame, relief="solid", font=("Times New Roman", 18), bg="lightgray")
        self.txt_request_id.place(x=1030, y=20, width=60, height=35)

        # Search Button
        self.search = ImageTk.PhotoImage(file="C:/Users/Swaraj/Desktop/Icons/Icons/Search.png")
        events_search = Button(event_list_frame, bg="white", bd=0, fg="light grey", command=self.search2,
                               image=self.search).place(x=1100, y=20, width=25, height=33)

        # Marked as Done button
        self.done = ImageTk.PhotoImage(file="C:/Users/Swaraj/Desktop/Icons/Icons/tick.png")
        events_done = Button(event_list_frame, bg="white", bd=0, fg="light grey", command=self.done2, image=self.done).place(x=1140, y=20, width=25, height=33)

        # Table
        columns = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10')

        self.table = tkinter.ttk.Treeview(event_list_frame, columns=columns, show="headings", selectmode='browse')
        self.table.place(x=50, y=75, width=1150, height=500)

        verscrlbar = tkinter.ttk.Scrollbar(event_list_frame, orient="horizontal", command=self.table.xview)

        # Calling pack method w.r.to verical
        # scrollbar
        verscrlbar.place(x=51, y=560, width=1148)

        # Configuring treeview
        self.table.configure(xscrollcommand=verscrlbar.set)

        # style = tkinter.ttk.Style()
        # style.theme_use("clam")

        # Define headings
        self.table.heading('1', text='Request ID')
        self.table.heading('2', text='Event Name')
        self.table.heading('3', text='Event Date')
        self.table.heading('4', text='Start Time')
        self.table.heading('5', text='End Time')
        self.table.heading('6', text='Event Duration')
        self.table.heading('7', text='Max.Guest')
        self.table.heading('8', text='Venue')
        self.table.heading('9', text='Contact Number')
        self.table.heading('10', text='Event Description')

        self.table.column("1", width=50, anchor='c')
        self.table.column("2", width=100, anchor='c')
        self.table.column("3", width=120, anchor='c')
        self.table.column("4", width=90, anchor='c')
        self.table.column("5", width=80, anchor='c')
        self.table.column("6", width=60, anchor='c')
        self.table.column("7", width=60, anchor='c')
        self.table.column("8", width=90, anchor='c')
        self.table.column("9", width=90, anchor='c')
        self.table.column("10", width=90, anchor='c')

        try:
            con = pymysql.connect(host="localhost", user="root", password="root", db="event_management", port=3307)
            cur = con.cursor()

            cur.execute("SELECT * FROM user_event_request")
            rows = cur.fetchall()
            con.commit()
            con.close()

            for i in rows:
                self.table.insert('', 'end', values=i)

        except Exception as es:
            messagebox.showerror("Error", f"Error Due to: {str(es)}", parent=self)

    def refresh(self):
        self.txt_request_id.delete(0, END)
        try:
            con = pymysql.connect(host="localhost", user="root", password="root", db="event_management", port=3307)
            cur = con.cursor()

            cur.execute("SELECT * FROM user_event_request")
            rows2 = cur.fetchall()
            con.commit()
            con.close()

            for i in self.table.get_children():
                self.table.delete(i)

        except Exception as es:
            messagebox.showerror("Error", f"Error Due to: {str(es)}", parent=self)

        try:
            con = pymysql.connect(host="localhost", user="root", password="root", db="event_management", port=3307)
            cur = con.cursor()

            cur.execute("SELECT * FROM user_event_request")
            rows = cur.fetchall()
            con.commit()
            con.close()

            for i in rows:
                self.table.insert('', 'end', values=i)

        except Exception as es:
            messagebox.showerror("Error", f"Error Due to: {str(es)}", parent=self)
    def search2(self):

        for i in self.table.get_children():
            self.table.delete(i)
        try:
            con = pymysql.connect(host="localhost", user="root", password="root", db="event_management", port=3307)
            cur = con.cursor()

            cur.execute(
                "SELECT * FROM user_event_request where req_id=%s",
                (
                    self.txt_request_id.get()
                ))
            rows = cur.fetchall()
            con.commit()
            con.close()

            if len(rows) < 1:
                messagebox.showerror("Error", "Invalid Request ID", parent=self)

            for i in rows:
                self.table.insert('', 'end', values=i)

        except Exception as es:
            messagebox.showerror("Error", f"Error Due to: {str(es)}", parent=self)

    def done2(self):
        try:
            con = pymysql.connect(host="localhost", user="root", password="root", db="event_management", port=3307)
            cur = con.cursor()

            cur.execute(
                "SELECT * FROM user_event_request where req_id=%s",
                (
                    self.txt_request_id.get()
                ))
            rows = cur.fetchall()
            con.commit()
            con.close()

        except Exception as es:
            messagebox.showerror("Error", f"Error Due to: {str(es)}", parent=self)

        if len(rows) < 1:
                messagebox.showerror("Error", "Invalid Request ID", parent=self)

        else:
            msgBox = messagebox.askquestion('Confirm', 'Marked as Done?', icon='warning')
            if msgBox == 'yes':
                for i in self.table.get_children():
                    self.table.delete(i)
                try:
                    con = pymysql.connect(host="localhost", user="root", password="root", db="event_management",
                                          port=3307)
                    cur = con.cursor()

                    cur.execute(
                        "DELETE FROM user_event_request WHERE req_id=%s",
                        (
                            self.txt_request_id.get()
                        ))
                    con.commit()
                    con.close()

                except Exception as es:
                    messagebox.showerror("Error", f"Error Due to: {str(es)}", parent=self)

                try:
                    con = pymysql.connect(host="localhost", user="root", password="root", db="event_management",
                                          port=3307)
                    cur = con.cursor()

                    cur.execute("SELECT * FROM user_event_request")
                    rows2 = cur.fetchall()
                    con.commit()
                    con.close()

                    self.txt_request_id.delete(0, END)
                    for i in self.table.get_children():
                        self.table.delete(i)

                    for j in rows2:
                        self.table.insert('', 'end', values=j)

                except Exception as es:
                    messagebox.showerror("Error", f"Error Due to: {str(es)}", parent=self)

        # ------------------- CUSTOMER EVENT REQUEST LIST-------------------- #


class User_EventList(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.controller = controller
        self.config(bg="#F6F7F7")  # for solid bg

        # Blue Frame
        frame_1 = Frame(self, bg="#1589FF")
        frame_1.place(x=220, y=0, width=1920, height=40)

        # Title
        title = Label(frame_1, text="Event Management System", font=("Times New Roman", 20, "bold"), bg="#1589FF",
                      fg="white").place(x=10, y=0)

        # Refresh Button
        home = Button(frame_1, cursor="hand2", command=self.refresh, text="Refresh",
                      font=("Times New Roman", 14, "bold"), bg="#1589FF", bd=0,
                      fg="white").place(x=1000, y=3)

        # Contact Us Button
        contact_us = Button(frame_1, cursor="hand2", text="Contact Us", font=("Times New Roman", 14, "bold"), command=lambda: controller.show_frame(User_Contact_Us),
                            bg="#1589FF", bd=0, fg="white").place(x=1100, y=3)

        # Logout Button
        logout = Button(frame_1, cursor="hand2", command=lambda: controller.show_frame(Admin_Login), text="Logout",
                        font=("Times New Roman", 14, "bold"), bg="#1589FF", bd=0, fg="white").place(x=1230, y=3)

        # --GREY FRAME--#
        side_card = Frame(self, bg="#3C4248")
        side_card.place(x=0, y=0, width=225, height=1080)
        line_card = Frame(self, bg="white")
        line_card.place(x=0, y=45, width=225, height=1)

        # b = self.controller.app_data["admin"].get()
        title = Label(side_card, text="Welcome User", font=("Times New Roman", 20, "bold"), bg="#3C4248",
                      fg="white").place(x=10, y=0)

        # --DASHBOARD--#
        btn_dashboard = Button(side_card, text="Home", command=lambda: controller.show_frame(User_Dashboard),
                               font=("Helvetica", 18, "bold"),
                               bg="#3C4248", fg="white", bd=0).place(x=40, y=60)  # bg="light grey"
        self.bg4 = ImageTk.PhotoImage(file="C:/Users/Swaraj/Desktop/Icons/Icons/dashboard.png")
        events_icon4 = Label(side_card, bg="#3C4248", fg="light grey", image=self.bg4).place(x=10, y=70)

        # --EVENTS--#
        lb_events_side = Label(side_card, text="Events", font=("Helvetica", 20, "bold"), bg="#3C4248",
                               fg="light grey").place(x=40, y=130)
        self.bg = ImageTk.PhotoImage(file="C:/Users/Swaraj/Desktop/Icons/Icons/calendar.png")
        events_icon = Label(side_card, bg="#3C4248", fg="light grey", image=self.bg).place(x=10, y=135)
        self.bg2 = ImageTk.PhotoImage(file="C:/Users/Swaraj/Desktop/Icons/Icons/right-arrow.png")
        events_icon2 = Label(side_card, bg="#3C4248", fg="light grey", image=self.bg2).place(x=150, y=140)

        # --REQUEST EVENT--#
        btn_events_create = Button(side_card, command=lambda: controller.show_frame(User_Event_Request),
                                   text="Request Events", font=("Helvetica", 18, "bold"), bg="#3C4248",
                                   fg="white", bd=0).place(x=35, y=170)  # bg="light grey"
        self.bg3 = ImageTk.PhotoImage(file="C:/Users/Swaraj/Desktop/Icons/Icons/calendar_add.png")
        events_icon3 = Label(side_card, bg="#3C4248", fg="light grey", image=self.bg3).place(x=10, y=180)

        # --EVENT LIST--#
        btn_events_list = Button(side_card, text="Event List", font=("Helvetica", 18, "bold"),
                                 command=lambda: controller.show_frame(User_EventList),
                                 bg="#3C4248", fg="white", bd=0).place(x=35, y=214)  # bg="light grey"
        self.bg7 = ImageTk.PhotoImage(file="C:/Users/Swaraj/Desktop/Icons/Icons/list.png")
        events_icon7 = Label(side_card, bg="#3C4248", fg="light grey", image=self.bg7).place(x=13, y=225)

        # WHITE FRAME
        event_list_frame = Frame(self, bg="white")
        event_list_frame.place(x=265, y=125, width=1225, height=600)
        title = Label(event_list_frame, text="EVENT LIST", font=("Times New Roman", 20, "bold", "underline"), bg="white",
                      fg="#08A3D2").place(x=520, y=20)

        columns = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12')

        self.table = tkinter.ttk.Treeview(event_list_frame, columns=columns, show="headings", selectmode='browse')
        self.table.place(x=50, y=75, width=1150, height=500)

        verscrlbar = tkinter.ttk.Scrollbar(event_list_frame, orient="horizontal", command=self.table.xview)

        # Calling pack method w.r.to verical
        # scrollbar
        verscrlbar.place(x=51, y=557, width=1148)

        # Configuring treeview
        self.table.configure(xscrollcommand=verscrlbar.set)

        style = tkinter.ttk.Style()
        style.theme_use("clam")

        # Define headings
        self.table.heading('1', text='Event ID')
        self.table.heading('2', text='Event Theme')
        self.table.heading('3', text='Event Name')
        self.table.heading('4', text='Event Date')
        self.table.heading('5', text='Event Duration')
        self.table.heading('6', text='Start Time')
        self.table.heading('7', text='End Time')
        self.table.heading('8', text='Max.Guest')
        self.table.heading('9', text='Venue')
        self.table.heading('10', text='Contact Number')
        self.table.heading('11', text='Event Fees')
        self.table.heading('12', text='Event Status')

        self.table.column("1", width=50, anchor='c')
        self.table.column("2", width=100, anchor='c')
        self.table.column("3", width=120, anchor='c')
        self.table.column("4", width=90, anchor='c')
        self.table.column("5", width=80, anchor='c')
        self.table.column("6", width=60, anchor='c')
        self.table.column("7", width=60, anchor='c')
        self.table.column("8", width=90, anchor='c')
        self.table.column("9", width=90, anchor='c')
        self.table.column("10", width=90, anchor='c')
        self.table.column("11", width=90, anchor='c')
        self.table.column("12", width=90, anchor='c')

        try:
            con = pymysql.connect(host="localhost", user="root", password="root", db="event_management", port=3307)
            cur = con.cursor()

            cur.execute("SELECT event_id, theme_name, event_name, event_date, event_duration, start_time, end_time, max_guest, venue, contact_no, event_fees, event_status FROM event_123")
            rows = cur.fetchall()
            con.commit()
            con.close()

            for i in rows:
                self.table.insert('', 'end', values=i)

        except Exception as es:
            messagebox.showerror("Error", f"Error Due to: {str(es)}", parent=self)

    def refresh(self):
        try:
            con = pymysql.connect(host="localhost", user="root", password="root", db="event_management", port=3307)
            cur = con.cursor()

            cur.execute("SELECT event_id, theme_name, event_name, event_date, event_duration, start_time, end_time, max_guest, venue, contact_no, event_fees, event_status FROM event_123")
            rows2 = cur.fetchall()
            con.commit()
            con.close()

            for i in self.table.get_children():
                self.table.delete(i)

                # if i not in rows2:
                #     self.table.insert('', 'end', values=i)

        except Exception as es:
            messagebox.showerror("Error", f"Error Due to: {str(es)}", parent=self)

        try:
            con = pymysql.connect(host="localhost", user="root", password="root", db="event_management", port=3307)
            cur = con.cursor()

            cur.execute("SELECT event_id, theme_name, event_name, event_date, event_duration, start_time, end_time, max_guest, venue, contact_no, event_fees, event_status FROM event_123")
            rows = cur.fetchall()
            con.commit()
            con.close()

            for i in rows:
                self.table.insert('', 'end', values=i)

        except Exception as es:
            messagebox.showerror("Error", f"Error Due to: {str(es)}", parent=self)

    # ------------------- CUSTOMER FEEDBACK-------------------- #


class User_Contact_Us(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.controller = controller
        self.config(bg="#F6F7F7")  # for solid bg

        # Blue Frame
        frame_1 = Frame(self, bg="#1589FF")
        frame_1.place(x=220, y=0, width=1920, height=40)

        # Title
        title = Label(frame_1, text="Event Management System", font=("Times New Roman", 20, "bold"), bg="#1589FF",
                      fg="white").place(x=10, y=0)

        # Refresh Button
        home = Button(frame_1, cursor="hand2", command=self.refresh, text="Refresh",
                      font=("Times New Roman", 14, "bold"), bg="#1589FF", bd=0,
                      fg="white").place(x=1000, y=3)

        # Contact Us Button
        contact_us = Button(frame_1, cursor="hand2", text="Contact Us", font=("Times New Roman", 14, "bold"), command=lambda: controller.show_frame(User_Contact_Us),
                            bg="#1589FF", bd=0, fg="white").place(x=1100, y=3)

        # Logout Button
        logout = Button(frame_1, cursor="hand2", command=lambda: controller.show_frame(Customer_Login), text="Logout",
                        font=("Times New Roman", 14, "bold"), bg="#1589FF", bd=0, fg="white").place(x=1230, y=3)

        # --GREY FRAME--#
        side_card = Frame(self, bg="#3C4248")
        side_card.place(x=0, y=0, width=225, height=1080)
        line_card = Frame(self, bg="white")
        line_card.place(x=0, y=45, width=225, height=1)

        # b = self.controller.app_data["admin"].get()
        title = Label(side_card, text="Welcome User", font=("Times New Roman", 20, "bold"), bg="#3C4248",
                      fg="white").place(x=10, y=0)

        # --DASHBOARD--#
        btn_dashboard = Button(side_card, text="Home", command=lambda: controller.show_frame(User_Dashboard),
                               font=("Helvetica", 18, "bold"),
                               bg="#3C4248", fg="white", bd=0).place(x=40, y=60)  # bg="light grey"
        self.bg4 = ImageTk.PhotoImage(file="C:/Users/Swaraj/Desktop/Icons/Icons/dashboard.png")
        events_icon4 = Label(side_card, bg="#3C4248", fg="light grey", image=self.bg4).place(x=10, y=70)

        # --EVENTS--#
        lb_events_side = Label(side_card, text="Events", font=("Helvetica", 20, "bold"), bg="#3C4248",
                               fg="light grey").place(x=40, y=130)
        self.bg = ImageTk.PhotoImage(file="C:/Users/Swaraj/Desktop/Icons/Icons/calendar.png")
        events_icon = Label(side_card, bg="#3C4248", fg="light grey", image=self.bg).place(x=10, y=135)
        self.bg2 = ImageTk.PhotoImage(file="C:/Users/Swaraj/Desktop/Icons/Icons/right-arrow.png")
        events_icon2 = Label(side_card, bg="#3C4248", fg="light grey", image=self.bg2).place(x=150, y=140)

        # --REQUEST EVENT--#
        btn_events_create = Button(side_card, command=lambda: controller.show_frame(User_Event_Request),
                                   text="Request Events", font=("Helvetica", 18, "bold"), bg="#3C4248",
                                   fg="white", bd=0).place(x=35, y=170)  # bg="light grey"
        self.bg3 = ImageTk.PhotoImage(file="C:/Users/Swaraj/Desktop/Icons/Icons/calendar_add.png")
        events_icon3 = Label(side_card, bg="#3C4248", fg="light grey", image=self.bg3).place(x=10, y=180)

        # --EVENT LIST--#
        btn_events_list = Button(side_card, text="Event List", font=("Helvetica", 18, "bold"),
                                 command=lambda: controller.show_frame(User_EventList),
                                 bg="#3C4248", fg="white", bd=0).place(x=35, y=214)  # bg="light grey"
        self.bg7 = ImageTk.PhotoImage(file="C:/Users/Swaraj/Desktop/Icons/Icons/list.png")
        events_icon7 = Label(side_card, bg="#3C4248", fg="light grey", image=self.bg7).place(x=13, y=225)

        # WHITE FRAME
        self.event_frame = Frame(self, bg="white")
        self.event_frame.place(x=265, y=75, width=1225, height=720)

        title = Label(self.event_frame, text="CONTACT US", font=("Times New Roman", 20, "bold", "underline"),
                      bg="white", fg="#08A3D2").place(x=20, y=20)

        title2 = Label(self.event_frame, text="You can reach us at:", font=("Times New Roman", 18, "bold"),
                      bg="white").place(x=20, y=70)

        ph_no = Label(self.event_frame, text="Phone Number:", font=("Times New Roman", 18, "bold", "underline"),
                       bg="white").place(x=20, y=110)
        ph_no1 = Label(self.event_frame, text="+91 9757110277", font=("Times New Roman", 18),
                      bg="white").place(x=190, y=110)

        ph_no2 = Label(self.event_frame, text="+91 8850332922", font=("Times New Roman", 18),
                      bg="white").place(x=190, y=140)

        email_id = Label(self.event_frame, text="Email ID:", font=("Times New Roman", 18, "bold", "underline"),
                      bg="white").place(x=82, y=190)
        ph_no1 = Label(self.event_frame, text="eventmanagementhelp@gmail.com", font=("Times New Roman", 18),
                       bg="white").place(x=190, y=190)

        feedback = Label(self.event_frame, text="FEEDBACK", font=("Times New Roman", 20, "bold", "underline"),
                         bg="white", fg="#08A3D2").place(x=20, y=260)

        # --DESCRIPTION--#
        event_description = Label(self.event_frame, text="Description:", font=("Times New Roman", 18, "bold"),
                                  bg="white",
                                  fg="#2C3539").place(x=50, y=310)
        self.event_description = Text(self.event_frame, relief="solid", font=("Times New Roman", 18), bg="lightgray")
        self.event_description.place(x=190, y=320, width=400, height=200)

        # --SUBMIT BUTTON--#
        btn_create = Button(self.event_frame, text="Submit", command=self.event, font=("Times New Roman", 20, "bold"),
                            fg="white", bg="#B00857", cursor="hand2").place(x=310, y=550, width=180, height=40)

    def clear(self):
        # self.txt_request_id.delete(0, END)
        self.event_description.delete(1.0, END)

    def event(self):
        if self.event_description.get(1.0, END) == "":
            messagebox.showerror("Error", "Please fill the feedback field.", parent=self)

        else:
            try:
                con = pymysql.connect(host="localhost", user="root", password="root", db="event_management", port=3307)
                cur = con.cursor()
                cur.execute(
                    "INSERT INTO user_feedback (username,description) values(%s,%s)",
                    (
                        self.controller.app_data["Username"],
                        self.event_description.get(1.0, END)
                    ))
                con.commit()
                messagebox.showinfo("Alert", "Feedback Submitted Successful", parent=self)

                self.clear()
                self.controller.show_frame(User_Contact_Us)
                con.close()

            except Exception as es:
                messagebox.showerror("Error", f"Error Due to: {str(es)}", parent=self)

    def refresh(self):
        self.clear()


app = tkinterApp()
app.mainloop()
