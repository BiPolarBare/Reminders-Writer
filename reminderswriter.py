from tkinter import *
import sys
global file
class Application(Frame):
    def __init__(self,master):
        Frame.__init__(self,master)
        self.grid()
        self.points = []
        self.file = open("reminders.html","r+")
        self.createscreen()
        
    def createscreen(self):
        Label(text = 'thanks for using :D').grid(row=1, column = 0, columnspan = 2)
        self.c = 2
        self.file.seek(0)
        while True:
            self.text = self.file.readline()
            if self.text.startswith("<li>"):
                self.reminder = Entry(width = 100)
                self.reminder.grid(row = self.c, columnspan = 2)
                self.stripped = self.text.replace("<li>","")
                self.stripped = self.stripped.replace("</li>","")
                self.reminder.insert(0,str(self.stripped))
                self.points.append(self.reminder)
                self.c+=1
            if self.text.startswith("</html>"):
                break
                
        self.savebutton = Button(
            text = "Save",
            fg = "green",
            command = self.save)
        self.savebutton.grid(row = self.c+2, column = 0)
        self.exitbutton = Button(
            text = "Exit",
            fg = "red",
            command = self.tkexit)
        self.exitbutton.grid(row = self.c+2, column = 1)
        self.addline = Button(
            text = "Add new line",
            fg = "green",
            command = self.addline)
        self.addline.grid(row = self.c+1,column = 0)
        self.removeline = Button(
            text = "Remove a line",
            fg = "red",
            command = self.removeline)
        self.removeline.grid(row = self.c+1, column = 1)
    def addline(self):
        self.reminder = Entry(width = 100)
        self.reminder.grid(row = self.c, columnspan = 2)
        self.points.append(self.reminder)
        self.c+=1
        self.savebutton.grid(row = self.c + 2)
        self.exitbutton.grid(row = self.c + 2)
        self.addline.grid(row = self.c + 1)
        self.removeline.grid(row = self.c + 1)
    def removeline(self):
        temp = self.points.pop()
        temp.destroy()
        self.c -= 1
        self.savebutton.grid(row = self.c + 2)
        self.exitbutton.grid(row = self.c + 2)
        self.addline.grid(row = self.c + 1)
        self.removeline.grid(row = self.c + 1)
    def save(self): # The functuion that saves reminders
        reminderstext = ""
        for i in self.points:
            temp = "<li>" + i.get() + "</li>\n"
            reminderstext += temp
        tempconcat = """<!Doctype HTML>\n<html>\n<head>\n<title>Reminders</title>\n</head>\n<body style="background-image:url('https://raw.githubusercontent.com/BiPolarBare/Reminders-Writer/master/background.png');background-size: cover;background-repeat:no-repeat;">\n<div style='position:absolute;left:600px;'>\n<h1>Reminders</h1>\n<ul>\n""" + reminderstext + """\n</ul>\n</div>\n</body>\n</html>"""
        print(tempconcat)
        self.file.seek(0)
        self.file.write(tempconcat)
        try:
            messagebox.showinfo("Saved","Reminders saved...")
        except:
            print("saved")
    def tkexit(self):
        exit()
def createfile():
    try:
        if messagebox.askyesno("Create","Failed to open file.\nWould you like to create a new one?"):
            file = open("reminders.html","w")
            file.write("""<!Doctype HTML>\n<html>\n<head>\n<title>Reminders</title>\n</head>\n<body style="background-image:url('https://raw.githubusercontent.com/BiPolarBare/Reminders-Writer/master/background.png');background-size: cover;background-repeat:no-repeat;">\n<div style='position:absolute;left:600px;'>\n<h1>Reminders</h1>\n<ul>\n\n</ul>\n</div>\n</body>\n</html>""")
        else:
            exit()
    except:
        print("failed to use msg box\nusing legacy.")
        if legacyyesno("Failed to open file.\nWould you like to create a new one?"):
            file = open("reminders.html","w")
            file.write("""<!Doctype HTML>\n<html>\n<head>\n<title>Reminders</title>\n</head>\n<body style="background-image:url('https://raw.githubusercontent.com/BiPolarBare/Reminders-Writer/master/background.png');background-size: cover;background-repeat:no-repeat;">\n<div style='position:absolute;left:600px;'>\n<h1>Reminders</h1>\n<ul>\n\n</ul>\n</div>\n</body>\n</html>""")
        else:
            exit()
def legacyyesno(question): # Problems with messagebox redirect here
    print(question)
    while True:
        temp = input("Enter Yes (y) or No (n): ")
        temp = temp.lower()
        if temp == "yes" or temp == "y":
            return True
        elif temp == "no" or temp == "n":
            return False
        else:
            print("That was not concievable sorry.")
# defining and starting program
try:
    file = open("reminders.html","r+")
except:
    createfile()

root = Tk();
app = Application(root)
root.title('html reminders editor')
root.mainloop()
