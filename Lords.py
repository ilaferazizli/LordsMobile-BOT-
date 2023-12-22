import idna
import os
import sys
import pyautogui
import time
import keyboard
from tkinter import*
from tkinter import messagebox
from tkinter.ttk import*
from PIL import Image, ImageTk


def main_page():
    page_1.pack_forget()
    page_2.pack_forget()
    page_3_1.pack_forget()
    main_page_frame.pack()

def page1():
    main_page_frame.pack_forget()
    page_1.pack()
    

def page2():
    main_page_frame.pack_forget()
    page_2.pack()

def page3():
    main_page_frame.pack_forget()
    page_3_1.pack()
    

def page3_2():
    page_3_1.pack_forget()
    page_3_2.pack()  

def page3_1():
    page_3_2.pack_forget()
    page_3_1.pack()  



screen = Tk()
screen.geometry("330x200+900+100")
screen.title('Lords Mobile Otomations')
screen.attributes('-topmost', True)
screen.resizable(False,False)
icon = PhotoImage(file="routine.png")
screen.iconphoto(True,icon)

main_page_frame = Frame(screen)
main_page_frame.pack()
Label(main_page_frame, text="Select Otomation").grid(sticky=EW,pady=7,padx=10)
Button(main_page_frame, text="Puzzle Otomation", command=page1).grid(sticky=EW,pady=5,ipady=5,ipadx=5)
Button(main_page_frame, text="OtoTaskComplete", command=page2).grid(sticky=EW,ipady=5,ipadx=5)
Button(main_page_frame, text="Supply Helper", command=page3).grid(sticky=EW,pady=5,ipady=5,ipadx=5)


###############################################################################################################################

page_1 = Frame(screen)

def Start():
    string = e.get()
    puzzle_time = string
    if string =="How many times?" or string =="":
      string = "Nothing"
    try :
        int(puzzle_time)
        pyautogui.click(514,685)
        time.sleep(1)
        confirm_button = pyautogui.screenshot(region=(704,410,167,37))
        pyautogui.keyDown('esc')
        pyautogui.keyUp('esc')
        time.sleep(1)
        upgrade_button = pyautogui.screenshot(region=(742,674,226,68))
        pyautogui.click(855,685)
        time.sleep(1)
        help_button = pyautogui.screenshot(region=(742,674,226,68))

        pyautogui.click(855,685,2,1)
        time.sleep(1)
        speed_page = pyautogui.screenshot(region=(922,385,211,75))
        pyautogui.keyDown('esc')
        pyautogui.keyUp('esc')
        time.sleep(1)
        cancel_button = pyautogui.screenshot(region=(400,675,229,64))
        pyautogui.click(514,685,3)
        time.sleep(1)
        yes_button = pyautogui.screenshot(region=(704,410,167,37))
        pyautogui.click(787,428)
        time.sleep(1)
        n = 0
        while n <= int(puzzle_time):
                if keyboard.is_pressed('shift'):
                    break
                else:
                    while upgrade_button == pyautogui.screenshot(region=(742,674,226,68)):
                        pyautogui.click(855,685)

                    while help_button == pyautogui.screenshot(region=(742,674,226,68)):
                        pyautogui.click(855,685)
                        time.sleep(0.5)
                        if speed_page == pyautogui.screenshot(region=(922,385,211,75)):
                            time.sleep(0.5)
                            pyautogui.keyDown('esc')
                            pyautogui.keyUp('esc')
                    
                    while cancel_button == pyautogui.screenshot(region=(400,675,229,64)):
                        pyautogui.click(514,685)
                        time.sleep(0.5)
                        if confirm_button == pyautogui.screenshot(region=(704,410,167,37)):
                            time.sleep(0.5)
                            pyautogui.keyDown('esc')
                            pyautogui.keyUp('esc')
                            
                    while yes_button == pyautogui.screenshot(region=(704,410,167,37)):
                        pyautogui.click(787,428)
                        n+=1
            
    except:     
          messagebox.showinfo("Wrong Input",f" You Entered <{string}> \n Please Enter Number") 

name = Label(page_1,text="Puzzle Otomation")
name.grid(sticky=N,row=0,padx=5,pady=5)                   
  
