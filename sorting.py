from tkinter import *
from tkinter import ttk
import random as rn
from bubble_sort import bubble_sort
from insert_sort import insert_sort

root = Tk()
root.title('Sorting Algorithm Visualisation')
root.maxsize(1025, 610)
root.minsize(1025, 610)
root.config(bg='black')

# Variables

selected_alg = StringVar()
data = []  


def drawdata(data, colorarray):
    canvas.delete('all')
    c_height = 480
    c_width = 1000
    x_width = c_width / len(data)
    offset = 5
    spacing = 5
    norm_data = [i / max(data) for i in data]
    for i, height in enumerate(norm_data):
        # top left of rectangle
        x0 = i * x_width + offset + spacing
        y0 = c_height - height * 440
        # bottom right of rectangle
        x1 = (i + 1) * x_width + offset
        y1 = c_height

        canvas.create_rectangle(x0, y0, x1, y1, fill=colorarray[i])
        canvas.create_text(x0+2, y0, anchor=SW, text=str(data[i]))

    root.update()


def generate():
    global data
    minval = min_value.get()
    maxval = max_value.get()
    size = size_scale.get()
    if minval > maxval:
        minval, maxval = maxval, minval
    data = []
    for _ in range(size):
        data.append(rn.randrange(minval, maxval + 1))
    drawdata(data, ['deep sky blue' for x in range(len(data))])


def start_algo():
    global data
    if not data:
        return

    if algmenu.get() == 'Bubble Sort':
        bubble_sort(data, drawdata, speed_scale.get())
    elif algmenu.get() == 'Insertion Sort':
        insert_sort(data, drawdata, speed_scale.get())
    for i in range(len(data)):
        drawdata(data, ['salmon' if x ==
                        i else 'deep sky blue' for x in range(len(data))])
    drawdata(data, ['spring green' for x in range(len(data))])


# Frames
ui_frame = Frame(root, width=1000, height=200, bg='black')
ui_frame.grid(row=0, column=0, padx=10, pady=5)

canvas = Canvas(root, width=1000, height=480, bg='white')
canvas.grid(row=1, column=0, padx=10, pady=5)

# User interface area
# Row[0]

algmenu = ttk.Combobox(ui_frame, width=9, textvariable=selected_alg,
                       values=['Bubble Sort', 'Insertion Sort'])
algmenu.grid(row=0, column=0, padx=5, pady=5)
algmenu.current(0)

Button(ui_frame, text='Generate',bg='red', command=generate).grid(
    row=0, column=1, padx=5, pady=5)

Button(ui_frame, text='Start', bg ='green', command=start_algo).grid(
    row=0, column=3, padx=5, pady=5)


# Row[1]
size_scale = Scale(ui_frame, from_=0, to_=350, resolution=1,
                   orient=HORIZONTAL, width=10, label='Data Size')
size_scale.grid(
    row=1, column=0, padx=5, pady=5, sticky=W)

min_value = Scale(ui_frame, from_=0, to_=20,
                  orient=HORIZONTAL, width=10, label='Min Value')
min_value.grid(
    row=1, column=1, padx=5, pady=5, sticky=W)

max_value = Scale(ui_frame, from_=50, to_=999,
                  orient=HORIZONTAL, width=10, label='Max Value')
max_value.grid(
    row=1, column=2, padx=5, pady=5, sticky=W)

speed_scale = Scale(ui_frame, from_=0.01, to_=1.0, orient=HORIZONTAL,
                    resolution=0.01, width=10, label='Speed (S)')
speed_scale.grid(
    row=1, column=3, padx=5, pady=5)


root.mainloop()
