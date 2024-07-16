import customtkinter as ctk
from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk



root = ctk.CTk()
root.geometry("800x950")
root.resizable(False, False)
root.configure(fg_color="#eeeeee")
root.title("My resume")

def image_load(path, size1, size2):
    var1 = Image.open(path)
    varr2 = ctk.CTkImage(light_image=var1, size=(size1, size2))
    return varr2


# Frames
side_frame = ctk.CTkFrame(root, width=250, height=950,fg_color="#333333", corner_radius=1)
side_frame.pack(side=LEFT, fill=Y, expand=FALSE)

# side frames

my_img = Image.open("pics_asst/1213121POGI.jpg")
my_pfp = ctk.CTkImage(light_image=my_img, size=(200, 220))

image_lbl = ctk.CTkLabel(side_frame, fg_color="#eeeeee", anchor=CENTER, image=my_pfp, text="")
image_lbl.place(x=25,y=30)

under_line = ctk.CTkLabel(side_frame, text="_________________", font=("Serif", 24, "bold"), fg_color="transparent", text_color="#f2f2f2", bg_color="transparent")
under_line.place(x=15, y=300)

contact_lbl = ctk.CTkLabel(side_frame, text="Contacts", font=("Serif", 28), fg_color="transparent", anchor=CENTER)
contact_lbl.place(x=25, y=290)

cp_pic = image_load("pics_asst/icons8-phone-50.png", 30, 30)

contact_lbl = ctk.CTkLabel(side_frame, text="#0991-760-4723", font=("Robot", 20, "bold"), fg_color="transparent", anchor=CENTER, image=cp_pic, compound=LEFT)
contact_lbl.place(x=30, y=350)

email_pic = image_load("pics_asst/icons8-email-48.png", 30, 30)

contact_lbl = ctk.CTkLabel(side_frame, text="jerwinquijano@gmail.com", font=("Robot", 14, "bold"), fg_color="transparent", anchor=CENTER, image=email_pic, compound=LEFT)
contact_lbl.place(x=30, y=390)

house_pic = image_load("pics_asst/icons8-home-48.png", 30, 30)

contact_lbl = ctk.CTkLabel(side_frame, text="Lucena City, Quezon Prov.", font=("Robot", 14, "bold"), fg_color="transparent", anchor=CENTER, image=house_pic, compound=LEFT)
contact_lbl.place(x=30, y=430)

# hobbies
under_line = ctk.CTkLabel(side_frame, text="_________________", font=("Serif", 24, "bold"), fg_color="transparent", text_color="#f2f2f2", bg_color="transparent")
under_line.place(x=15, y=500)

contact_lbl = ctk.CTkLabel(side_frame, text="Hobbies", font=("Serif", 28), fg_color="transparent", anchor=CENTER)
contact_lbl.place(x=25, y=490)

contact_lbl = ctk.CTkLabel(side_frame, text="• Programming", font=("Robot", 20, "bold"), fg_color="transparent", anchor=CENTER)
contact_lbl.place(x=30, y=540)

contact_lbl = ctk.CTkLabel(side_frame, text="• Watching Movies", font=("Robot", 20, "bold"), fg_color="transparent", anchor=CENTER)
contact_lbl.place(x=30, y=580)

contact_lbl = ctk.CTkLabel(side_frame, text="• Reading Books", font=("Robot", 20, "bold"), fg_color="transparent", anchor=CENTER)
contact_lbl.place(x=30, y=620)

contact_lbl = ctk.CTkLabel(side_frame, text="• Playing Computer\nGames\t           ", font=("Robot", 20, "bold"), fg_color="transparent", anchor=CENTER)
contact_lbl.place(x=30, y=660)

# skills 
under_line = ctk.CTkLabel(side_frame, text="_________________", font=("Serif", 24, "bold"), fg_color="transparent", text_color="#f2f2f2", bg_color="transparent")
under_line.place(x=15, y=730)

