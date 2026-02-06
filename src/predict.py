#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  6 11:53:24 2026

@author: sayantansengupta
"""
#src/predict.py
import joblib
import numpy as np

def predict(input_data):
    model=joblib.load('iris_model.pkl')
    prediction=model.predict(np.array(input_data).reshape(1,-1))
    return int(prediction[0])