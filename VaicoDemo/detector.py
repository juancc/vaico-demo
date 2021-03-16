"""
Script for Movilab Demoday
Run AI-movility package for detect and track vehicles
 - Generates report of number of vehicles and pedestrians
 - Create video output of detections

JCA
Vaico
"""
import sys
import logging
from os import path, makedirs
import json



from MLinference.architectures import Yolo4
from AImovility.analyzer_linear import analyze_linear

# Assemble configuration
with open('VaicoDemo/config.json', 'r') as f:
    config = json.load(f)

# Create save path if doesnt exists
makedirs(config['save_path'], exist_ok=True)

# Set logger
logging.basicConfig(level=logging.DEBUG)


# Load model
labels =Yolo4.read_class_names(config['labels_path'])

kwargs = {
    'labels': labels,
    'input_size': 416,
    'backend': 'tf'
}

model = Yolo4.load(config['model_path'], **kwargs)

# Make analysis
analyze_linear(config, model)