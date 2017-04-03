---
layout: post
title: "How to draw frequency distribution graph in python?"
date: 2017-04-03
tags: [tips]
comments: true
---


I have extracted the EC50 values from few papers. The values are in the units of micromolar. You can download the file [here](/data/active_compounds.txt). I have to convert EC50 to pIC50.


<img src="/images/active-compounds.png?raw=true" style="width: 800px;"/>

&nbsp;

First I have to convert these values to pIC50. The below definition is from [wikipedia](https://en.wikipedia.org/wiki/IC50)


As per the information "pIC50 is usually given in terms of molar concentration (mol/L, or M). Therefore, to obtain a pIC50, an IC50 should be specified in units of M. When IC50 is expressed in μM or nM, it will need to be converted to M before conversion to pIC50".

if it is micromolar

    pIC50 [log M] = -log10(IC50 [M]) = -log10(IC50 [μM]) + 6

if it is nanomolar

    pIC50 [log M] = -log10(IC50 [M]) = -log10(IC50 [μM]) + 9


I wrote this small to convert EC50 to pIC50 in a new file "pIC50.txt". 

    import pandas as pd
    import numpy as np

    active_compounds = pd.read_csv('active_compounds.txt')

    concentration = active_compounds.EC50
    data = []

    for line in concentration:
        logIC50_n = np.log10(line)
        b = 6 - logIC50_n
        b = '{0:.4f}'.format(b)
        data.append(b)


    newDF = pd.DataFrame({'pIC50': data})
    active_compounds = newDF

    active_compounds.to_csv('pIC50.txt',index=False)

    print(active_compounds)


To create a frequeny distribution graph, I have used this script to draw frequency distribution graph.


    import numpy as np
    import matplotlib.pyplot as plt
    from numpy import *

    data = np.loadtxt('pIC50.txt', dtype=float, usecols=(0,), skiprows=1)
    print(data)

    plt.hist(data, color='black',edgecolor='white')
    plt.show()


<img src="/images/frequency-distribution.png?raw=true" style="width: 800px;"/>

&nbsp;


### Refer

1. [https://en.wikipedia.org/wiki/IC50](https://en.wikipedia.org/wiki/IC50)
2. [https://en.wikipedia.org/wiki/Molar_concentration](https://en.wikipedia.org/wiki/Molar_concentration)
3. [https://mirams.wordpress.com/2016/06/13/should-i-work-with-ic50s-or-pic50s/](https://mirams.wordpress.com/2016/06/13/should-i-work-with-ic50s-or-pic50s/)
4. [http://www.abap.co.in/tool-development-prediction-pic50-values-ic50-values-pic50-value-calculator](http://www.abap.co.in/tool-development-prediction-pic50-values-ic50-values-pic50-value-calculator)

