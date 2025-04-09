import streamlit as st
import numpy as np
import pandas as pd
import datetime

# config
st.set_page_config(layout="wide")

# values to preset
userFile, degreeList, courseList, todoList = None, [], [], []

try:
    userFile = open("tester.txt", "r")
    curReading = 0
    curLine = -1
    for line in userFile:
        curLine += 1

        # switch type
        if line.startswith("degreeList"):
            curReading = 1
        elif line.startswith("courseList"):
            curReading = 2
        elif line.startswith("todoList"):
            curReading = 3
        elif curLine == 0:
            raise Exception(curLine)
        
        splitLine = line.split(",")
        
        if curReading == 1:
            degreeList.append(splitLine)
        elif curReading == 2:
            courseList.append(splitLine)
        elif curReading == 3:
            todoList.append(splitLine)
        

        
except:
    st.markdown("Issue loading file")


st.title("Hello!")
