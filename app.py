import streamlit  as st
st.title("My Streamlit App")
st.write("Welcome to my Streamlit application!")
name = st.text_input("Enter a number:")
if st.button("Submit"):
    st.write(f"Hello, {name},streamlit is  successfully running!")
