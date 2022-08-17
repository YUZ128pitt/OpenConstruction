_base_ = '../faster_rcnn/faster_rcnn_x101_64x4d_fpn_1x_coco.py'


# 1. dataset settings
dataset_type = 'CocoDataset'
classes = (['Mobile Crane', 
            'Tower Crane', 
            'Backhoe Loader', 
            'Wheeled Loader', 
            'landfill Compactor', 
            'Dumper', 
            'Excavator', 
            'Tractor Dozer', 
            'Grader', 
            'Concrete Mixer', 
            'Worker', 
            'Helmet', 
            'Vest', 
            'Board', 
            'Wood', 
            'Rebar', 
            'Brick', 
            'Scaffold', 
            'Handcart', 
            'Cutter', 
            'Ebox', 
            'Hopper', 
            'Hook', 
            'Fence', 
            'Slogan', 
            'Roller', 
            'Bulldozer', 
            'Truck', 
            'Loader', 
            'Pump truck', 
            'Pile driver'])


ACID_Classes =(['Mobile Crane', 
                'Tower Crane', 
                'Backhoe Loader', 
                'Wheeled Loader', 
                'landfill Compactor', 
                'Dumper', 
                'Excavator', 
                'Tractor Dozer', 
                'Grader', 
                'Concrete Mixer'])
train_pipeline = [
    dict(type='LoadImageFromFile'),
    dict(type='LoadAnnotations', with_bbox=True),
    dict(type='Resize', img_scale=(1333, 800), keep_ratio=True),
    dict(type='RandomFlip', flip_ratio=0.5),
    dict(
        type='Normalize',
        mean=[123.675, 116.28, 103.53],
        std=[58.395, 57.12, 57.375],
        to_rgb=True),
    dict(type='Pad', size_divisor=32),
    dict(type='DefaultFormatBundle'),
    dict(type='Collect', keys=['img', 'gt_bboxes', 'gt_labels'])
]

test_pipeline = [
    dict(type='LoadImageFromFile'),
    dict(
        type='MultiScaleFlipAug',
        img_scale=(1333, 800),
        flip=False,
        transforms=[
            dict(type='Resize', keep_ratio=True),
            dict(type='RandomFlip'),
            dict(
                type='Normalize',
                mean=[123.675, 116.28, 103.53],
                std=[58.395, 57.12, 57.375],
                to_rgb=True),
            dict(type='Pad', size_divisor=32),
            dict(type='ImageToTensor', keys=['img']),
            dict(type='Collect', keys=['img'])
        ])
]

# '/shared/users/yz7008/mmdetection/src/OpenConstruction/soda_train.json'
data = dict(
    samples_per_gpu=2,
    workers_per_gpu=2,
    train= dict(
        type='ClassBalancedDataset',
        oversample_thr=1e-3,
        dataset=dict(
        type=dataset_type,
        # explicitly add your class names to the field `classes`
        classes=classes,
        ann_file= '/shared/users/yz7008/cvcie_bu/mmdetection_bu/src/Reply_example/acid_infor_soda.json',
        pipeline=train_pipeline,
        img_prefix= '/shared/users/yz7008/mmdetection/CVCIE22/')),

    val=dict(
        type=dataset_type,
        # explicitly add your class names to the field `classes`
        classes=classes,
        ann_file=['/shared/users/yz7008/mmdetection/src/OpenConstruction/acid_test.json',\
            '/shared/users/yz7008/mmdetection/src/OpenConstruction/soda_test.json'],
        pipeline=test_pipeline,
        img_prefix='/shared/users/yz7008/mmdetection/CVCIE22/'),
    test=dict(
        type=dataset_type,
        # explicitly add your class names to the field `classes`
        classes=classes,
        ann_file='/shared/users/yz7008/mmdetection/src/OpenConstruction/soda_train.json',
        img_prefix='/shared/users/yz7008/mmdetection/CVCIE22/'))

model = dict(
    type='CascadeRCNN',
    backbone=dict(
        type='ResNeXt',
        depth=101,
        groups=64,
        base_width=4,
        num_stages=4,
        out_indices=(0, 1, 2, 3),
        frozen_stages=3, # fix the backbone
        norm_cfg=dict(type='BN', requires_grad=True),
        style='pytorch',
        init_cfg=dict(
            type='Pretrained', checkpoint='open-mmlab://resnext101_64x4d')),
    roi_head=dict(
        type='StandardRoIHead',
        bbox_roi_extractor=dict(
            type='SingleRoIExtractor',
            roi_layer=dict(type='RoIAlign', output_size=7, sampling_ratio=0),
            out_channels=256,
            featmap_strides=[4, 8, 16, 32]),
        bbox_head=dict(
            type='Shared2FCBBoxHead',
            in_channels=256,
            fc_out_channels=1024,
            roi_feat_size=7,
            num_classes=31,
            bbox_coder=dict(
                type='DeltaXYWHBBoxCoder',
                target_means=[0., 0., 0., 0.],
                target_stds=[0.1, 0.1, 0.2, 0.2]),
            reg_class_agnostic=False,
            loss_cls=dict(
                type='CrossEntropyLoss', use_sigmoid=False, loss_weight=1.0),
            loss_bbox=dict(type='L1Loss', loss_weight=1.0)))
            )
            
runner = dict(max_epochs=6)

#  We can use the pre-trained Fatser-RCNN model that learned with t1(ACID)
load_from ='/shared/users/yz7008/mmdetection/work_dirs/faster_openconstruction_t1/epoch_12.pth'
