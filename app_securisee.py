# Mettez en place la page de connexion obligatoire tant que l'utilisateur n'est pas identifié.
import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu
# --- 1. INITIALISATION DE LA SESSION ---
if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False
if "username" not in st.session_state:
    st.session_state["username"] = ""
# --- 2. FONCTION DE VÉRIFICATION DES IDENTIFIANTS ---
@st.cache_data
def load_accounts():
    return pd.read_csv("Data\\accounts.csv")
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
            options=["Accueil", "Galerie Photos"],
            icons=["house", "images"],
            default_index=0
        )

    # 3. Contenu principal des pages
    if selected_page == "Accueil":
        st.title(" Page d'Accueil Réservée")
        st.write("Ce contenu est uniquement accessible aux utilisateurs authentifiés.")
    elif selected_page == "Galerie Photos":
        st.title(" Album Photos")
        st.write("Voici la galerie multimédia organisée sur 3 colonnes:")

    # Exemple d'affichage d'images alignées sur 3 colonnes
    cols = st.columns(3)
    sample_images = [
        "https://static.streamlit.io/examples/cat.jpg",
        "https://static.streamlit.io/examples/dog.jpg",
        "https://static.streamlit.io/examples/owl.jpg"
    ]
    for idx, img_url in enumerate(sample_images):
        with cols[idx % 3]:
            st.image(img_url, caption=f"Image {idx+1}", use_container_width=True)



