#### mmaction2 library
[https://github.com/open-mmlab/mmaction2]

I like mmlab it's a nice library.
Multiple models to choose from based on requirements.
Models used from documentation https://mmaction2.readthedocs.io/en/latest/recognition_models.html

Demo documentation was used as reference:
https://github.com/open-mmlab/mmaction2/tree/master/demo#video-demo

Ideally with more time, it would be better to test out all the models and compare the inference speed + GPU usage of the model (Since real-time is a requirement). Anyways,


#### Findings
Quantitative:
For accuracy, PoseC3D has the highest.
For total inference speed, SlowOnly+Fast R-CNN is the fastest.

Qualitative:
PoseC3D did not perform well on our custom test video.
SlowOnly+Fast R-CNN also did not perform well.
TimeSformer had decent results. 

TimeSformer should be used here.

#### Action Recognition (TimeSformer divST):
(Works)
[https://github.com/open-mmlab/mmaction2/blob/master/configs/recognition/timesformer/README.md]

Custom test video results: https://drive.google.com/file/d/1C1L4SHuc7ESAvWKrfVNXgNSCaXTROZHG/view?usp=sharing

Accuracy based on paper: top 1 > 77.92
Inference speed on 3070: 0.16-0.18s per frame (Action detector only)
GPU: Around 2400mb

Scripts to run:
python demo/long_video_demo.py configs/recognition/timesformer/timesformer_divST_8x32x1_15e_kinetics400_rgb.py ./models/timesformer_divST_8x32x1_15e_kinetics400_rgb-3f8e5d03.pth ../A1.mp4 tools/data/kinetics/label_map_k400.txt demo/A1_Timesformer_divST.mp4 --label-color 255 255 0


#### Spatio-Temporal Action Detection (SlowOnly+Fast R-CNN):
(Works)
[https://github.com/open-mmlab/mmaction2/blob/master/configs/detection/ava/README.md]
Using human detector + action detector

Custom test video results: https://drive.google.com/file/d/1WCh7vXIQMByFZgol1IoAalrP4IkYAgY3/view?usp=sharing

Accuracy based on paper: top 1 > 80.4 (+3.9)
Human detector: 85s / 4631 = 0.018s per frame (Estimated)
Inference speed on 3070: 0.07-0.08s per frame (Action detector only)
Total = 0.018 + 0.08 = 0.098s per frame (Estimated)
GPU: Around 2500mb

Scripts to run:
If downloading files online:
python demo/demo_spatiotemporal_det.py --video ../A1.mp4 --config configs/detection/ava/slowonly_omnisource_pretrained_r101_8x8x1_20e_ava_rgb.py --checkpoint https://download.openmmlab.com/mmaction/detection/ava/slowonly_omnisource_pretrained_r101_8x8x1_20e_ava_rgb/slowonly_omnisource_pretrained_r101_8x8x1_20e_ava_rgb_20201217-16378594.pth --det-config demo/faster_rcnn_r50_fpn_2x_coco.py --det-checkpoint http://download.openmmlab.com/mmdetection/v2.0/faster_rcnn/faster_rcnn_r50_fpn_2x_coco/faster_rcnn_r50_fpn_2x_coco_bbox_mAP-0.384_20200504_210434-a5d8aa15.pth --det-score-thr 0.9 --action-score-thr 0.5 --label-map tools/data/ava/label_map.txt

If already downloaded files:
python demo/demo_spatiotemporal_det.py --video ../A1.mp4 --config configs/detection/ava/slowonly_omnisource_pretrained_r101_8x8x1_20e_ava_rgb.py --checkpoint ./models/slowonly_omnisource_pretrained_r101_8x8x1_20e_ava_rgb_20201217-16378594.pth --det-config demo/faster_rcnn_r50_fpn_2x_coco.py --det-checkpoint ./models/faster_rcnn_r50_fpn_2x_coco_bbox_mAP-0.384_20200504_210434-a5d8aa15.pth --det-score-thr 0.9 --action-score-thr 0.5 --label-map tools/data/ava/label_map.txt 


#### Skeleton-based Action Recognition PoseC3D:
(Works)
[https://github.com/open-mmlab/mmaction2/blob/master/configs/skeleton/posec3d/README.md]
Using human detector + pose estimator + skeleton recognizer

Custom test video results: https://drive.google.com/file/d/1lFmxBTPaACI0DXwkS3QWsDTBFZjBiGiK/view?usp=sharing

Accuracy based on paper: top 1 > 83.27
Human detector time: 542s / 4631 = 0.117s per frame (Estimated)
Human pose time: 281s / 4631 = 0.060 per frame (Estimated)
Inference speed on 3070: 17.28 / 4631 = 0.0037 (Action detector only)
Total = 0.117 + 0.060 + 0.0037 = 0.1807 (Estimated)
GPU: Around 2400mb

Scripts to run:
python demo/demo_video_structuralize.py --skeleton-stdet-checkpoint ./models/posec3d_ava.pth --det-config demo/faster_rcnn_r50_fpn_2x_coco.py --det-checkpoint ./models/faster_rcnn_r50_fpn_2x_coco_bbox_mAP-0.384_20200504_210434-a5d8aa15.pth --pose-config demo/hrnet_w32_coco_256x192.py --pose-checkpoint ./models/hrnet_w32_coco_256x192-c78dce93_20200708.pth --skeleton-config configs/skeleton/posec3d/slowonly_r50_u48_240e_ntu120_xsub_keypoint.py --skeleton-checkpoint ./models/posec3d_k400.pth --use-skeleton-stdet --use-skeleton-recog --label-map-stdet tools/data/ava/label_map.txt --label-map tools/data/kinetics/label_map_k400.txt --video ../A1.mp4 --out-filename ./demo/A1_PoseC3D.mp4

####
Video clip taken from:
https://www.youtube.com/watch?v=FICCSDVvlz4
4631 frames