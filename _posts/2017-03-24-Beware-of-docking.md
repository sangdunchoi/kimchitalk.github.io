---
layout: post
title: "Beware of docking"
date: 2017-03-24
tags: [Interesting articles]
comments: true
---

&nbsp;

This is a very comprehensive and interesting review - [Beware of docking](http://www.sciencedirect.com/science/article/pii/S0165614714002144). I have learned few things from my experience, and I hope some of the comments related to docking may help the beginners

* Experimental data about the protein is essential like site directed mutagenesis, active site, same protein but may be published using different organisms, etc. One has to collect all the related experimental information before doing docking calculations in particular related to protein. Other computational studies related to the protein will also help.

* Use of consensus docking tools may help(in the case of very few compounds).

* Use of more than two structures of the same protein (crystal structure from different groups or different protocol). If one doesn't have protein structural information, homology modeled protein must be of reasonable quality.

* Use of controls (known protein-ligand crystal structure) can be docked to see whether the experimental information (like the active site) helps in predicting the correct docking pose (with less RMSD difference).

* Like the author said molecular dynamics (MD) helps but the timescale is not long enough to capture the correct binding mode. Perhaps two or three different best modes can be chosen to do MD simulations and see whether it ends in a same binding pose. In some cases, it helps. Otherwise one can use Random Acceleration Molecular Dynamics simulations (usage of other methods than classical MD techniques).

* Active ligand conformers exists are to be considered (DOI:10.1186/1758-2946-3-4).

* It is to be important to consider active pH (at least the protonation states for few residues like HIS)

* Usage of protein flexibility in docking (active site residues)

* Try to use two or more different algorithms both in searching algorithms as well as scoring function to see how the results are different.

* Read the tips from the published validation studies of the docking algorithms (DOI:10.1021/ci800293n) or for the particular protein (for e.g.,; case studies of HEME containing protein or PMID: 15177081)
