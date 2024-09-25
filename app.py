import streamlit as st
import pickle
import pandas as pd
import requests  

movies = pickle.load(open("movies_list.pkl",'rb'))
similarity = pickle.load(open("similarity.pkl",'rb'))
movies_list=movies['title'].values

st.header("Movie Recommender System")
selectvalue = st.selectbox("select movie from dropdown", movies_list)

def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=d28ff6dda1970828595671f95edaae76'.format(movie_id))
    data=response.json()
    return "http://image.tmdb.org/t/p/w500/" + data['poster_path']

 
def recommand(movie):
    index=movies[movies['title']==movie].index[0]
    distance = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda vector:vector[1])
    recommend_movies=[]
    recommend_movies_poster=[]
    for i in distance[0:10]:
        movies_id=movies.iloc[i[0]].id
        recommend_movies.append(movies.iloc[i[0]].title)
        recommend_movies_poster.append(fetch_poster(movies_id))
    return recommend_movies, recommend_movies_poster


if st.button("show movies list"):
    names,poster = recommand(selectvalue)
    col1, col2, col3, col4, col5, col6, col7, col8, col9, col10 = st.columns(10)
    
    with col1:
        st.text(names[0])
        st.image(poster[0])

    with col2:
        st.text(names[1])
        st.image(poster[1])

    with col3:
        st.text(names[2])
        st.image(poster[2])
    with col4:
        st.text(names[3])
        st.image(poster[3])
    with col5:
        st.text(names[4])
        st.image(poster[4])
    with col6:
        st.text(names[5])
        st.image(poster[5])
    with col7:
        st.text(names[6])
        st.image(poster[6])
    with col8:
        st.text(names[7])
        st.image(poster[7])
    with col9:
        st.text(names[8])
        st.image(poster[8])
    with col10:
        st.text(names[9])
        st.image(poster[9])
        