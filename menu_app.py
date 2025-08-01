import streamlit as st

st.set_page_config(page_title="Il Ristorantino Italiano", page_icon="🍝", layout="wide")

# Custom styled header
st.markdown("""
    <div style="background-color:#fff7f0;padding:40px 20px;border-radius:15px;margin-bottom:30px;">
        <h1 style="color:#b22222;text-align:center;font-family:'Georgia',serif;font-size:60px;">
            🍝 Il Ristorantino Italiano
        </h1>
        <h3 style="text-align:center;color:#555;font-family:'Verdana';">
            🇮🇹 Authentic Italian Cuisine • Fine Wines • Craft Beer 🍷
        </h3>
    </div>
""", unsafe_allow_html=True)

# --- Utility function ---
def render_menu_section(title, emoji, menu_dict):
    with st.expander(f"{emoji} {title}", expanded=True):
        st.markdown("<div style='margin-top:10px;'>", unsafe_allow_html=True)
        for item, details in menu_dict.items():
            st.markdown(f"""
                <div style='padding:10px 0; border-bottom:1px solid #eee;'>
                    <div style='display:flex; justify-content:space-between; align-items:center;'>
                        <div style='font-weight:bold; font-size:20px; color:#333;'>{item}</div>
                        <div style='font-size:18px; color:#b22222;'>{details['price']}</div>
                    </div>
                    <div style='color:#777; font-size:15px;'>{details.get('description', '')}</div>
                </div>
            """, unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

# --- Menu Data ---
antipasti_menu = {
    "Tagliere di Salumi e Formaggi": {"price": "€15", "description": "Cuts Meat and Cheeses"},
    "Polpo all'Aglio": {"price": "€18", "description": "Octopus in Garlic"},
    "Impepata di Cozze": {"price": "€16", "description": "Mussels Sauté"},
    "Sauté di Cozze e Vongole": {"price": "€18", "description": "Mussels and Clams Sauté"},
    "Bruschetta di Bufala": {"price": "€10", "description": "Bruschetta with Bufala"}
}

pasta_menu = {
    "Linguine allo Scoglio": {"price": "€18", "description": "Seafood linguine"},
    "Linguine Lipari": {"price": "€18", "description": "Swordfish, black olives, capers, cherry tomatoes"},
    "Linguine Pesce Spade": {"price": "€18", "description": "Swordfish and pistachio"}
}

risotti_menu = {
    "Risotto ai Frutti di Mare": {"price": "€18", "description": "Seafood risotto"},
    "Risotto Funghi e Crema di Tartufo": {"price": "€15", "description": "Beef, mushrooms & truffle cream"},
    "Risotto Salmone ed Asparagi": {"price": "€16", "description": "Salmon and asparagus"}
}

pesce_menu = {
    "Grigliata Michelangelo": {"price": "€29.50", "description": "Grilled mixed fish"},
    "Orata alla Griglia": {"price": "€17.50", "description": "Grilled sea bream"},
    "Orata alla Mediterranea": {"price": "€18.50", "description": "Whole grilled sea bream"},
    "Filetto di crata e vellutata di Asparagi": {"price": "€18.50", "description": "fillet sea-bream Asparagus velvet"},
    "Gamberoni Reali Speziati": {"price": "€18", "description": "Grilled king prawns Flavoring"},
    "Salmone al Cartoccio": {"price": "€18.50", "description": "Baked salmon"},
    "Pesce Spada alla Sarmoriglio": {"price": "€18", "description": "Grilled swordfish"},
    "Frittura Mista": {"price": "€20", "description": "Mixed fried seafood"}
}

spirits_menu = {
    "Jack Daniel's": {"price": "€5"},
    "J&B": {"price": "€5"},
    "Grappa Barricata Invecchiata": {"price": "€6"},
    "Absolut Vodka": {"price": "€5"},
    "Frangelico": {"price": "€5"},
    "Baileys": {"price": "€5"},
    "Black Label": {"price": "€5"},
    "Rum Captain Morgan": {"price": "€5"},
    "Jameson": {"price": "€5"}
}

drinks_menu = {
    "Soft Drinks (0.33 ltr)": {"price": "€2.5"},
    "Still/Sparkling Water (0.75 ltr)": {"price": "€3.5"},
    "Orange/Apple Juice": {"price": "€3"}
}

beers_menu = {
    "Cisk (0.5 ltr)": {"price": "€3.5"},
    "Ichnusa non filtrata (0.33 ltr)": {"price": "€5"}
}

cane_nero_beers = {
    "CAUTHA": {"price": "€5", "description": "Alc. 5.0% • Plato 12.3"},
    "NETHUNS": {"price": "€5", "description": "Alc. 7.3% • Plato 16.2"},
    "MARIA": {"price": "€5", "description": "Alc. 5.2% • Plato 13.0"},
    "IPA": {"price": "€5", "description": "Alc. 5.5% • Plato 13.5"},
    "GALATEA": {"price": "€8", "description": "Alc. 6.5% • Plato 14.5"}
}

# --- Render Menu ---
render_menu_section("Antipasti", "🥖", antipasti_menu)
render_menu_section("Pasta", "🍝", pasta_menu)
render_menu_section("Risotti", "🍚", risotti_menu)
render_menu_section("Pesce", "🐟", pesce_menu)

st.markdown("<hr>", unsafe_allow_html=True)

render_menu_section("Spirits", "🥃", spirits_menu)
render_menu_section("Drinks", "🥤", drinks_menu)
render_menu_section("Beers", "🍺", beers_menu)
render_menu_section("Cane Nero Craft Beers", "🍻", cane_nero_beers)

# --- Footer Info ---
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("""
    <div style="background-color:#f6f6f6; padding:15px; border-radius:10px;">
        <h4 style='margin-bottom:5px;'>🍺 Cane Nero Brewery</h4>
        <p style='margin:0;'>📍 <i>Via I Maggio, 249, Badia Agnano, Bucine, Arezzo, Tuscany</i></p>
        <p style='margin:0;'>🌐 <a href='http://www.birracanenero.it' target='_blank'>birracanenero.it</a></p>
        <p style='margin:0;'>📱 Instagram / Facebook: <b>@birrificiocanenero</b></p>
    </div>
""", unsafe_allow_html=True)

st.info("💬 All Fish main courses are served with mixed salad.")
