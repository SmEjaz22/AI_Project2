import streamlit as st
from streamlit_lottie import st_lottie
import requests
from PIL import Image

st.set_page_config(page_title="AI", page_icon=":relaxed:",
                   layout="wide")  #by default it is centered


def code1(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


def code2(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


def code3(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


gif1 = code1("https://assets2.lottiefiles.com/packages/lf20_jh9gfdye.json")
gif2 = code1("https://assets6.lottiefiles.com/private_files/lf30_zZJryv.json")
gif3 = code2("https://assets6.lottiefiles.com/packages/lf20_fKTyo2Pwki.json")

with st.container():
    st.title(":blue[_**Welcome To** Artificial Intelligence **Project**_]")
    st.markdown(
        "<h2 style='text-align: center; color:Grey;'><u> 'Object Detector' </u></h2>",
        unsafe_allow_html=True)

with st.container():
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("What is ARITIFICIAL INTELLIGENCE ?")
        st.write(
            ':red[Aritificial Intelligence] is mimicking the intelligence and rationality from the human beings. Machines are programmed about what to think. But in the case of machine learning, machines are made to analyze, read data, observe and learn from their mistakes. Artificial Intelligence is probably the most complex of creation of humanity. This is disregarding the fact that the field itself is "largely unexplored".'
        )
        st.write(
            "The huge amount of data that we generate every day digitally has further helped with the rapid growth of artificial intelligence. Making the machine faster and more efficient for businesses and consumers alike. These intelligent machines not only try to mimic human-like thinking but over time learns to do new operations as well."
        )

        # st.markdown(
        #     "<h3 style='text-align: left; color:white;'> What is Object Detection ? </h3>",
        #     unsafe_allow_html=True)
        # st.markdown(
        #     "<h6 style='color:white ;'> Object detection is a computer vision technique that works to identify and locate objects within an image or video. Specifically, object detection draws bounding boxes around these detected objects, which allow us to locate where said objects are in (or how they move through) a given scene.</h6>",
        #     unsafe_allow_html=True)
        st.subheader("COMPUTER VISION")
        st.write(
            "Object tracking is one of the most important tasks in :red[**Computer Vision**].It has a multitude of real-life applications, including use cases such as traffic monitoring, robotics, medical imaging, autonomous vehicle tracking, and more."
        )
        st.write(
            "Video tracking is widely used in traffic monitoring, self-driving cars, and security because it can process real-time footage."
        )

        st.subheader("Means of Object Detection")
        st.write(
            "Our Project focuses the idea :red[**Object Detection**] which is the process of detecting a target object in an image or a single frame of the video. Object detection will only work if the target image is visible on the given input. If the target object is hidden by any interference it will not be able to detect it."
        )
        st.write(
            "Object Detection in Video, is the task of detecting a moving object/Object of interest by giving some predefined values to the algorithm in a video. The idea of detecting an object in a video is to associate or establish a relationship between target objects as it appears in each video frame. In other words, Object Detection in video is analyzing the video frames sequentially and creating a bounding box around the object of interest. Object Detection in Video is widely used in traffic monitoring, self-driving cars, and security because it can process real-time footage."
        )
        st.text("")

    image1 = Image.open('Picture4.png')
# with col1:

# st.write("2020F-BCE-048, Syed Muhammad Ejaz Hasnain ")
#     # st.markdown("***")
# st.write("2020F-BCE-020, Syed Hamza Munawar ")
#     # st.markdown("***")
# st.write("2020F-BCE-012, Mudabbir Alim ")
_, col22, col33 = st.columns([1, 1, 1])
with col33:
    st.image(
        image1,
        caption=
        'RESEARCH BASED PROJECT ON ARTIFICIAL INTELLIGENCE PRESENTED BY STUDENTS OF \n "SIR SYED UNIVERSITY OF ENGINEERING AND TECHNOLOGY KARACHI"',
        width=250)
with _:
    st.subheader('Conclusion')
    st.write("As You go through our project")
st.markdown(
    "<h2 style='text-align: center; color: red;'><u> GROUP MEMBERS </u></h2>",
    unsafe_allow_html=True)
st.markdown(
    "<h5 style='text-align: center; color: white;'>Syed Muhammad Ejaz Hasnain <br> 2020F-BCE-048</h5>",
    unsafe_allow_html=True)
st.markdown(
    "<h5 style='text-align: center; color: white;'>Syed Hamza Munawar <br> 2020F-BCE-020 </h5>",
    unsafe_allow_html=True)
st.markdown(
    "<h5 style='text-align: center; color: white;'>Mudabbir Alim <br> 2020F-BCE-012 </h5>",
    unsafe_allow_html=True)

with col2:
    # image2 = Image.open(
    #     'D:/PYTHON CODE/object_detection_vs_image_recognition.jpg')
    # st.image(image2,
    #          caption='An Example of Image Recognition and Object Recognition',
    #          width=250,
    #          use_column_width=5000)
    st.text("")
    st_lottie(gif1, height=250, key="robot")
    st.text("")
    st.text("")
    st.text("")
    st_lottie(gif2, height=200, key="vision")
    st.text("")
    st.text("")
    st_lottie(gif3, height=250, key="objectrecog")

# st.title("AI")
