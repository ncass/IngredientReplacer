import tkinter as tk
from tkinter import *
from PIL import ImageTk
from PIL import Image
from selenium.webdriver import Chrome
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

H = 600
W = 600

def masterlist(sub_choice):
    subs = {
        "Meat" : ["ChickPeas", "Lentils", "Tofu"],
        "Dairy" : ["Oat Milk", "Soy Yogurt", "Coconut Oil"],
        "Fish" : ["Walnuts", "Canola Oil", "Tempeh"],
        "Misc" : ['Holder']
    }
    # for item in subs[sub_choice]:
    #     return(item)
    return subs[sub_choice]

def meat_list():
    m = {
        "Chicken" : ["Tofu"],
        "Beef" : ["Tofu"],
        "Bacon" : ["Tofu"],
        "Turkey" : ["Tofu"],
        "Pork" : ["Tofu"]
    }
# def dairy_list():
#     d = {

#     }
# def fish_list()
# def misc_list()

base = tk.Tk()

def getinp():
    a = base_entry.get()
    #webdriver = "Main HD:/Users/nicholascassara/Documents/Python Projects/ChromeDriver -Selenium Webscraper/chromedriver.exe"
    webdriver = "Users\\NicholasCassara\\Documents\\Python Projects\\ChromeDriver -Selenium Webscraper\\chromedriver.exe"
    driver = Chrome(webdriver)
    url = "https://www.pinterest.com/"
    driver.get(url)

    #base.destroy()

def inner_func(event):
    results = tk.Toplevel(bg='#F4BFA3')
    results.title("Viable Substitutions")
    results.geometry("300x300")

def Middle(event):
    print("Middle")

def Right(event):
    print("Right")

def Left(event):
    new_window = tk.Toplevel()#bg='#F4BFA3')
    new_window.title("Here are some options:")
    new_window.geometry("1920x1080")
    # print("x = " , event.x_root)
    # print("y = ", event.y_root)
    
    #Button 1 functionality
    if (270 < event.x_root < 400) and (180 < event.y_root < 310):
        print("meat button")
        mlabel = tk.Label(new_window, image=meat_background_img)
        mlabel.pack()
        '''
        banner = Label(new_window, text="Please select a category to see alternatives :)", bg="#F4BFA3")
        banner.place(relx=0, rely=0)
        mb = tk.Button(new_window, text="Chicken")
        mb.place(relx=0.1,rely=0.15)
        mb.bind("<Button-1>", inner_func)
        mb2 = tk.Button(new_window, text="Beef")
        mb2.place(relx=0.8,rely=0.15)
        mba = tk.Button(new_window, text="Bacon")
        mba.place(relx=0.45,rely=0.4)
        mb3 = tk.Button(new_window, text="Turkey")
        mb3.place(relx=0.1,rely=0.65)
        mb4 = tk.Button(new_window, text="Pork")
        mb4.place(relx=0.8,rely=0.65)
        # lbl1 = Label(new_window, text="Some Meat Substitutions are:")
        # lbl1.place(x=50,y=0)
        # lbl2 = Label(new_window, text=str(masterlist("Meat")))
        # lbl2.place(x=75,y=125)
        '''
    #Button 2 functionality
    elif (430 < event.x_root < 575) and (180 < event.y_root < 310):
        print("dairy button")
        dlabel = tk.Label(new_window, image=dairy_background_img)
        dlabel.pack()
        '''
        mb5 = tk.Button(new_window, text="Chicken")
        mb5.place(relx=0.1,rely=0.25)
        mb6 = tk.Button(new_window, text="Beef")
        mb6.place(relx=0.8,rely=0.25)
        mb7 = tk.Button(new_window, text="Sausage")
        mb7.place(relx=0.1,rely=0.75)
        mb8 = tk.Button(new_window, text="Eggs")
        mb8.place(relx=0.8,rely=0.75)
        # lbl3 = Label(new_window, text="Some Dairy Substitutions are:")
        # lbl3.place(x=50,y=0)
        # lbl4 = Label(new_window, text=str(masterlist("Dairy")))
        # lbl4.place(x=75,y=125)
        '''
    #Button 3 functionality
    elif (270 < event.x_root < 400) and (375 < event.y_root < 515):
        print("fish button")
        mb9 = tk.Button(new_window, text="Chicken")
        mb9.place(relx=0.1,rely=0.25)
        mb10 = tk.Button(new_window, text="Beef")
        mb10.place(relx=0.8,rely=0.25)
        mb11 = tk.Button(new_window, text="Sausage")
        mb11.place(relx=0.1,rely=0.75)
        mb12 = tk.Button(new_window, text="Eggs")
        mb12.place(relx=0.8,rely=0.75)
        # lbl5 = Label(new_window, text="Some Fish Substitutions are:")
        # lbl5.place(x=50,y=0)
        # lbl6 = Label(new_window, text=masterlist("Fish"))
        # lbl6.place(x=75,y=125) 
    #Button 4 functionality
    elif (430 < event.x_root < 575) and (375 < event.y_root < 515):
        print("misc button")
        mb13 = tk.Button(new_window, text="Chicken")
        mb13.place(relx=0.1,rely=0.25)
        mb14 = tk.Button(new_window, text="Beef")
        mb14.place(relx=0.8,rely=0.25)
        mb15 = tk.Button(new_window, text="Sausage")
        mb15.place(relx=0.1,rely=0.75)
        mb16 = tk.Button(new_window, text="Eggs")
        mb16.place(relx=0.8,rely=0.75)
        # lbl7 = Label(new_window, text="Some Misc Substitutions are:")
        # lbl7.place(x=50,y=0)
        # lbl8 = Label(new_window, text=masterlist("Misc"))
        # lbl8.place(x=75,y=125) 


