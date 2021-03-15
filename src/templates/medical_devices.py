"""This page is for searching and viewing the list of awesome resources"""
import logging

import streamlit as st
import pandas as pd
import graphistry

import awesome_streamlit as ast
from awesome_streamlit.core.services import resources

import matplotlib.pyplot as plt
import pyTigerGraphBeta as tg

import seaborn as sns
import re
from random import random
from PIL import Image
import plotly.express as px

sns.set(style="ticks")
sns.set(rc={'figure.figsize':(15,10)})

logging.basicConfig(format="%(asctime)s - %(message)s", level=logging.INFO)


graphistry.register(api=3, protocol="https", server="hub.graphistry.com", username="landry", password="istanbul.1957")


conn = tg.TigerGraphConnection(host="https://tggraph.i.tgcloud.io", graphname="tggraphhack", apiToken="c8l0pe58m15he0v8t6q9p709oh598is4")

authToken = conn.getToken("en84d51mdrapbb6b5b6h83q0mrijubst", "100000000000000000")

aaa=""

@st.cache(suppress_st_warning=True)
def get_vision_markdown():
    global aaa
    aaa="# aaaaaaaaazzzaaaaaaa"

countries = [random()]
datasource = [random()]
daviceclassification = [random()]
devices = [random()]
devicesncount = [random()]
manufactures = [random()]
devicesbycountry = [random()]

@st.cache(suppress_st_warning=True)
def getcountries():
    global countries
    countries = conn.runInstalledQuery("getcountries") 
    countries = countries[0]['@@country']
    for c in countries:
        if (re.search('[a-zA-Z]', c) == None) or (re.search('""', c)!= None):
            countries.remove(c)

@st.cache(suppress_st_warning=True)
def getcountriesfreq():
    global devicesbycountry
    devicesbycountry = []
    dev = conn.runInstalledQuery("getcountriesfreq") 
    dev = dev[0]['@@country']
    for i in dev:
        if {"country": i, "number": dev.count(i)} not in devicesbycountry:
            devicesbycountry.append({"country": i, "number": dev.count(i)})
    devicesbycountry = pd.DataFrame(devicesbycountry)


@st.cache(suppress_st_warning=True)
def getdatasource():
    global datasource
    datasource = conn.runInstalledQuery("getdatasource") 
    datasource = datasource[0]['@@manufacture']
    for d in datasource:
        if (re.search('[a-zA-Z]', d) == None) or (re.search('""', d)!= None):
            datasource.remove(d)

@st.cache(suppress_st_warning=True)
def getclassifications():
    global daviceclassification
    daviceclassification = conn.runInstalledQuery("getclassifications") 
    daviceclassification = daviceclassification[0]['@@dvc']
    for d in daviceclassification:
        if (re.search('[a-zA-Z]', d) == None) or (re.search('""', d)!= None):
            daviceclassification.remove(d)

@st.cache(suppress_st_warning=True)
def getdevicesbycountry(country):
    global devices
    devices = conn.runInstalledQuery("getdevicesbycountry", {"country": country})
    devices = devices[0]['res']
    for i in range(len(devices)):
        devices[i] = devices[i]["attributes"]
    devices = pd.DataFrame(devices)

@st.cache(suppress_st_warning=True)
def getmanufanddevices():
    global manufactures
    manufactures = conn.runInstalledQuery("getmanufanddevices")
    manufactures = pd.DataFrame(manufactures[0]['@@res'])
    # for i in range(len(devices)):
    #     devices[i] = devices[i]["attributes"]

@st.cache(suppress_st_warning=True)
def getmanufanddevicesbycountry(country):
    global manufactures
    manufactures = conn.runInstalledQuery("getmanufanddevices", {"country": country})
    manufactures = pd.DataFrame(manufactures[0]['@@res'])


@st.cache(suppress_st_warning=True)
def getdevicesandcountries():
    global devicesncount
    devicesncount = conn.runInstalledQuery("getdevicesandcountries")
    devicesncount = devicesncount[0]['res']
    for i in range(len(devicesncount)):
        devicesncount[i] = devicesncount[i]["attributes"]
    devicesncount = pd.DataFrame(devicesncount)
    # st.write(devicesncount)


