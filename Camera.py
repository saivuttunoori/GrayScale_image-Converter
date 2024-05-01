import streamlit as st
from PIL import Image

st.header("Gray scale converter")
uploaded_image = st.file_uploader("Upload Image")
with st.expander("Start Camera"):
    # start the camera
    camera_image = st.camera_input("Camera")

if camera_image:
    # create a pillow image instance
    img = Image.open(camera_image)

    # convert image to grayscale
    img_gray = img.convert("L")

    # renders the gray scale image
    st.image(img_gray)
if uploaded_image:
    img1 = Image.open(uploaded_image)

    img1_gray = img1.convert("L")

    st.image(img1_gray)

