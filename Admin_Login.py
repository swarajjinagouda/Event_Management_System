from PIL import Image, ImageTk  # Install Pillow
from tkinter import * # Install future
import pymysql # Install pymysql
from tkinter import messagebox


class Login_window():
    def __init__(self, root):
        self.root = root
        self.root.title("Admin Login")
        self.root.geometry("1920x1080+0+0")
        self.root.config(bg="sky blue")  # for solid bg

        login_frame = Frame(self.root, bg="white")
        login_frame.place(x=350, y=100, width=800, height=500)

        title = Label(login_frame, text="ADMIN LOGIN", font=("Times New Roman", 30, "bold"), bg="white", fg="#08A3D2").place(x=250, y=50)

        username = Label(login_frame, text="Username", font=("Times New Roman", 18, "bold"), bg="white", fg="#2C3539").place(x=250, y=150)
        self.txt_username = Entry(login_frame, font=("Times New Roman", 18), bg="lightgray")
        self.txt_username.place(x=250, y=180, width=350, height=35)

        pass_ = Label(login_frame, text="Password", font=("Times New Roman", 18, "bold"), bg="white", fg="#2C3539").place(x=250, y=250)
        self.txt_pass_ = Entry(login_frame, font=("Times New Roman", 18), bg="lightgray", show="*")
        self.txt_pass_.place(x=250, y=280, width=350, height=35)

        btn_reg = Button(login_frame, cursor="hand2", command=self.register_window, text="Register new Account?", font=("Times New Roman", 14), bg="white", bd=0, fg="#B00857").place(x=250, y=320)

        btn_login = Button(login_frame, text="Login", command=self.login, font=("Times New Roman", 20, "bold"), fg="white", bg="#B00857", cursor="hand2").place(x=250, y=380, width=180, height=40)

    def register_window(self):
        self.root.withdraw()
        #self.root.deiconify()
        import Admin_Registration


    def login(self):
        if self.txt_username.get() == "" or self.txt_pass_.get() == "":
            messagebox.showerror("Error", "All Fields are Required", parent=self.root)
        else:
            try:
                con = pymysql.connect(host="localhost", user="root", password="root", db="event_management", port=3307)
                cur = con.cursor()
                cur.execute("SELECT * FROM ADMIN WHERE USERNAME=%s and PASSWORD=%s", (self.txt_username.get(), self.txt_pass_.get()))
                row = cur.fetchone()
                if row==None:
                    messagebox.showerror("Error", "Invalid USERNAME or PASSWORD", parent=self.root)

                else:
                    messagebox.showinfo("Success", "Welcome", parent=self.root)
                    self.root.withdraw()
                    #self.root.deiconify()
                    import Admin_1
                con.close()

            except Exception as es:
                messagebox.showerror("Error", f"Error Due to: {str(es)}", parent=self.root)





