import os
from pathlib import Path
import streamlit as st
from PIL import Image

#----------------------------------------------
# current directory and files
current_dir = Path.cwd()

css_file = current_dir / "styles" /"main.css"
resume_file = current_dir / "assets" / "my_cv.pdf"
picture_file = current_dir / "assets" / "my_photo.jpg"


#----------------------------------------------
# general settings
PAGE_TITLE = "Digital CV | Claudia Wehrhahn"
PAGE_ICON = ":wave:"
NAME = "Claudia Wehrhahn"
DESCRIPTION = """
Senior Data Scientist, short description.
"""
EMAIL = "clau.wehrhahn@gmail.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/claudia-wehrhahn/",
    "GitHub": "https://github.com/claudiawehrhahn",
}
PROJECTS = {
    "🏆 Sales Dashboard - Comparing sales across three stores": "https://youtu.be/Sb0A9i6d320",
}


# configuracion de pagina
st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


#-- load css, pdf, and resumen picture
with open(css_file) as f_css:
    st.markdown("<style>{}</style>".format(f_css.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as f_pdf:
    PDFbyte = f_pdf.read()
profile_pic = Image.open(picture_file)


#-- hero section
col1, col2 = st.columns(2, gap="small")
with col1: # picture
    st.image(profile_pic, width=230) # pixels
with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label = "Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("Email:", EMAIL)

#-- social links (iteratively)
st.write("#") # adds extra space
cols = st.columns(len(SOCIAL_MEDIA)) 
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")


#-- experience and qualifications
st.write("#")
st.subheader("Experience + Qualifications")
st.write(
    """
- 8+ Years of experience developing statistical models to describe real life problems
- 2+ Years of experience leveraging data to guide business decisions and strategies
- 
    """
)

#----------------------------------------------
# title
st.title("Hello there!!")

