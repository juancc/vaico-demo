"""
Script for Movilab Demoday
Run AI-movility package for detect and track vehicles
 - Generates report of number of vehicles and pedestrians
 - Create video output of detections

"https://youtu.be/eJ7ZkQ5TC08" # street
"https://youtu.be/CkVJyAKwByw" # funny
"http://185.194.123.84:8001/mjpg/video.mjpg" # shop online


JCA
Vaico
"""
import sys
import logging
import tkinter as tk
import json

from subprocess import Popen, PIPE


logging.basicConfig(level=logging.DEBUG)


with open('VaicoDemo/config.json', 'r') as f:
    config = json.load(f)

LOGGER = logging.getLogger()

def run():
    config['video'] = Entry3.get()
    config['save_path'] = Entry4.get()
    config['sampling'] = Entry5.get()

    # Cast to int if digits
    config['video'] = int(config['video']) if config['video'].isdigit() else str(config['video'])
    config['sampling'] = int(config['sampling']) if config['sampling'].isdigit() else str(config['sampling'])

    
    with open('VaicoDemo/config.json', 'w') as f:
        json.dump(config, f)

    process_detect = Popen(['./venv/bin/python', '-m', 'VaicoDemo.detector'], stdout=PIPE, stderr=PIPE)
    process_draw = Popen(['./venv/bin/python', '-m', 'VaicoDemo.dashboard'], stdout=PIPE, stderr=PIPE)
    stdout, stderr = process_detect.communicate()
    print('Done!')


# Create interface for configuration and launch detector and dashboard
root = tk.Tk()
root.geometry("600x200")
root.title('Vaico-Demo')
root.grid_columnconfigure((0,1), weight=1)

Label3 = tk.Label(root, text="Source")
Label4 = tk.Label(root, text="Save Path")
Label5 = tk.Label(root, text="Sampling")

Entry3 = tk.Entry(root)
Entry3.insert(0, config['video'])
Entry4 = tk.Entry(root)
Entry4.insert(0, config['save_path'])
Entry5 = tk.Entry(root)
Entry5.insert(0, config['sampling'])


Label3.grid(row=3, column=0)
Entry3.grid(row=3, column=1, sticky="ew")
Label4.grid(row=4, column=0)
Entry4.grid(row=4, column=1, sticky="ew")
Label5.grid(row=5, column=0)
Entry5.grid(row=5, column=1, sticky="ew")

button = tk.Button(root, text='Start', width=25, command=run) 
button.grid(row=7, column=1, sticky="ew")


root.mainloop()