T1 = Text(page_1,width=41,height=4)
T1.tag_configure("center", justify='center')
T1.insert("1.0", f"1.Set Construction Gear up \n 2.Prepare Resources\n 3.Press and Hold <Shift> to Finish \n (while doing puzzle)")
T1.tag_add("center", "1.0", "end")
T1.grid(sticky=S,row=6,pady=35)


e = Entry(page_1, justify="center")
e.insert(0,"How many times?")
e.config(justify="center")
e.bind("<FocusIn>", lambda args: e.delete('0', 'end'))
e.grid(sticky=N,row=2,pady=5)

b = Button(page_1,text='Start Puzzle',command=Start)
b.grid(sticky=W,row=3,padx=80,pady=5)
back_main = Button(page_1,text='Back',command=main_page)
back_main.grid(sticky=E,row=3,padx=80)
#######################################################################################################################

page_2 = Frame(screen)

entry = Entry(page_2, justify="center",width=40)
entry.insert(0,"How many times?")
entry.config(justify="center")
entry.bind("<FocusIn>", lambda args: entry.delete('0', 'end'))
entry.grid(sticky=W,row=1)
task = "None"
def admin_task():
    global task
    task = 10
def Guild_task():
    global task
    task = 9

def enter():
    global entry
    string = entry.get()
    if type(string) != int:
      string = "Nothing"
    else:
        puzzle_time = int(string)
        puzzle_time +=1
    try:
        for i in range(int(puzzle_time)):
             if keyboard.is_pressed('shift'):
                  break
             else:  
                for i in range(task):
                     if keyboard.is_pressed('shift'):
                         break
                     else:
                        pyautogui.click(1141,327)
                        time.sleep(1)
                if keyboard.is_pressed('shift'):
                         break
                else:
                    pyautogui.click(560,266)
                    pyautogui.click(671,508)
                        
    except:  
        if task == "None":
            messagebox.showinfo("Task Not Selected",f" Select Task Type") 
        else:
            messagebox.showinfo("Wrong Input",f" You Entered <{string}> \n Please Enter Number") 

Label(page_2,text="Select task type").grid(sticky=W,row=2,pady=5)
Label(page_2,text="Actions").grid(sticky=E,row=2,padx=11,pady=5)
name = Label(page_2,text="Oto Task Complete")
name.grid(sticky=N,row=0,padx=5,pady=5)

admin = Button(page_2, text='Admin Tasks', command= admin_task)
admin.grid(sticky=W,row=3)

Guild = Button(page_2, text='Guild Tasks', command= Guild_task)
Guild.grid(sticky=W,row=4)
number = Button(page_2,text='Start',command=enter)
number.grid(sticky=E,row=3)

back_main2 = Button(page_2,text='Back',command=main_page)
back_main2.grid(sticky=E,row=4)

T1 = Text(page_2,width=30,height=2)
T1.tag_configure("center", justify='center')
T1.insert("1.0", f"1.Press and Hold <Shift>\n to Finish")
T1.tag_add("center", "1.0", "end")
T1.grid(sticky=S,row=5)

##############################################################################################################

page_3_1 = Frame(screen)

click = 0
def resize_supply(event):
    global click
    if click == 0:
        on_enter_supply()
        click +=1
    else:
        on_leave_supply()
        click = 0

def resize_travel(event):
    global click
    if click == 0:
        on_enter_travel()
        click +=1
    else:
        on_leave_travel()
        click = 0

def resize_label(event):
    global click
    if click == 0:
        on_enter()
        click +=1
    else:
        on_leave()
        click = 0



def on_enter():
     label_img.config(image=image_large)
     label_img.image = image_large
     global widget_list
     widget_list = []
     for widget in page_3_1.grid_slaves():
        if widget != label_img:
            widget_list.append((widget,widget.grid_info()))
            widget.grid_remove()
     label_img.grid(row=0,column=0)

def on_leave():   
     label_img.config(image=image_small)
     label_img.image = image_small
     global widget_list 
     for widget, grid_info in widget_list:
        widget.grid(row=grid_info["row"],column=grid_info["column"])
     label_img.grid(row=0,column=2,columnspan=2)

