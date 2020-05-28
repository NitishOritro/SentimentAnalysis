# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd

excel_file = "Restaurant.xlsx"
dataset = pd.read_excel(excel_file, encoding="utf-8", usecols="E")

Y = pd.DataFrame(dataset.iloc[:, :].values)