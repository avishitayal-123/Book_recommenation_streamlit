import streamlit as st
import pickle
import pandas as pd
import numpy as np
import requests

def fetch_cover(book_id):
    requests.get('http://images.amazon.com/images/P/{}.01.LZZZZZZZ.jpg'.format(ISBN))
def recommend(book_name):
    # index fetch
    index = np.where(pt.index==book_name)[0][0]
    similar_items = sorted(list(enumerate(similarity_scores[index])),key=lambda x:x[1],reverse=True)[1:5]
    
    data = []
    for i in similar_items:
        item = []
        temp_df = book[book['Book-Title'] == pt.index[i[0]]]
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Title'].values))
        #item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Author'].values))
        #item.extend(list(temp_df.drop_duplicates('Book-Title')['Image-URL-M'].values))
        
        for i in item:
            data.append(i)
    
    return data
book_dict=pickle.load(open('popular_dict.pkl','rb'))
similarity_scores=pickle.load(open('similarity_scores.pkl','rb'))
pt=pickle.load(open('pt.pkl','rb'))
book=pd.DataFrame(book_dict)
st.title("Book_Recommendation")
option=st.selectbox('How would you like to be contracted?',
                    book['Book-Title'].values)

if st.button('Recommend'):
    recommendations=recommend(option)
    for i in recommendations:
        st.write(i)