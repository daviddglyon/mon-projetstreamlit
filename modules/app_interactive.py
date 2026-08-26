import streamlit as st
import pandas as pd
# Chargement direct du dataset "flights" depuis GitHub
@st.cache_data
def load_data():
    url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/refs/heads/master/flights.csv"
    return pd.read_csv(url)
df_flights = load_data()

## 1. Charger et Manipuler des Données dans Streamlit
st.subheader("Aperçu des données")
st.dataframe(df_flights.head(10))
# Affichage de KPI
total_passengers = df_flights["passengers"].sum()
st.metric(label="Total de passagers historiques", value=f"{total_passengers:,}")

## 2. Intégrer des Visualisations : Les 3 Approches 
### Approche 1 : Les graphiques natifs Streamlit (st.*_chart)
# Préparation des données : évolution annuelle du total des passagers
annual_passengers = df_flights.groupby("year")["passengers"].sum()
st.subheader("Évolution du trafic aérien (Bar Chart natif)")
st.bar_chart(annual_passengers)
### Approche 2 : Matplotlib & Seaborn (st.pyplot) 
import matplotlib.pyplot as plt
import seaborn as sns
df_iris = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/refs/heads/master/iris.csv")
st.subheader("Distribution par espèce (Seaborn)")
   # 1. Création explicite de la figure
fig, ax = plt.subplots(figsize=(8, 4))
sns.barplot(data=df_iris, x="species", y="sepal_length", ax=ax, palette="viridis")
ax.set_title("Longueur moyenne des sépales par espèce")
   # 2. Rendu dans Streamlit
st.pyplot(fig)
# Approche 3 : Plotly pour des graphiques ultra-interactifs (st.plotly_chart) 
import plotly.express as px
fig_plotly =  px.scatter(
 df_iris,
 x="sepal_width",
 y="sepal_length",
 color="species",
 size="petal_length",
 hover_data=["petal_width"],
 title="Relation Sépale vs Pétale"
)
# Rendu dans Streamlit
st.plotly_chart(fig_plotly, use_container_width=True)
