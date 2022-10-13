from tkinter import *
import backend
# Layout of the UI
windows = Tk()

# Label on the UI
title = Label(windows, text="Title")
title.grid(row=0, column=0)

Author = Label(windows, text="Author")
Author.grid(row=0, column=2)

Year = Label(windows, text="Year")
Year.grid(row=1, column=0)

ISBN = Label(windows, text="ISBN")
ISBN.grid(row=1, column=2)

# Input on the UI
title_text = StringVar()
e1 = Entry(windows, textvariable=title_text)
e1.grid(row=0, column=1)
Author_text = StringVar()
e2 = Entry(windows, textvariable=Author_text)
e2.grid(row=0, column=3)
Year_text = StringVar()
e3 = Entry(windows, textvariable=Year_text)
e3.grid(row=1, column=1)
ISBN_text = StringVar()
e4 = Entry(windows, textvariable=ISBN_text)
e4.grid(row=1, column=3)

# List of book and scroll button on the UI
list1 = Listbox(windows, height=6, width=35)
list1.grid(row=2, column=0, rowspan=6, columnspan=2)

sb = Scrollbar(windows)
sb.grid(row=2, column=2, rowspan=6)

sb.config(command=list1.yview)
list1.config(yscrollcommand=sb.set)

# Button on the UI
b1 = Button(windows, text="View All", width=12)
b1.grid(row=2, column=3)
b2 = Button(windows, text="select an entry", width=12)
b2.grid(row=3, column=3)
b3 = Button(windows, text="Add entry", width=12)
b3.grid(row=4, column=3)
b4 = Button(windows, text="Update entry", width=12)
b4.grid(row=5, column=3)
b5 = Button(windows, text="Delete", width=12)
b5.grid(row=6, column=3)
b6 = Button(windows, text="Close", width=12)
b6.grid(row=7, column=3)
windows.mainloop()
