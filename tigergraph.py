import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import pyTigerGraphBeta as tg
import dateparser
import graphistry
from PIL import Image


import awesome_streamlit as ast



#-----------------------------------
import src.templates.about
import src.templates.home
import src.templates.medical_devices
import src.templates.gallery

ast.core.services.other.set_logging_format()


#------------------------------------------
st.set_option('deprecation.showPyplotGlobalUse', False)


PAGES = {
    "Home": src.templates.home,
    "Explore data": src.templates.medical_devices,
    "gallery": src.templates.gallery,
    "About": src.templates.about,
}


st.sidebar.markdown('<h2 style="text-align: center; font-family: cursive; color: rgb(255, 127, 39)"><b>WELCOME</b></h2>', unsafe_allow_html=True)
image = Image.open("./img/logo.PNG")
st.sidebar.image(image, use_column_width=True)
st.sidebar.info(
    """
	        multi-pages Web-App for data visualization and analysis
	"""
)


selection = st.sidebar.radio("Navigate to", list(PAGES.keys()))

page = PAGES[selection]

with st.spinner(f"Loading {selection} ..."):
    ast.shared.components.write_page(page)







# dataset_name = st.sidebar.selectbox('Select The data you want to analyse', ('about', 'Suside Statistics', 'Suicide Statistics over years',  'Survey on Mental Health in the Tech Workplace'))


graphistry.register(api=3, protocol="https", server="hub.graphistry.com", username="landry", password="istanbul.1957")


conn = tg.TigerGraphConnection(host="https://tggraph.i.tgcloud.io", graphname="tggraphhack", apiToken="c8l0pe58m15he0v8t6q9p709oh598is4")

authToken = conn.getToken("en84d51mdrapbb6b5b6h83q0mrijubst", "100000000000000000")

preInstalledResult = conn.runInstalledQuery("demo", {'a': 10}) 

# print(preInstalledResult)
# preInstalledResult[0]["cc"][0]["attributes"]


# bank_connections = pd.read_csv("./data/bank_connections.csv", sep=",")
# transactions = pd.read_csv("./data/transactions_map.csv", sep=",")
# country_stats = pd.read_csv("./data/country_data.csv", sep=",")

# st.write(country_stats)


# g = graphistry.bind(source="source", destination="target")
# g.edges(country_stats).plot()

# g = graphistry.edges(pd.read_csv('./data/country_data.csv')).bind(source='col_s', destination='col_d')
# g.plot()

# hg = graphistry.hypergraph(pd.read_csv('./data/country_data.csv'), ['name', 'latitude', 'longitude', 'pop2019', 'GrowthRate', 'area', 'Density'], direct=True)
# hg['graph'].plot()

# if dataset_name == 'Suside Statistics':
# 	links = pd.read_csv('./data/lesmiserables.csv')
# 	g = graphistry.bind(source="source", destination="target")
# 	links["label"] = links.value.map(lambda v: "#Meetings: %d" % v)
# 	g = g.bind(edge_title="label")
# 	g.edges(links).plot()

# g = graphistry.edges(pd.read_csv('./data/lesmiserables.csv')).bind(source='source', destination='target')
# g.plot()