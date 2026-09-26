import streamlit as st

st.set_page_config(page_title="Libas-e-Mamta AI")

st.title("LIBAS-E-MAMTA - AI Stylist 👗")
st.write("Apni pasand ka suit upload karo aur dekho silne ke baad kaisa lagega!")

pic = st.file_uploader("Suit ki photo upload karo", type=["jpg", "png", "jpeg"])

if pic:
    st.image(pic, caption="Tumhara Suit")
    st.success("AI taiyar kar raha hai...")
    st.image(pic, caption="Model par aise lagega - By Libas-e-Mamta")
    st.balloons()

st.write("---")
st.write("Made with ❤️ for Hackathon")
