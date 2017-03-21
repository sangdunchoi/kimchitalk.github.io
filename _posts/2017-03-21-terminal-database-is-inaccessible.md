---
layout: post
title: "Terminal database is inaccessible - ncruses issue"
date: 2017-03-21
tags: [tips]
comments: true
---


I got this error message today
&nbsp;

<img src="/images/database-inaccessible.png?raw=true" style="width: 800px;"/>

&nbsp;

I saw the solution in the [issue in github](https://github.com/ContinuumIO/anaconda-issues/issues/994).

**Update ncurses solves the problem.**

Step 1. "conda remove -c r ncurses"

Step 2. "conda install -c r ncurses"

&nbsp;

<img src="/images/database-inaccessible-1.png?raw=true" style="width: 800px;"/>







