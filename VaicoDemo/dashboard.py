# python_live_plot.py

import random
from itertools import count
from random import random


import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib.dates as mdates

import AImovility.auxfunc.globals as gb


import VaicoDemo.config as cnf

# plt.style.use('fivethirtyeight')

colors_1 = [(random(),random(),random()) for o in cnf.objects_interest]
colors_2 = [(random(),random(),random()) for o in cnf.objects_interest]

def animate(i):
    data = pd.read_csv('/home/juanc/results/live_plot_data.csv')

    # fig, axs = plt.subplots(2)

    x_time = data['time']
    i=0
    for o in cnf.objects_interest:
        y_values = data[o]
        axs[0].plot(x_time, y_values, color=colors_1[i])
        i += 1

    axs[0].legend(cnf.objects_interest) 
    # axs[0].xlabel('Tiempo')
    # axs[0].ylabel('Número')
    # axs[0].title('Número objetos en tiempo')

    date_formatter = mdates.DateFormatter('%H%M%S')

    # Set the major tick formatter to use your date formatter.
   
    i=0
    for d in gb.DIRECTIONS:
        y_values = data[d]
        axs[1].plot(x_time, y_values, color=colors_2[i])
        i += 1
    axs[1].legend(gb.DIRECTIONS) 

    # axs[1].xaxis.set_major_formatter(date_formatter)


    # plt.tight_layout()


fig, axs = plt.subplots(2)
fig.autofmt_xdate()


# ani = FuncAnimation(plt.gcf(), animate, 5000)
ani = FuncAnimation(fig, animate, 5000)

plt.tight_layout()
plt.show()