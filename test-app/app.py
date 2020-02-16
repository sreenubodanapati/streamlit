# Import Pkgs
import streamlit as st
import numpy as np
import pandas as pd
# import matplotlib.pyplot as plt
# import matplotlib
# matplotlib.use('Agg')

import re



def main(st):
    """ Main Function """
    st.title("Explore Data")

    data = st.file_uploader("Upload Your CSV Dataset",type=["csv","txt"])

    components = ["Analyse Data", "visualization", "Modal Building"]

    if data is not None:
        choice = st.sidebar.selectbox("chouse options", components)

        df = pd.read_csv(data)


        # Data Analytics

        if choice == "Analyse Data":
            st.subheader("Raw Data")
            show_data = st.selectbox("Show Data", ("Head", "Tail", "Show all data", "Show Summary", "Custom your data"))

            if show_data == "Head":
                st.dataframe(df.head())
            elif show_data == "Tail":
                st.dataframe(df.tail())
            elif show_data == "Show all data":
                st.dataframe(df)
            elif show_data == "Show Summary":
                st.dataframe(df.describe())
            elif show_data == "Custom your data":
                select_rows = st.number_input("enter number", value=5, key="select_rows")
                all_columns = df.columns.to_list()
                select_colums = st.multiselect("Select Columns What You Want To Show", all_columns, default=all_columns[1])            
                new_df = df[select_colums]
                st.dataframe(new_df.head(select_rows))
            else:
                st.dataframe(df(2))

            more_analytics = st.sidebar.selectbox("Advanced Data filters", ["Show data groupby", "Option-1", "Option-1"])

            if more_analytics == "Show data groupby":
                st.subheader(more_analytics)
                
                st.write(df.groupby(['Survived']).head())


                all_columns = df.columns.to_list()
                st.write(all_columns)
                # gb_data = select_colums.df[new_df]

                # new_df = df.loc["Name"].str.contains("Mrs", float=re.I, regex=True)
                
                
                # st.dataframe(new_df.head())



            elif more_analytics == "Option-1":
                st.subheader(more_analytics)

            

            


        # visualization
        elif choice == "visualization":
            st.dataframe(df.head())

            st.subheader("Data Visualization")

        # Modal Building
        elif choice == "Modal Building":
            st.subheader("Modal Building")



if __name__ == "__main__":
    main(st)