contact_lbl = ctk.CTkLabel(side_frame, text="Skills", font=("Serif", 28), fg_color="transparent", anchor=CENTER)
contact_lbl.place(x=25, y=720)

contact_lbl = ctk.CTkLabel(side_frame, text="• Software Application\nDevelopment (Python)", font=("Robot", 20, "bold"), fg_color="transparent", anchor=CENTER)
contact_lbl.place(x=30, y=770)

contact_lbl = ctk.CTkLabel(side_frame, text="• Proficient in Tkinter", font=("Robot", 20, "bold"), fg_color="transparent", anchor=CENTER)
contact_lbl.place(x=30, y=820)
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------

main_frame = ctk.CTkFrame(root, fg_color="#f2f2f2", corner_radius=1)
main_frame.pack(side=RIGHT, fill=BOTH, expand=True)
main_frame.pack_propagate(False)


my_name = ctk.CTkLabel(main_frame, text="Jerwin Nico H. Quijano", font=("Serif", 32,"bold"), fg_color="transparent", anchor=CENTER, text_color="#000000")
my_name.pack(pady=20, padx=10)

my_name = ctk.CTkLabel(main_frame, text="Python Software Developer", font=("Serif", 24), fg_color="transparent", anchor=CENTER, text_color="#000000")
my_name.pack(pady=10, padx=10)

under_line = ctk.CTkLabel(main_frame, text="______________________________________", font=("Serif", 24, "bold"), fg_color="transparent", text_color="#000000", bg_color="transparent")
under_line.place(x=30, y=220)

contact_lbl = ctk.CTkLabel(main_frame, text="Objectives", font=("Serif", 28), fg_color="transparent", anchor=CENTER, text_color="#000000")
contact_lbl.place(x=40, y=210)

my_obj = ''''
To further enhance my Python skills and expand my abilities to contribute\neffectively in a dynamic and challenging evironment, leveraging\nmy technical expertise and dedication to continuous learning.
'''

contact_lbl = ctk.CTkLabel(main_frame, text=my_obj, font=("Robot", 14), fg_color="transparent", anchor=CENTER, text_color="#000000")
contact_lbl.place(x=35, y=250)

under_line = ctk.CTkLabel(main_frame, text="______________________________________", font=("Serif", 24, "bold"), fg_color="transparent", text_color="#000000", bg_color="transparent")
under_line.place(x=30, y=350)

contact_lbl = ctk.CTkLabel(main_frame, text="Education", font=("Serif", 28), fg_color="transparent", anchor=CENTER, text_color="#000000")
contact_lbl.place(x=40, y=340)


contact_lbl = ctk.CTkLabel(main_frame, text="COLLEGE", font=("Robot", 13, "bold"), fg_color="transparent", anchor=CENTER, text_color="#000000")
contact_lbl.place(x=45, y=400)

contact_lbl = ctk.CTkLabel(main_frame, text="DALUBHASAAN NG LUNGSOD NG LUCENA", font=("Robot", 13), fg_color="transparent", anchor=CENTER, text_color="#000000")
contact_lbl.place(x=250, y=400)

contact_lbl = ctk.CTkLabel(main_frame, text="BACHELOR OF SCIENCE IN\nINFORMATION TECHNOLOGY", font=("Robot", 18, "bold"), fg_color="transparent", anchor=CENTER, text_color="#000000")
contact_lbl.place(x=250, y=430)

contact_lbl = ctk.CTkLabel(main_frame, text="2023-Present", font=("Robot", 13), fg_color="transparent", anchor=CENTER, text_color="#000000")
contact_lbl.place(x=45, y=430)

#
contact_lbl = ctk.CTkLabel(main_frame, text="SENIOR HIGH", font=("Robot", 13, "bold"), fg_color="transparent", anchor=CENTER, text_color="#000000")
contact_lbl.place(x=45, y=500)