def on_enter_supply():
     supply_label.config(image=supply_large)
     supply_label.image = supply_large
     global widget_list
     widget_list = []
     for widget in page_3_1.grid_slaves():
        if widget != supply_label:
            widget_list.append((widget,widget.grid_info()))
            widget.grid_remove()
     supply_label.grid(row=0,column=0)

def on_leave_supply():   
     supply_label.config(image=image_supply)
     supply_label.image = image_supply
     global widget_list 
     for widget, grid_info in widget_list:
        widget.grid(row=grid_info["row"],column=grid_info["column"])
     supply_label.grid(row=5,column=0,rowspan=2,sticky=S)

def on_enter_travel():
     travel_label.config(image=travel_large)
     travel_label.image = travel_large
     global widget_list
     widget_list = []
     for widget in page_3_1.grid_slaves():
        if widget != travel_label:
            widget_list.append((widget,widget.grid_info()))
            widget.grid_remove()
     travel_label.grid(row=0,column=0)

def on_leave_travel():   
     travel_label.config(image=image_travel)
     travel_label.image = image_travel
     global widget_list 
     for widget, grid_info in widget_list:
        widget.grid(row=grid_info["row"],column=grid_info["column"])
     travel_label.grid(row=5,column=2,rowspan=2,sticky=S)

img = Image.open("PNG image.png")

small_img =img.resize((160,68))
larger_image = img.resize((320,180))

image_large = ImageTk.PhotoImage(larger_image)
image_small = ImageTk.PhotoImage(small_img)

label_img = Label(page_3_1,image=image_small)
label_img.grid(row=0,column=2,columnspan=2,rowspan=3)
label_img.bind('<Button-1>',resize_label)

Label(page_3_1,text=f'1.Go to profile\nwho you send supply').grid(sticky=W,row=0,column=0,columnspan=2)
Label(page_3_1,text='2.Left click to resize images').grid(sticky=W,row=1,column=0,columnspan=2)
Label(page_3_1,text='3.Then go next page').grid(sticky=W,row=2,column=0,columnspan=2)

Label(page_3_1,text="Supply Capacity").grid(row=5,column=0,columnspan=2)

Label(page_3_1,text="Travel Time").grid(row=5,column=2,columnspan=2)

Label(page_3_1,text="Army Limit").grid(row=7,column=0,columnspan=4)

space = Frame(page_3_1,width=100,height=10).grid(row=4,column=0,columnspan=4)

image_supply = Image.open("Supply.jpg")
supply_large = image_supply.resize((320,180))
image_supply = image_supply.resize((32,32))
image_supply = ImageTk.PhotoImage(image_supply)
supply_large = ImageTk.PhotoImage(supply_large)
supply_label= Label(page_3_1,image=image_supply)
supply_label.grid(row=5,column=0,rowspan=2,sticky=S)
supply_label.bind('<Button-1>', resize_supply)

supply_capacity = Entry(page_3_1, justify="center",width=20)
supply_capacity.insert(0,"4670000")
supply_capacity.config(justify="center")
supply_capacity.bind("<FocusIn>", lambda args: supply_capacity.delete('0', 'end'))
supply_capacity.grid(row=6,column=1)

image_travel = Image.open("Travel.jpg")
travel_large = image_travel.resize((320,180))
image_travel = image_travel.resize((32,32))
image_travel = ImageTk.PhotoImage(image_travel)
travel_large = ImageTk.PhotoImage(travel_large)
travel_label= Label(page_3_1,image=image_travel)
travel_label.grid(row=5,column=2,rowspan=2,sticky=S)
travel_label.bind('<Button-1>',resize_travel)

travel_time = Entry(page_3_1, justify="center",width=20)
travel_time.insert(0,"e.g. 00:13")
travel_time.config(justify="center")
travel_time.bind("<FocusIn>", lambda args: travel_time.delete('0', 'end'))
travel_time.grid(row=6,column=3)

army_limit = Entry(page_3_1, justify="center",width=20)
army_limit.insert(0,"e.g. 3 empty troops")
army_limit.config(justify="center")
army_limit.bind("<FocusIn>", lambda args: army_limit.delete('0', 'end'))
army_limit.grid(row=8,column=0,columnspan=4)

