#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  3 16:25:27 2021

@author: Pessa001
"""

import opensmile
import glob
import os


smile = opensmile.Smile(
    feature_set=opensmile.FeatureSet.ComParE_2016,
    feature_level=opensmile.FeatureLevel.Functionals,
)

list_audio_files = glob.glob(os.path.join(os.getcwd(), 'data', 'audio_wav', '*.wav'))

y = smile.process_file(list_audio_files[0])