class Register:

    def __init__(self, root):

        self.root = root
        self.root.title("Admin Registration")
        self.root.geometry("1920x1080+0+0")
        self.root.config(bg="sky blue")  # for solid bg

        # Background Image
        # self.bg = ImageTk.PhotoImage(file="images/5.jpg")
        # bg = Label(self.root, image=self.bg).place(x=250, y=0, relwidth=1, relheight=1)

        # Left Image
        # self.left = ImageTk.PhotoImage(file="images/8.jpg")
        # left = Label(self.root,image=self.left).place(x=80,y=100,width=400,height=500)

        # Register Frame
        frame1 = Frame(self.root, bg="white")
        frame1.place(x=425, y=100, width=700, height=550)

        title = Label(frame1, text="ADMIN REGISTRATION", font=("Times new roman", 20, "bold"), bg="white", fg="green").place(x=50, y=30)

        # First Name
        f_name = Label(frame1, text="First Name:", font=("Times new roman", 15, "bold"), bg="white", fg="black").place(x=50, y=100)
        self.txt_fname = Entry(frame1, font=("Times new roman", 15), bg="lightgray", relief="solid")
        self.txt_fname.place(x=50, y=130, width=250)

        # Last Name
        l_name = Label(frame1, text="Last Name:", font=("Times new roman", 15, "bold"), bg="white", fg="black").place(x=50, y=170)  #x=370
        self.txt_lname = Entry(frame1, font=("Times new roman", 15), bg="lightgray", relief="solid")
        self.txt_lname.place(x=50, y=200, width=250)

        # Gender
        gender = Label(frame1, text="Gender:", font=("Times new roman", 15, "bold"), bg="white", fg="black").place(x=50, y=240)
        self.gender = Entry(frame1, font=("Times new roman", 15), bg="lightgray", relief="solid")
        self.gender.place(x=50, y=270, width=250)

        # self.r1 = Radiobutton(frame1, text="Male", value="Male", font=("Times new roman", 15, "bold"), bg="white", fg="black", variable=self.v)
        # self.r1.place(x=130, y=240)
        # self.r2 = Radiobutton(frame1, text="Female", value="Female", font=("Times new roman", 15, "bold"), bg="white", fg="black", variable=self.v)
        # self.r2.place(x=130, y=270)

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
        btn_register = Button(frame1, text="Register", font=("Times new roman", 13, "bold"), relief="solid", bg="white", fg="green", cursor="hand2", command=self.register_data).place(x=300, y=460)

        # Sign In Button
        sign_in_label = Label(frame1, cursor="hand2", text="Already a User?", font=("Times New Roman", 14), bg="white", fg="black").place(x=240, y=504)
        sign_in = Button(frame1, cursor="hand2", command=self.login_window, text="Sign In", relief="solid", font=("Times New Roman", 13, "bold"), bg="white", fg="green").place(x=370, y=500)




    def clear(self):
        self.txt_fname.delete(0, END)
        self.txt_lname.delete(0, END)
        self.gender.delete(0, END)
        self.txt_emailid.delete(0, END)
        self.txt_phno.delete(0, END)
        self.txt_username.delete(0, END)
        self.txt_password.delete(0, END)
        self.txt_confirmpwd.delete(0, END)

    def login_window(self):
        self.root.destroy()
        #self.root.deiconify()
        import Admin_Login

    def register_data(self):
        if self.txt_fname.get() == "" or self.txt_lname.get() == "" or self.gender.get() == "" or self.txt_emailid.get() == "" or self.txt_phno.get() == "" or self.txt_username.get() == "" or self.txt_password.get() == "" or self.txt_confirmpwd.get() == "":
            messagebox.showerror("Error", "All Fields are Required", parent=self.root)
        elif self.gender.get() != "Male" and self.gender.get() != "Female" and self.gender.get() != "male" and self.gender.get() != "female" and self.gender.get() != "MALE" and self.gender.get() != "FEMALE":
            messagebox.showerror("Error", "Input correct Gender", parent=self.root)
        # elif self.txt_emailid.get() != '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$':
            # messagebox.showerror("Error", "Enter valid Email ID", parent=self.root)
        elif self.txt_password.get() != self.txt_confirmpwd.get():
            messagebox.showerror("Error", "Password and Confirm Password should match", parent=self.root)
        elif len(self.txt_phno.get()) != 10:
            messagebox.showerror("Error", "Phone number is not valid", parent=self.root)
        else:
            try:
                con = pymysql.connect(host="localhost", user="root", password="root", db="event_management", port=3307)
                cur = con.cursor()
                cur.execute("select * from admin where username=%s", self.txt_username.get())
                row = cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error", "Username Already exists, Try Another username", parent=self.root)
                else:
                    cur.execute("insert into admin (f_name,l_name,gender,email_id,ph_no,username,password) values(%s,%s,%s,%s,%s,%s,%s)",
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
                    messagebox.showinfo("Success", "Register Successful", parent=self.root)
                    self.clear()
                    self.root.withdraw()
                 #   self.root.deiconify()
                    import Admin_Login

            except Exception as es:
                messagebox.showerror("Error", f"Error due to:{str(es)}", parent=self.root)


root = Tk()
obj1 = Register(root)
root.mainloop()


root = Tk()
obj = Login_window(root)
root.mainloop()
