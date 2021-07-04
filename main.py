from tkinter import *
from tkinter import ttk
import random
from colors import *

# Importing algorithms 
from Sorting_python.BubbleSort import bubble_sort
from Sorting_python.SelectionSort import selection_sort
from Sorting_python.InsertionSort import insertion_sort
from Sorting_python.MergeSort import merge_sort
from Sorting_python.quickSort import quick_sort
# from Python.quickSort import quick_sort
# from Python.heapSort import heap_sort
# from Python.countingSort import counting_sort


# Main window 
root = Tk()
root.geometry("1200x700")
root.title("Sorting Algorithms Visualization")
root.resizable(False, False) 
root.config(bg = DARK_GRAY)

lret = []
algorithm_name = StringVar()
speed_name = StringVar()
arr = []
algo_list = ['Bubble Sort', 'Insertion Sort', 'Selection Sort', 'Merge Sort','Quick Sort']
speed_list = ['Fast(100%)', 'Medium(65%)', 'Slow(25%)']


# Drawing the numerical array as bars
def drawArray(arr, colorArray):
    canvas.delete("all")
    canvas_width = 1150
    canvas_height = 400
    x_width = canvas_width / (len(arr) + 1)
    offset = 4
    spacing = 1.5
    normalizedData = [i / max(arr) for i in arr]
    # playsound("./resources/note.mp3")
    for i, height in enumerate(normalizedData):
        x0 = i * x_width + offset + spacing
        y0 = canvas_height - height * 390
        x1 = (i + 1) * x_width + offset
        y1 = canvas_height
        canvas.create_rectangle(x0, y0, x1, y1, fill=colorArray[i])
    root.update_idletasks()


# Randomly generate array
def generate():
    global arr
    global lret
    for widgets in UI_frame1.winfo_children():
      widgets.destroy() 
    arr = []
    for i in range(0, 200):
        random_value = random.randint(1, 150)
        arr.append(random_value)

    drawArray(arr, [BLUE for x in range(len(arr))])


def set_speed():
    # spd = int(speed_menu.get()
    if speed_menu.get() == 'Slow(25%)':
        return 0.25
    elif speed_menu.get() == 'Medium(60%)':
        return 0.09
    else:
        return 0.00003




### User interface ###
UI_frame = Frame(root, width= 500, height=300, bg=LIGHT_GRAY)
UI_frame.grid(row=0, column=0, padx=0, pady=10)

l1 = Label(UI_frame, text="Algorithm: ", bg=LIGHT_GRAY)
l1.grid(row=0, column=0, padx=10, pady=5, sticky=W)
algo_menu = ttk.Combobox(UI_frame, textvariable=algorithm_name, values=algo_list)
algo_menu.grid(row=0, column=1, padx=5, pady=5)
algo_menu.current(0)

l2 = Label(UI_frame, text="Visualization Speed: ", bg=LIGHT_GRAY)
l2.grid(row=1, column=0, padx=10, pady=5, sticky=W)
speed_menu = ttk.Combobox(UI_frame, textvariable=speed_name, values=speed_list)
speed_menu.grid(row=1, column=1, padx=5, pady=5)
speed_menu.current(0)

UI_frame1 = Frame(root ,bg=LIGHT_GRAY)
UI_frame1.grid(row=3, column=0, padx=0, pady=5)

def display_stats(lret):
    ldefine = Label(UI_frame1,font=("Arial", 12), text=str(lret[3]), bg=LIGHT_GRAY,width=80,wraplength=700, justify="center")
    ldefine.grid(row=0, column=0, padx=0, pady=5, sticky=W)

    lcomp = Label(UI_frame1,font=("Arial", 13), text="Comparison: "+str(lret[0]), bg=LIGHT_GRAY,width=80)
    lcomp.grid(row=1, column=0, padx=0, pady=3, sticky=W)

    ltime = Label(UI_frame1,font=("Arial", 13), text="Time Complexity: "+str(lret[1]), bg=LIGHT_GRAY,width=80)
    ltime.grid(row=2,column=0, padx=10, pady=3, sticky=W)

    lspace = Label(UI_frame1,font=("Arial", 13), text="Space Complexity: "+str(lret[2]), bg=LIGHT_GRAY,width=80)
    lspace.grid(row=3,column=0, padx=0, pady=3, sticky=W)



canvas = Canvas(root, width=1150, height=400, bg=BLACK)
canvas.grid(row=1, column=0, padx=25, pady=5)

def sort():
    global arr
    global lret
    timer = set_speed()
    
    if algo_menu.get() == 'Bubble Sort':
        timer = 0
        lret = bubble_sort(arr, drawArray, timer)
        display_stats(lret)
    elif algo_menu.get() == 'Selection Sort':
        lret = selection_sort(arr, drawArray, timer)
        display_stats(lret)
    elif algo_menu.get() == 'Insertion Sort':
        lret =insertion_sort(arr, drawArray, timer)
        display_stats(lret)
    elif algo_menu.get() == 'Quick Sort':
        lret = quick_sort(arr, 0, len(arr)-1, drawArray, timer)
        display_stats(lret)
    else:
        lret =  merge_sort(arr,0,len(arr)-1,drawArray,timer)
        display_stats(lret)
    # elif algo_menu.get() == 'Quick Sort':
    #     quick_sort(arr, 0, len(arr)-1, drawArray, timer)
    # elif algo_menu.get() == 'Heap Sort':
    #     heap_sort(arr, drawArray, timer)
    # else:
    #     counting_sort(arr, drawArray, timer)
b1 = Button(UI_frame, text="Sort", command=sort,fg=WHITE, bg=GRAY)
b1.grid(row=2, column=1, padx=5, pady=5)

b3 = Button(UI_frame, text="Generate Array", command=generate, fg=WHITE,bg=GRAY)
b3.grid(row=2, column=0, padx=5, pady=5)



root.mainloop()
