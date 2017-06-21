# Python Club at Nesys  
This repository contains the meeting notes and piece of code the Nesys group will discuss during the Python Club every Friday.

## 001 (2017-05-12) : Installation, teaching material and projects
The notes of the meeting can be find in this [jupyter notebook](https://github.com/ChrCoello/PythonClub/blob/master/2017_05_12__Introduction_Python.ipynb) and as a [web page](https://github.com/ChrCoello/PythonClub/blob/master/2017_05_12__Introduction_Python.md)

## 002 (2017-05-19) : Working with images
The notes of the meeting can be find in this [jupyter notebook](https://github.com/ChrCoello/PythonClub/blob/master/2017_05_19__Work_with_images.ipynb)

## 003 (2017-06-02) : Web scraping using Beautiful Soup
Krister presented how to web scrap the [Finn](www.finn.no) website. His objective was to obtain a graph of the size of a house in relation to its price in a given location. The code is available [here](https://github.com/ChrCoello/PythonClub/tree/master/2017_06_02/).

## 004 (2017-06-16) : Interacting with Allen Brain using ecallen package
The meeting introduced a packqge to download images AND spatial coordinate from the Allen Brain institute using the [ecallen](https://efferencecopy.net/ecallen-a-python-package-for-the-allen-institutes-api/). This is very useful in order to get the orginal section AND its position within the Common Coordinate Framework.

## 005 (2017-06-23) : Downsampling an image
Each member of the club was asked (if time) to write a Python function/script that achieves the downsampling of an image or a collection of images.
Inputs :
 - input 1: either an absolute filename path (i.e C:\data\test\section_001.tif) or an absolute path (i.e C:\data\test\)
 - input 2: a real number between 0 and 1 that will be used as downsampling factor (ds_factor) : newX = X \* ds_factor and newY = Y \* ds_factor
Output :
 - output 1: either an absolute filename path or an absolute path

These instructions are deliberatly vague (where to save, format, name, interpolation, etc... not specified) to give some flexibility to the user and see the choices you came up with.
The script and/or function will be tested using this data located [here](http://folk.uio.no/sebastcc/export_res/test_downsize/)
