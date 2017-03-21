---
layout: post
title: "Installing rdkit using anaconda with jupyter notebook"
date: 2017-03-21
tags: [tips]
comments: true
---

&nbsp;

__Step 1. Download (Python 3)__

Go to [anaconda website](https://www.continuum.io/downloads) and download.

__Step 2. Install__

bash Anaconda3-4.3.1-Linux-x86_64.sh


__Step 3.__

conda create -c rdkit -n my-rdkit-env rdkit

__Step 4.__

source activate my-rdkit-env


__Step 5.__

conda install ipykernel

__Step 6.__

python -m ipykernel install my-rdkit-env --display-name "Python3 (rdkit)"


__Step 7.__

jupyter notebook (if you dont have install conda install jupyter)

__Step 8.__

from rdkit import Chem 

<img src="/images/rdkit.png?raw=true" alt="Drawing" style="width: 600px;"/>


__Helpfull resources:__

1. [http://fch.upol.cz/en/teaching/advanced-in-silico-drug-design-add/](http://fch.upol.cz/en/teaching/advanced-in-silico-drug-design-add/)

2. [http://www.rdkit.org/docs/Install.html](http://www.rdkit.org/docs/Install.html)

3. [http://rdkit.blogspot.kr/](http://rdkit.blogspot.kr/)

4. [https://github.com/rdkit/rdkit-tutorials/blob/master/notebooks/001_ReadingMolecules1.ipynb](https://github.com/rdkit/rdkit-tutorials/blob/master/notebooks/001_ReadingMolecules1.ipynb)









