import streamlit as st
import pandas as pd 
import seaborn as sns


st.header('**This is a header**')
st.subheader('subheader')
st.write('this is a comment')
st.text('hello world') # raw text


# Draw a title and some text to the app:
'''
# This is the document title

This is some _markdown_.
'''

df = pd.DataFrame({'col1': [1,2,3],
				   'col2':[1,2,3]})
df  # <-- Draw the dataframe

x = 10
'x', x  # <-- Draw the string 'x' and then the value of x


x = 4
x, 'squared is', x * x

x = st.slider('slider')  # 👈 this is a widget
st.write(x, 'squared is', x * x)


# Add a selectbox to the sidebar:
add_selectbox = st.sidebar.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone')
)

# Add a slider to the sidebar:
add_slider = st.slider(
    'Select a range of values',
    0.0, 100.0, (25.0, 75.0)
)


@st.cache  # 👈 This function will be cached
def my_slow_function(arg1, arg2):
    # Do something really slow in here!
    return the_output