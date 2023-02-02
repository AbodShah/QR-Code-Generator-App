from tkinter import *
import qrcode
from PIL import Image , ImageDraw 
import customtkinter
import os
customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

root = customtkinter.CTk()

def qrgen():
 global logo
 global logoname
 global data
 global qrimagename 
 qrimagename = input3.get()
 data = input_1.get() 
 if data == ""  : 
     logoname = input_4.get()
     filename = input3.get()
     label2.configure(text="Error : invalid input " , text_color = "red" )
     lablel_3()
     label_4()
 elif data != "" : 
    try:    
     logoname = input_4.get()
     filename = input3.get()
     logo = Image.open(logoname)#
     basewidth = 100#
     wpercent =(basewidth/float(logo.size[0]))#
     hsize = int((float ( logo.size[1])*float(wpercent)))#
    # logo = logo.resize((basewidth, hsize), Image.ANTIALIAS )#
     logo = logo.resize((basewidth, hsize), Image.LANCZOS )#

     qr_big= qrcode.QRCode (error_correction=qrcode.constants.ERROR_CORRECT_H , version=1, box_size=15, border=2)#
     qr_big.add_data(data)#
     qr_big.make()#
     img_qr_big = qr_big.make_image(fill_color= 'black', back_color="white").convert('RGB')
     pos = ((img_qr_big.size[0]- logo.size[0]) // 2 , (img_qr_big.size[1] - logo.size[1] ) // 2)
     img_qr_big.paste(logo, pos)
     img_qr_big.save(filename + '.jpg')
     label2.configure(text="Done : QR code created", text_color="green" )
     Image.open( filename +".jpg").show()
     input_1.delete(0 , "end")
     input_4.delete(0 , "end")
     input3.delete(0 , "end")
     lablel_3()
     label_4()
    except:
    
     qr = qrcode.QRCode(version=1, box_size=15, border=2)
     qr.add_data(data)
     qr.make(fit=True)
     img = qr.make_image(fill_color="black", back_color="white")
     img.save( qrimagename + ".jpg")
     label2.configure(text="Done : QR code created", text_color="green" )
     Image.open(qrimagename + ".jpg").show()
     input_1.delete(0 , "end")
     input3.delete(0 , "end")
     input_4.delete(0 , "end")

     lablel_3()
     label_4()
     

# label 3 config
def lablel_3():
    if qrimagename != "" and data != "" : 
        label3.configure(text="file saved in [" + qrimagename + ".jpg]  " , text_color="green"  )
        input3.delete(0 , "end")
    elif data == "" and qrimagename != "" :
        label3.configure(text="file saved in [" + "can't save file " + "] (add link to create qr code file) " , 
        text_color="#F39011"  )
    
    elif qrimagename == "" : 
        label3.configure(text="No file saved " , text_color="red"  )
        input3.delete(0 , "end")

    

def label_4():
    if logoname == ""  :
      label4.configure(text="Logo havn't added" , text_color="red")
      input_4.delete(0 , "end")
    elif qrimagename == "" and logoname != "":
     label4.configure(text="logo have been added but (" + "can't find file location , image name invalid" + ")" ,
     text_color="#F39011")
    elif data == "" and qrimagename != "" :
     label4.configure(text="logo have been added but (" + "Invalid link to create QR code" + ")" ,
     text_color="#F39011")


    elif logoname != "":
         if os.path.exists(logoname) :
           label4.configure(text="logo have been added (" + logoname+ ")" , text_color="green")
           input_4.delete(0 , "end")
         else:
          label4.configure(text="Something wronge (file name / path) ", text_color="red")
          input_4.delete(0 , "end")

 

# program
root.title("Qr Code Generator")
root.geometry("500x500")
root.resizable(False,False)
root.after(201, lambda :root.iconbitmap("C:\\Users\\user\\OneDrive\\Desktop\\WorkStation\\logo.ico"))

def start_program(): 
 global input_4
 global label3
 global input3
 global input_1
 global label2
 global label4
 # logo image
 #logo1 = PhotoImage(file="hi.png").subsample(3)
 #qrtitle = Label(root , image=logo1)
 #qrtitle.pack()

 # title ( label )
 font1 = customtkinter.CTkFont(size=25)
 label1 = customtkinter.CTkLabel(master = root , text="\nA Generator to create QR code\n\n ",
  font=font1 ,
  text_color="lightblue" , )
 label1.pack(pady=10)

 # label for entry 

 labelforentry = customtkinter.CTkLabel(master = root , text="input link to create QR code : *")
 labelforentry.pack()

 # entry
 input_1 = customtkinter.CTkEntry(master=root , placeholder_text = "Add URL" , width=300) 
 input_1.pack(pady="10")

 labelforentry2 = customtkinter.CTkLabel(root , text="input image name of QR code [example.jpg] : ")
 labelforentry2.pack()

 # entry 3
 input3 = customtkinter.CTkEntry(master=root , placeholder_text = "Add Name" ,width=300 )
 input3.pack()

 #label
 label4 = customtkinter.CTkLabel(master=root , text="Input logo to add it into QR image [ input: filename or path] \nleave it empty if you won't add logo" , )
 label4.pack(pady = 4)

 #entry
 input_4 = customtkinter.CTkEntry(master=root , placeholder_text = "Add Logo" ,  width=300) 
 input_4.pack()




 # label for gen 
 font2 = customtkinter.CTkFont(size=15 ,)
 labelforgen = customtkinter.CTkLabel(master = root ,  text="\nClick Generate to create : " , font=font2 , text_color = "#4361ee")
 labelforgen.pack()

 #button
 button1 = customtkinter.CTkButton(master=root , text="Generate" , command=qrgen , )
 button1.pack(pady="10" )


 # label 2 
 label2 = customtkinter.CTkLabel(master = root , text="" , ) 
 label2.pack()
 label2.place(relx="0.0" , rely="0.85")
 # label 3
 label3 = customtkinter.CTkLabel(master = root , text="") 
 label3.pack()
 label3.place( relx="0.0" , rely="0.90")

 label4 = customtkinter.CTkLabel(master = root , text="") 
 label4.pack()
 label4.place( relx="0.0" , rely="0.95")




 root.mainloop()




  
start_program() # start def