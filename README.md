<h1>streamlit Data Analysis Application with Tigergraph, graphistry </h1
<br>

<h1 style="font-family: cursive; color: rgb(255, 127, 39)"><b><i>INTRODUCTION</i></b></h1>
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

<h3><b>Video Demo </b></h3>

[![IMAGE ALT TEXT HERE](https://raw.githubusercontent.com/landry95/TigerGraph-Streamli-Graphistry-WebApp/main/src/img/12.PNG)](https://www.youtube.com/watch?v=ilUijXK0Qc8)



<h1> To run the application </h1>
<p>Follow the steps below : </p>

<ol>
	<li>
		Clone this project
	</li><br>
	<li>
		install python : <br> <a href="https://www.python.org/downloads/" target="blank">See here</a>
	</li><br>
	<li>
		install python virtual environment in the project location: <br> pip install virtualenv 
	</li><br>
	<li>
		Activate the virtual envirenment: <br> venv/bin/activate.bat
	</li><br>
	<li>
		Install the requirements: <br> pip install -r requirements.txt
	</li><br>
	<li>
		Lunch the application: <br> streamlit run tigergraph.py
	</li><br>
  	<li>
		Copy the link it generates from your console and past it in your navigator
	</li><br>
</ol>



<h1 style="font-family: cursive; color: rgb(255, 127, 39)"><b><i>About</i></b></h1>
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


<h1><b><i>GALLERY</i></b></h1>
<div>
	<div style="padding-bottom: 25px; border-bottom: 1px solid black">
		<img src="./src/img/schema.PNG">
		<small>Shemas from TigerGraph</small>
	</div>
	<h1></h1>
	<div>
		<img src="./src/img/graph_explorer.PNG">
		<small>Graph Explorer from TigerGraph cloud</small>
	</div>
	<div>
		<img src="./src/img/map_data.PNG">
		<small>Data maping  from TigerGraph cloud</small>
	</div>
	<div>
		<img src="./src/img/example_querry.PNG">
		<small>Query example from TigerGraph cloud</small>
	</div>
	<div>
		<img src="./src/img/graphistory.PNG">
		<small>Graphistory platform</small>
	</div>
</div>