# -*- coding: utf-8 -*-
"""Untitled20.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ku08I6uvbfdmExjR1_YhMNulmq7GbUFN
"""
import en_core_web_sm
nlp = en_core_web_sm.load()

import streamlit as st
st.set_page_config(page_title="Interview Prep Tool", layout="wide")

from streamlit_option_menu import option_menu
from modules import mock_interview, resume_analyzer, interview_preparation

#st.set_page_config(page_title="Interview Prep Tool", layout="wide")

# Sidebar navigation
with st.sidebar:
    selected = option_menu(
        menu_title="Main Menu",
        options=["Mock Interview", "Resume Analyzer", "Interview Preparation"],
        icons=["mic", "file-earmark-text", "briefcase"],
        default_index=0,
    )

# Routing based on selection
if selected == "Mock Interview":
    mock_interview.show()

elif selected == "Resume Analyzer":
    resume_analyzer.show()

elif selected == "Interview Preparation":
    interview_preparation.show()