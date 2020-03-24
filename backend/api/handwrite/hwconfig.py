#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
config
@author: chineseocr
"""
import os
from django.conf import settings

ocrType = 'chinese'
ocrPath  = os.path.join(os.getcwd(),"backend","api","handwrite", "models", "ocr", ocrType, "ocr.weights")
textPath = os.path.join(os.getcwd(),"backend","api","handwrite", "models", "text", "text.weights")
darkRoot = os.path.join(os.getcwd(),"backend","api","handwrite", "darknet", "libdarknet.so") ##darknet
TEXT_LINE_SCORE=0.7##text line prob
scale = 900##可动态修改 no care text.cfg height,width
maxScale = 1800
# GPU=True ## gpu for darknet  or cpu for opencv.dnn
GPU = settings.IS_GPU
anchors = '16,11, 16,16, 16,23, 16,33, 16,48, 16,68, 16,97, 16,139, 16,198, 16,283'
