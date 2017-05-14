
# 2017.05.12 -- Introduction: installation, tutorial material and projects


```python
print('Hello Nesys world')
```

    Hello Nesys world
    

## Installation with Anaconda (conda)

Though there are various ways to install Python, the one I would suggest – particularly if you wish to eventually use the data science tools mentioned above – is via the cross-platform Anaconda distribution which is accessible through the [Software Centre](https://kiosk.uio.no/) at UiO.
[Anaconda](https://www.continuum.io/downloads) includes both Python and ``conda``, and additionally bundles a suite of other pre-installed packages geared toward scientific computing.
Any others package not included with Anaconda distribution can also be installed manually on top. For example if your want to install the IPython notebook package:
```
[~]$ conda install ipython-notebook
```
For more information on ``conda``, including information about creating and using conda environments, refer to the Anaconda package documentation linked at the above page.

In term of version, the newest version is 3.6 and I would recommend to start learning Python 3 instead of PYthon 2. But some packages are only availble in Python 2. In some cases, you might have to install both in parallel. 

## Running Python code
Python is an interpreted language (like Matlab or R) rather than compiled language (like Fortran, C or Java). There are four main ways to interpret Python code: 
- **Python interpreter**
- **Anaconda Notebook **
- **IPython inpterpreter**
- **Self-contained scripts**
- **Jupyter notebook**

You'll get more details on these different ways to interact on [Jake VdP Tutorial](https://github.com/jakevdp/WhirlwindTourOfPython/01-How-to-Run-Python-Code.ipynb ).

## Online free material for learning the basic
Here are listed a few known resources that can be used to get familiar with the Python language
- [Solo Learn](https://www.sololearn.com/Course/Python/) -- general introduction to the syntax
- [Tutorialspoint](www.tutorialspoint.com) -- general introduciton to the syntax
- [WhirlwindTourOfPython](https://github.com/jakevdp/WhirlwindTourOfPython) online books in Jupyter Notebooks -- general overview of the syntax. Exist in a free [PDF](http://www.oreilly.com/programming/free/files/a-whirlwind-tour-of-python.pdf).
- [Python for Data Science](https://github.com/jakevdp/PythonDataScienceHandbook) online books in Jupyter Notebooks -- focusing more on data science packages numpy, scipy, panda, etc...
- [Stack Overflow](http://stackoverflow.com/) : if you don't find the answer you wnant for a specific question using Google, this is the website where you can ask any question and get the answer in less than 10 minutes.

## Projects
Here are some of the projects that the team has put forward. We will create common code repositories for each of this projects, so that it is easy to access by the lab members. This will be msot probably live under the lab GitHub page.
- Extract information frmo websites (PLA, Allen Brain Mouse, etc...) using package like Beautiful Soup
- Manipulating high-resolution tiff files : resizing, renaming, basic operations
- Automatisation of tranformation of mesh files into VR ready files using Blender command line
- Using convolutional neural networks for predictng z-coordinate of a microscopic section


```python
print('Bye Nesys world')
```

    Bye Nesys world
    


```python

```
