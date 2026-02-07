#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  6 11:54:00 2026

@author: sayantansengupta
"""

# tests/test_app.py
from src.predict import predict

def test_prediction():
    result = predict([5.1, 3.5, 1.4, 0.2])
    assert result in [0, 1, 2]