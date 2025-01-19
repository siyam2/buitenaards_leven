import streamlit as st
import math

# Zet de instellingen voor de pagina
st.set_page_config(
    page_title="Zoeken naar buitenaards leven 🌌", 
    page_icon="🌌", 
    initial_sidebar_state="collapsed",  # De zijbalk is standaard gesloten
)

st.markdown("""
    <style>
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .css-1j4l4p8 {visibility: hidden;}  # Verbergt de 'Made with Streamlit' text
    .css-1l7k7sb {visibility: hidden;}  # Verbergt de Streamlit logo en tekst onderaan
    </style>
""", unsafe_allow_html=True)



# Titel en introductie
st.title("Zoeken naar buitenaards leven 🌌")

# Tabbladen voor uitleg en simulatie
tab1, tab2, tab3 = st.tabs(["Drake Uitleg", "Sterren en Leven Simulator", "Atmosferische Data en Leven"])

# Tab 1: Uitleg van de Drake-vergelijking en invullen van de vergelijking
with tab1:
    st.title("De Drake Vergelijking: Zoeken naar buitenaards leven!")
    st.write(
        """
        Eerst gaan wij kijken naar de bekende Drake Equation. Deze vergelijking staat
        bekend om een waarde te geven aan de kans op communicatief leven te vinden in
        onze melkweg. De vergelijking ziet er zo uit:
        """
    )

    # Weergave van de Drake Vergelijking
    st.latex(r"""
        N = R^* \cdot f_p \cdot n_e \cdot f_l \cdot f_i \cdot f_c \cdot L
    """)

    st.write(
        """
        Waar:
        - **N**: Het aantal detecteerbare buitenaardse samenlevingen in de Melkweg. 🌌
        - **R***: Het aantal nieuwe sterren dat per jaar wordt gevormd. Wat voor onze Melkweg wordt geschat op 1 per jaar. 🌟
        - **fₚ**: Het percentage sterren met planeten. Waarvan er geschat wordt dat de helft van de sterren planeten hebben 🌍
        - **nₑ**: Het gemiddelde aantal planeten met vloeibaar water. Op dit moment hebben we onze zonnestelsel als enige concrete bewijs. Waar aarde de enigste is. Dus 1 💧
        - **fₗ**: Het percentage van die planeten waar leven ontstaat. 🌱
        - **fᵢ**: Het percentage van die planeten waar intelligent leven ontstaat. 🧠
        - **f꜀**: Het percentage van intelligente samenlevingen die signalen uitzenden. 📡
        - **L**: De gemiddelde tijdsduur dat een wezen signalen uitzendt (in jaren). ⏳
        """
    )

    # Waarde invullen voor de Drake Vergelijking met sliders
    st.header("Vul de waarden in om de kansen voor buitenaards leven te berekenen!")

    R_star = st.slider("Aantal nieuwe sterren per jaar (R*) 🌠", min_value=0.0, max_value=10.0, value=1.0, step=0.1)
    f_p = st.slider("Percentage sterren met planeten (fₚ) 🌍", min_value=0.0, max_value=1.0, value=0.5, step=0.01)
    n_e = st.slider("Aantal leefbare planeten per ster (nₑ) 🌱", min_value=0.0, max_value=5.0, value=1.0, step=0.1)
    f_l = st.slider("Percentage planeten waar leven ontstaat (fₗ) 💚", min_value=0.0, max_value=1.0, value=0.1, step=0.01)
    f_i = st.slider("Percentage planeten met intelligent leven (fᵢ) 🧠", min_value=0.0, max_value=1.0, value=0.01, step=0.01)
    f_c = st.slider("Percentage van beschavingen die signalen uitzenden (f꜀) 📡", min_value=0.0, max_value=1.0, value=0.1, step=0.01)
    L = st.slider("Levensduur van beschavingen in jaren (L) ⏳", min_value=0.0, max_value=10000.0, value=1000.0, step=100.0)

    # Berekeningen van de Drake Vergelijking
    N = R_star * f_p * n_e * f_l * f_i * f_c * L
    st.write(f"Het geschatte aantal buitenaardse samenlevingen in de melkweg is: {N:.0f} 👽")

# Tab 2: Sterren en Leven Simulator
with tab2:
    st.title("⭐ Sterren en Leven Simulator") 
    st.write(
    """
    de zone waarin het mogelijk is dat er vloeibaar water bestaat - hangt af van het type ster.  
     Op welke afstand leven mogelijk is, heet de GOLDILOCK zone.
    """
    )

    st.write(
        """
        Hier kun je ontdekken hoeveel de afstand tot een ster invloed heeft op de kansen voor leven.
        Kies het type ster en de afstand tot de ster, en ontdek of de planeet in de Goldilocks zone ligt! 🚀
        """
    )

    # Keuze voor stertype
    ster_type = st.selectbox(
        "Kies het type ster:",
        ("Zonachtige ster", "Rode dwergster", "Blauwe reus", "Witte dwerg")
    )

    # Bepalen van de Goldilocks zone afhankelijk van het stertype
    def goldilocks_zone(ster_type):
        """Retourneer de Goldilocks zone afhankelijk van het stertype"""
        if ster_type == "Zonachtige ster":
            return (0.95, 1.37)  # Afstand in AU (Astronomische Eenheden)
        elif ster_type == "Rode dwergster":
            return (0.1, 0.2)
        elif ster_type == "Blauwe reus":
            return (1.5, 2.5)
        elif ster_type == "Witte dwerg":
            return (0.02, 0.1)
        return (0, 0)

    # Verklaring van de Goldilocks zone voor geselecteerde ster
    goldilocks_min, goldilocks_max = goldilocks_zone(ster_type)
    st.write(f"De Goldilocks zone voor een {ster_type} ligt tussen {goldilocks_min:.2f} AU en {goldilocks_max:.2f} AU.")

    # Slider voor de afstand van de planeet tot de ster
    afstand = st.slider(
        "Wat is de afstand van de planeet tot de ster? (in AU)",
        min_value=0.01,
        max_value=10.0,
        value=1.0,
        step=0.01
    )

    # Bepalen of de planeet in de Goldilocks zone ligt
    in_goldilocks = goldilocks_min <= afstand <= goldilocks_max

    if in_goldilocks:
        st.success("De planeet ligt in de Goldilocks zone en heeft mogelijk de juiste omstandigheden voor leven! 💧🌱")
    else:
        st.warning("De planeet ligt niet in de Goldilocks zone en heeft mogelijk geen geschikte omstandigheden voor leven. ⚠️")

# Tab 3: Kans op Leven en Biologische Veranderingen op Andere Planeten
with tab3:
    st.title("🌍 Kans op Leven in het Heelal en Biologische Veranderingen")
    st.write(
        """
        De kans op leven buiten de Aarde hangt af van de atmosferische condities van andere planeten. 
        Dit tabblad onderzoekt de mogelijkheden voor leven in verschillende atmosferen en hoe organismen zich zouden kunnen 
        aanpassen aan die omstandigheden.
        """
    )

