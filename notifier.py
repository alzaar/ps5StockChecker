from tkinter import Tk, Label, Button
import tkinter.messagebox

def copy_link(notifier, link):
  notifier.clipboard_clear()
  notifier.clipboard_append(link)
  tkinter.messagebox.showinfo( "Message", "Copied!")

def notify_user(products):
  notifier = Tk()
  notifier.title('!!!Stock Available!!!')
  notifier.geometry('1200x1200')
  increment = 50
  button_y = 50
  Label(notifier, text= "Note -- Click below to copy link", fg="red",bg="black",font="Arial").place(x=20,y=20)
  for product in products:
    Button(
      notifier, 
      text=product['details'], 
      fg='blue', relief='solid', 
      font=("Helevetica",20,"bold"), 
      command=lambda: copy_link(notifier, product['link'])).place(x=25, y=button_y)
    button_y += increment
  notifier.mainloop()
