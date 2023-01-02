import streamlit as st
from streamlit_lottie import st_lottie
import requests

# from collections import deque
# from imutils.video import VideoStream
# # import numpy as np
# # import argparse
# # import cv2
# # import imutils
# # import time

st.set_page_config(page_title="AI", page_icon=":relaxed:",
                   layout="wide")  #by default it is centered


def code1(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


gif1 = code1("https://assets7.lottiefiles.com/packages/lf20_1hz14qor.json")
st.title("Object Detection Using :red[Pre-recorded Video]")

with st.container():
    st.header("Thing You Need To Know")
    st.write(
        "Make Sure you record the video using this laptops camera/webcam because of the argument. "
    )
with st.container():
    col1, col2 = st.columns(2)
    col1.subheader(
        "Why the same color looks so different on different devices?")
    col1.write(
        "Most likely, the devices use a different screen type. Colors vary between LCDs, LEDs and other screen types because of the way the screen is built. For example, some screens will turn pixels of completely to display black, while some will show a shade of grey."
    )
    col1.write(
        ":blue[**No two screens are usually identical, when it comes to color.**]"
    )
videoo = st.file_uploader("Upload Video")
# video_file = open(videoo, 'rb')
# st.video(videoo)
# upvid = videoo.read()

with col2:
    st_lottie(gif1, height=250, key="vision")
#     with col1:
#         if videoo:
#             # readd = video.read()
#             print("pressing \" Esc \" key will terminate your Program.")
#             ap = argparse.ArgumentParser()
#             ap.add_argument("-v",
#                             "--video",
#                             help="path to the (optional) video file")
#             ap.add_argument("-b",
#                             "--buffer",
#                             type=int,
#                             default=16,
#                             help="max buffer size")
#             args = vars(ap.parse_args())
#             #**********************************************************************************************************
#             # define the lower and upper boundaries of the "green"
#             # ball in the HSV color space, then initialize the
#             # list of tracked points
#             redlower = (0, 100, 100)
#             redupper = (4, 255, 255)
#             greenLower = (20, 100, 100)  # 0, 96, 96
#             greenUpper = (41, 255, 255)  #173, 255, 255
#             pts = deque(maxlen=args["buffer"])
#             # if a video path was not supplied, grab the reference
#             # to the webcam
#             # if not args.get("video", False):
#             #     vs = VideoStream(src=0).start()
#             # otherwise, grab a reference to the video file
#             # else:
#             # vs = cv2.VideoCapture(args["video"])
#             # # allow the camera or video file to warm up
#             if not args.get("video", False):
#                 upvid = VideoStream(src=0).start()
#             # otherwise, grab a reference to the video file
#             else:
#                 upvid = cv2.VideoCapture(args["video"])
#             time.sleep(2.0)
#             ##**********************************************************************************************************
#             # keep looping
#             while True:
#                 # grab the current frame
#                 frame = upvid.read()
#                 # handle the frame from VideoCapture or VideoStream
#                 frame = frame[1] if args.get(
#                     "video", False) else frame  # Video Stream VS Video Capture
#                 # if we are viewing a video and we did not grab a frame,
#                 # then we have reached the end of the video
#                 if frame is None:
#                     st.stop()
#                 # resize the frame, blur it, and convert it to the HSV
#                 # color space
#                 frame = imutils.resize(
#                     frame,
#                     width=600,
#                 )
#                 blurred = cv2.GaussianBlur(frame, (11, 11), 0)
#                 hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)
#                 # construct a mask for the color "green", then perform
#                 # a series of dilations and erosions to remove any small
#                 # blobs left in the mask
#                 mask = cv2.inRange(hsv, greenLower,
#                                    greenUpper)  # change it to see the effects.
#                 mask = cv2.erode(mask, None, iterations=2)
#                 mask = cv2.dilate(mask, None, iterations=2)
#                 # time to perform compute the contour (i.e. outline) of the green ball and draw it on our frame:
#                 #**********************************************************************************************************
#                 # find contours in the mask and initialize the current
#                 # (x, y) center of the ball
#                 cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,
#                                         cv2.CHAIN_APPROX_SIMPLE)
#                 cnts = imutils.grab_contours(cnts)
#                 center = None
#                 # only proceed if at least one contour was found
#                 if len(cnts) > 0:
#                     # find the largest contour in the mask, then use
#                     # it to compute the minimum enclosing circle and
#                     # centroid
#                     c = max(cnts, key=cv2.contourArea)
#                     ((x, y), radius) = cv2.minEnclosingCircle(c)
#                     M = cv2.moments(c)
#                     center = (int(M["m10"] / M["m00"]),
#                               int(M["m01"] / M["m00"]))
#                     # only proceed if the radius meets a minimum size
#                     if radius > 10 and radius < 100:  #*************************************************************************
#                         # draw the circle and centroid on the frame,
#                         # then update the list of tracked points
#                         cv2.circle(frame, (int(x), int(y)), int(radius),
#                                    (0, 17, 255), 2)
#                         cv2.circle(frame, center, 5, (0, 0, 255), -1)
#                 # update the points queue
#                 pts.appendleft(center)
#                 #**********************************************************************************************************
#                 # loop over the set of tracked points
#                 for i in range(1, len(pts)):
#                     # if either of the tracked points are None, ignore
#                     # them
#                     if pts[i - 1] is None or pts[i] is None:
#                         continue
#                     # otherwise, compute the thickness of the line and
#                     # draw the connecting lines
#                     thickness = int(
#                         np.sqrt(args["buffer"] / float(i + 1)) * 2.5)
#                     cv2.line(frame, pts[i - 1], pts[i], (0, 0, 255), thickness)
#                 # show the frame to our screen
#                 st.video(cv2.imshow("Ball Tracking System", frame))
#                 # key = cv2.waitKey(1) & 0xFF
#                 # # if the 'q' key is pressed, stop the loop
#                 # if key == ord("q"):
#                 #     break
#                 # button = st.button("Click Me To Stop")
#                 # if button:
#                 #     st.write("Program Successfully terminated ")
#                 #     st.stop()
#                 # if cv2.waitKey(20) & 0xFF == 27:
#                 #     break
#                 # if we are not using a video file, stop the camera video stream
#                 #do we get out of while loop ?#**********************************************************************************************************
#                 if not args.get("video", False):
#                     upvid.stop()
#                 # otherwise, release the camera
#                 else:
#                     upvid.release()
#                     # close all windows
#                 cv2.destroyAllWindows()
#                 print("Program Successfully terminated ")
