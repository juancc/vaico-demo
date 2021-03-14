"""
Instance configuration file example

PARAMETERS
video: File or URL to analyze
detector_sampling: frames the detector is trigger
frame_scale: Scale video frames
sampling: frames the tracker is trigger
save_report_time: Time in seconds for save the report
save_path: Local path to save video. If dont exists will be created. All content will be overwritted
save_video: If Create video with predictions
min_score: redictions min score to be accepted
model_path: Location of prediction model file
labels_path: Text file with the labels of the models
tracker: Tracker algorithm
roi: Area of analyzis, for full video: None
anomaly_thresh: percentual difference between time gap and learned mean and std 
    of anomaly detector to be considered anomaly
anomaly_learning: frames to learn mean and std
anomaly_frame_gap: time gaps to evaluate anomalies
start_time: time of the video to start analysis. In seconds


Trackers
kcf   -> Balanced
mosse -> Speed
csrt  -> Precision

Scales
1920 × 1080 -> 0.3 (576x324)
1280 × 720 -> 0.5(640x360)

JCA
Vaico
"""

# video = "https://youtu.be/eJ7ZkQ5TC08" # street
video = "https://youtu.be/CkVJyAKwByw" # funny
# video = 2
save_path = '/home/juanc/results/'
roi = None
start_time = 0

detector_sampling = 50
frame_scale = 0.6 
sampling = 1
save_report_time =  15*60 

save_video =  True
min_score = 0.15
model_path = '/misdoc/vaico/movilab-demoday/models/yolo4_coco.tflite'
labels_path = '/misdoc/vaico/movilab-demoday/models/coco.nombres'
tracker = "kcf"

anomaly_thresh = 0.35
anomaly_learning = 450
anomaly_exclude = ["persona"]
force_learning = False
anomaly_detection = False
objects_interest = ['coche', 'camion', 'persona', 'moto']
scene_change_thresh = 0.4
show_all = True
live_record = True
min_iou = 0.1
max_tracked = 5