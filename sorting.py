from tkinter import *
from tkinter import ttk
import random
import matplotlib.pyplot as plt
import time
import math
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from bubblesort import bubble_sort, insertion_sort, selection_sort, merge_sort, heap_sort, quick_sort

root = Tk()
root.title('Sorting Algorithm Visualiser')
root.geometry('900x700+200+80')
root.config(bg='#082A46')
data = []

comparison_count = 0
is_running = False

def drawData(data, colorArray, chartType):
    global comparison_count, is_running
    plt.clf()
    speed_value = speedscale.get()

    if chartType == 'Scatter':
        plt.scatter(range(len(data)), data, color=colorArray)
    elif chartType == 'Bar':
        plt.bar(range(len(data)), data, color=colorArray)
    elif chartType == 'Stem':
        plt.stem(range(len(data)), data, linefmt='-', markerfmt='.', basefmt=' ')

    plt.xticks(range(len(data)), range(len(data)))  # X koordinatlarına sayıları ekler
    plt.yticks(data)  # Y koordinatlarına sayıları ekler
    for i, value in enumerate(data):
        plt.text(i, value, str(value), ha='center', va='bottom', fontsize=8)
    plt.pause(speed_value)
    canvas.draw()

    comparison_count += 1
    if comparison_count % 100 == 0:
        comparison_label.config(text="Karşılaştırma Sayısı: " + str(comparison_count))
        root.update_idletasks()

    if not is_running:  # Animasyon durduysa
        return

def stopAlgorithm():
    global is_running
    is_running = False

def StartAlgorithm():
    global data, comparison_count, is_running
    comparison_count = 0
    comparison_label.config(text="Karşılaştırma Sayısı" + str(comparison_count))
    selected_chart = selected_chart_type.get()
    selected_algorithm = algo_menu.get()

    if selected_algorithm == 'Bubble Sort':
        is_running = True
        bubble_sort(data, drawData, speedscale.get(), selected_chart)
        print(data)
    elif selected_algorithm == 'Insertion Sort':
        is_running = True
        insertion_sort(data, drawData, speedscale.get(), selected_chart)
        print(data)
    elif selected_algorithm == 'Selection Sort':
        is_running = True
        selection_sort(data, drawData, speedscale.get(), selected_chart)
        print(data)
    elif selected_algorithm == 'Merge Sort':
        is_running = True
        merge_sort(data, drawData, speedscale.get(), selected_chart)
        print(data)
    elif selected_algorithm == 'Heap Sort':
        is_running = True
        heap_sort(data, drawData, speedscale.get(), selected_chart)
        print(data)
    elif selected_algorithm == 'Quick Sort':
        is_running = True
        quick_sort(data, 0, len(data) - 1, drawData, speedscale.get(), selected_chart)
        print(data)

    comparison_label.config(text="Karşılaştırma Sayısı: " + str(comparison_count))
    complexity_label.config(text="Karmaşıklık Analizi:"  )
    if selected_algorithm == 'Merge Sort':
        complexity_label.config( text="Karmaşıklık Analizi:" + str(int (sizevalue.get()) ** 2) )
    elif selected_algorithm == 'Heap Sort':
     size = int(sizevalue.get())
     complexity = size * math.log(size)
     complexity_label.config(text="Karmaşıklık Analizi: " + str(complexity))
    elif selected_algorithm == 'Quick Sort':
     size = int(sizevalue.get())
     complexity2 = size * math.log(size)
     complexity_label.config(text="Karmaşıklık Analizi: " + str(complexity2))
    elif selected_algorithm == 'Selection Sort':
        complexity_label.config (text="Karmaşıklık Analizi:" + str(int (sizevalue.get()) ** 2) )
    elif selected_algorithm == 'Bubble Sort':
        complexity_label.config (text="Karmaşıklık Analizi:" + str(int (sizevalue.get()) ** 2 ) ) 
    elif selected_algorithm == 'Insertion Sort':
        complexity_label.config (text="Karmaşıklık Analizi:" +  str(int (sizevalue.get()) ** 2 ) )


