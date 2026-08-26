import streamlit as st
import pandas as pd
# # Titre principal de la page
# st.title("Mon Premier Dashboard Streamlit ")
# # Texte de présentation
# st.write("Bienvenue sur cette application interactive dédiée à l'analyse de données.")

# # Hiérarchie des titres
# st.title("Titre Principal (H1)")
# st.header("Titre de Section (H2)")
# st.subheader("Sous-titre (H3)")
# # Texte simple et Markdown
# st.text("Ceci est un texte brut sans mise en forme.")
# st.markdown("On peut utiliser le **gras**, l' *italique* et du :rainbow:[texte en couleur].")
# # Affichage polyvalent avec st.write()
# st.write("`st.write()` est une fonction universelle : elle affiche du texte, des dataframes, des dicts ou des graphiques.")


# # A. Les Boutons et SélecteursPython 
# # Bouton simple
# if st.button("Cliquez ici"):
#  st.success("Bouton cliqué avec succès !")
# st.divider() # Ligne de séparation visuelle
# # Case à cocher (Checkbox)
# afficher_details = st.checkbox("Afficher plus d'informations")
# if afficher_details:
#  st.info("Voici des détails supplémentaires affichés dynamiquement.")
# # Bouton Radio (Choix unique)
# reponse = st.radio("Quel est votre niveau d'expérience en Python ?",
#  ["Débutant", "Intermédiaire", "Avancé"]
# )
# st.write(f"Niveau sélectionné : **{reponse}**")
# # Menu déroulant (Selectbox)
# choix_outil = st.selectbox(
#  "Choisissez votre outil de visualisation préféré :",
#  ["Seaborn", "Matplotlib", "Plotly", "Power BI"]
# )
# st.write(f"Vous avez choisi : **{choix_outil}**")
# # Liste à choix multiples (Multiselect)
# competences = st.multiselect(
#  "Sélectionnez vos compétences Data :",
#  ["Python", "SQL", "Pandas", "Machine Learning", "Git"],
#  default=["Python", "SQL"] # Valeurs sélectionnées par défaut
# )
# st.write("Compétences choisies :", competences)



# #B. Saisies de Texte et Numériques
# # Champ de texte monoligne
# nom_utilisateur = st.text_input("Saisissez votre prénom :",
# value="Alexandre")
# st.write(f"Bonjour **{nom_utilisateur}** !")
# # Champ de texte multiligne
# commentaire = st.text_area("Laissez une note ou un commentaire :")
# # Entrée numérique contrôlée

# age = st.number_input("Entrez votre âge :", min_value=18,
# max_value=100, value=25, step=1)
# # Curseur numérique (Slider)
# annee = st.slider("Sélectionnez l'année d'analyse :", min_value=2015,
# max_value=2026, value=2024)
# st.write(f"Année d'analyse fixée à : **{annee}**")

# 3. Application pratique : Logique conditionnelle sur la saisie utilisateur
st.subheader("Simulateur d'Objectifs Data Analyst")
# Récupération des entrées
tache_sql = st.checkbox("Maitriser les requêtes SQL complexes")
tache_pandas = st.checkbox("Nettoyer un jeu de données avec Pandas")
tache_streamlit = st.checkbox("Développer une application web Streamlit")
# Logique conditionnelle basée sur les variables
if tache_sql and tache_pandas and tache_streamlit:
 st.balloons() # Animation de ballons de célébration !
 st.success("Bravo ! Vous avez validé tous vos objectifs du module.")
elif tache_sql or tache_pandas or tache_streamlit:
 st.warning("Vous avancez bien ! Continuez vos efforts pour valider l'ensemble des tâches.")
else:
 st.info("Cochez les tâches réalisées au fur et à mesure de votre progression.")