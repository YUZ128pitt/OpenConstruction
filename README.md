# OpenConstruction

[Ruoxin Xiong](https://www.linkedin.com/in/ruoxin-xiong-56773815b/), [Yuansheng Zhu](https://sites.google.com/view/yuz128/home), [Yanyu Wang](https://www.linkedin.com/in/yanyu-wang-984bb61b7/), [Pengkun Liu](https://www.linkedin.com/in/pengkunliu/), and [Pingbo Tang](https://sites.google.com/site/tangpingbo/)

This is the offecial implementtaion of paper "Facilitating Construction Scene Understanding Knowledge Sharing and Reuse via Lifelong Site Object Detection", which will be seen in first cvcie workshop at ECCV 2022. 

![overview2](https://user-images.githubusercontent.com/43504654/183323676-1d70bd4c-3282-489c-9239-5d48d8f6df61.png)
**Abstruct**：Automatically recognizing diverse construction resources (\eg workers and equipment) from construction scenes supports efficient and intelligent workplace management. Previous studies have focused on identifying static and limited object categories, which are inefficient and unscalable for continuously learning from various construction scenarios. This work proposed a novel lifelong construction resource detection framework for continuously learning from dynamic changing construction contexts without catastrophically forgetting previous knowledge. In particular, we contribute: (1) a hierarchical OpenConstruction Taxonomy, unifying heterogeneous label space from various construction scenarios; (2) an OpenConstruction Dataset with 31 unique construction object categories, integrating three large datasets for validating lifelong object detection algorithms; and (3) a new informativeness-based lifelong construction resource detector by leveraging limited and informative instances in previous tasks. We train and evaluate the proposed method on the OpenConstruction Dataset in sequential data streams and show mAP improvement on the overall task.

## Demo
![vis.pdf](https://github.com/YUZ128pitt/OpenConstruction/files/9278163/vis.pdf)

# Data preparation and proprecessing

# Running enviorment
This repro is largely based on the [MMdetection2](https://github.com/open-mmlab/mmdetection), please follow their installation instruction.

# Training and testing

# Acknowledgements