def write():
    getcountries()

    st.markdown('<h2 style="text-align: center; font-family: cursive; color: rgb(255, 127, 39)"><b>Data Visualization</b></h3>', unsafe_allow_html=True)
    st.sidebar.markdown('<h2 style="margin-top: 20px; font-family: cursive; color: rgb(255, 127, 39)"><b>Options</b></h3>', unsafe_allow_html=True)

    st.info(
            """Please be patient when you select an option. It can be slow because of the **large amount of data!**"""
        )

    country = st.sidebar.selectbox('Select The country.', ["All"] + countries)



    if (country == 'All'):
        overview = st.sidebar.selectbox('Select an option.', ["Overview", "Specific"])
        if overview == "Overview":
            st.markdown('''<p style="color: #d9534f">
                            This data represents the the <b>countries</b>,  <b>manufactures</b> and the <b>devices</b>. It is showing the global description of some dataset I made while testing.
                            </p>
                            <p>
                                I am sure you want to test it yourself.
                            </p>
                            <p><b>Please Select the criretias on the navigation bar to get specific data, visualize the data and enjoy the app.</b></p>
                        ''', unsafe_allow_html=True)
            st.markdown('''
                <p> Here is an example of visualisation we got from our test </p>
                
            ''', unsafe_allow_html=True)
            image = Image.open("./src/img/14.PNG")
            st.image(image, use_column_width=True)
            st.markdown('''</p><hr style="border:1px solid black">''', unsafe_allow_html=True)
        
        
        # st.sidebar.markdown('<br>', unsafe_allow_html=True)
        else:

            if st.checkbox('Compare the devices supply between countries'):
                st.markdown('''<p>This data represents the compareson of the number of medical devices provided to countries</p>''', unsafe_allow_html=True)
                getcountriesfreq()
                # devicesbycountry.drop([''])
                devicesbycountr = devicesbycountry[devicesbycountry.country != '']
                st.write(devicesbycountr)
                sns.relplot(x="country", y="number", data=devicesbycountr)
                st.pyplot()

            if st.sidebar.checkbox('Show manufacturers and devices'):
                st.markdown('''
                        <h3><b>Manufacturers and devices</b></h3>
                        <p>
                            The following dataset show the different manufacturers and all the devices they provide. Using it, we will be able to explore a graphistry clearly showing the all the devices linked to the manufacturers who supply them
                        </p>
                    ''', unsafe_allow_html=True)
                st.markdown('''
                        <h3 style="color: blue"><b>Dataset description</b></h3>
                    ''', unsafe_allow_html=True)
                getmanufanddevices()
                st.write(manufactures)
                numeric_columns = manufactures.select_dtypes(['float64', 'float32', 'int32', 'int64']).columns
                st.markdown('''<h3 style="font-family: cursive; color: #f0ad4e"><b>Histogram</b></h3> 
                    <p style="background-color: black; color: white; padding: 30px; border-radius: 8px">
                        The following diagram presents the density of manufacturers or devices. Means that we can visualize the manufacturers that provide more the devices and the most provided devices 
                    </p>''', 
                    unsafe_allow_html=True
                )
                st.markdown('''
                        <p style="color: #f0ad4e"><b>Click on "Show manufactures and their devices in graphistry" to open graphistry</b></p>
                    ''', unsafe_allow_html=True)
                select_box3 = st.selectbox(label="Chose the variable you want to visualize", options=numeric_columns)
                histogram_slider = st.slider(label="Number of Bins",min_value=5, max_value=10000, value=30)
                sns.distplot(manufactures[select_box3], bins=histogram_slider)
                st.pyplot()

                if st.checkbox('Show manufactures and their devices in graphistry'):
                    g = graphistry.bind(source="manufacturer_id", destination="divid")
                    g.edges(manufactures).plot()


            if st.sidebar.checkbox('Show countries and devices'):
                st.markdown('''
                        <h3><b>Countries provided</b></h3>
                        <p>
                            Here we show the different countries and all the devices provided to them. Using it, we will be able to explore a graphistry clearly showing the devices linked to the countries supplied to them
                        </p>
                    ''', unsafe_allow_html=True)
                st.markdown('''
                        <h3 style="color: blue"><b>Dataset description for Countries and Devices</b></h3>
                    ''', unsafe_allow_html=True)
                getdevicesandcountries()
                st.write(devicesncount)
                numeric_columns = devicesncount.select_dtypes(['float64', 'float32', 'int32', 'int64']).columns
                st.sidebar.markdown('<br>', unsafe_allow_html=True)
                st.markdown('''<h3 style="font-family: cursive; color: #5cb85c"><b>Graph</b></h3> 
                    <p style="background-color: #5cb85c; color: white; padding: 30px; border-radius: 8px">
                        The following diagram presents the density of manufacturers, devices, countries... Meaning that we can visualize the entities that intervene the more in the system
                    </p>''', 
                    unsafe_allow_html=True
                )
                st.markdown('''
                        <p style="color: #d9534f"><b>Click on "Show manufactures and their devices in graphistry" to open graphistry</b></p>
                    ''', unsafe_allow_html=True)
                select_box3 = st.selectbox(label="Chose the variable you want to visualize", options=numeric_columns)
                histogram_slider = st.slider(label="Nbr of Bins",min_value=5, max_value=10000, value=30)
                sns.distplot(devicesncount[select_box3], bins=histogram_slider)
                st.pyplot()

                if st.checkbox('Show devices and their devices in graphistry'):
                    g = graphistry.bind(source="divid", destination="country")
                    g.edges(devicesncount).plot()


    else:
        getdevicesbycountry(country)
        getdatasource()
        getclassifications()
        device = st.sidebar.selectbox('Select the Data by : ', ["All", "Source", "Device Classification"])
        # dataset_name = st.sidebar.selectbox('Select The Device Classification', ["All"] + daviceclassification)
        
        if device == "All":
            st.markdown('''
                        <h3><b>Countries and providers</b></h3>
                        <p>
                            This dataset shows us the country you selected with all the manufacturers that provides them with the devices
                        </p>
                    ''', unsafe_allow_html=True)
            st.markdown('''
                        <h3 style="color: blue"><b>Dataset description for single Country and device providers</b></h3>
                    ''', unsafe_allow_html=True)
            st.write(devices)
            if st.checkbox('Show in graphistry'):
                # g = graphistry.edges(devices).bind(source='country', destination='divid')
                # g.plot()
                # hg = graphistry.hypergraph(devices, ['country', 'divid', 'name'], direct=True)
                # hg['graph'].plot()
                # import cudf
                g = graphistry.edges(devices).bind(source='country', destination='manufacturer_id')
                g.plot()

        elif device == "Source":
            st.markdown('''
                        <h3><b>Countries and devices depending on the device sources</b></h3>
                        <p>
                            There, we show the countries with all the devices they are provided with, depending on the source of the equipments
                        </p>
                    ''', unsafe_allow_html=True)
            st.markdown('''
                        <p style="color: #d9534f"><b>Please check on Show interactions between countries and device providers in graphistry" checkbox to open graphistry and explore the interactions</b></p>
                    ''', unsafe_allow_html=True)
            st.markdown('''
                        <h3 style="color: blue"><b>Dataset description </b></h3>
                    ''', unsafe_allow_html=True)
            getmanufanddevices()
            st.write(manufactures)
            
            if st.checkbox('Show interactions between countries and device providers in graphistry'):
                g = graphistry.edges(manufactures).bind(source='source', destination='divid')
                g.plot()

        else:
            st.markdown('''
                        <h3><b>Countries and devices depending on the device Classification</b></h3>
                        <p>
                            There, we show the countries with all the devices they are provided with, depending on the classification of the equipments
                        </p>
                    ''', unsafe_allow_html=True)
            st.markdown('''
                        <p style="color: #5cb85c"><b>Please check on "Show the data with graphistry" checkbox to open graphistry and explore the interactions</b></p>
                    ''', unsafe_allow_html=True)
            st.markdown('''
                        <h3 style="color: #d9534f"><b>Dataset description </b></h3>
                    ''', unsafe_allow_html=True)
            getmanufanddevicesbycountry(country)
            st.write(manufactures)
            # state_total_graph = px.bar(
            # manufactures, 
            # x='Status',
            # y='Number of cases',
            # labels={'Number of cases':'Number of cases in '},
            # color='Status')
            # st.plotly_chart(state_total_graph)

            if st.checkbox('Show the data with graphistry '):
                # g = graphistry.edges(manufactures).bind(source='classification', destination='divid')
                hg = graphistry.hypergraph(devices, ['classification', 'divid', 'manufacturer_id'], direct=True)
                hg['graph'].plot()
                # g.plot()




if __name__ == "__main__":
    write()