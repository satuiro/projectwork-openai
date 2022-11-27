from tkinter import *
from tkinter import messagebox
import returnCompletion;

app = Tk()

#defining the dimensions for the app
app.geometry("1000x600")
app.title(f"Text Completion")
app.resizable(False, True)
app.config(background = '#FFFFFF')

# Entry boxes
pincode_text_var = StringVar()
pincode_textbox = Entry(app,width = 50, bg = '#ffffff', fg= 'black', textvariable = pincode_text_var, font='verdana 11')
pincode_textbox['textvariable'] = pincode_text_var
pincode_textbox.place(x= 250, y=25)

#Textbox
result_box_cent = Text(app, height = 10, width = 50, bg='#354B30',fg='#fff',borderwidth=20, relief=FLAT, font='verdana 10')
result_box_cent.place(x= 280 , y= 152)

def search():
    text = pincode_text_var.get()
    a = ""    
    li = []
    def go(counter=0):
        # This function will execute every 150ms and add a part of the response to the screen.
        result_box_cent.insert(END,li[counter]+ " ")
        if counter < len(li)-1:
            app.after(150, lambda: go(counter+1))
  
    txtToComplete = text
    if(txtToComplete!=0):
        res = returnCompletion.returnText(txtToComplete) # This will return text completion grabbed from open-ai API
        print("Pong! Code:200")
        a =res
        li = a.split(" ")
        print(a,li)
        go()
# Buttons
img0 = PhotoImage(file = f"img0.png")

b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command =search,
    relief = "flat")

b0.place(
    x = 390, y = 50,
    width = 243,
    height = 82)

app.mainloop()