import tkinter

main_window = tkinter.Tk()

label1  = tkinter.Label(main_window,text="hallo world")
label2  = tkinter.Label(main_window,text="hallo cai")

tombol1 = tkinter.Button(main_window,text="tombol1")
tombol2 = tkinter.Button(main_window,text="tombol2")
# methood positioning
label1.pack()
label2.pack()
tombol1.pack()
tombol2.pack()

# method GUI

main_window.mainloop()