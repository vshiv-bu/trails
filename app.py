# -*- coding: utf-8 -*-
"""
Created on Dec 21, 2022
@author: VSHIV

"""

#!/usr/bin/env python
# Author: Vinod Shiv
# Date: 2022-12-21


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
    st.title("Bay Area Paved Trails :mountain:")
    st.markdown("##### Rainy Days?")
    st.markdown ("***")

    ############################

    trail_list = [
        "east-shore-indian-cove-mcgregor-and-ten-hills-loop",
        "ten-hills-east-shore-loop",
        "lake-chabot-via-east-shore-trail",
        "stanford-dish-loop-trail",
        "bayview-and-meadowlark-trail-loop",
        "devil-s-slide",
        "sawyer-camp-trail",
        "bay-trail-shoreline-lake"]
   
    for i in trail_list:    
        make_iframe(i)

    # Partially paved
