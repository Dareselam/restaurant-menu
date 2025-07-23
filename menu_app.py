import streamlit as st

st.set_page_config(page_title="Il Ristorantino Italiano", page_icon="🍝", layout="centered")
st.title("Il Ristorantino Italiano 🍷🇮🇹")
st.subheader("Authentic Italian Cuisine, Beverages & Craft Beer Menu")

# General function to render any menu section
def render_menu(menu):
    for item, details in menu.items():
        st.write(f"{item}** - {details['price']}")
        if 'description' in details:
            st.caption(details['description'])

# Antipasti
st.header("🥖 Antipasti")
antipasti_menu = {
    "Tagliere di Salumi e Formaggi": {"price": "€14", "description": "Cuts Meat and Cheeses"},
    "Polpo all'Aglio": {"price": "€18", "description": "Octopus in Garlic"},
    "Impepata di Cozze": {"price": "€14", "description": "Mussels Sauté"},
    "Sauté di Cozze e Vongole": {"price": "€18", "description": "Mussels and Clams Sauté"},
    "Bruschetta di Bufala": {"price": "€8", "description": "Bruschetta with Bufala"}
}

# Pasta
st.header("🍝 Pasta")
pasta_menu = {
    "Linguine allo Scoglio": {"price": "€18", "description": "SEA FOOD"},
    "Linguine Lipari": {"price": "€18", "description": "Swordfish, whole black olives, capers and cherry tomatoes"},
    "Linguine Pesce Spade": {"price": "€18", "description": "Swordfish, pistachio"}
}

# Risotti
st.header("🍚 Risotti")
risotti_menu = {
    "Risotto ai Frutti di Mare": {"price": "€18", "description": "SEA FOOD"},
    "Risotto con Manzo e Funghi e Crema di Tartufo": {"price": "€15", "description": "Beef, mushrooms and truffle cream"},
    "Risotto Salmone ed Asparagi": {"price": "€15", "description": "Salmon and asparagus"}
}

# Pesce
st.header("🐟 Pesce")
pesce_menu = {
    "Grigliata Michelangelo": {"price": "€20.95", "description": "Grilled Mix Fish"},
    "Orata alla Griglia": {"price": "€17.95", "description": "Grilled Sea Bream"},
    "Orata alla Mediterranea": {"price": "€18.95", "description": "Grilled Sea Bream Whole"},
    "Filetto di Branzino": {"price": "€18.95", "description": "Black Sea Bass Fillet"},
    "Filetto di Branzino alla Mediterranea": {"price": "€18.95", "description": "Black Sea Bass Whole"},
    "Filetto di Branzino alla Griglia": {"price": "€18.95", "description": "Black Sea Bass Fillet"},
    "Gamberoni Reali Speziati": {"price": "€16.95", "description": "Grilled King Prawns Flavoring"},
    "Salmone al Cartoccio": {"price": "€18.95", "description": "Baked Salmon"},
    "Pesce Spada alla Sarmoriglio": {"price": "€16.95", "description": "Grilled Swordfish"},
    "Frittura Mista": {"price": "€20.95", "description": "Mixed Fried Sea Food"}
}

# Spirits
st.header("🥃 Spirits")
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

# Drinks
st.header("🥤 Drinks")
drinks_menu = {
    "Soft Drinks (0.33 ltr)": {"price": "€2.5"},
    "Still/Sparkling Water (0.75 ltr)": {"price": "€3.5"},
    "Orange/Apple Juice": {"price": "€3"}
}

# Beers
st.header("🍺 Beers")
beers_menu = {
    "Cisk (0.5 ltr)": {"price": "€3.5"},
    "Ichnusa non filtrata (0.33 ltr)": {"price": "€5"}
}

# Cane Nero Craft Beers
st.header("🍻 Cane Nero Brewery - Toscana")
cane_nero_beers = {
    "CAUTHA": {"price": "€5", "description": "Alc. 5.0% • Plato 12.3"},
    "NETHUNS": {"price": "€5", "description": "Alc. 7.3% • Plato 16.2"},
    "MARIA": {"price": "€5", "description": "Alc. 5.2% • Plato 13.0"},
    "IPA": {"price": "€5", "description": "Alc. 5.5% • Plato 13.5"},
    "GALATEA": {"price": "€8", "description": "Alc. 6.5% • Plato 14.5"}
}

# Render everything
render_menu(antipasti_menu)
render_menu(pasta_menu)
render_menu(risotti_menu)
render_menu(pesce_menu)
render_menu(spirits_menu)
render_menu(drinks_menu)
render_menu(beers_menu)
render_menu(cane_nero_beers)

# Brewery info (optional)
st.markdown("""
📍 Produced by Cane Nero Brewery - Via I Maggio, 249, Badia Agnano, Bucine, Arezzo, Tuscany  
🌐 [birracanenero.it](http://www.birracanenero.it)  
📱 Instagram / Facebook: @birrificiocanenero
""")

# Final note
st.markdown("💬 All main courses will be served with mixed salad.")