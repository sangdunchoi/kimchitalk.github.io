---
layout: post
title: "Updating your fork with the original repo"
date: 2017-03-25
tags: [tips]
comments: true
---

&nbsp;

### Clone your repositiory
git clone git@github.com:amrithasuresh/Theano.git

### Add remote
cd Theano/
git remote add upstream git://github.com/Theano/Theano.git
git fetch upstream

### Updating your fork 
git pull upstream master


[Refer:](https://gist.github.com/CristinaSolana/1885435)

