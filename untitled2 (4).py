# -*- coding: utf-8 -*-
"""Untitled2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/162i6dKr-Q9MrOlp_XLNmdoCsZUIBJyC3
"""

class vehicle:
  def __init__ (self,fare):
    self.f=fare
  def __add__ (self,other):
    return self.f+other.f
bus=vehicle(100)
car=vehicle(20)
print(car+bus)