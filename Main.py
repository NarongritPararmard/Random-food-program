from tkinter import *
from PIL import Image, ImageTk
import pandas as pd
import random
from tkmacosx import Button

#สร้างหน้าต่าง desktop
root = Tk()
root.title("กินอะไรดีน๊าาา")
root.geometry("600x600+600+200")


#blackground
bg = Image.open("background.png")
bg = bg.resize((600,600))
bg = ImageTk.PhotoImage(bg)
background = Canvas(root, height=600, width = 600)
background.pack(fill = "both", expand = True)
background.create_image(0, 0, image = bg, anchor = NW)


#ฟังก์ชันสุ่ม
def random():
    
    import random
    df = pd.read_excel(r'Food.xlsx')
    
    #เพื่อให้ฟังก์ชัน delete รู้จัก
    global text_name
    global text_cal
    global text_carbohydrate
    global text_protein
    global text_fat
    global text_sodium
    global text_potassium
    global text_vitamin
    global text_cholesterol


    cal = etCal.get()
    carbohydrate = etCarbohydrate.get()
    protein = etProtein.get()
    fat = etFat.get()
    sodium = etSodium.get()
    potassium = etPotassium.get()
    cholesterol = etCholesterol.get()
        
        
    #ใช้เก็บ index เข้าเงื่อนไข
        
    Index_random = []
    

    try:    
        for i in range(len(df)):
            
            if((int(df['แคล'][i:i+1]) <= float(cal)) 
                and (int(df['คาร์โบไฮเดรต'][i:i+1]) >= float(carbohydrate))
                and (int(df['โปรตีน'][i:i+1]) >= float(protein)) 
                and (int(df['ไขมัน'][i:i+1]) >= float(fat))
                and (int(df['โซเดียม'][i:i+1]) <= float(sodium))
                and (int(df['โพแทสเซียม'][i:i+1]) <= float(potassium))
                and (int(df['คอเรสเตอรอล'][i:i+1]) <= float(cholesterol))
                ):
                

                Index_random.append(i)

        #random
        
        if(len(Index_random) != 0):

            i = random.choice(Index_random)
            
            Name_Food = df['ชื่ออาหาร'][i:i+1].get(i)
            Cal_Food = df['แคล'][i:i+1].get(i)
            Carbohydrate_Food = df['คาร์โบไฮเดรต'][i:i+1].get(i)
            Protein_Food = df['โปรตีน'][i:i+1].get(i)
            Fat_Food = df['ไขมัน'][i:i+1].get(i) 
            Sodium_Food = df['โซเดียม'][i:i+1].get(i)
            Potassium_Food = df['โพแทสเซียม'][i:i+1].get(i)
            Cholesterol_Food = df['คอเรสเตอรอล'][i:i+1].get(i)
            Vitamin_Food = df['วิตามิน'][i:i+1].get(i)
        
            

            #แสดงรายละเอียดอาหาร
            background.itemconfig(text_cal, text = Cal_Food)
            background.itemconfig(text_name, text = Name_Food)
            background.itemconfig(text_carbohydrate, text = Carbohydrate_Food)
            background.itemconfig(text_protein, text = Protein_Food)
            background.itemconfig(text_fat, text = Fat_Food)
            background.itemconfig(text_sodium, text = Sodium_Food)
            background.itemconfig(text_potassium, text = Potassium_Food)
            background.itemconfig(text_cholesterol, text = Cholesterol_Food)
            background.itemconfig(text_vitamin, text = Vitamin_Food)

            
        #กรณีไม่มีอาหาร
        else :
            background.itemconfig(text_cal, text = "")
            background.itemconfig(text_name, text = "")
            background.itemconfig(text_carbohydrate, text = "")
            background.itemconfig(text_protein, text = "")
            background.itemconfig(text_fat, text = "")
            background.itemconfig(text_sodium, text = "")
            background.itemconfig(text_potassium, text = "")
            background.itemconfig(text_cholesterol, text = "")
            background.itemconfig(text_vitamin, text = "")
            error_text = ["ไม่มีจ้าาาาา", "เอาใหม่ๆ มันไม่มี", "หาไม่เจอ TT"]
            i = random.choice(error_text)
            background.itemconfig(text_name, text = i)

        
    except:

        text_name = background.create_text(300, 13,fill = "black",
                                            text = "Input Error", font = ("",27), anchor=N)


#สร้างปุ่ม

button1 = Button(root, bg = '#fff4ee', text = "สุ่ม", width = 250,height = 55,
                  font =('Modern', 23),highlightbackground = "#eeadab", command = random)
button1 = background.create_window(300, 525, window = button1, anchor = N)


#สร้างช่องใส่ input
carbohydrate_input = None
etCarbohydrate = Entry(background="white",fg="black")
EntryCarbohydrate = background.create_window(225, 140, width=40,window=etCarbohydrate)

protein_input = None
etProtein = Entry(background="white",fg="black")
EntryProtein = background.create_window(225, 173,width=40,window=etProtein)

fat_input = None
etFat = Entry(background="white",fg="black")
EntryCFat = background.create_window(225, 205,width=40,window=etFat)

sodium_input = None
etSodium = Entry(background="white",fg="black")
EntrySodium = background.create_window(225,239,width=40,window=etSodium)

potassium_input = None
etPotassium = Entry(background="white",fg="black")
EntryPotassium = background.create_window(225,274,width=40,window=etPotassium)

cholesterol_input = None
etCholesterol = Entry(background="white",fg="black")
EntryCholesterol = background.create_window(225, 309,width=40,window=etCholesterol)

cal_input = None
etCal = Entry(background="white",fg="black")
EntryCal = background.create_window(160, 495, width=40,window=etCal) 



#สร้าง text เปล่า
text_name = background.create_text(300, 15,fill = "black",
                                    text = "", font = ("",27), anchor=N)
text_cal = background.create_text(440, 480,fill = "black",
                                   text = "", font = ("",27), anchor=N)
text_vitamin = background.create_text(300, 397,fill = "black",
                                       text = "", font = ("",24), anchor=N)
            

text_carbohydrate = background.create_text(497, 131,fill = "black",
                                            text = "", font = ("",20), anchor=N)
text_protein = background.create_text(497, 162,fill = "black",
                                       text = "", font = ("",20), anchor=N)
text_fat = background.create_text(497, 195,fill = "black", 
                                  text = "", font = ("",20), anchor=N)
text_sodium = background.create_text(497, 230,fill = "black",
                                      text = "", font = ("",20), anchor=N)
text_potassium = background.create_text(497, 265,fill = "black", text = "", font = ("",20), anchor=N)
text_cholesterol = background.create_text(497, 300,fill = "black",
                                           text = "", font = ("",20), anchor=N)

#เมื่อกดช่องให้ลบค่าเดิม
etCal.bind("<Button-1>", lambda x : etCal.delete(0, "end"))
etCarbohydrate.bind("<Button-1>", lambda x : etCarbohydrate.delete(0, "end"))
etProtein.bind("<Button-1>", lambda x : etProtein.delete(0, "end"))
etFat.bind("<Button-1>", lambda x : etFat.delete(0, "end"))
etSodium.bind("<Button-1>", lambda x : etSodium.delete(0, "end"))
etPotassium.bind("<Button-1>", lambda x : etPotassium.delete(0, "end"))
etCholesterol.bind("<Button-1>", lambda x : etCholesterol.delete(0, "end"))


root.mainloop()