def resetAlgorithm():
    global data, is_running
    is_running = False
    data = []
    canvas.get_tk_widget().destroy()
    comparison_label.config(text="Karşılaştırma Sayısı:" + str(comparison_count) )
    complexity_label.config(text="Karmaşıklık Analizi:"  )
    if selected_algorithm == 'Merge Sort':
        complexity_label.config( text="Karmaşıklık Analizi:" + str(int (sizevalue.get()) ** 2) )
    elif selected_algorithm == 'Heap Sort':
     size = int(sizevalue.get())
     complexity = size * math.log(size)
     complexity_label.config(text="Karmaşıklık Analizi: " + str(complexity))
    elif selected_algorithm == 'Quick Sort':
     size = int(sizevalue.get())
     complexity2 = size * math.log(size)
     complexity_label.config(text="Karmaşıklık Analizi: " + str(complexity2))
    elif selected_algorithm == 'Selection Sort':
        complexity_label.config (text="Karmaşıklık Analizi:" + str(int (sizevalue.get()) ** 2) )
    elif selected_algorithm == 'Bubble Sort':
        complexity_label.config (text="Karmaşıklık Analizi:" + str(int (sizevalue.get()) ** 2 ) ) 
    elif selected_algorithm == 'Insertion Sort':
        complexity_label.config (text="Karmaşıklık Analizi:" +  str(int (sizevalue.get()) ** 2 ) )


def speed():
    speed_value = speedscale.get()
    if speed_value == 000.1:
        return 0.001
    elif speed_value == 0.3:
        return 0.05
    elif speed_value == 0.5:
        return 0.1
    elif speed_value == 0.7:
        return 0.2
    elif speed_value == 0.9:
        return 0.3
    elif speed_value == 1.1:
        return 0.4
    elif speed_value == 1.3:
        return 0.6
    elif speed_value == 1.5:
        return 0.8
    elif speed_value == 1.7:
        return 1.0
    elif speed_value == 1.9:
        return 1.2
    else:
        return 0.001

def Generate():
    global data
    print('Selected Algorithm: ' + algo_menu.get())
    minivalue = int(minvalue.get())
    maxivalue = int(maxvalue.get())
    sizeevalue = int(sizevalue.get())

    if minivalue >= maxivalue:
        maxivalue = minivalue + 1

    if sizeevalue < 3:
        sizeevalue = 3

    data = random.sample(range(minivalue, maxivalue + 1), sizeevalue)
    print(data)
    drawData(data, ['yellow' for _ in range(len(data))], selected_chart_type.get())
    comparison_label.config(text="Karşılaştırma Sayısı:" + str(comparison_count) )
    complexity_label.config(text="Karmaşıklık Analizi:"  )
    if selected_algorithm == 'Merge Sort':
        complexity_label.config( text="Karmaşıklık Analizi:" + str(int (sizevalue.get()) ** 2) )
    elif selected_algorithm == 'Heap Sort':
     size = int(sizevalue.get())
     complexity = size * math.log(size)
     complexity_label.config(text="Karmaşıklık Analizi: " + str(complexity))
    elif selected_algorithm == 'Quick Sort':
     size = int(sizevalue.get())
     complexity2 = size * math.log(size)
     complexity_label.config(text="Karmaşıklık Analizi:" + str(complexity2))
    elif selected_algorithm == 'Selection Sort':
        complexity_label.config (text="Karmaşıklık Analizi:" + str(int (sizevalue.get()) ** 2) )
    elif selected_algorithm == 'Bubble Sort':
        complexity_label.config (text="Karmaşıklık Analizi:" + str(int (sizevalue.get()) ** 2 ) ) 
    elif selected_algorithm == 'Insertion Sort':
        complexity_label.config (text="Karmaşıklık Analizi:" +  str(int (sizevalue.get()) ** 2 ) )
selected_algorithm = StringVar()
selected_chart_type = StringVar()
 

chart_type_menu = ttk.Combobox(root, width=10, font=("new roman", 12, "italic bold"),
                              textvariable=selected_chart_type, values=['Scatter', 'Bar', 'Stem'])
chart_type_menu.place(x=155, y=10)
chart_type_menu.current(0)

mainlabel = Label(root, text= "Algorithm :", font = ("new roman",16,"italic bold"),bg = "#0E6DA5",
                  width = 10, fg= "black", relief = GROOVE,bd = 5 )
mainlabel.place(x=0, y=0)

algo_menu = ttk.Combobox(root, width=15 , font = ("new roman",19,"italic bold"), textvariable= selected_algorithm,
values= ['Bubble Sort','Insertion Sort', 'Selection Sort', 'Merge Sort','Heap Sort','Quick Sort'])
algo_menu.place(x=145, y=0)
algo_menu.current(0)

mainlabel = Label(root, text= "Graphic :", font = ("new roman",16,"italic bold"),bg = "#0E6DA5",
                  width = 10, fg= "black", relief = GROOVE,bd = 5 )
