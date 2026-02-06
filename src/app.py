#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  6 11:53:42 2026

@author: sayantansengupta
"""

#src/app.py
from fastapi import FastAPI
from pydantic import BaseModel
from src.predict import predict

app = FastAPI()

class InputData(BaseModel):
    features: list
@app.get('/')
def home():
    return {'message': 'ML Model API is runing'}

@app.post('/predict')
def get_prediction(data: InputData):
    result = predict(data.features)
    return {'prediction':result}