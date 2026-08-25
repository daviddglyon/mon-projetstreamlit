import streamlit as st
import pandas as pd

df = pd.read_csv("Data\\Taxis.csv")

# 1. Affichez un titre personnalisé avec votre prénom : "Dashboard Analyse Taxis -[Votre Prénom]"
st.title("Dashboard Analyse Taxis - Groupe Mouna et Davit")

# 2. Ajoutez un menu déroulant (st.selectbox) permettant à l'utilisateur de choisir un quartier de prise en charge (pickup_borough).
choix_outil = st.selectbox(
 "Un quartier de prise en charge  :",
 df["pickup_borough"].dropna().unique()
)


# Filtrez le dataframe Pandas en fonction de l'arrondissement choisi et affichez les 5 premières lignes du tableau filtré avec st.dataframe().
#st.write(f"Vous avez choisi : **{choix_outil}**")
df_filter = df.loc[df["pickup_borough"] == choix_outil]
st.write(df_filter.head(5) )



# Affichez une métrique (st.metric) indiquant le nombre total de courses enregistrées dans cet arrondissement.
vc = df_filter.shape[0]
# st.write(vc)
st.metric("nombre total de courses dans cet arrondissement", value= vc)