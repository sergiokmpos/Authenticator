import streamlit as st
import streamlit_authenticator as stauth

import yaml
from yaml.loader import SafeLoader


idiomas = ['Português', 'Inglês', 'Español']

# Using object notation
idioma = st.sidebar.selectbox(
    "'🗺️ Idioma/Language'",
    ('Português', 'Inglês', 'Español')
)

#idioma = st.selectbox('🗺️ Idioma/Language', idiomas)


# Cria o widget de redefinição de senha

if idioma == 'Português':
    campos_login = { 'Form name': 'Iniciar Seção','Username': 'Usuário','Password': 'Senha','Login': 'Entrar' }

elif idioma == 'Inglês':
    campos_login = { 'Form name': 'Login','Username': 'User','Password': 'Password','Login': 'Login' }

else :
    campos_login = { 'Form name': 'Iniciar sesión','Username': 'Usuario','Password': 'Contraseña','Login': 'Ingresar' }



with open('config.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)

authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['preauthorized']
)


authenticator.login(fields = campos_login)

if st.session_state["authentication_status"]:
    authenticator.logout()
    st.write(f'Seja bem vindo *{st.session_state["name"]}*')
    st.title('Pagina Inicial')
elif st.session_state["authentication_status"] is False:
    st.error('Usuario ou senha incorreto')
elif st.session_state["authentication_status"] is None:
    st.warning('Please enter your username and password')



# Using "with" notation
with st.sidebar:
    add_radio = st.radio(
        "Choose a shipping method",
        ("Standard (5-15 days)", "Express (2-5 days)")
    )