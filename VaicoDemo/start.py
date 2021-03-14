"""
Script for Movilab Demoday
Run AI-movility package for detect and track vehicles
 - Generates report of number of vehicles and pedestrians
 - Create video output of detections


Installation:
git clone https://jarbest@bitbucket.org/jarbest/movilab-demoday.git
cd movilab-demoday
./install.sh

Running
./run.sh

Progress
watch -n 3 tail -n 10 log

Connect AWS instance
ssh -i "vaico_jca.pem" ubuntu@ec2-3-137-152-119.us-east-2.compute.amazonaws.com

Transfer files
To local:
scp -i vaico_jca.pem -r ubuntu@ec2-3-137-152-119.us-east-2.compute.amazonaws.com:/home/ubuntu/res  /home/juanc/

To remote:
scp -i vaico_jca.pem myfile.txt ubuntu@ec2-3-137-152-119.us-east-2.compute.amazonaws.com:/home/ubuntu/


Mount SSD
# Check disks
lsblk

# Check format system 
sudo file -s /dev/nvme1n1

# Make forma system
sudo file -s /dev/nvme1n1

# Mount
sudo mkdir /misdoc
sudo mount /dev/nvme1n1 /misdoc

# Verify
df -H

# Instance
Name           Core     RAM     Price
c5a.12xlarge	48		96 GiB	1.848 per Hour
c5a.16xlarge	64		128 GiB	$2.464 per Hour

Download video from Drive
** Go to the link in : Share for everyone 
Copy link from "Download Anyway" button
pip install gdown
gdown "link"
** Use ""

If tracker error on opencv
re install this versions
pip install opencv-python== 4.4.0.46
pip install opencv-contrib-python== 4.4.0.46



------ Example -------
    1  git clone https://jarbest@bitbucket.org/jarbest/movilab-demoday.git
    2  cd movilab-demoday/
    3  ./install.sh 
    4  ./run.sh 
    5  watch -n 3 tail -n 20 ../results/log 
    6  htop
    7  rm ../video.mp4 
    8  rm ../results/ -rvf
    9  source movilab-demoday/venv/bin/activate
   10  gdown "https://drive.google.com/u/0/uc?export=download&confirm=e5wr&id=1QepAEEHbgPf-n8AiuWbzrOxrfBfk_iV7"
   11  ls
   12  gdown "https://drive.google.com/u/0/uc?export=download&confirm=HXy9&id=11r73MMjQXAfdnFp4pBcKyHkjIFZ5Q_kr"
   13  ls
   14  gdown "https://drive.google.com/u/0/uc?export=download&confirm=W0wM&id=1yX8gn9rN3gdjfWosHcGy9h7mSgyuQ1qW"
   15  ls
   16  mv '28 (2020-12-07 06'\''00'\''00 - 2020-12-07 07'\''00'\''00)_1.avi' 1.avi
   17  mv '28 (2020-12-07 06'\''00'\''00 - 2020-12-07 07'\''00'\''00)_2.avi' 2.avi
   18  mv '28 (2020-12-07 06'\''00'\''00 - 2020-12-07 07'\''00'\''00)_3.avi' 3.avi
   19  ls
   21  deactivate 
   22  cd movilab-demoday/
   23  nano config.py 
   24  ./run.sh 
   25  watch -n 3 tail -n 10 ../results/1/log 



JCA
Vaico
"""
import sys
# sys.stdout = open('log', 'w')

import logging
from os import path, makedirs

from MLinference.architectures import Yolo4

from AImovility.analyzer_linear import analyze_linear

import VaicoDemo.config as cnf

# Create save path if doesnt exists
makedirs(cnf.save_path, exist_ok=True)

# Set logger
# log_path = path.join(cnf.save_path, 'log')
logging.basicConfig(level=logging.DEBUG)

# Assemble configuration
config = {
    "video":cnf.video,
    "detector_sampling": cnf.detector_sampling,
    "frame_scale": cnf.frame_scale,
    "tracker": cnf.tracker,
    "sampling": cnf.sampling,
    "save_report_time": cnf.save_report_time,
    "save_path": cnf.save_path,
    "save_video": cnf.save_video,
    "min_score": cnf.min_score,
    "debug": True,
    "roi": cnf.roi,
    "start_time": cnf.start_time,
    "anomaly_thresh": cnf.anomaly_thresh,
    "anomaly_learning": cnf.anomaly_learning,
    "anomaly_exclude": cnf.anomaly_exclude,
    "force_learning": cnf.force_learning,
    'anomaly_detection': cnf.anomaly_detection,
    'objects_interest' : cnf.objects_interest,
    'scene_change_thresh' : cnf.scene_change_thresh,
    'show_all' : cnf.show_all,
    'live_record' : cnf.live_record,
    'min_iou' : cnf.min_iou,
    'max_tracked' : cnf.max_tracked,


}

# Load model
labels =Yolo4.read_class_names(cnf.labels_path)

kwargs = {
    'labels': labels,
    'input_size': 416,
    'backend': 'tf'
}

model = Yolo4.load(cnf.model_path, **kwargs)

# Make analysis
analyze_linear(config, model)