# 130. Importing Modules, Installing Packages, and Working with Aliases

### 130.1  Basic Import

# import turtle
# tim = turtle.Turtle()


### 130.2  from [ModuleName] import [Thing in Module]

# from turtle import Turtle
#
# tim = Turtle()
# tom = Turtle()
# terry = Turtle()


### 130.3  from [ModuleName] import *

# from turtle import *
#
# forward(100)


### 130.4 Aliasing

import turtle as t

tim = t.Turtle()
