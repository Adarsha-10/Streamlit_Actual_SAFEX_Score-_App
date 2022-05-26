from asyncio import coroutine
import streamlit as st

st.markdown("<h1 style = 'text-align: center; color: Blue;'>Actual SAFEX Score</h1>", unsafe_allow_html = True)

#st.subheader("Mandatory")

with st.form('Form1'):
        
        col1, col2 = st.columns(2)   
        counts = 0
        with col1:
            st.subheader('Life Insurance')
            uploaded_files = st.file_uploader("Upload file", accept_multiple_files=True)
            counts = counts + 0
            
            for uploaded_file in uploaded_files:
                bytes_data = uploaded_file.read()
                st.write("filename:", uploaded_file.name)
                st.write(bytes_data)
            submitted = st.form_submit_button('Submit')
        
        with col2:
            #a = st.write(count)
            st.metric(label="Actual SAFEX Score", value= counts,  delta_color="inverse")


with st.form('Form2'):
        
        col1, col2 = st.columns(2)   
        counts = 0
        with col1:
            st.subheader('Health & Well-being')
            uploaded_files = st.file_uploader("Upload file", accept_multiple_files=True)
            counts = counts + 0
            
            for uploaded_file in uploaded_files:
                bytes_data = uploaded_file.read()
                st.write("filename:", uploaded_file.name)
                st.write(bytes_data)
            submitted = st.form_submit_button('Submit')
        
        with col2:
            #a = st.write(count)
            st.metric(label="Actual SAFEX Score", value= counts,  delta_color="inverse")

with st.form('Form3'):
        
        col1, col2 = st.columns(2)   
        counts = 0
        with col1:
            st.subheader('Pets')
            uploaded_files = st.file_uploader("Upload file", accept_multiple_files=True)
            counts = counts + 0
            
            for uploaded_file in uploaded_files:
                bytes_data = uploaded_file.read()
                st.write("filename:", uploaded_file.name)
                st.write(bytes_data)
            submitted = st.form_submit_button('Submit')
        
        with col2:
            #a = st.write(count)
            st.metric(label="Actual SAFEX Score", value= counts,  delta_color="inverse")

with st.form('Form4'):
        
        col1, col2 = st.columns(2)   
        counts = 0
        with col1:
            st.subheader('Valuables')
            uploaded_files = st.file_uploader("Upload file", accept_multiple_files=True)
            counts = counts + 0
            
            for uploaded_file in uploaded_files:
                bytes_data = uploaded_file.read()
                st.write("filename:", uploaded_file.name)
                st.write(bytes_data)
            submitted = st.form_submit_button('Submit')
        
        with col2:
            #a = st.write(count)
            st.metric(label="Actual SAFEX Score", value= counts,  delta_color="inverse")

with st.form('Form5'):
        
        col1, col2 = st.columns(2)   
        counts = 0
        with col1:
            st.subheader('Warranty')
            uploaded_files = st.file_uploader("Upload file", accept_multiple_files=True)
            counts = counts + 0
            
            for uploaded_file in uploaded_files:
                bytes_data = uploaded_file.read()
                st.write("filename:", uploaded_file.name)
                st.write(bytes_data)
            submitted = st.form_submit_button('Submit')
        
        with col2:
            #a = st.write(count)
            st.metric(label="Actual SAFEX Score", value= counts,  delta_color="inverse")

