import tkinter as tk
from tkinter import *
import tkinter.messagebox
import pyttsx3
import webbrowser
import json
import random
import threading
from bs4 import BeautifulSoup
import requests
voice = pyttsx3.init()
newVoiceRate = 147
voice.setProperty('rate', newVoiceRate)


def compliments_func():
        compliments = ["To be yourself in a world that is constantly trying to make you something else is the greatest accomplishment",
                      "Never be bullied into silence. Never allow yourself to be made a victim. Accept no one’s definition of your life, but define yourself.",
                      "Beauty begins the moment you decide to be yourself.",
                      "Nothing can stop the man with the right mental attitude from achieving his goal; nothing on earth can help the man with the wrong mental attitude",
                      "Successful people have fear, successful people have doubts, and successful people have worries. They just don’t let these feelings stop them",
                      "There are so many more important things to worry about than how you’re perceived by strangers",
                      "There came a time when the risk to remain tight in the bud was more painful than the risk it took to blossom.",
                      "A man cannot be comfortable without his own approval.",
                      "Don't waste your energy trying to change opinions … Do your thing, and don't care if they like it",
                      "One of the greatest regrets in life is being what others would want you to be, rather than being yourself",
                      "No other love no matter how genuine it is, can fulfill one’s heart better than unconditional self-love",
                      "To fall in love with yourself is the first secret to happiness",
                      "Don't waste your energy trying to change opinions, Do your thing, and don't care if they like it",
                      "Owning our story and loving ourselves through that process is the bravest thing that we'll ever do.",
                      "He who is not courageous enough to take risks will accomplish nothing in life."]
        voice.say("Greetings Phil George, your assistant has been enabled. I would like to begin by saying a good quote you'd love.")
        voice.runAndWait()
        voice.say(random.choice(compliments))
        voice.runAndWait()
        voice.say("I hope you liked that quote sir, if you would like me to assist, call me at any time and I would be pleased to assist you. I hope you enjoy your day Mr.Phil.")
        voice.runAndWait()
        voice.say("In the meantime, i will open up chrome and your essentials as you require, Mr.Phil. Your custom schedule will open up.")
        voice.runAndWait()
        webbrowser.open("https://accounts.google.com/b/0/AddMailService")
        webbrowser.open("https://calendar.google.com/calendar/u/0/r")

