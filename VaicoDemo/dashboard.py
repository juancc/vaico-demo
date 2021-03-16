# python_live_plot.py

import random
from itertools import count
from random import random
import json

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib.dates as mdates

import AImovility.auxfunc.globals as gb

with open('VaicoDemo/config.json', 'r') as f:
    config = json.load(f)


# plt.style.use('fivethirtyeight')

COLORS_1 = [(random(),random(),random()) for o in config['objects_interest']]
COLORS_2 = [(random(),random(),random()) for o in gb.MOVEMENT]
COLORS_3 = [(random(),random(),random()) for o in gb.DIRECTIONS]


def animate(i):
    try:
        data = pd.read_csv('/home/juanc/results/live_plot_data.csv')
                
        # Count on time
        x_time = data['time']
        i=0
        for o in config['objects_interest']:
            y_values = data[o]
            axs[0].plot(x_time, y_values, color=COLORS_1[i])
            i += 1

        axs[0].legend(config['objects_interest']) 
        # axs[0].xlabel('Tiempo')
        # axs[0].ylabel('Número')
        # axs[0].title('Número objetos en tiempo')

        # date_formatter = mdates.DateFormatter('%H%M%S')

        # Movement state
        dir_count = []
        for d in gb.MOVEMENT:
            dir_count.append(sum(data[d]))

        axs[1].bar(gb.MOVEMENT, dir_count, color=COLORS_2)
        axs[1].legend(gb.MOVEMENT, labelcolor=COLORS_2) 

        # Directions
        i=0
        for o in gb.DIRECTIONS:
            y_values = data[o]
            axs[2].plot(x_time, y_values, color=COLORS_3[i])
            i += 1

        axs[2].legend(gb.DIRECTIONS) 
        plt.xticks([])


        # plt.tight_layout()
    except FileNotFoundError:
        print('live_plot_data not found')


fig, axs = plt.subplots(3, sharex=False, sharey=False)
fig.autofmt_xdate()
ani = FuncAnimation(fig, animate, 5000)

plt.tight_layout()
plt.show()