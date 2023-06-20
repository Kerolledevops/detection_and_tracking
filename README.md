# yolov8-tracking-module

## Installation

```
git clone https://github.com/HASHIRAMA21/yolov8_tracking.git
cd yolov8_tracking
pip install -r requirements.txt  # install dependencies
```

<details>
<summary>Tutorials</summary>

* [Yolov5 training (link to external repository)](https://github.com/ultralytics/yolov5/wiki/Train-Custom-Data)&nbsp;
* [Deep appearance descriptor training (link to external repository)](https://kaiyangzhou.github.io/deep-person-reid/user_guide.html)&nbsp;
* [ReID model export to ONNX, OpenVINO, TensorRT and TorchScript](https://github.com/mikel-brostrom/Yolov5_StrongSORT_OSNet/wiki/ReID-multi-framework-model-export)&nbsp;
* [Evaluation on custom tracking dataset](https://github.com/mikel-brostrom/Yolov5_StrongSORT_OSNet/wiki/How-to-evaluate-on-custom-tracking-dataset)&nbsp;
* Inference acceleration with Nebullvm
  * [Yolov5](https://colab.research.google.com/drive/1J6dl90-zOjNNtcwhw7Yuuxqg5oWp_YJa?usp=sharing)&nbsp;
  * [ReID](https://colab.research.google.com/drive/1APUZ1ijCiQFBR9xD0gUvFUOC8yOJIvHm?usp=sharing)&nbsp;
  
  </details>
  
<details>
<summary>Experiments</summary>

In inverse chronological order:

* [Evaluation of the params evolved for first half of MOT17 on the complete MOT17](https://github.com/mikel-brostrom/Yolov5_StrongSORT_OSNet/wiki/Evaluation-of-the-params-evolved-for-first-half-of-MOT17-on-the-complete-MOT17)

* [Segmentation model vs object detetion model on MOT metrics](https://github.com/mikel-brostrom/Yolov5_StrongSORT_OSNet/wiki/Segmentation-model-vs-object-detetion-model-on-MOT-metrics)
  
* [Effect of masking objects before feature extraction](https://github.com/mikel-brostrom/Yolov5_StrongSORT_OSNet/wiki/Masked-detection-crops-vs-regular-detection-crops-for-ReID-feature-extraction)
  
* [conf-thres vs HOTA, MOTA and IDF1](https://github.com/mikel-brostrom/Yolov5_StrongSORT_OSNet/wiki/conf-thres-vs-MOT-metrics)

* [Effect of KF updates ahead for tracks with no associations on MOT17](https://github.com/mikel-brostrom/Yolov5_StrongSORT_OSNet/wiki/Effect-of-KF-updates-ahead-for-tracks-with-no-associations,-on-MOT17)

* [Effect of full images vs 1280 input to StrongSORT on MOT17](https://github.com/mikel-brostrom/Yolov5_StrongSORT_OSNet/wiki/Effect-of-passing-full-image-input-vs-1280-re-scaled-to-StrongSORT-on-MOT17)

* [Effect of different OSNet architectures on MOT16](https://github.com/mikel-brostrom/Yolov5_StrongSORT_OSNet/wiki/OSNet-architecture-performances-on-MOT16)

* [Yolov5 StrongSORT vs BoTSORT vs OCSORT](https://github.com/mikel-brostrom/Yolov5_StrongSORT_OSNet/wiki/StrongSORT-vs-BoTSORT-vs-OCSORT)
    * Yolov5 [BoTSORT](https://arxiv.org/abs/2206.14651) branch: https://github.com/mikel-brostrom/Yolov5_StrongSORT_OSNet/tree/botsort

* [Yolov5 StrongSORT OSNet vs other trackers MOT17](https://github.com/mikel-brostrom/Yolov5_StrongSORT_OSNet/wiki/MOT-17-evaluation-(private-detector))&nbsp;

* [StrongSORT MOT16 ablation study](https://github.com/mikel-brostrom/Yolov5_StrongSORT_OSNet/wiki/Yolov5DeepSORTwithOSNet-vs-Yolov5StrongSORTwithOSNet-ablation-study-on-MOT16)&nbsp;

* [Yolov5 StrongSORT OSNet vs other trackers MOT16 (deprecated)](https://github.com/mikel-brostrom/Yolov5_StrongSORT_OSNet/wiki/MOT-16-evaluation)&nbsp;

  </details>
  
<details>
<summary>Custom object detection architecture</summary>

The trackers provided in this repo can be used with other object detectors than Yolov8. Make sure that the input to the trackers is of the following format:

```bash
Nx6 (x, y, x, y, conf, cls)
```

</details>

## Tracking

```bash
$ python track.py --yolo-weights yolov8n.pt      # bboxes only
                                 yolov8n-seg.pt  # bboxes + segmentation masks
                                 yolov8n-pose.pt # bboxes + pose estimation
```

<details>
<summary>Tracking methods</summary>

```bash
$ python track.py --tracking-method deepocsort
                                    strongsort
                                    ocsort
                                    bytetrack
                                    botsort
```
  
</details>

<details>
<summary>Tracking sources</summary>

Tracking can be run on most video formats

```bash
$ python track.py --source 0                               # webcam
                           img.jpg                         # image
                           vid.mp4                         # video
                           path/                           # directory
                           path/*.jpg                      # glob
                           'https://youtu.be/Zgi9g1ksQHc'  # YouTube
                           'rtsp://example.com/media.mp4'  # RTSP, RTMP, HTTP stream
```

</details>

<details>
<summary>Select Yolov8 model</summary>

There is a clear trade-off between model inference speed and overall performance. In order to make it possible to fulfill your inference speed/accuracy needs you can select a Yolov5 family model for automatic download. These model can be further optimized for you needs by the [export.py](https://github.com/ultralytics/yolov5/blob/master/export.py) script

```bash


$ python track.py --source 0 --yolo-weights yolov8n.pt --img 640
                                            yolov8s.tflite
                                            yolov8m.pt
                                            yolov8l.onnx 
                                            yolov8x.pt --img 1280
                                            ...
```
  
</details>

<details>
<summary>Select ReID model</summary>

Some tracking methods combine appearance description and motion in the process of tracking. For those which use appearance, you can choose a ReID model based on your needs from this [ReID model zoo](https://kaiyangzhou.github.io/deep-person-reid/MODEL_ZOO). These model can be further optimized for you needs by the [reid_export.py](https://github.com/mikel-brostrom/Yolov5_StrongSORT_OSNet/blob/master/reid_export.py) script

```bash
$ python track.py --source 0 --reid-weights lmbn_n_cuhk03_d.pt
                                            osnet_x0_25_market1501.pt
                                            mobilenetv2_x1_4_msmt17.engine
                                            resnet50_msmt17.onnx
                                            osnet_x1_0_msmt17.pt
                                            ...
```

</details>
  
<details>
<summary>Filter tracked classes</summary>

By default the tracker tracks all MS COCO classes.

If you want to track a subset of the classes that you model predicts, add their corresponding index after the classes flag,

```bash
python track.py --source 0 --yolo-weights yolov8s.pt --classes 16 17  # COCO yolov8 model. Track cats and dogs, only
```

[Here](https://tech.amikelive.com/node-718/what-object-categories-labels-are-in-coco-dataset/) is a list of all the possible objects that a Yolov8 model trained on MS COCO can detect. Notice that the indexing for the classes in this repo starts at zero

</details>

<details>
<summary>MOT compliant results</summary>
  
Can be saved to your experiment folder `runs/track/<yolo_model>_<deep_sort_model>/` by 

```bash
python track.py --source ... --save-txt
```

</details>

<details>
<summary>Tracker hyperparameter tuning</summary>

We use a fast and elitist multiobjective genetic algorithm for tracker hyperparameter tuning. By default the objectives are: HOTA, MOTA, IDF1. Run it by

```bash
$ python evolve.py --tracking-method strongsort --benchmark MOT17 --n-trials 100  # tune strongsort for MOT17
                   --tracking-method ocsort     --benchmark <your-custom-dataset> --objective HOTA # tune ocsort for maximizing HOTA on your custom tracking dataset
```

The set of hyperparameters leading to the best HOTA result are written to the tracker's config file.
