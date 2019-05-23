# -*- coding: utf-8 -*-
"""
Created on Thu May 23 18:24:36 2019

@author: Chess
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
]