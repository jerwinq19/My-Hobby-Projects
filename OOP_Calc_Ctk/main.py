import customtkinter as ctk
from tkinter import *



class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        # size
        self.geometry(f"500x500")
        self.resizable(False,False)
        self.title("Simple OOP calculator")
        self.configure(fg_color="#f2f2f2")
        
        # font
        self.number_font = ("Roboto", 13, "bold")
        self.entry_font = ("Serif", 32, "bold")
        
        
        
        
        # widgets
        self.my_top_entry = ctk.CTkEntry(self, fg_color="#e2e2e2", width=400, height=130, border_color="#000000", border_width=2, font=self.entry_font, text_color="#000000")
        self.my_top_entry.pack(side=TOP, padx=10, pady=10, fill=X, expand=False)
        self.my_top_entry.pack_propagate(False)
        
        
        self.buttons_frame = ctk.CTkFrame(self, fg_color="#e2e2e2", border_color="#000000", border_width=2)
        self.buttons_frame.pack(side=BOTTOM, fill=BOTH, expand=True, padx=10, pady=10)
        self.buttons_frame.grid_propagate(False)
        
        # calculator buttons
        
        # row 7 to division 
        self.buttons_7 = ctk.CTkButton(self.buttons_frame, fg_color="#000000", text="7", font=self.number_font, width=110,height=50, command=lambda:self.add_number_ent_func("7"))
        self.buttons_7.grid(row=0, column=0, padx=5,pady=5)
        
        self.buttons_9 = ctk.CTkButton(self.buttons_frame, fg_color="#000000", text="8", font=self.number_font, width=110,height=50, command=lambda:self.add_number_ent_func("8"))
        self.buttons_9.grid(row=0, column=1, padx=5,pady=5)
        
        self.buttons_9 = ctk.CTkButton(self.buttons_frame, fg_color="#000000", text="9", font=self.number_font, width=110,height=50, command=lambda:self.add_number_ent_func("9"))
        self.buttons_9.grid(row=0, column=2, padx=5,pady=5)
        
        self.buttons_div = ctk.CTkButton(self.buttons_frame, fg_color="#000000", text="/", font=self.number_font, width=110,height=50, command=lambda:self.add_number_ent_func("/"))
        self.buttons_div.grid(row=0, column=3, padx=5,pady=5)

        # row 4 to multiplication
        self.buttons_4 = ctk.CTkButton(self.buttons_frame, fg_color="#000000", text="4", font=self.number_font, width=110,height=50, command=lambda:self.add_number_ent_func("4"))
        self.buttons_4.grid(row=1, column=0, padx=5,pady=5)
        
        self.buttons_5 = ctk.CTkButton(self.buttons_frame, fg_color="#000000", text="5", font=self.number_font, width=110,height=50, command=lambda:self.add_number_ent_func("5"))
        self.buttons_5.grid(row=1, column=1, padx=5,pady=5)
        
        self.buttons_6 = ctk.CTkButton(self.buttons_frame, fg_color="#000000", text="6", font=self.number_font, width=110,height=50, command=lambda:self.add_number_ent_func("6"))
        self.buttons_6.grid(row=1, column=2, padx=5,pady=5)
        
        self.buttons_mutli = ctk.CTkButton(self.buttons_frame, fg_color="#000000", text="*", font=self.number_font, width=110,height=50, command=lambda:self.add_number_ent_func("*"))
        self.buttons_mutli.grid(row=1, column=3, padx=5,pady=5)

        # row 1 to minus
        self.buttons_1 = ctk.CTkButton(self.buttons_frame, fg_color="#000000", text="1", font=self.number_font, width=110,height=50, command=lambda:self.add_number_ent_func("1"))
        self.buttons_1.grid(row=2, column=0, padx=5,pady=5)
        
        self.buttons_2 = ctk.CTkButton(self.buttons_frame, fg_color="#000000", text="2", font=self.number_font, width=110,height=50, command=lambda:self.add_number_ent_func("2"))
        self.buttons_2.grid(row=2, column=1, padx=5,pady=5)
        
        self.buttons_3 = ctk.CTkButton(self.buttons_frame, fg_color="#000000", text="3", font=self.number_font, width=110,height=50, command=lambda:self.add_number_ent_func("3"))
        self.buttons_3.grid(row=2, column=2, padx=5,pady=5)
        
        self.buttons_minus = ctk.CTkButton(self.buttons_frame, fg_color="#000000", text="-", font=self.number_font, width=110,height=50, command=lambda:self.add_number_ent_func("-"))
        self.buttons_minus.grid(row=2, column=3, padx=5,pady=5)
        
        # row 0 to equal
        self.buttons_0 = ctk.CTkButton(self.buttons_frame, fg_color="#000000", text="0", font=self.number_font, width=110,height=50, command=lambda:self.add_number_ent_func("0"))
        self.buttons_0.grid(row=3, column=0, padx=5,pady=5)
        
        self.buttons_dot = ctk.CTkButton(self.buttons_frame, fg_color="#000000", text=".", font=self.number_font, width=110,height=50, command=lambda:self.add_number_ent_func("."))
        self.buttons_dot.grid(row=3, column=1, padx=5,pady=5)
        
        self.buttons_del = ctk.CTkButton(self.buttons_frame, fg_color="#000000", text="del", font=self.number_font, width=110,height=50, command=lambda:self.delete_ent_num_func())
        self.buttons_del.grid(row=3, column=2, padx=5,pady=5)
        
        self.buttons_plus = ctk.CTkButton(self.buttons_frame, fg_color="#000000", text="+", font=self.number_font, width=110,height=50, command=lambda:self.add_number_ent_func("+"))
        self.buttons_plus.grid(row=3, column=3, padx=5,pady=5)
        
        # Del All and Equal
        
        self.buttons_eq = ctk.CTkButton(self.buttons_frame, fg_color="#000000", text="C", font=self.number_font, width=110,height=50, command=lambda:self.delete_all_ent())
        self.buttons_eq.grid(row=4, column=2, padx=5,pady=5)
            
        self.buttons_eq = ctk.CTkButton(self.buttons_frame, fg_color="#000000", text="=", font=self.number_font, width=110,height=50, command=lambda:self.equal_btn_func())
        self.buttons_eq.grid(row=4, column=3, padx=5,pady=5)
    
    def add_number_ent_func(self, num):
        self.my_top_entry.configure(font=("Serif", 32, "bold"))
        self.my_top_entry.insert(END, num)
    
    def delete_ent_num_func(self):
        self.my_top_entry.delete(len(self.my_top_entry.get()) - 1, END)
    
    def delete_all_ent(self):
        self.my_top_entry.delete(0, END)
    
    def equal_btn_func(self):
        get_num = self.my_top_entry.get()

        try:    
            tite = eval(get_num)
            self.delete_all_ent()
            self.my_top_entry.insert(0, tite)
        except ZeroDivisionError:
            self.delete_all_ent()
            self.my_top_entry.configure(font=("Serif", 24, "bold"))
            self.my_top_entry.insert(0, "You cannot devide Zero by Zero")
        except SyntaxError:
            self.delete_all_ent()
            self.my_top_entry.configure(font=("Serif", 24, "bold"))
            self.my_top_entry.insert(0, "Syntax Error")
            
        
app = App()
app.mainloop()