Button(page_3_1,text='Back',command=main_page).grid(sticky=W,row=9,column=0,columnspan=2)
Button(page_3_1, text="Next Page", command=page3_2).grid(sticky=E,row=9,column=3)
#################################################################################################################

page_3_2 = Frame(screen)

def start_supply():
    global wheet
    global ore
    global wood
    global gold
    global stone
    global supply_capacity
    global travel_time
    global army_limit
    wheet_amount = wheet.get()
    stone_amount = stone.get()
    ore_amount = ore.get()
    wood_amount = wood.get()
    gold_amount = gold.get()
    capacity_amount = supply_capacity.get()
    time_amount = travel_time.get()
    army_amount = army_limit.get()
    
    profile_button = pyautogui.screenshot(region=(1037,126,62,35))
    pyautogui.click(1058,165)
    time.sleep(1)
    send_button = pyautogui.screenshot(region=(447,336,474,63))
    pyautogui.click(756,382)
    time.sleep(1)
    supply_button = pyautogui.screenshot(region=(872,658,340,97))
    pyautogui.click(959,686)
    time.sleep(1)
    confrm_button = pyautogui.screenshot(region=(705,368,170,38))
    pyautogui.keyDown('esc')
    pyautogui.keyUp('esc')
    time.sleep(0.5)
    pyautogui.keyDown('esc')
    pyautogui.keyUp('esc')
    try:
        for i in range(int(wheet_amount)//int(capacity_amount)):

            while profile_button == pyautogui.screenshot(region=(1037,126,62,35)):
                pyautogui.click(1058,165)
            while send_button == pyautogui.screenshot(region=(447,336,474,63)):
                pyautogui.click(756,382)
            pyautogui.click(701,345)
            while supply_button == pyautogui.screenshot(region=(872,658,340,97)):
                pyautogui.click(959,686)
            while confrm_button == pyautogui.screenshot(region=(705,368,170,38)):
                pyautogui.click(782,393)
            while profile_button != pyautogui.screenshot(region=(1037,126,62,35)):
                pass
    except:
        print('wheet')
    try:
        for i in range(int(stone_amount)//int(capacity_amount)):

            while profile_button == pyautogui.screenshot(region=(1037,126,62,35)):
                pyautogui.click(1058,165)
            while send_button == pyautogui.screenshot(region=(447,336,474,63)):
                pyautogui.click(756,382)
            pyautogui.click(702,442)
            while supply_button == pyautogui.screenshot(region=(872,658,340,97)):
                pyautogui.click(959,686)
            while confrm_button == pyautogui.screenshot(region=(705,368,170,38)):
                pyautogui.click(782,393)
            while profile_button != pyautogui.screenshot(region=(1037,126,62,35)):
                pass
    except:
        print('stone')
    try:
        for i in range(int(wood_amount)//int(capacity_amount)):

            while profile_button == pyautogui.screenshot(region=(1037,126,62,35)):
                pyautogui.click(1058,165)
            while send_button == pyautogui.screenshot(region=(447,336,474,63)):
                pyautogui.click(756,382)
            pyautogui.click(701,545)
            while supply_button == pyautogui.screenshot(region=(872,658,340,97)):
                pyautogui.click(959,686)
            while confrm_button == pyautogui.screenshot(region=(705,368,170,38)):
                pyautogui.click(782,393)
            while profile_button != pyautogui.screenshot(region=(1037,126,62,35)):
                pass
    except:
        print('wood')
    try:
        for i in range(int(ore_amount)//int(capacity_amount)):

            while profile_button == pyautogui.screenshot(region=(1037,126,62,35)):
                pyautogui.click(1058,165)
            while send_button == pyautogui.screenshot(region=(447,336,474,63)):
                pyautogui.click(756,382)
            pyautogui.click(700,644)
            while supply_button == pyautogui.screenshot(region=(872,658,340,97)):
                pyautogui.click(959,686)
            while confrm_button == pyautogui.screenshot(region=(705,368,170,38)):
                pyautogui.click(782,393)
            while profile_button != pyautogui.screenshot(region=(1037,126,62,35)):
                pass
    except:
        print('ore')

    try:
        for i in range(int(gold_amount)//int(capacity_amount)):

            while profile_button == pyautogui.screenshot(region=(1037,126,62,35)):
                pyautogui.click(1058,165)
            while send_button == pyautogui.screenshot(region=(447,336,474,63)):
                pyautogui.click(756,382)
            pyautogui.click(701,743)
            while supply_button == pyautogui.screenshot(region=(872,658,340,97)):
                pyautogui.click(959,686)
            while confrm_button == pyautogui.screenshot(region=(705,368,170,38)):
                pyautogui.click(782,393)
            while profile_button != pyautogui.screenshot(region=(1037,126,62,35)):
                pass
    except:
        print('gold')
        
           
Label(page_3_2,text='Enter amount of Supply').grid(row=0,column=0,columnspan=4)
Label(page_3_2,text='Enter 1B = For 1,000,000,000').grid(row=5,column=0,columnspan=2)
Label(page_3_2,text='Enter 1M = For 1,000,000').grid(row=4,column=0,columnspan=2,pady=5)
Label(page_3_2,text='Enter 1K = For 1000').grid(row=4,column=2,columnspan=2,pady=5)
Label(page_3_2,text='Enter 1.125B = For 1,125,000').grid(row=5,column=2,columnspan=2)

image_wheet = Image.open("Wheet.PNG")
image_wheet = image_wheet.resize((32,32))
image_wheet = ImageTk.PhotoImage(image_wheet)
wheet_label = Label(page_3_2,image=image_wheet)
wheet_label.grid(row=1,column=0)

wheet = Entry(page_3_2, justify="center",width=20)
wheet.insert(0,"Wheet")
wheet.config(justify="center")
wheet.bind("<FocusIn>", lambda args: wheet.delete('0', 'end'))
wheet.grid(row=1,column=1)

image_stone = Image.open("Stone.PNG")
image_stone = image_stone.resize((32,32))
image_stone = ImageTk.PhotoImage(image_stone)
stone_label = Label(page_3_2,image=image_stone)
stone_label.grid(row=2,column=0)

stone = Entry(page_3_2, justify="center",width=20)
stone.insert(0,"Stone")
stone.config(justify="center")
stone.bind("<FocusIn>", lambda args: stone.delete('0', 'end'))
stone.grid(row=2,column=1)

image_wood = Image.open("Wood.PNG")
image_wood = image_wood.resize((32,32))
image_wood = ImageTk.PhotoImage(image_wood)
wood_label = Label(page_3_2,image=image_wood)
wood_label.grid(row=3,column=0)

wood = Entry(page_3_2, justify="center",width=20)
wood.insert(0,"Wood")
wood.config(justify="center")
wood.bind("<FocusIn>", lambda args:wood.delete('0', 'end'))
wood.grid(row=3,column=1)

image_ore = Image.open("Ore.PNG")
image_ore = image_ore.resize((32,32))
image_ore = ImageTk.PhotoImage(image_ore)
ore_label= Label(page_3_2,image=image_ore)
ore_label.grid(row=1,column=2,rowspan=2)

ore = Entry(page_3_2, justify="center",width=20)
ore.insert(0,"Ore")
ore.config(justify="center")
ore.bind("<FocusIn>", lambda args:ore.delete('0', 'end'))
ore.grid(row=1,column=3,rowspan=2)

image_gold = Image.open("Gold.PNG")
image_gold = image_gold.resize((32,32))
image_gold = ImageTk.PhotoImage(image_gold)
gold_label = Label(page_3_2,image=image_gold)
gold_label.grid(row=2,column=2,rowspan=2)

gold = Entry(page_3_2, justify="center",width=20)
gold.insert(0,"Gold")
gold.config(justify="center")
gold.bind("<FocusIn>", lambda args:gold.delete('0', 'end'))
gold.grid(row=2,column=3,rowspan=2)


Button(page_3_2,text='Back',command=page3_1).grid(sticky=W,row=9,column=0,columnspan=2)
Button(page_3_2,text='Start',command=start_supply).grid(sticky=E,row=9,column=3)


main_page()
mainloop()