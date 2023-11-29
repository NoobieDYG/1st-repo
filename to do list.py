#to do list
from tkinter import * 
from tkinter.font import Font

root=Tk()
root.geometry('500x500')

#font
my_font= Font(
    family="Brush Script MT",
    size=30,
    weight="bold")

my_frame = Frame(root)
my_frame.pack(pady=10)

#list

my_list = Listbox(my_frame, font = my_font, width = 25, height= 15, highlightthickness=0, selectbackground="#a6a6a6", activestyle="none", bg="SystemButtonFace")

my_list.pack()

stuff=["walk the dog", "learn tkinter", "rule the world"]
for item in stuff:
    my_list.insert(END, item)

#add scrollbar
my_scrollbar = Scrollbar(my_frame)
my_scrollbar.pack(side=RIGHT, fill=BOTH)

my_list.config(yscrollcommand=my_scrollbar.set)
my_scrollbar.config(command=my_list.yview)

#entrybox


my_entry = Entry(root, font=('Helvetica', 24), selectbackground="#a6a6a6")
my_entry.pack(pady=20)



#create button frame

button_frame = Frame(root, bg="red")
button_frame.pack(pady=20)

#functions
def delete_item():
    my_list.delete(ANCHOR)
def add_item():
    my_list.insert(END, my_entry.get())
    my_entry.delete(0,END)
def cross_off_item():
    my_list.itemconfig(my_list.curselection(), fg="#dedede")
    my_list.selection_clear(0, END)
def uncross_item():
    my_list.itemconfig(my_list.curselection(), fg="#464646")
    my_list.selection_clear(0, END)
def delete_crossed():
    count = 0
    while count < my_list.size():
        if my_list.itemcget(count, 'fg') == "#dedede":
            my_list.delete(my_list.index(count))
    count = count+1


#add button
delete_button= Button(button_frame, text="Delete Item", command=delete_item)
add_button= Button(button_frame, text="ADD ITEM", command=add_item)
cross_off_button= Button(button_frame, text="Cross off ITEM", command=cross_off_item)
uncross_button= Button(button_frame, text="Uncross ITEM", command=uncross_item)
delete_crossed_button= Button(button_frame, text="Delete crossed", command= delete_crossed)


delete_button.pack(side="left")
add_button.pack(side="left", padx=20)
cross_off_button.pack(side="left")
uncross_button.pack(side="left", padx=20)
delete_crossed_button.pack(side="left", padx=20)

root.mainloop()
