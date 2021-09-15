from PIL import Image, ImageTk  # Install Pillow
from tkinter import * # Install future
import pymysql # Install pymysql
from tkinter import messagebox


class Login_window:
    def __init__(self, root):
        self.root = root
        self.root.title("Customer Login")
        self.root.geometry("1920x1080+0+0")
        self.root.config(bg="sky blue")  # for solid bg

        login_frame = Frame(self.root, bg="white")
        login_frame.place(x=350, y=100, width=800, height=500)

        title = Label(login_frame, text="CUSTOMER LOGIN", font=("Times New Roman", 30, "bold"), bg="white", fg="#08A3D2").place(x=250, y=50)

        username = Label(login_frame, text="Username", font=("Times New Roman", 18, "bold"), bg="white", fg="#2C3539").place(x=250, y=150)
        self.txt_username = Entry(login_frame, font=("Times New Roman", 18), bg="lightgray")
        self.txt_username.place(x=250, y=180, width=350, height=35)

        pass_ = Label(login_frame, text="Password", font=("Times New Roman", 18, "bold"), bg="white", fg="#2C3539").place(x=250, y=250)
        self.txt_pass_ = Entry(login_frame, font=("Times New Roman", 18), bg="lightgray", show="*")
        self.txt_pass_.place(x=250, y=280, width=350, height=35)

        btn_reg = Button(login_frame, cursor="hand2", command=self.register_window, text="Register new Account?", font=("Times New Roman", 14), bg="white", bd=0, fg="#B00857").place(x=250, y=320)

        btn_login = Button(login_frame, text="Login", command=self.login, font=("Times New Roman", 20, "bold"), fg="white", bg="#B00857", cursor="hand2").place(x=250, y=380, width=180, height=40)

    def register_window(self):
        self.root.destroy()
        import Customer_Registration

    def login(self):
        if self.txt_username.get() == "" or self.txt_pass_.get() == "":
            messagebox.showerror("Error", "All Fields are Required", parent=self.root)
        else:
            try:
                con = pymysql.connect(host="localhost", user="root", password="root", db="event_management", port=3307)
                cur = con.cursor()
                cur.execute("SELECT * FROM CUSTOMER WHERE USERNAME=%s and PASSWORD=%s", (self.txt_username.get(), self.txt_pass_.get()))
                row = cur.fetchone()
                if row==None:
                    messagebox.showerror("Error", "Invalid USERNAME or PASSWORD", parent=self.root)

                else:
                    messagebox.showinfo("Success", "Welcome", parent=self.root)
                    self.root.destroy()
                    import Admin_1
                con.close()

            except Exception as es:
                messagebox.showerror("Error",f"Error Due to: {str(es)}", parent=self.root)


root = Tk()
obj = Login_window(root)
root.mainloop()