background_img = Image.open('/Users/nicholascassara/Documents/Python Projects/Ingredient App/UI Elements/app_background.gif')
background = ImageTk.PhotoImage(background_img)
label = tk.Label(base, image = background)
label.pack()

meat_background_img = ImageTk.PhotoImage(Image.open('/Users/nicholascassara/Documents/Python Projects/Ingredient App/UI Elements/Meat_Sub.png'))
dairy_background_img = ImageTk.PhotoImage(Image.open('/Users/nicholascassara/Documents/Python Projects/Ingredient App/UI Elements/Dairy_Sub.gif'))

base.title('Ingredient Replacing Dieting Tool')
base_canvas = tk.Canvas(base, height=H, width=W)
base_canvas.pack()

base_frame = tk.Frame(base, bg='#F4BFA3')
base_frame.place(relx=0.25,rely=0.07,relheight=0.7, relwidth=0.55)

base_entry = tk.Entry(base_frame, bg='#F4BFA3')
base_entry.place(relx=0.2, rely=0.08, relwidth=0.65,relheight=0.05)
submit_button = tk.Button(base_frame, bg='#e6b4de', text='Submit', command=getinp)
submit_button.place(relx=0.85, rely=0.08, relwidth=0.1,relheight=0.05)
search_term = base_entry.get()
print(search_term)

button1img = ImageTk.PhotoImage(Image.open('/Users/nicholascassara/Documents/Python Projects/Ingredient App/UI Elements/button_meat.gif'))
button_1 = tk.Button(base_frame, text='Button #1', image=button1img) #bg='#E0B9E1')
button_1.place(relx=0.2,rely=0.2,relwidth=0.25,relheight=0.25)
button_1.bind("<Button-1>", Left)
button_1.bind("<Button-2>", Middle)
button_1.bind("<Button-3>", Right)

button2img = ImageTk.PhotoImage(Image.open('/Users/nicholascassara/Documents/Python Projects/Ingredient App/UI Elements/button_dairy.gif'))
button_2 = tk.Button(base_frame, text='Button #2', image=button2img)
button_2.place(relx=0.6,rely=0.2,relheight=0.25,relwidth=0.25)
button_2.bind("<Button-1>", Left)
button_2.bind("<Button-2>", Middle)
button_2.bind("<Button-3>", Right)

button3img = ImageTk.PhotoImage(Image.open('/Users/nicholascassara/Documents/Python Projects/Ingredient App/UI Elements/button_recipes.gif'))
button_3 = tk.Button(base_frame, text='Button #3', image=button3img)
button_3.place(relx=0.2,rely=0.6,relheight=0.25,relwidth=0.25)
button_3.bind("<Button-1>", Left)
button_3.bind("<Button-2>", Middle)
button_3.bind("<Button-3>", Right)

button4img = ImageTk.PhotoImage(Image.open('/Users/nicholascassara/Documents/Python Projects/Ingredient App/UI Elements/button_misc.gif'))
button_4 = tk.Button(base_frame, text='Button #3', image=button4img)
button_4.place(relx=0.6,rely=0.6,relheight=0.25,relwidth=0.25)
button_4.bind("<Button-1>", Left)
button_4.bind("<Button-2>", Middle)
button_4.bind("<Button-3>", Right)

welcome_label = tk.Label(base_frame, text='Which Ingredient do you wish to replace?', bg='#F5DE6B')
welcome_label.place(relx=0.2,rely=0.03,relwidth=0.65,relheight=0.05)

base.mainloop()