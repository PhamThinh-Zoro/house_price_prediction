import streamlit as st
import pickle 
import numpy as np

with open('best_tree.pkl','rb') as f:
    model=pickle.load(f)

st.title('House price prediction')
st.write('Nhap thong tin de du doan gia: ')

area=st.number_input('Nhap dien tich:', min_value=0.0, step=0.1)
rooms=st.slider('So phong: ', 1, 10, 1)
#rooms=st.number_input('Nhap so phong:', min_value=0, step=1)

if st.button('Predict'):
    input_data = np.array([[area, rooms]])
    prediction = model.predict(input_data)
    st.success(f"Model du doan la: {prediction[0]:.3f} $")