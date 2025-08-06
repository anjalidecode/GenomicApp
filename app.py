import streamlit as st
import requests
import numpy as np
import matplotlib.pyplot as plt

st.title('Genomic Data Analysis - Identifying Genetic Variations')

sequence = st.text_input('Enter DNA Sequence')

if st.button('Identify Genetic Variations'):
    input_data = np.array([[ord(c) for c in sequence]])  # Convert DNA to numbers
    response = requests.post('http://127.0.0.1:5000/predict', json={'input': input_data.tolist()})

    if response.status_code == 200:
        result = response.json()
        st.write("Genetic Variations Identified:")
        st.write(result['variations'])

        fig, ax = plt.subplots()
        ax.bar(range(len(result['variations'][0])), result['variations'][0])
        ax.set_xlabel('Variation Index')
        ax.set_ylabel('Frequency')
        ax.set_title('Genetic Variation Frequency')
        st.pyplot(fig)
    else:
        st.error("API request failed.")