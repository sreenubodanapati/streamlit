import streamlit as st
import numpy as np
import pandas as pd 


def main():
    """ Main Function """
    st.title("File Uploading")

    st.file_uploader("Upload Dataset",type=["csv","txt"])

if __name__ == "__main__":
    main()



