# -*- coding: utf-8 -*-
"""
Created on Dec 21, 2022
@author: VSHIV

"""

#!/usr/bin/env python
# Author: Vinod Shiv
# Date: 2022-12-21

# Pandas
import pandas as pd

# Streamlit
import streamlit as st
import streamlit.components.v1 as comp


def make_iframe(trail_name):
    
    base_url = "https://www.alltrails.com/widget/trail/us/california/"

    return comp.iframe(src=base_url + trail_name + "?u=i", 
        width=800, height=400, scrolling=False)

# Main
if __name__ == "__main__":


    #### Set page config ####
    st.set_page_config(
        page_title="Bay Area Paved Trails",
        page_icon="mountain",
        layout="centered",
        initial_sidebar_state="collapsed"
    )

    # Add Title
    st.title("Partially Paved Trails :mountain:")
    st.subheader("Kid friendly too!")
    st.markdown("##### San Franscisco Bay Area | Rainy Days?")
    st.markdown ("***")

    ############################

    trail_list = pd.read_csv("./trails.csv", header=0)
   
    trail_list.trail_name.apply(make_iframe)
