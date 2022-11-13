#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#!/usr/bin/env python
# coding: utf-8

#st.set_page_config(page_title="Dashboard Noah en Julius", layout = "wide", initial_sidebar_state="expanded")

# In[43]:


#!pip install streamlit


# In[44]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import geopandas as gpd
import plotly.express as px
import streamlit as st
import folium


st.set_page_config(page_title="Dashboard Noah en Julius", layout = "wide", initial_sidebar_state="expanded")

# In[3]:


unemp = pd.read_csv('unemployment analysis.csv')


# In[4]:


unemp1 = pd.read_csv('unemployment analysis.csv')


# In[5]:


unemp_long= pd.melt(unemp, id_vars=['Country Name','Country Code'], var_name="Year", value_name= 'Unemployment Rate')
#unemp_long


# In[6]:


unemp_long['Unemployment Rate'].hist() #de data betreft een rechts-scheve (positief-scheve) verdeling.


# In[7]:


unemp.drop(columns = ['Country Code'], inplace = True)
unemp.set_index('Country Name', inplace = True)


# In[8]:


df1 = unemp.T
#df1


# In[9]:


fig = px.line(df1[['Africa Eastern and Southern', 'Africa Western and Central',"Middle East & North Africa", 'Central Europe and the Baltics',
                    "Europe & Central Asia",
                    'East Asia & Pacific', "Latin America & Caribbean", 'United States', 'Australia']])
#fig1 = fig.history(period= 'Year', start='1991' , end='2021')


# In[10]:


highun=df1.mean(axis=0).nlargest(10)
#highun


# In[11]:


df3 = {'Lesotho':30.396452 , 'North Macedonia':29.789677 , 'South Africa':28.232581 , 'Djibouti':27.733226, 
       'Eswatini':24.391290, 'Bosnia and Herzegocina':24.044516, 'Montenegro':23.048387, 'Namibia':21.033548, 
       'Cong, Rep.':20.291613, 'Botswana':19.814839}


# In[12]:


courses = list(df3.keys())
values = list(df3.values())
  
fig1 = plt.figure(figsize = (12, 6))
 
# creating the bar plot
plt.bar(courses, values, color ='r',
        width = 0.4)
 
plt.xticks(rotation = 45) 
plt.ylabel("% Unemployed")
plt.title("Highest Unemployed Countries")
plt.show()


# In[13]:


lowun=df1.mean(axis=0).nsmallest(10)
#lowun


# In[14]:


df5 = {'Qatar':0.569355, 'Cambodia':0.767419, 'Myanmar':0.916774, 'Rwanda':0.916774, 
       'Chad':0.950000, 'Bahrain':1.164839, 'Thailand':1.315806, 'benin':1.346452, 
       'Solomon Islands':1.370645, 'Niger':1.376452}


# In[15]:


courses = list(df5.keys())
values = list(df5.values())
  
fig3 = plt.figure(figsize = (10, 5))
 
# creating the bar plot
plt.bar(courses, values, color ='r',
        width = 0.4)
 
plt.xticks(rotation = 45) 
plt.ylabel("% Unemployed")
plt.title("Highest Unemployed Countries")
plt.show()


# In[16]:


#gk = unemp_long.groupby('Year')
#gk.get_group('1991')


# In[17]:


#fig4 = plt.scatter(x="Year", y="Unemployment Rate", data=unemp_long)
#plt.title("Unemployment Rate", size=20, color="red")
#plt.xlabel("Year")
#plt.xticks(rotation = 90) 
#plt.ylabel("Unemployment Rate")
#plt.show()


# In[20]:


#import geopandas as gpd
#import matplotlib.pyplot as plt
#import folium


countries = gpd.read_file('countries.geojson')

dfn = countries.merge(unemp_long, left_on='ISO_A3', right_on='Country Code',how='right')

m = folium.Map(location=[0,0], zoom_start=1, zoom_control=False, tiles='Cartodb Positron')
folium.Choropleth(geo_data = countries,
                 name = 'geometry',
                 data = dfn,
                 columns = ['ADMIN', 'Unemployment Rate'],
                 key_on = 'feature.properties.ADMIN',
                 fill_color = 'RdGy',
                 fill_opacity=0.5,
                 line_opacity=0.2,
                 zoom_on_click=True,
                 legend_name = 'unemployment rate per country').add_to(m)

m


#plt.title('Unemployment rate per country')
#plt.show()


# In[24]:


happiness= pd.read_csv('world-happiness-report-2021.csv')
#happiness


# In[27]:


unemp_2021 =unemp1[['Country Name','2021']] # we willen alleen de unemployment data van 2021
unemp_2021.rename(columns = {'2021'  : 'unemployment_rate'}, inplace=True) #hernamen van de kolom


# In[48]:


happiness['Country Name'] = happiness['Country name']
happiness_merge = happiness.merge(unemp_2021, on='Country Name',how='left')
# happiness_merge


# In[32]:


happiness_merge.dropna(inplace=True)
# happiness_merge['unemployment_rate'].unique()
# print(happiness_merge['unemployment_rate'].values)


