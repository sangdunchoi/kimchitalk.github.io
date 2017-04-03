---
layout: post
title: "Frequency distribution graph"
date: 2017-04-03
tags: [tips]
comments: true
---

&nbsp;


I have extract these EC50 values from a few papers. The values are in the units of micromolar. You can download the file [here](/data/active_compounds.txt). I have to convert EC50 to pIC50.


First I have to convert these values to pIC50. The below definition is from [wikipedia](https://en.wikipedia.org/wiki/IC50)


<img src="/images/pIC50.png?raw=true" style="width: 1500px;"/>

As per the information "pIC50 is usually given in terms of molar concentration (mol/L, or M). Therefore, to obtain a pIC50, an IC50 should be specified in units of M. When IC50 is expressed in μM or nM, it will need to be converted to M before conversion to pIC50".

if it is micromolar

pIC50 [log M] = -log10(IC50 [M]) = -log10(IC50 [μM]) + 6

if it is nanomolar

pIC50 [log M] = -log10(IC50 [M]) = -log10(IC50 [μM]) + 9


I wrote this small [python script](data/pIC50.py) to convert EC50 to pIC50 in a new file "pIC50.txt". To create a frequeny distribution graph, I have used this ["bin.py" script](/data/bin.py).


<img src="/images/frequency-distribution.png?raw=true" style="width: 800px;"/>

https://en.wikipedia.org/wiki/IC50
https://en.wikipedia.org/wiki/Molar_concentration
http://www.mathbootcamps.com/making-frequency-distributions-and-histograms-by-hand/
