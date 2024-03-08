import streamlit as st
import streamlit_authenticator as stauth
import json

import yaml
from yaml.loader import SafeLoader

# Carrega o arquivo JSON
with open("i18n.json", "r") as f:
    i18n = json.load(f)

idiomas = ['Português', 'Inglês', 'Español']

st.sidebar.image("images/logo-250-100-transparente.png")

# Using object notation
idioma = st.sidebar.selectbox(
    "'🗺️ Idioma/Language'",
    ('Português', 'Inglês', 'Español')
)

# Cria o widget de redefinição de senha

if idioma == 'Português':
    campos_login = { 'Form name': 'Iniciar Seção','Username': 'Usuário','Password': 'Senha','Login': 'Entrar' }
    idioma_i18 = "pt"

elif idioma == 'Inglês':
    campos_login = { 'Form name': 'Login','Username': 'User','Password': 'Password','Login': 'Login' }
    idioma_i18 = "en"

else :
    campos_login = { 'Form name': 'Iniciar sesión','Username': 'Usuario','Password': 'Contraseña','Login': 'Ingresar' }
    idioma_i18 = "es"


with open('config.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)

authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['preauthorized']
)

title = i18n ["title"].get(idioma_i18, "Translation not available")
subtitle = i18n ["subtitle"].get(idioma_i18, "Translation not available")

st.title(title)
st.subheader(subtitle)


authenticator.login(fields = campos_login)

if st.session_state["authentication_status"]:
    authenticator.logout()
    st.write(f'Seja bem vindo *{st.session_state["name"]}*')
    st.title('Pagina Inicial')
elif st.session_state["authentication_status"] is False:
    st.error('Usuario ou senha incorreto')
elif st.session_state["authentication_status"] is None:
    st.warning(i18n["Alerta_login"].get(idioma_i18, "Translation not available"))


# Using "with" notation
with st.sidebar:
    add_radio = st.radio(
        "Choose a shipping method",
        ("Standard (5-15 days)", "Express (2-5 days)")
    )


st.write("----")

footer = "Developed with Python 🐍"

st.markdown(footer, unsafe_allow_html=True)
