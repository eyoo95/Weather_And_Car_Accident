import streamlit as st
from streamlit_option_menu import option_menu
from app_home import run_home
from app_eda import run_eda
from app_ml import run_ml
from PIL import Image

def main():
    st.title('기상정보를 통한 교통사고율 예측 앱')
    with st.sidebar:
        st.image('https://media.istockphoto.com/vectors/protecting-car-vector-id1001190124?k=20&m=1001190124&s=612x612&w=0&h=UrLRro8ea7uQyV2BdO-ikWnChKT-JGaCEtDTgUejhVY=')
        menu = option_menu('Menu',['Home','EDA','ML'], icons = ['house-door-fill','bar-chart-line-fill','gear-wide-connected'],menu_icon="caret-down-fill", default_index=0,
                         styles={
        "container": {"padding": "5!important", "background-color": "#fafafa"},
        "icon": {"color": "black", "font-size": "25px"}, 
        "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
        "nav-link-selected": {"background-color": "#198fc2"},
    })
    if menu == 'Home':
        run_home()
    elif menu == 'EDA':
        run_eda()
    elif menu == 'ML':
        pass # run_ml()


if __name__ == '__main__':
    main()