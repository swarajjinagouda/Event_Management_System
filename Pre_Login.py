from tkinter import *  # Install future
from tkinter import ttk, StringVar, messagebox
from PIL import Image, ImageTk  # Install pillow
import pymysql # Install pymysql


class Pre_Login:
    def __init__(self, root):
        self.root = root
        self.root.title("Pre Login")
        self.root.geometry("1920x1080+0+0")
        self.root.config(bg="sky blue")  # for solid bg

        frame1 = Frame(self.root, bg="#FEFCFF", relief="solid")
        frame1.place(x=650, y=440, width=240, height=230)

        # Background Image
        self.bg = ImageTk.PhotoImage(file="images/9.jpg")
        bg = Label(self.root, image=self.bg, relief="solid").place(x=250, y=50)

        login_as = Label(frame1, text="Login As", font=("Times new roman", 25, "bold"), bg="#FEFCFF", fg="black").place(x=55, y=30)# x=700, y=450

        admin_login = Button(frame1, text="Admin", font=("Times new roman", 18, "bold"), relief="solid", bg="#FEFCFF", fg="green", cursor="hand2", command=self.admin_login).place(x=78, y=85)# x=720, y=520

        customer_login = Button(frame1, text="Customer", font=("Times new roman", 18, "bold"), relief="solid", bg="#FEFCFF", fg="green", cursor="hand2", command=self.customer_login).place(x=65, y=145)# x=708, y=580

    def admin_login(self):
        self.root.destroy()
        import Admin_Login

    def customer_login(self):
        self.root.destroy()
        import Customer_Login



root = Tk()
obj = Pre_Login(root)
root.mainloop()