"""Home page shown when the user enters the application"""
import streamlit as st

import awesome_streamlit as ast

from PIL import Image
# pylint: disable=line-too-long

# image = Image.open("./src/img/img.jpg")
# st.image(image, use_column_width=True)
def write():
    """Used to write the page in the app.py file"""
    image = Image.open("./src/img/1.PNG")
    st.sidebar.image(image, use_column_width=True)
    st.markdown('<h2><b><font color=‘#5bc0de’> <i><u>Project : </u></i> Web-App for data visualization !</font></b></h2>', unsafe_allow_html=True)
    with st.spinner("Loading About ..."):
        # ast.shared.components.title_awesome(" - About")
        st.markdown('''
                <h3 style="font-family: cursive; color: rgb(255, 127, 39)"><b>Demo in video</b></h3>
                <p style="margin-top: 10px; margin-bottom: 50px"> 
                    This is a demonstration of the application
                </p>
                </p><hr style="border:1px solid black">
            ''', 
            unsafe_allow_html=True
        )

        st.markdown('''<p> </p>''', unsafe_allow_html=True)
        image = Image.open("./src/img/5.PNG")
        st.image(image, use_column_width=True)
        image = Image.open("./src/img/11.PNG")
        st.image(image, use_column_width=True)
        st.markdown('''</p><hr style="border:1px solid black">''', unsafe_allow_html=True)

        st.markdown('''<p> Shemas from TigerGraph </p>''', unsafe_allow_html=True)
        image = Image.open("./src/img/schema.PNG")
        st.image(image, use_column_width=True)
        st.markdown('''</p><hr style="border:1px solid black">''', unsafe_allow_html=True)

        st.markdown('''<p> Graph Explorer from TigerGraph cloud</p> </div>''', unsafe_allow_html=True)
        image = Image.open("./src/img/graph_explorer.PNG")
        st.image(image, use_column_width=True)
        st.markdown('''</p><hr style="border:1px solid black">''', unsafe_allow_html=True)

        st.markdown('''<p> Data maping  from TigerGraph cloud </p> </div>''', unsafe_allow_html=True)
        image = Image.open("./src/img/map_data.PNG")
        st.image(image, use_column_width=True)
        st.image(Image.open("./src/img/export.png"), use_column_width=True)
        st.markdown('''</p><hr style="border:1px solid black">''', unsafe_allow_html=True)

        st.markdown('''<p> Query example from TigerGraph cloud </p> </div>''', unsafe_allow_html=True)
        image = Image.open("./src/img/example_querry.PNG")
        st.image(image, use_column_width=True)
        st.markdown('''</p><hr style="border:1px solid black">''', unsafe_allow_html=True)

        st.markdown('''<p> Graphistory platform </p> </div>''', unsafe_allow_html=True)
        image = Image.open("./src/img/graphistory.PNG")
        st.image(image, use_column_width=True)
        st.markdown('''</p><hr style="border:1px solid black">''', unsafe_allow_html=True)


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