---
layout: post
title: "Search a pattern in a folder"
date: 2017-04-10
tags: [tips]
comments: true
---


In Theano there are few python file imported as 

    import numpy as np

and other files are

    import numpy 

I want to see file names that contain

    import numpy

The below few line script helped me to spot the files

    import os
    import re
    list = []


    for root, dirs, files in os.walk("/home/tlr8/contribute/Theano"):  #location of the folder in my case
        for file in files:
            if file.endswith(".py"):
                list.append(os.path.join(root, file))
                #print(list)

    for file in list:
        read_file = open(file, "r")
        for line in read_file:
            if re.match("^import numpy$", line):  #exact pattern is import numpy
            print(file)
            print(line)
