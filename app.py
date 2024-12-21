import pandas as pd
import streamlit as st
import plotly.express as px

df = pd.read_csv('vehicles_us.csv')

st.header('market of Cars.Original data')
st.write("Use the filters below to view advertisements by model")



model_option = df['model'].unique()

selected_model = st.selectbox('Select a model', model_option )

min_year, max_year = int(df['model_year'].min()), int(df['model_year'].max())


time_period = st.slider("Select the year", value=(min_year, max_year), min_value=min_year,max_value=max_year)


actual_range = list(range(time_period[0], time_period[1]+1))



df_filtered = df[  (df.model == selected_model) & (df.model_year.isin(list(actual_range)) )]

df_filtered



st.header('Price Analysis')
st.write("""
###### Let's explore the key factors that impact price. We'll examine how price distribution changes based on transmission type, number of cylinders, and body style
""")

list_for_hist = ['transmission', 'cylinders', 'type']

specified_type = st.selectbox('Analysis of price distribution', list_for_hist)

fig1 = px.histogram(df, x="price",color = specified_type )
fig1.update_layout(title= "<b> Split of price by {}</b>".format(specified_type))
st.plotly_chart(fig1)


def age_category(x):
    if x<5: return '<5'
    elif x>=5 and x<10: return '5-10'
    elif x>=10 and x<11: return '10-11'
    else: return '>10'


df['age'] = 2020 - df['model_year']

df['age_category'] = df['age'].apply(age_category)

list_for_scatter = ['odometer', 'fuel', 'condition']

option_for_scatterplot = st.selectbox('Price determination based on', list_for_scatter)

fig2 = px.scatter(df, x="price", y=option_for_scatterplot, color = "age_category", hover_data= ['model_year'])
fig2.update_layout(title="<b> Price vs {}</b>".format(option_for_scatterplot))
st.plotly_chart(fig2)