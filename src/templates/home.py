"""Home page shown when the user enters the application"""
import streamlit as st

import awesome_streamlit as ast
from PIL import Image

# pylint: disable=line-too-long
def write():
    
    """Used to write the page in the app.py file"""
    # ataset_name = st.sidebar.selectbox('lyse', ('about', 'Suside Statistics', 'Suicide Statistics over years',  'Survey on Mental Health in the Tech Workplace'))
    with st.spinner("Loading Home ..."):
        st.markdown('<h2><b><font color=‘#5bc0de’> <i><u>Project : </u></i> Web-App for data visualization !</font></b></h2>', unsafe_allow_html=True)
        st.markdown('<h4 style="color: #d9534f"><b> <i><u>multi-pages streamlit applicxation </u></i> </b></h4>', unsafe_allow_html=True)

        st.write("# International Medical Devices Database")

        st.write('''
                <iframe width="700" height="500" src="https://www.youtube.co">
                </iframe>
            ''', 
            unsafe_allow_html=True)

        st.markdown('''<p> </p>''', unsafe_allow_html=True)
        image = Image.open("./src/img/9.PNG")
        st.image(image, use_column_width=True)
        st.markdown('''</p><hr style="border:1px solid black">''', unsafe_allow_html=True)


        st.markdown(
            """ 
                <div>
                    <p>In this project, Here, we are analyzing the <b>"<i>International Medical Devices Database</i>"</b> dataset.</p>
                    <p>It contains information on more than 120,000 Recalls, Safety Alerts and Field Safety Notices about medical devices distributed worldwide. The information connects with medical device companies and their subsidiaries.</p>
                    <p>Thus, We will be Exploring more than 120,000 Recalls, Safety Alerts and Field Safety Notices of medical devices and their connections with their manufacturers.</p>
                    <b>
                    This application provides : 
                        <ul>
                            <li>Recall of manufacturers</li>
                            <li>Safety Alert</li>
                            <li>Field Safety Notice</li>
                            <li>Product Classification</li>
                            <li>Implanted device</li>
                            <li>Quantity in Commerce</li>
                            <li>Event Risk Class</li>
                            <li>Local Authorities Determined Cause</li>
                            <li>etc.</li>
                        </ul>
                    </b>
                    <p style="color: rgb(255, 127, 39)"><b>Just use the menu on the left navigation bar to navigate throughout the application and explore the data</b></p>
                </div>
            """ , 
            unsafe_allow_html=True
        )

        st.markdown('''<p> <b>Enjoy the app</b></p>''', unsafe_allow_html=True)
        image = Image.open("./src/img/12.PNG")
        st.image(image, use_column_width=True)
        st.markdown('''</p><hr style="border:1px solid black">''', unsafe_allow_html=True)
#         st.write(
#             """ 
# [Streamlit](https://streamlit.io/) is [announced](https://towardsdatascience.com/coding-ml-tools-like-you-code-ml-models-ddba3357eace) as being **The fastest way to build custom Machine Learning tools** but I believe it has the potential to become much more awesome than that.


# I believe Streamlit has the **potential to become the Iphone of Data Science Apps**. And maybe it can even become the Iphone of Technical Writing, Code, Micro Apps and Python.
# The **purpose** of the **Awesome Streamlit Project** is to share knowledge on how Awesome Streamlit is and can become.
# This application provides
# - A list of awesome Streamlit **resources**.
# - A **gallery** of awesome streamlit applications.
# - A **vision** on how awesome Streamlit can be.
# ## The Magic of Streamlit
# The only way to truly understand how magical Streamlit is to play around with it.
# But if you need to be convinced first, then here is the **4 minute introduction** to Streamlit!
# Afterwards you can explore examples in the Gallery and go to the [Streamlit docs](https://streamlit.io/docs/) to get started.
    
#     """
#         )
#         ast.shared.components.video_youtube(
#             src="https://www.youtube.com/embed/B2iAodr0fOo"
#         )