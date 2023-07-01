import streamlit as sp
import pickle
import pandas as pd


def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movies = []
    for i in movies_list:
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies


similarity = pickle.load(open('similarity.pkl', 'rb'))

movies_dict = pickle.load(open('movieslist.pkl', 'rb'))

movies = pd.DataFrame(movies_dict)

option = sp.selectbox('How would you like to be contacted? ', movies['title'])

if sp.button('Recommend'):
    recommend_movies = recommend(option)
    for i in recommend_movies:
        sp.write(i)
