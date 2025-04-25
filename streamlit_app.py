import streamlit as st
import numpy as np
import pandas as pd
import datetime

# config
st.set_page_config(layout="wide")

is_file_loaded = False

# values to preset
# userFile, degreeList, courseList, todoList = None, [], [], []

# try:
#     userFile = open("tester.txt", "r")
#     curReading = 0
#     curLine = -1
#     for line in userFile:
#         curLine += 1

#         # switch type
#         if line.startswith("degreeList"):
#             curReading = 1
#         elif line.startswith("courseList"):
#             curReading = 2
#         elif line.startswith("todoList"):
#             curReading = 3
#         elif curLine == 0:
#             raise Exception(curLine)
        
#         splitLine = line.split(",")
        
#         if curReading == 1:
#             degreeList.append(splitLine)
#         elif curReading == 2:
#             courseList.append(splitLine)
#         elif curReading == 3:
#             todoList.append(splitLine)
        

        
# except:
#     st.markdown("Issue loading file")


# MAIN PAGE

if not is_file_loaded:
    st.title("One Dashboard, All your planning needs.")
    st.divider()

    col1, col2 = st.columns([1,3], border=True)

    if col1.button("Continue Your Semester", use_container_width=True):
        is_file_loaded = True
        st.write("hi")
    if col1.button("Start a New Semester", use_container_width=True):
        is_file_loaded = True
    if col1.button("Start Anew", use_container_width=True):
        is_file_loaded = True
    
    col2.markdown("Upload your :blue-background[semester.txt] file to continue planning this semester.")
    col2.markdown("Upload your :blue-background[semester.txt] file. Start a new semester plan, keeping your grade and degree trackers in tact.")
    col2.markdown("Start a completely blank dashboard.")
else:
    st.write("Hi!")