happiness_merge['unemployment_rate']= np.array([ 7.53,  4.8,  5.32,  5.4,  4.01,  4.99,  8.66,  5.23,  4.12,
        6.3,  5.11,  5.05,  3.54,  7.51,  6.63, 17.95,  4.53,  2.89,
        5.46,  6.42,  8.06,  1.87,  3.5 , 0,  3.36,  7.36, 14.73,  9.83,
        4.42,  3.57, 10.45,  3.62, 14.4 ,  4.38,  9.18,  7.9 ,  6.13,
        6.33, 12.09,  7.16,  9.13,  3.37,  4.9,  5.17,  3.71, 11.81,
        5.94,  7.41,  7.6 , 14.34, 4.12,  1.42,  5.96,  2.8 , 10.9 ,  6.65,
        8.51,  8.68,  2.41,  4.83, 15.22,  3.96,  6.43, 14.8, 8.51,  7.08,
        7.21, 18.49,  8.5 ,  4.74,  7.75,  2.17, 19.58,  4.61,  4.41,
        4.82, 20.9 , 5.05,  5.42,  6.08,  6.58,  3.87,  3.72, 11.82, 16.2,
        4.7,  0.75,  5.08,  1.57,  6.34, 33.56,  4.35, 11.47, 10.66,
       12.7,  8.88, 14.19, 22.26,  4.76,  0.61,  3.98,  9.79,  7.72,
        2.94,  4.09,  5.74, 16.82, 14.49, 21.68, 2.17, 19.25,  1.88,  5.39,
        9.45,  3.69, 11.46,  2.59,  4.0  , 13.03,  5.33,  5.98,  1.79,
        2.65, 15.73,  7.02, 24.6 , 24.72,  1.61, 5.17, 13.28])

happiness_merge= happiness_merge[['Country name','Country Name','Regional indicator','unemployment_rate','Healthy life expectancy',
                                  'Freedom to make life choices','Generosity','Perceptions of corruption','Logged GDP per capita','Social support' ]]

# In[33]:


#import statsmodels.api as sm
#x = happiness_merge["Freedom to make life choices"]
#y = happiness_merge["unemployment_rate"]


# model = sm.OLS(y, x).fit()

#import statsmodels.formula.api as smf
#model = smf.ols(formula = "x ~ y", data=happiness_merge)
#model = model.fit()

#predictions = model.predict() 

#dfn2= model.summary()
#dfn2


# In[34]:


# Create a new figure, fig
# dfn3 = plt.figure()

#sns.regplot(x=x,
#            y=y,
#            data=happiness_merge,
#            dropna = True,
#            ci=60)
# Add a scatter plot layer to the regplot
#sns.scatterplot(x=x,
#            y=y,
#            data=happiness_merge,
#            color= 'red')
# Show the layered plot
#plt.show()


# In[45]:


#st.set_page_config(page_title="Dashboard Noah en Julius", layout = "wide", initial_sidebar_state="expanded")


# In[46]:


st.title('Dashboard employment worldwide')


# In[47]:


st.sidebar.title('Navigatie')


# In[41]:


pages = st.sidebar.radio('paginas', options=['Home','Datasets', 'Visualisaties', 'Einde'])

if pages == 'Home':
    st.markdown("Welkom op het dashboard van Noah Wijnheijmer en Julius Slobbe. Samen hebben wij gekozen om de dataset 'unemployment analysis' te kiezen, dit hebben wij gedaan omdat het ten eerste ons een leuke dataset leek en ten tweede omdat wij vonden dat er goed gewerkt kon worden met deze data set.")
    st.markdown("Gebruik de knoppen in de sidebar om tussen de verschillende paginas te navigeren. ")
elif pages == 'Datasets':
    st.subheader('Gebruikte Datasets.')
    st.markdown("Hieronder wordt de dataset met data over het gebruik van de unemployment weergegeven.")
    st.dataframe(data=unemp_long, use_container_width=False)
    st.subheader('Dataset van de wereldwijde happiness.')
    st.markdown("Deze dataset gebruiken wij om te vergelijken op land code, wat de correlatie is tussen de unemployment rate en de happiness rate in een land. deze data sets zijn samengevoegd door de 'Country Name', te mergen.")
    st.dataframe(data=happiness_merge, use_container_width=False)
elif pages == 'Visualisaties':
    st.subheader("Hier worden de visualisaties weergegeven die wij hebben opgesteld.")
    st.markdown("Hieronder wordt een grafiek weergegeven met data wereldwijd over de unemployment rate.")
    st.plotly_chart(fig, use_container_width=True)
    st.markdown("Hieronder wordt een barplot weergegeven met een overzicht van de 10 hoogste unemployment rate landen wereldwijd.")
    st.pyplot(fig1) 
    st.markdown("Hieronder wordt een grafiek weergegeven met een overzicht van de 10 laagste unemployment rate landen wereldwijd.")
    st.pyplot(fig3), folium_static(m)
elif pages == 'Einde':
    st.markdown('Bedankt voor het bezoeken.')
    st.markdown('Noah Wijnheimer, Julius Slobbe')

