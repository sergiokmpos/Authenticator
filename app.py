import streamlit as st
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader

with open('config.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)

authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['preauthorized']
)

authenticator.login()

if st.session_state["authentication_status"]:
    authenticator.logout()
    st.write(f'Bem Vindo *{st.session_state["name"]}*')
    st.title('Pagina Inicial')
elif st.session_state["authentication_status"] is False:
    st.error('Usuario/Senha está incorreto')
elif st.session_state["authentication_status"] is None:
    st.warning('Por favor, entre com seu suario e senha')


if st.session_state["authentication_status"]:
    try:
        if authenticator.reset_password(st.session_state["username"]):
            st.success('Password modified successfully')
    except Exception as e:
        st.error(e)


with open('config.yaml', 'w') as file:
    yaml.dump(config, file, default_flow_style=False)            

