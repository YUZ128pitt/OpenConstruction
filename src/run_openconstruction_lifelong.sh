#!/bin/sh

CONFIG_FILE_t1='./configs/OpenConstructionConfig/faster_openconstruction_t1.py'
CONFIG_FILE_t2='./configs/OpenConstructionConfig/faster_openconstruction_t2.py'
CONFIG_FILE_t3='./configs/OpenConstructionConfig/faster_openconstruction_t3.py'

CHECKPOINT_FILE='./work_dirs/faster_openconstruction_t3/epoch_4.pth'

GPU_NUM=2
RESULT_FILE='openconstruction_results.pkl'
EVAL_METRICS=[bbox]


#  for training
./tools/dist_train_26.sh ${CONFIG_FILE_t1} ${GPU_NUM};
./tools/dist_train_04.sh ${CONFIG_FILE_t2} ${GPU_NUM};
./tools/dist_train_04.sh ${CONFIG_FILE_t4} ${GPU_NUM};


# for testing of locally trained model
./tools/dist_test.sh ${CONFIG_FILE} ${CHECKPOINT_FILE} ${GPU_NUM} \
-out results.pkl --eval bbox --eval-options "classwise=True"

# for testing the pre-trained model
CHECKPOINT_FILE=''#the local path of downloaded model
./tools/dist_test.sh ${CONFIG_FILE} ${CHECKPOINT_FILE} ${GPU_NUM} \
-out results.pkl --eval bbox --eval-options "classwise=True"






