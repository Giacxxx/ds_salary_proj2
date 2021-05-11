#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 21 11:40:49 2021

@author: gm
"""


import glassdoor_scraper as gs
import pandas as pd
path = "/Users/gm/documents/ds_salary_proj2/chromedriver"

df = gs.get_jobs('data scientist',7, False, path, 10 )





