# OpenConstruction

[Ruoxin Xiong](https://www.linkedin.com/in/ruoxin-xiong-56773815b/), [Yuansheng Zhu](https://sites.google.com/view/yuz128/home), [Yanyu Wang](https://www.linkedin.com/in/yanyu-wang-984bb61b7/), [Pengkun Liu](https://www.linkedin.com/in/pengkunliu/), and [Pingbo Tang](https://sites.google.com/site/tangpingbo/)

This is the offecial implementtaion of paper "Facilitating Construction Scene Understanding Knowledge Sharing and Reuse via Lifelong Site Object Detection", which will be seen in first [CVCIE workshop](https://vap.aau.dk/cvcie/) at ECCV 2022. 

## Introduction

**Abstruct**：Automatically recognizing diverse construction resources (e.g., workers and equipment) from construction scenes supports efficient and intelligent workplace management. Previous studies have focused on identifying static and limited object categories, which are inefficient and unscalable for continuously learning from various construction scenarios. This work proposed a novel lifelong construction resource detection framework for continuously learning from dynamic changing construction contexts without catastrophically forgetting previous knowledge. In particular, we contribute: (1) a hierarchical OpenConstruction Taxonomy, unifying heterogeneous label space from various construction scenarios; (2) an OpenConstruction Dataset with 31 unique construction object categories, integrating three large datasets for validating lifelong object detection algorithms; and (3) a new informativeness-based lifelong construction resource detector by leveraging limited and informative instances in previous tasks. We train and evaluate the proposed method on the OpenConstruction Dataset in sequential data streams and show mAP improvement on the overall task.

<img src="https://user-images.githubusercontent.com/43504654/183323676-1d70bd4c-3282-489c-9239-5d48d8f6df61.png" width=50% height=50%>

## Demo
![vis.pdf](https://github.com/YUZ128pitt/OpenConstruction/files/9278163/vis.pdf)

## Data preparation and prprecessing

### ACID
Description: 10 categories of construction machines, 10,000 labeled images
15,767 construction machine objects
Category: Mobile Crane; Tower Crane; Concrete Mixer Truck; Backhoe Loader; Wheel Loader; Compactor; Dozer; Dump truck; Excavator; Grader. [Source](https://www.acidb.ca/)

### SODA
Description: 19,846 images in the dataset and 15 categories of objects
Category: person (worker), helmet, vest, board, wood, rebar, brick, scaffold, handcart, cutter, ebox, hopper, hook, fence, slogan. [Source](https://linjiarui.net/en/portfolio/2022-02-22-SODA-site-object-detection-dataset-for-deep-learning-in-construction) 

### MOCS
Description: 41,668 images in the dataset and 13 categories of objects
Category: Worker, Tower crane, Hanging hook, Vehicle crane, Roller, Bulldozer, Excavator, Truck, Loader, Pump truck, Concrete transport Mixer, Pile driver, Other vehicle.[Source](http://www.anlab340.com/Archives/IndexArctype/index/t_id/17.html)



## Running enviorment
This repro is largely based on the [MMdetection2](https://github.com/open-mmlab/mmdetection), please follow their installation instruction.

## Training and testing

## Acknowledgements
We sincerely thank [Anlab](http://www.anlab340.com), [AIRCon-Lab](https://profsckang.wixsite.com/uofa-rlab), and [Mechanics Computing and Simulation Laboratory](https://linjiarui.net/en/) for providing the datasets.  
