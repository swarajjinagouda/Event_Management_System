from PIL import Image, ImageTk  # Install Pillow
from tkinter import * # Install future
import pymysql # Install pymysql
from tkinter import messagebox
from tkinter import ttk


class First_Page:
    def __init__(self, root):
        self.root = root
        self.root.title("Admin")
        self.root.geometry("1920x1080+0+0")
        self.root.config(bg="white")  # for solid bg

        frame_1 = Frame(self.root, bg="#1589FF")
        frame_1.place(x=220, y=0, width=1920, height=40)

        # Title
        title = Label(frame_1, text="Event Management System", font=("Times New Roman", 20, "bold"), bg="#1589FF", fg="white").place(x=10, y=0)

        # Home Button
        home = Button(frame_1, cursor="hand2", text="Home", font=("Times New Roman", 14, "bold"), bg="#1589FF", bd=0, fg="white").place(x=1000, y=3)

        # Contact Us Button
        contact_us = Button(frame_1, cursor="hand2", text="Contact Us", font=("Times New Roman", 14, "bold"), bg="#1589FF", bd=0, fg="white").place(x=1100, y=3)

        # Logout Button
        logout = Button(frame_1, cursor="hand2", command=self.login_window, text="Logout", font=("Times New Roman", 14, "bold"), bg="#1589FF", bd=0, fg="white").place(x=1230, y=3)

        # Dashboard
        dashboard = Label(text="DASHBOARD", font=("Times New Roman", 18, "bold"), bg="white",fg="green").place(x=230, y=50)

        card_1 = Frame(self.root, bg="#ef255f")
        card_1.place(x=240, y=90, width=350, height=250)
        lb_events = Label(card_1, text="Total Events", font=("Times New Roman", 20, "bold"), bg="#ef255f",
                          fg="white").place(x=100, y=200)

        lb_event_no = Label(card_1, text="2", font=("Times New Roman", 65, "bold"), bg="#ef255f",
                            fg="white").place(x=150, y=60)

        card_2 = Frame(self.root, bg="#FDD017")
        card_2.place(x=640, y=90, width=350, height=250)
        lb_events = Label(card_2, text="Users Registered", font=("Times New Roman", 20, "bold"), bg="#fccf4d",
                          fg="white").place(x=75, y=200)

        lb_event_no = Label(card_2, text="6", font=("Times New Roman", 65, "bold"), bg="#fccf4d",
                            fg="white").place(x=140, y=60)

        card_3 = Frame(self.root, bg="#49beb7")
        card_3.place(x=1040, y=90, width=350, height=250)
        lb_events = Label(card_3, text="Completed Events", font=("Times New Roman", 20, "bold"), bg="#49beb7",
                          fg="white").place(x=70, y=200)

        lb_event_no = Label(card_3, text="0", font=("Times New Roman", 65, "bold"), bg="#49beb7",
                            fg="white").place(x=145, y=60)

        side_card = Frame(self.root, bg="#3C4248")
        side_card.place(x=0, y=0, width=225, height=1080)
        line_card = Frame(self.root, bg="white")
        line_card.place(x=0, y=45, width=225, height=1)
        admin = "Swaraj"
        title = Label(side_card, text="Welcome " + admin, font=("Times New Roman", 20, "bold"), bg="#3C4248",
                      fg="white").place(x=10, y=0)

        btn_dashboard = Button(side_card, text="Dashboard", command=self.dash_window, font=("Helvetica", 18, "bold"),
                               bg="#3C4248", fg="white", bd=0).place(x=40, y=60)  # bg="light grey"

        self.bg4 = ImageTk.PhotoImage(file="C:/Users/Swaraj/Desktop/Icons/Icons/dashboard.png")
        events_icon4 = Label(side_card, bg="#3C4248", fg="light grey", image=self.bg4).place(x=10, y=70)

        lb_events_side = Label(side_card, text="Events", font=("Helvetica", 20, "bold"), bg="#3C4248",
                               fg="light grey").place(x=40, y=130)

        self.bg = ImageTk.PhotoImage(file="C:/Users/Swaraj/Desktop/Icons/Icons/calendar.png")
        events_icon = Label(side_card, bg="#3C4248", fg="light grey", image=self.bg).place(x=10, y=135)

        self.bg2 = ImageTk.PhotoImage(file="C:/Users/Swaraj/Desktop/Icons/Icons/right-arrow.png")
        events_icon2 = Label(side_card, bg="#3C4248", fg="light grey", image=self.bg2).place(x=150, y=140)

        btn_events_create = Button(side_card, text="Create Events", font=("Helvetica", 18, "bold"), bg="#3C4248",
                                   fg="white", bd=0).place(x=35, y=170)  # bg="light grey"

        self.bg3 = ImageTk.PhotoImage(file="C:/Users/Swaraj/Desktop/Icons/Icons/calendar_add.png")
        events_icon3 = Label(side_card, bg="#3C4248", fg="light grey", image=self.bg3).place(x=10, y=180)

        btn_events_mod = Button(side_card, text="Modify Event", font=("Helvetica", 18, "bold"),
                                bg="#3C4248", fg="white", bd=0).place(x=35, y=215)  # bg="light grey"

        self.bg5 = ImageTk.PhotoImage(file="C:/Users/Swaraj/Desktop/Icons/Icons/calendar_mod.png")
        events_icon5 = Label(side_card, bg="#3C4248", fg="light grey", image=self.bg5).place(x=10, y=225)

        btn_events_request = Button(side_card, text="Event Requests", font=("Helvetica", 18, "bold"),
                                    bg="#3C4248", fg="white", bd=0).place(x=35, y=260)  # bg="light grey"

        self.bg6 = ImageTk.PhotoImage(file="C:/Users/Swaraj/Desktop/Icons/Icons/calendar_notification.png")
        events_icon6 = Label(side_card, bg="#3C4248", fg="light grey", image=self.bg6).place(x=10, y=270)

        btn_events_list = Button(side_card, text="Event List", font=("Helvetica", 18, "bold"),
                                 bg="#3C4248", fg="white", bd=0).place(x=35, y=305)  # bg="light grey"

        self.bg7 = ImageTk.PhotoImage(file="C:/Users/Swaraj/Desktop/Icons/Icons/list.png")
        events_icon7 = Label(side_card, bg="#3C4248", fg="light grey", image=self.bg7).place(x=10, y=315)

    def login_window(self):
        self.root.destroy()
        import Login

    def dash_window(self):
        self.root.destroy()
        import Admin_1

    def abtus_window(self):
        pass








    def login_window(self):
        self.root.destroy()
        import Admin_Login

root = Tk()
obj = First_Page(root)
root.mainloop()
