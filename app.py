# -*- coding: utf-8 -*-
"""
Created on Dec 21, 2022
@author: VSHIV

"""

#!/usr/bin/env python
# Author: Vinod Shiv
# Date: 2022-12-21


# Misc
import pandas as pd
import json, requests, re
from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.parse import quote

# Streamlit
import streamlit as st
import streamlit.components.v1 as comp

# PDF
from fpdf import FPDF, HTMLMixin
from fpdf.html import HTML2FPDF
from datetime import date
import base64


#--------------------------------------------------------------
# PDF EXport Setup
#--------------------------------------------------------------
class HTMLMixinCustom(object):
    def write_html(self, text, image_map=None):
        "Parse HTML and convert it to PDF"
        h2p = HTML2FPDF(self, image_map = image_map)
        h2p.set_font('Arial',8)
        h2p.feed(text)

class myPDF(FPDF, HTMLMixinCustom):
    pass

pdf = myPDF('L','in',(11,17))
pdf.set_auto_page_break(True, margin=.5)
pdf.set_display_mode(zoom='fullwidth',layout='default')
pdf.set_margins(.25,.25,.25)

def create_download_link(val, filename):
    b64 = base64.b64encode(val)  # val looks like b'...'
    return f'<br/> &nbsp; 💾 &nbsp; <a href="data:application/octet-stream;base64,{b64.decode()}" download="{filename}.pdf"><b>DOWNLOAD RESULTS</b> </a>'


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
