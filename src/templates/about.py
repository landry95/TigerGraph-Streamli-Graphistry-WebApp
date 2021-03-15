"""Home page shown when the user enters the application"""
import streamlit as st

import awesome_streamlit as ast
from PIL import Image

# pylint: disable=line-too-long


def write():
    st.balloons()
    image = Image.open("./src/img/1.PNG")
    st.sidebar.image(image, use_column_width=True)
    """Used to write the page in the app.py file"""
    st.markdown('<h2><b><font color=‘#5bc0de’><i><u>Project : </u></i> Web-App for data visualization !</font></b></h2>', unsafe_allow_html=True)
    with st.spinner("Loading About ..."):
        # ast.shared.components.title_awesome(" - About")
        st.markdown('''
            <h3 style="font-family: cursive; color: rgb(255, 127, 39)"><b>About</b></h3>
            <p style="margin-top: 10px"> 
                In this project, we are using the <b> International Medical Devices Database's </b> dataset about the medical devices distribution statistics in the world.
            </p>
            <p>
                I developed it taking part in the TigerGraph Web-App hashton. And it has been an adventure full of learning
            </p>
            I used many technologies :
            <ul>
                <li>python ; </li>
                <li>Streamlit ; </li>
                <li>tgcloud ; </li>
                <li>GrapgSql ; </li>
                <li>graphistry ; </li>
                <li>and many other libraries. </li>
            </ul>
            <hr style="border:1px solid black">
            <h3 style="font-family: cursive; color: rgb(255, 127, 39)"><b>Why did I chose this dataset ?</b></h3>
            <p>I chosed to work on this dataset because it refers to medical domain. Since more than one year, the world is facing a lot of pression, so a such a system can analyse the repartition of medical devices in the countries, and determine the ones that do not have enough and put on strategies to provide them</p>
            <p style="margin-bottom: 30px">
                We can therefore visualize the data and identify the inequal repartition of this phenomene in countries and also, we can understand the differences depending on the age of the victims and through years
            </p><hr style="border:1px solid black">
            <h3 style="font-family: cursive; color: rgb(255, 127, 39)"><b>What did I do ?</b></h3>
            <div>
                <p>So, what I have been doing is, saving the data in the tgcloud.io cloud database, and use the GSgl queries to retrieve the data that I wanted to manipulate in the streamlit application.</p>
                <p>In addition, I also discovered the technology "graphistry" with its library (graphistry), which allowed me to make professional graphs and superb data visualization.</p>
                <p>Finally, I was able to work with the python libraries also to have an appreciable interface and a multi-pages application</p>
                <span style="font-size-30px"><b>N.B. </b></span> It was my first time to work with TigerGraph and I discoverd a very great and powerfull technology that I can no longer do without. 
                <b style="color: orange">I literally fell in love with this technology</b>
                <p></p>
            </div>
            ''', 
            unsafe_allow_html=True
        )

#         st.markdown(
#             """## Contributions
# This an open source project and you are very welcome to **contribute** your awesome
# comments, questions, resources and apps as
# [issues](https://github.com/MarcSkovMadsen/awesome-streamlit/issues) or
# [pull requests](https://github.com/MarcSkovMadsen/awesome-streamlit/pulls)
# to the [source code](https://github.com/MarcSkovMadsen/awesome-streamlit).
# For more details see the [Contribute](https://github.com/marcskovmadsen/awesome-streamlit#contribute) section of the README file.
# ## The Developer
# This project is developed by Marc Skov Madsen. You can learn more about me at
# [datamodelsanalytics.com](https://datamodelsanalytics.com).
# Feel free to reach out if you wan't to join the project as a developer. You can find my contact details at [datamodelsanalytics.com](https://datamodelsanalytics.com).
# [<img src="https://github.com/MarcSkovMadsen/awesome-streamlit/blob/master/assets/images/datamodelsanalytics.png?raw=true" style="max-width: 700px">](https://datamodelsanalytics.com)
# """,
#             unsafe_allow_html=True,
#         )