def main_win():
    def remind_task():
        with open('database.json','r') as stuffs:
            stuffs_bruh = json.load(stuffs)
            if not 'task_database' in stuffs_bruh or len(stuffs_bruh['task_database']) == 0:
                print("NONE")
                voice.say("You have no tasks to complete today sir!")
                voice.runAndWait()
            else:
                voice.say("Mr.Phil You have some tasks that are due sir, they are the following.")
                voice.runAndWait()
                voice.say(stuffs_bruh["task_database"])
                voice.runAndWait()
    remind_task()
    def remind_event():
        with open('database.json', 'r') as stuffs:
            stuffs_bruh = json.load(stuffs)
            if not 'event_database' in stuffs_bruh or len(stuffs_bruh['event_database']) == 0:
                print("NONE")
                voice.say("You have no events that take place today Mr.Phil!")
                voice.runAndWait()
            else:
                voice.say("Mr.Phil You have some upcoming events sir, they are the following.")
                voice.runAndWait()
                voice.say(stuffs_bruh["event_database"])
                voice.runAndWait()
    remind_event()
    def remind_reminder():
        with open('database.json', 'r') as stuffs:
            stuffs_bruh = json.load(stuffs)
            if not 'reminder_database' in stuffs_bruh or len(stuffs_bruh['reminder_database']) == 0:
                print("NONE")
                voice.say("You have no reminders for today Mr.Phil!")
                voice.runAndWait()
            else:
                voice.say("Mr.Phil You have some reminders that I am required to tell you sir, they are the following.")
                voice.runAndWait()
                voice.say(stuffs_bruh["reminder_database"])
                voice.runAndWait()
    remind_reminder()
    win = tk.Tk()
    win.title("Reminder Assistant")
    win.geometry("881x530")
    win.config(bg="black")
    win.attributes("-alpha", 0.7)

    l_one = Label(text="Phils Schedule")
    l_one.config(bg="black", width="20", fg="white", font=('Helvetica bold', 20))
    l_one.place(x="280", y="0")

    b_one = Button(text="Add Task",command=lambda:add_task(1))
    b_one.config(width=30)
    b_one.place(x="0", y="50")

    def add_task(arg):
        if arg == 1:
            tkinter.messagebox.showinfo("Notification","You may type your task...")
            add_task_l = Label(text="Name:")
            add_task_l.place(x=0,y=120)
            add_task_e = Entry()
            add_task_e.place(x=50,y=120)

            add_task_l_2 = Label(text="Date:")
            add_task_l_2.place(x=0,y=145)
            add_task_e_2 = Entry()
            add_task_e_2.place(x=50,y=145)

            add_task_l_3 = Label(text="Time:")
            add_task_l_3.place(x=0,y=170)
            add_task_e_3 = Entry()
            add_task_e_3.place(x=50,y=170)

            add_task_b = Button(text="Submit",height="4",command=lambda:submit_1(4))
            add_task_b.place(x=200,y=120)
            add_event_clear_b = Button(text="Clear", height="4", command=lambda: clear_3(9))
            add_event_clear_b.place(x=260, y=120)

            def clear_3(arg):
                if arg == 9:
                    add_task_e.delete(0, "end")
                    add_task_e_2.delete(0, "end")
                    add_task_e_3.delete(0, "end")
                    tkinter.messagebox.showinfo("Notification", "Cleared")
            def submit_1(arg):
                if arg == 4:
                    def write_json_task(new_data, filename='database.json'):
                        with open(filename, 'r+') as file:
                            # First we load existing data into a dict.
                            file_data = json.load(file)
                            # Join new_data with file_data inside emp_details
                            file_data["task_database"].append(new_data)
                            # Sets file's current position at offset.
                            file.seek(0)
                            # convert back to json.
                            json.dump(file_data, file, indent=4)

                        # python object to be appended
                    name_1 = str(add_task_e.get())
                    date_1 = str(add_task_e_2.get())
                    time_1 = str(add_task_e_3.get())
                    y = {"name": f"{name_1}",
                         "date": f"{date_1}",
                         "time": f"{time_1}"
                         }

                    write_json_task(y)
                    tkinter.messagebox.showinfo("Notification","Successfully Added Task")
    b_two = Button(text="Add Reminder",command=lambda:add_reminder(2))
    b_two.config(width="30")
    b_two.place(x="220", y="50")
    def add_reminder(arg):
        if arg == 2:
            tkinter.messagebox.showinfo("Notification", "You may type your reminder...")
            add_reminder_l = Label(text="Name:")
            add_reminder_l.place(x=0, y=120)
            add_reminder_e = Entry()
            add_reminder_e.place(x=50,y=120)

            add_reminder_l_2 = Label(text="Date:")
            add_reminder_l_2.place(x=0,y=145)
            add_reminder_e_2 = Entry()
            add_reminder_e_2.place(x=50,y=145)

            add_reminder_l_3 = Label(text="Time:")
            add_reminder_l_3.place(x=0,y=170)
            add_reminder_e_3 = Entry()
            add_reminder_e_3.place(x=50,y=170)

            add_reminder_b = Button(text="Submit",height="4",command=lambda:submit_2(5))
            add_reminder_b.place(x=200,y=120)
            add_event_clear_b = Button(text="Clear", height="4", command=lambda: clear_3(8))
            add_event_clear_b.place(x=260, y=120)

            def clear_3(arg):
                if arg == 8:
                    add_reminder_e.delete(0, "end")
                    add_reminder_e_2.delete(0, "end")
                    add_reminder_e_3.delete(0, "end")
                    tkinter.messagebox.showinfo("Notification", "Cleared")
            def submit_2(arg):
                if arg == 5:
                    def write_json_task(new_data, filename='database.json'):
                        with open(filename, 'r+') as file:
                            # First we load existing data into a dict.
                            file_data = json.load(file)
                            # Join new_data with file_data inside emp_details
                            file_data["reminder_database"].append(new_data)
                            # Sets file's current position at offset.
                            file.seek(0)
                            # convert back to json.
                            json.dump(file_data, file, indent=4)

                        # python object to be appended
                    name_2 = str(add_reminder_e.get())
                    date_2 = str(add_reminder_e_2.get())
                    time_2 = str(add_reminder_e_3.get())
                    y = {"name": f"{name_2}",
                         "date": f"{date_2}",
                         "time": f"{time_2}"
                         }

                    write_json_task(y)
                    tkinter.messagebox.showinfo("Notification","Successfully Added Reminder")

    b_three = Button(text="Add Event",command=lambda:add_event(2))
    b_three.config(width="30")
    b_three.place(x="440", y="50")
    def add_event(arg):
        if arg == 2:
            tkinter.messagebox.showinfo("Notification", "You may type your event...")
            add_event_l = Label(text="Name:")
            add_event_l.place(x=0, y=120)
            add_event_e = Entry()
            add_event_e.place(x=50,y=120)

            add_event_l_2 = Label(text="Date:")
            add_event_l_2.place(x=0,y=145)
            add_event_e_2 = Entry()
            add_event_e_2.place(x=50,y=145)

            add_event_l_3 = Label(text="Time:")
            add_event_l_3.place(x=0,y=170)
            add_event_e_3 = Entry()
            add_event_e_3.place(x=50,y=170)

            add_event_b = Button(text="Submit",height="4",command=lambda:submit_4(6))
            add_event_b.place(x=200,y=120)
            add_event_clear_b = Button(text="Clear", height="4", command=lambda:clear_4(7))
            add_event_clear_b.place(x=260, y=120)
            def clear_4(arg):
                if arg == 7:
                    add_event_e.delete(0,"end")
                    add_event_e_2.delete(0,"end")
                    add_event_e_3.delete(0,"end")
                    tkinter.messagebox.showinfo("Notification","Cleared")
            def submit_4(arg):
                if arg == 6:
                            def write_json_task(new_data, filename='database.json'):
                                with open(filename, 'r+') as file:
                                    # First we load existing data into a dict.
                                    file_data = json.load(file)
                                    # Join new_data with file_data inside emp_details
                                    file_data["event_database"].append(new_data)
                                    # Sets file's current position at offset.
                                    file.seek(0)
                                    # convert back to json.
                                    json.dump(file_data, file, indent=4)

                                # python object to be appended
                            name_3 = str(add_event_e.get())
                            date_3 = str(add_event_e_2.get())
                            time_3 = str(add_event_e_3.get())
                            y = {"name": f"{name_3}",
                                 "date": f"{date_3}",
                                 "time": f"{time_3}"
                                 }

                            write_json_task(y)
                            tkinter.messagebox.showinfo("Notification","Successfully Added Event")

    b_four = Button(text="Open Essentials",command=lambda:open_essentials(19))
    b_four.config(width="30")
    b_four.place(x="660", y="50")

    def open_essentials(arg):
        if arg == 19:
            voice.say("Opening all your essentials as you require, Mr.Phil.")
            voice.runAndWait()
            webbrowser.open("https://accounts.google.com/b/0/AddMailService")
            webbrowser.open("https://drive.google.com/?ogsrc=32&tab=mo&authuser=0")
    
    win.mainloop()
compliments_func()
main_win()