mainlabel.place(x=0, y=40)

chart_type_menu = ttk.Combobox(root, width=15, font=("new roman", 19, "italic bold"),
                              textvariable=selected_chart_type,
                              values=['Scatter', 'Bar', 'Stem'])
chart_type_menu.place(x=145, y=40)
chart_type_menu.current(0)

random_generate = Button(root, text="Generate",bg = "#0E6DA5",font = ("arial",12,"italic bold"),relief = SUNKEN,
activebackground = "#05945B", activeforeground= "white",bd=5,width=8,command = Generate)
random_generate.place(x=750,y=110)

sizevaluelabel = Label(root, text= "Size : ", font= ("new roman",12,"italic bold"),bg="#0E6DA5",
                       width=10, height=2, fg= "black", relief= GROOVE, bd=5)
sizevaluelabel.place(x=0,y=90)

sizevalue = Scale(root,from_ = 0 , to = 30, resolution = 1, orient = HORIZONTAL, font = ("arial",14,"italic bold"),
                relief = GROOVE, bd = 2, width = 10)
sizevalue.place(x=120,y=90)

minsizevaluelabel = Label(root, text= "Min Value: ", font= ("new roman",12,"italic bold"),bg= "#0E6DA5",
                       width=10, height=2, fg= "black", relief= GROOVE, bd=5)
minsizevaluelabel.place(x=250,y=90)

minvalue = Scale(root,from_ = 0 , to = 10, resolution = 1, orient = HORIZONTAL, font = ("arial",14,"italic bold"),
                relief = GROOVE, bd = 2, width = 10)
minvalue.place(x=370,y=90)

maxsizevaluelabel = Label(root, text= "Max Value: ", font= ("new roman",12,"italic bold"),bg= "#0E6DA5",
                       width=10, height=2, fg= "black", relief= GROOVE, bd=5)
maxsizevaluelabel.place(x=500,y=90)

maxvalue = Scale(root,from_ = 0 , to = 100, resolution = 1, orient = HORIZONTAL, font = ("arial",14,"italic bold"),
                relief = GROOVE, bd = 2, width = 10)
maxvalue.place(x=620,y=90)

start = Button(root, text="Start",bg = "#0E6DA5",font = ("arial",12,"italic bold"),relief = SUNKEN,
activebackground = "#05945B", activeforeground= "white",bd=5,width=8, command=StartAlgorithm)
start.place(x=750,y=0)

stop = Button(root, text="Stop", bg="#0E6DA5", font=("arial", 12, "italic bold"), relief=SUNKEN,
              activebackground="#05945B", activeforeground="white", bd=5, width=8, command=stopAlgorithm)
stop.place(x=750, y=30)

reset = Button(root, text="Reset", bg="#0E6DA5", font=("arial", 12, "italic bold"), relief=SUNKEN,
               activebackground="#05945B", activeforeground="white", bd=5, width=8, command=resetAlgorithm)
reset.place(x=750, y=60)

speedlabel = Label(root, text= "Speed : ", font= ("new roman",12,"italic bold"),bg= "#0E6DA5",
                       width=10, height=2, fg= "black", relief= GROOVE, bd=5)
speedlabel.place(x=400,y=0)

speedscale = Scale(root,from_ = 0.1 , to = 2.0, resolution = 0.2, length=200, digits=2,  orient = HORIZONTAL, font = ("arial",14,"italic bold"),
                relief = GROOVE, bd = 2, width = 10)
speedscale.place(x=520,y=0)
comparison_label = Label(root, text="Karşılaştırma Sayısı:", font=("new roman", 12, "italic bold"), bg="#0E6DA5",
                         width=17, height=2, fg="black", relief=GROOVE, bd=5)
comparison_label.place(x=0, y=630)

complexity_label = Label(root, text="Karmaşıklık Analizi:", font=("new roman", 12, "italic bold"), bg="#0E6DA5",
                         width=25, height=2, fg="black", relief=GROOVE, bd=5)
complexity_label.place(x=200, y=630)

figure = plt.Figure(figsize=(6, 5), dpi=100)
ax = figure.add_subplot(111)

# canvas = Canvas(root, width = 870, height = 450, bg= "black" )
# canvas.place(x=10,y=170)

canvas = plt.figure(figsize=(8.7, 4.5))
canvas = FigureCanvasTkAgg(canvas, master=root)
canvas.get_tk_widget().place(x=10, y=170)

root.mainloop()

