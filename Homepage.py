import streamlit as st
import pandas

col1, col2 = st.columns(2)

with col1:
    st.image("images\\picture.png")

with col2:
    st.title("Dimitris Tsagkaridis")

    content = """Hi!
My name is Dimitris.

I was born and raised in Greece and have been living in the Netherlands since 2016.

My Python Programming career starter on 2020 and still going strong!

In my free time, I like to play water polo, paint miniatures, and play tabletop games."""

    st.info(content)

content2 = """
My Apps
"""

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])
st.write(content2)

df = pandas.read_csv("data.csv", sep=";")

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")