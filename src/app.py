import streamlit as st
import pandas as pd


def carrega_dados(caminho):
    dados = pd.read_csv(caminho)
    return dados


def main():

    st.title("Minha primeira aplicação <3 <3")

    obitos_2019 = carrega_dados("dados/obitos-2019.csv")
    st.dataframe(obitos_2019)


if __name__ == "__main__":
    main()
