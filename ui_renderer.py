
import streamlit as st

def display_insight_cards(insights):
    for idx, card in enumerate(insights, 1):
        with st.expander(f"🧩 Theme {idx}: {card['theme']} ({card['sentiment']})"):
            for quote in card['quotes']:
                st.markdown(f"- {quote}")
