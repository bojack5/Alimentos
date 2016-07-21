#!/usr/bin/env python
import openpyxl
from sql.models import *

class Excel(object):
    """docstring for Excel"""
    def __init__(self, archivo):
        self.archivo = archivo
    
    def reporte_ventas(self , parametro):
        wb = openpyxl.Workbook()


        
        
