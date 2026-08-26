# Mettez en place la page de connexion obligatoire tant que l'utilisateur n'est pas identifié.
import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu
import matplotlib.pyplot as plt

# --- 1. INITIALISATION DE LA SESSION ---
if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False
if "username" not in st.session_state:
    st.session_state["username"] = ""
# --- 2. FONCTION DE VÉRIFICATION DES IDENTIFIANTS ---
@st.cache_data
def load_accounts():
    return pd.read_csv("accounts.csv")
def authenticate(username_input, password_input):
    accounts_df = load_accounts()
    # Verification de la correspondance nom d'utilisateur et mot de  passe
    user_match = accounts_df[(accounts_df["name"] == username_input) & (accounts_df["password"] == password_input)]
    return not user_match.empty
# --- 3. GESTION DE L'AFFICHAGE CONDITIONNEL ---
if not st.session_state["logged_in"]:
    # --- PAGE DE CONNEXION ---
    st.title(" Connexion à l'Application Data")
    st.subheader("Veuillez vous identifier pour accéder au contenu")

    username_input = st.text_input("Nom d'utilisateur")
    password_input = st.text_input("Mot de passe", type="password")

    if st.button("Se connecter"):
        if authenticate(username_input, password_input):
            st.session_state["logged_in"] = True
            st.session_state["username"] = username_input
            st.success(f"Bienvenue {username_input} !")
            st.rerun() # Relance le script pour afficherl'application sécurisée
        else:
            st.error("Nom d'utilisateur ou mot de passe incorrect.")
else:
    # --- APPLICATION SÉCURISÉE (UTILISATEUR CONNECTÉ) ---

    # 1. Barre latérale : Message de bienvenue et bouton de déconnexion
    with st.sidebar:
        st.write(f" Bienvenue, **{st.session_state['username']}**!")
        if st.button("Se déconnecter"):
            st.session_state["logged_in"] = False
            st.session_state["username"] = ""
            st.rerun()
        st.divider()

    # 2. Barre latérale : Menu de navigation
    with st.sidebar:
        selected_page = option_menu(
            menu_title="Menu principal",
            options=["Accueil", "Dashboard", "Galerie Photos"],
            icons=["house", "images"],
            default_index=0
        )

    # 3. Contenu principal des pages
    if selected_page == "Accueil":
        st.title(" Page d'Accueil Réservée")
        st.write("Ce contenu est uniquement accessible aux utilisateurs authentifiés.")
        
    elif selected_page == "Dashboard":
        st.title("Dashboard Data Visualisation - Flights")

        ## includ dashboard start________________________________________

        # 1. Sélection du jeu de données
        dataset_name = "flights"

        # Chargement dynamique
        @st.cache_data
        def get_dataset(name):
            return pd.read_csv(f"https://raw.githubusercontent.com/mwaskom/seaborn-data/refs/heads/master/{ name }.csv")
        df = get_dataset(dataset_name)

        st.subheader("Aperçu des données")
        st.dataframe(df.head(10))
        ordre_mois = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
        annee_min, annee_max = st.slider(
            "Sélectionnez une plage d'années :",
            min_value=int(df["year"].min()),
            max_value=int(df["year"].max()),
            value=(1949, 1960)
        )

        mois_disponibles = ["Tous les mois"] + df["month"].unique().tolist()
        mois_choisi = st.selectbox("Choisissez un mois :", mois_disponibles)

        df_filtre = df[
            (df["year"] >= annee_min) & (df["year"] <= annee_max)
        ]
        if mois_choisi != "Tous les mois":
            df_filtre = df_filtre[df_filtre["month"] == mois_choisi]

        total_passagers = df_filtre["passengers"].sum()
        st.metric(label="Nombre total de passagers", value=f"{total_passagers:,}")

        st.subheader("Évolution du nombre de passagers")
        evolution = df_filtre.groupby("year")["passengers"].sum()
        evolution=evolution.reset_index()
        evolution["year"] = evolution["year"].astype(str)
        st.line_chart(evolution, x="year", y="passengers")

        st.divider()
 
        ## Une case à cocher (st.checkbox) qui, lorsqu'elle est activée, affiche la Heatmap Seaborn montrant la répartition des passagers par année et par mois (utilisez df.pivot(index='month', columns='year', values='passengers')).
        import plotly.express as px
        import seaborn as sns

        def heatmap(headertext, pivotdf, isannot):
            st.subheader(headertext)
            fig_corr, ax_corr = plt.subplots(figsize=(6, 4))
            sns.heatmap(pivotdf, annot=isannot, cmap="coolwarm", fmt=".2f",ax=ax_corr) # annot to False
            st.pyplot(fig_corr)

        pivot_df = df.pivot(index='month', columns='year', values='passengers')
        pivot_df = pivot_df.reindex(ordre_mois)  

        heatmap("Répartition des passagers par année et par mois", pivot_df, False)
        if st.checkbox("heatmap") :
            num_cols = pivot_df.select_dtypes(include=['int64']).columns.tolist()
            corr = pivot_df[num_cols].corr()
            heatmap("Correlation heatmap", corr, True)

        ## includ dashboard end________________________________________
    elif selected_page == "Galerie Photos":
        st.title(" Album Photos")
        st.write("Voici la galerie multimédia organisée sur 3 colonnes:")

        # Exemple d'affichage d'images alignées sur 3 colonnes
        cols = st.columns(3)
        sample_images = [
            "https://images.unsplash.com/photo-1436491865332-7a61a109cc05",
            "https://images.unsplash.com/photo-1569154941061-e231b4725ef1",
            "https://images.unsplash.com/photo-1544620347-c4fd4a3d5957"
        ]
        for idx, img_url in enumerate(sample_images):
            with cols[idx % 3]:
                st.image(img_url, caption=f"Image {idx+1}", use_container_width=True)



