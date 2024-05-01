import streamlit as st
from PIL import Image

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
