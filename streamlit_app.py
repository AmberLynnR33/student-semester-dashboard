import streamlit as st
import numpy as np
import pandas as pd
import datetime

# config
st.set_page_config(layout="wide")

if "is_file_loaded" not in st.session_state:
    st.session_state.is_file_loaded = False
    st.session_state.loaded_dashboard = False

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

if not st.session_state.is_file_loaded:
    st.title("One Dashboard, All your planning needs.")
    st.divider()

    col1, col2 = st.columns([1,3], border=True)

    if col1.button("Continue Your Semester", use_container_width=True):
        st.session_state.is_file_loaded = True
    if col1.button("Start a New Semester", use_container_width=True):
        st.session_state.is_file_loaded = True
    if col1.button("Start Anew", use_container_width=True):
        st.session_state.is_file_loaded = True
    
    col2.markdown("Upload your :blue-background[semester.txt] file to continue planning this semester.")
    col2.markdown("Upload your :blue-background[semester.txt] file. Start a new semester plan, keeping your grade and degree trackers in tact.")
    col2.markdown("Start a completely blank dashboard.")
else:
    if st.sidebar.button("Your Dashboard", use_container_width=True) or (not st.session_state.loaded_dashboard):
        st.session_state.loaded_dashboard = True
        st.write("HELLO!")
        pass
    if st.sidebar.button("Your Grades", use_container_width=True):
        pass
    if st.sidebar.button("Your Degree", use_container_width=True):
        pass
    if st.sidebar.button("About", use_container_width=True):
        pass
    if st.sidebar.button("**Download Your File**", use_container_width=True):
        pass
    