contact_lbl = ctk.CTkLabel(main_frame, text="QUEZON NATIONAL HIGH SCHOOL", font=("Robot", 13), fg_color="transparent", anchor=CENTER, text_color="#000000")
contact_lbl.place(x=260, y=500)

contact_lbl = ctk.CTkLabel(main_frame, text="TVL- ICT COMPUTER SYSTEM\nSERVICING", font=("Robot", 18, "bold"), fg_color="transparent", anchor=CENTER, text_color="#000000")
contact_lbl.place(x=250, y=530)

contact_lbl = ctk.CTkLabel(main_frame, text="2021-2023", font=("Robot", 13), fg_color="transparent", anchor=CENTER, text_color="#000000")
contact_lbl.place(x=45, y=530)

#

contact_lbl = ctk.CTkLabel(main_frame, text="JUNIOR HIGH", font=("Robot", 13, "bold"), fg_color="transparent", anchor=CENTER, text_color="#000000")
contact_lbl.place(x=45, y=600)

contact_lbl = ctk.CTkLabel(main_frame, text="QUEZON NATIONAL HIGH\nSCHOOL", font=("Robot", 18,"bold"), fg_color="transparent", anchor=CENTER, text_color="#000000")
contact_lbl.place(x=260, y=600)

contact_lbl = ctk.CTkLabel(main_frame, text="2017-2020", font=("Robot", 13), fg_color="transparent", anchor=CENTER, text_color="#000000")
contact_lbl.place(x=45, y=630)

#
contact_lbl = ctk.CTkLabel(main_frame, text="ELEMENTARY", font=("Robot", 13, "bold"), fg_color="transparent", anchor=CENTER, text_color="#000000")
contact_lbl.place(x=45, y=700)

contact_lbl = ctk.CTkLabel(main_frame, text="LUCENA SOUTH 1 ELEMENTARY\nSCHOOL", font=("Robot", 18,"bold"), fg_color="transparent", anchor=CENTER, text_color="#000000")
contact_lbl.place(x=250, y=700)

contact_lbl = ctk.CTkLabel(main_frame, text="2010-2016", font=("Robot", 13), fg_color="transparent", anchor=CENTER, text_color="#000000")
contact_lbl.place(x=45, y=730)

#
under_line = ctk.CTkLabel(main_frame, text="______________________________________", font=("Serif", 24, "bold"), fg_color="transparent", text_color="#000000", bg_color="transparent")
under_line.place(x=30, y=790)

contact_lbl = ctk.CTkLabel(main_frame, text="Language", font=("Serif", 28), fg_color="transparent", anchor=CENTER, text_color="#000000")
contact_lbl.place(x=40, y=780)


contact_lbl = ctk.CTkLabel(main_frame, text="Tagalog", font=("Robot", 18,"bold"), fg_color="transparent", anchor=CENTER, text_color="#000000")
contact_lbl.place(x=40, y=830)

contact_lbl = ctk.CTkLabel(main_frame, text="75%", font=("Robot", 14,"bold"), fg_color="transparent", anchor=CENTER, text_color="#000000")
contact_lbl.place(x=250, y=860)

my_progress_bar = ctk.CTkProgressBar(main_frame, mode="determinate")
my_progress_bar.set(75/100)
my_progress_bar.place(x=40, y=870)

#

contact_lbl = ctk.CTkLabel(main_frame, text="Skibidi", font=("Robot", 18,"bold"), fg_color="transparent", anchor=CENTER, text_color="#000000")
contact_lbl.place(x=290, y=830)

contact_lbl = ctk.CTkLabel(main_frame, text="100%", font=("Robot", 14,"bold"), fg_color="transparent", anchor=CENTER, text_color="#000000")
contact_lbl.place(x=500, y=860)

my_progress_bar = ctk.CTkProgressBar(main_frame, mode="determinate")
my_progress_bar.set(100/100)
my_progress_bar.place(x=290, y=870)
    

root.mainloop()