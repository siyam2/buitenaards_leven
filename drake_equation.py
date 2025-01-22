import streamlit as st
import math
import os

# Fetch the GitHub token from Streamlit secrets
github_token = os.getenv("GITHUB_TOKEN")

# Use the token to construct the repository URL
repo_url = f"https://{github_token}@github.com/username/repository.git"

# Example usage in your app
print("Repository URL:", repo_url)



# Zet de instellingen voor de pagina
st.set_page_config(
    page_title="Zoeken naar buitenaards leven 🌌", 
    page_icon="🌌", 
    initial_sidebar_state="collapsed",  # De zijbalk is standaard gesloten
)
# Verberg de footer
st.markdown("""
    <style>
    footer {visibility: hidden;}
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

    # Afbeeldingen van sterren
    if ster_type == "Zonachtige ster":
        st.image("zon.jpeg", caption="Zonachtige Ster 🌞", use_column_width=True)
    elif ster_type == "Rode dwergster":
        st.image("rode_dwergster.svg", caption="Rode Dwergster 🔴", use_column_width=True)
    elif ster_type == "Blauwe reus":
        st.image("blauwe_reus.png", caption="Blauwe Reus 🔵", use_column_width=True)
    elif ster_type == "Witte dwerg":
        st.image("witte_dwerg_ster.jpg", caption="Witte Dwerg ⚪", use_column_width=True)

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

    # Berekeningen van de temperatuur op basis van afstand
    def temperatuur(afstand, ster_type):
        """Bereken de temperatuur van de planeet op basis van de afstand tot de ster"""
        if ster_type == "Zonachtige ster":
            temperatuur_schaal = 280  # Gemiddelde temperatuur van een Zonachtige ster in Kelvin
        elif ster_type == "Rode dwergster":
            temperatuur_schaal = 220
        elif ster_type == "Blauwe reus":
            temperatuur_schaal = 300
        elif ster_type == "Witte dwerg":
            temperatuur_schaal = 400
        else:
            temperatuur_schaal = 280

        # De formule voor de efficiënte temperatuur (de oppervlaktetemperatuur van de planeet)
        temp = temperatuur_schaal * (1 / math.sqrt(afstand)) ** 0.5
        return temp

    # Bereken de temperatuur
    temp_planet = temperatuur(afstand, ster_type)

    st.write(f"De geschatte temperatuur van de planeet is {temp_planet:.2f} K.")

    # Bepaal of de temperatuur geschikt is voor leven
    if 273 <= temp_planet <= 373:
        st.success("De temperatuur is geschikt voor vloeibaar water en mogelijk leven! 🌊💫")
    else:
        st.warning("De temperatuur ligt buiten het bereik voor vloeibaar water. Leven zoals wij dat kennen is onwaarschijnlijk. 🚫")

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

    # Zuurstofconcentratie (O₂) en kans op leven
    o2_concentratie = st.slider(
        "Zuurstofconcentratie (O₂) in de atmosfeer (%)", 
        min_value=0.0, max_value=100.0, value=21.0, step=0.1
    )
    st.write(f"De zuurstofconcentratie is {o2_concentratie:.1f}%.")

    if o2_concentratie < 10.0:
        st.warning(
            "Bij een zuurstofconcentratie onder 10% zou leven zich kunnen ontwikkelen, maar met andere metabole systemen dan op Aarde. Leven zou er dan anders uitzien dan op Aarde"
        )
    elif 10.0 <= o2_concentratie < 21.0:
        st.info(
            "Dit zuurstofconcentratie kan nog steeds een vorm van leven ondersteunen, maar het zou beperkter zijn in omvang en diversiteit. Organismen kunnen zich aanpassen door efficiënter zuurstof te gebruiken. Wat resulteert in kleinere organismes"
        )
    elif 21.0 <= o2_concentratie <= 40.0:
        st.success(
            "Deze concentratie ondersteunt de meeste levensvormen zoals op Aarde, maar kan in bepaalde omgevingen resulteren in grotere organismen met verhoogde metabolische snelheden."
        )
    else:
        st.error(
            "Bij zuurstofconcentraties boven 40% zou het leven waarschijnlijk instabiel zijn, gezien de verhoogde kans op oxidatie en verbranding."
        )

    # Kooldioxideconcentratie (CO₂) en kans op leven
    co2_concentratie = st.slider(
        "Kooldioxideconcentratie (CO₂) in de atmosfeer (%)", 
        min_value=0.0, max_value=10.0, value=0.04, step=0.01
    )
    st.write(f"De kooldioxideconcentratie is {co2_concentratie:.2f}%.")

    if co2_concentratie < 0.01:
        st.warning(
            "Zeer lage CO₂-niveaus kunnen fotosynthese verhinderen, wat levensprocessen zou beperken. Organismen zouden afhankelijkheid van chemische stoffen moeten zijn in plaats van zonne-energie."
        )
    elif 0.01 <= co2_concentratie < 1.0:
        st.success(
            "Deze CO₂-concentraties zouden mogelijk leven ondersteunen."
        )
    elif 1.0 <= co2_concentratie <= 2.0:
        st.info(
            "Hogere CO₂-niveaus kunnen leiden tot een versterkt broeikaseffect, wat een warmer klimaat creëert. Dit kan leven ondersteunen, maar mogelijk ook verstoren afhankelijk van de stabiliteit van de atmosfeer."
        )
    else:
        st.error(
            "Extreem hoge CO₂-concentraties zouden een onleefbaar klimaat creëren door oververhitting en zuurvervuiling, wat organismen ernstig zou kunnen schaden."
        )

    # Stikstofconcentratie (N₂) en kans op leven
    n2_concentratie = st.slider(
        "Stikstofconcentratie (N₂) in de atmosfeer (%)", 
        min_value=0.0, max_value=100.0, value=78.0, step=0.1
    )
    st.write(f"De stikstofconcentratie is {n2_concentratie:.1f}%.")

    if n2_concentratie < 50.0:
        st.warning(
            "Stikstof is essentieel voor de opbouw van eiwitten en nucleïnezuren. Lage stikstofconcentraties zouden het moeilijk maken voor levensvormen om te groeien of zich voort te planten."
        )
    elif 50.0 <= n2_concentratie <= 90.0:
        st.success(
            "Dit is een ideale concentratie van stikstof voor de meeste levensvormen, die essentieel is voor de opbouw van biologisch materiaal."
        )
    else:
        st.info(
            "Extreem hoge stikstofconcentraties zouden mogelijk geen invloed hebben op de biologie van eenvoudige organismen, maar kunnen de atmosfeer instabiel maken."
        )

    # Methaanconcentratie (CH₄) en kans op leven
    ch4_concentratie = st.slider(
        "Methaanconcentratie (CH₄) in de atmosfeer (%)", 
        min_value=0.0, max_value=5.0, value=0.0002, step=0.0001
    )
    st.write(f"De methaanconcentratie is {ch4_concentratie:.4f}%.")

    if ch4_concentratie < 0.01:
        st.info(
            "lage niveaus zouden geen dramatische impact hebben op het potentieel voor leven, maar micro-organismen kunnen methaan gebruiken als energiebron."
        )
    elif 0.01 <= ch4_concentratie <= 1.0:
        st.success(
            "Methaan kan wijzen op een actieve chemische cyclus die leven ondersteunt, vooral in omgevingen zonder zuurstof. Dit is waar gezocht kan worden naar samenlevingen op afstand met telescopen"
        )
    else:
        st.error(
            "Hoge methaanniveaus zouden de planeet onleefbaar maken door oververhitting, wat de levensomstandigheden zou verstoren."
        )

    # Waterstofconcentratie (H₂) en kans op leven
    h2_concentratie = st.slider(
        "Waterstofconcentratie (H₂) in de atmosfeer (%)", 
        min_value=0.0, max_value=10.0, value=0.5, step=0.1
    )
    st.write(f"De waterstofconcentratie is {h2_concentratie:.1f}%.")

    if h2_concentratie < 2.0:
        st.success(
            "Waterstof kan een belangrijke energiebron zijn voor anaerobe organismen die leven onder extreme omstandigheden."
        )
    elif 2.0 <= h2_concentratie <= 5.0:
        st.warning(
            "Hogere waterstofconcentraties kunnen een gasrijke atmosfeer creëren die de ontwikkeling van complexe levensvormen remt, maar mogelijk geschikt is voor eenvoudige organismen."
        )
    else:
        st.error(
            "Extreem hoge waterstofniveaus kunnen leiden tot instabiliteit in de atmosfeer, wat de mogelijkheid voor leven zou verminderen."
        )

    # Totale atmosferische samenstelling en kans op leven
    totaal_concentratie = o2_concentratie + co2_concentratie + n2_concentratie + ch4_concentratie + h2_concentratie
    st.write(f"Totale atmosferische concentratie: {totaal_concentratie:.1f}%.")

    if totaal_concentratie > 100.0:
        st.error("De totale atmosferische concentratie overschrijdt 100%, wat fysiek onmogelijk is.")
    elif totaal_concentratie < 100.0:
        st.warning("De totale atmosferische concentratie is lager dan 100%, wat betekent dat er mogelijk onbekende gassen aanwezig zijn die invloed hebben op het leven.")
    else:
        st.success("De totale atmosferische concentratie is precies 100%, wat fysiek plausibel is voor een leefbare atmosfeer.")
