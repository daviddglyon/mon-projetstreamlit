import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
st.title("  Dashboard de Data Visualisation dynamique")
# 1. Sélection du jeu de données
dataset_name = "flights"

# Chargement dynamique
@st.cache_data
def get_dataset(name):
    return pd.read_csv(f"https://raw.githubusercontent.com/mwaskom/seaborn-data/refs/heads/master/{ name }.csv")
df = get_dataset(dataset_name)

#3. Permettez à l'utilisateur de :
# Filtrer les données sur une plage d'années à l'aide d'un st.slider (ex: entre 1949 et 1960).
annees = st.slider("plage d'années", min_value=1949, max_value=1960, step=1)
# Choisir un mois spécifique via un st.selectbox ou sélectionner tous les mois.
mois = st.selectbox("mois: ", ("January","February","March","April","May", "June","July","August","September","October","November","December"))
st.write(mois)

#4. Affichez :

## Un indicateur st.metric montrant le nombre total de passagers sur la période sélectionnée.
sel_data = df.loc[(df["year"]==annees) & (df["month"]==mois)]
passangers = st.metric(label="le nombre total de passagers sur la période sélectionnée", value=sel_data["passengers"])

## Un graphique évolutif en lignes (st.line_chart ou Plotly) du nombre de passagers au fil des mois/années.
passagers_annee= df.loc[(df["year"]==annees)]
st.line_chart(passagers_annee["passengers"])

st.divider()

## Une case à cocher (st.checkbox) qui, lorsqu'elle est activée, affiche la Heatmap Seaborn montrant la répartition des passagers par année et par mois (utilisez df.pivot(index='month', columns='year', values='passengers')).
import plotly.express as px
import seaborn as sns
if st.checkbox("heatmap") :
    pivot_df = df.pivot(index='month', columns='year', values='passengers')
    num_cols = pivot_df.select_dtypes(include=['float64','int64']).columns.tolist()

    st.subheader("corrélation")
    corr = pivot_df[num_cols].corr()

    fig_corr, ax_corr = plt.subplots(figsize=(6, 4))
    
    sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f",ax=ax_corr)
    st.pyplot(fig_corr)
