# -*- coding: utf-8 -*-
"""sort_object_y

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1cLJYL6t-sQyq32R0A-pfJAYPpGhvCUe0
"""

obj_detected = {"bottle" :[110,30],"glass" :[60,35],"book" :[310,23],"phone" :[90,33],"pen" :[155,100],"mouse" :[200,45],"remote" :[298,165],"fan" :[300,36]}
obj_detected

obj_detected.items()

sort_by_key = sorted(obj_detected.items(), key=lambda x: x[0],reverse=False)
sort_by_key