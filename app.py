import streamlit as st
from PIL import Image

st.set_page_config(page_title="Libas-e-Mamta AI", page_icon="👗", layout="centered")

st.title("LIBAS-E-MAMTA 👗")
st.subheader("AI Stylist for Desi Moms")
st.write("Suit upload karo aur dekho silne ke baad kaisa lagega!")
st.markdown("---")

pic = st.file_uploader("📸 Suit ki photo upload karo", type=["jpg", "png", "jpeg"])

if pic:
    img = Image.open(pic)
    c1, c2 = st.columns(2)
    with c1:
        st.image(img, caption="Tumhara Suit", use_container_width=True)
    with c2:
        st.image(img, caption="Model par Look ✨", use_container_width=True)
    
    st.success("MashAllah! Ye tum par bohat jachega! 😍")
    st.markdown("### 💡 AI Stylist Tips:")
    st.write("✔️ White khussa + jhumkay = perfect")
    st.write("✔️ Eid / Shaadi ke liye ideal hai")
    st.write("✔️ Dupatte pe lace lagwao to aur classy!")
    st.balloons()
else:
    st.info("👆 Upar se photo upload karo bestie!")

st.markdown("---")
st.caption("Made with ❤️ by Mamta for Hackathon 2026")
