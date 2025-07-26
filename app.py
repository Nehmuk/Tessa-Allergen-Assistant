import streamlit as st
import base64

st.set_page_config(page_title="Tessa – Allergy Safe Shopping", layout="wide")

def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

bg_image_base64 = get_base64_image("assets/header.png")

if "page" not in st.session_state:
    st.session_state.page = "home"
if "subcategory" not in st.session_state:
    st.session_state.subcategory = ""
if "show_subcategories" not in st.session_state:
    st.session_state.show_subcategories = False

def go_to_page(name):
    st.session_state.page = name
    st.session_state.subcategory = name
    st.session_state.show_subcategories = False

# ---------------------- Header ---------------------- #
st.markdown(f"""
    <style>
        .header {{
            margin-top: 0;
            height: 160px;
            background-image: url("data:image/png;base64,{bg_image_base64}");
            background-size: cover;
            background-position: center;
            border-radius: 12px;
            display: flex;
            align-items: center;
            justify-content: space-between;
            padding: 0 30px;
        }}
        .logo {{
            background: white;
            border-radius: 50%;
            width: 80px;
            height: 80px;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            font-family: Georgia;
        }}
        .logo-main {{ font-size: 18px; font-weight: bold; }}
        .logo-small {{ font-size: 10px; color: gray; }}
        h3, p {{ text-align: center; }}
    </style>
""", unsafe_allow_html=True)

st.markdown(f"""
<div class="header">
    <div class="logo">
        <div class="logo-small">THE</div>
        <div class="logo-main">Tessa</div>
        <div class="logo-small">SHOP</div>
    </div>
    <div style="text-align: center; width: 100%;">
        <div style="font-size: 50px; font-weight: bold; color: black;">Welcome to Tessa</div>
        <div style="font-size: 14px; color: black;">Your Allergy Safe Shopping Assistant</div>
    </div>
</div>
""", unsafe_allow_html=True)

# ---------------------- Home Page ---------------------- #
if st.session_state.page == "home":
    st.markdown("<p style='text-align:center; margin-top: 30px;'>Select a category below:</p>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)

    with col1:
        st.image("assets/grocery.png", width=180)
        if st.button("Select Grocery"):
            st.session_state.show_subcategories = True

    with col2:
        st.image("assets/pharmacy.png", width=180)
        st.button("Select Pharmacy", disabled=True)

    with col3:
        st.image("assets/fashion.png", width=180)
        st.button("Select Fashion", disabled=True)

    if st.session_state.show_subcategories:
        st.markdown("### Subcategories in Grocery")
        subcols = st.columns(4)

        with subcols[0]:
            st.image("assets/dairy.png", width=150)
            if st.button("Go to Dairy"):
                go_to_page("dairy")

        with subcols[1]:
            st.image("assets/frozen.png", width=150)
            if st.button("Go to Frozen"):
                go_to_page("frozen")

        with subcols[2]:
            st.image("assets/snacks.png", width=150)
            if st.button("Go to Snacks"):
                go_to_page("snacks")

        with subcols[3]:
            st.image("assets/beverages.png", width=150)
            if st.button("Go to Beverages"):
                go_to_page("beverages")

# ---------------------- Dairy Section ---------------------- #
elif st.session_state.page == "dairy":
    st.markdown("### 🥛 Products in Dairy")
    if st.button("🖙 Back to Home"):
        st.session_state.page = "home"

    left_col, right_col = st.columns([1, 3])
    dairy_allergies = ["Milk allergy", "Casein allergy", "Whey allergy"]
    dairy_products = [
        {"name": "Oreo Original Biscuits", "description": "Ingredients: Sugar, wheat flour, palm oil, cocoa, invert sugar syrup, salt, raising agents, soy lecithin, vanillin\n(Milk-free)", "allergens": ["Casein allergy", "Whey allergy"]},
        {"name": "Lay’s Classic Salted Chips", "description": "Ingredients: Potatoes, edible vegetable oil, iodized salt\n(Casein-free)", "allergens": ["Milk allergy", "Whey allergy"]},
        {"name": "Bournvita Biscuits", "description": "Ingredients: Wheat flour, sugar, edible vegetable oil, cocoa solids, raising agents, salt, emulsifiers, vitamins, minerals\n(Whey-free)", "allergens": ["Milk allergy", "Casein allergy"]},
        {"name": "Sunfeast Farmlite Digestive Biscuits (Milk-Free Variant)", "description": "Ingredients: Whole wheat flour, edible vegetable oil, sugar, wheat bran, salt, raising agents, emulsifiers, antioxidants\n✔️ Free from milk, casein, and whey proteins.", "allergens": []}
    ]

    with left_col:
        st.markdown("### 🧪 Filter by Dairy Allergies")
        selected_allergies = [a for a in dairy_allergies if st.checkbox(a)]

    with right_col:
        search_input = st.text_input("Search for a product...")

        filtered = dairy_products
        if selected_allergies:
            filtered = [p for p in filtered if all(a not in p["allergens"] for a in selected_allergies)]

        if search_input:
            filtered = [p for p in filtered if search_input.lower() in p["name"].lower()]

        if selected_allergies or search_input:
            if filtered:
                st.markdown(f"### 🥾 Showing {len(filtered)} product(s):")
                for product in filtered:
                    st.markdown(f"#### {product['name']}")
                    st.caption(product['description'])
            else:
                st.info("❌ No matching products found.")

# ---------------------- Frozen Section ---------------------- #
elif st.session_state.page == "frozen":
    st.markdown("### ❄️ Products in Frozen")
    if st.button("🖙 Back to Home"):
        st.session_state.page = "home"

    left_col, right_col = st.columns([1, 3])
    frozen_allergies = ["Egg Allergy", "Seafood Allergy (Fish & Shellfish)", "Peanut Allergy"]
    frozen_products = [
        {"name": "Frozen Whole Egg Liquid (1 L)", "description": "Ingredients: 100% whole egg (egg whites and yolks)", "allergens": ["Egg Allergy"]},
        {"name": "Frozen Peeled & Deveined Shrimp, 500 g", "description": "Ingredients: 100% shrimp.", "allergens": ["Seafood Allergy (Fish & Shellfish)"]},
        {"name": "Reese’s Breyers Frozen Peanut Butter Dessert, 48 oz", "description": "Ingredients: Milk, cream, whey, sugar, peanut butter swirl, chocolate base.", "allergens": ["Peanut Allergy"]}
    ]

    with left_col:
        st.markdown("### 🧪 Filter by Frozen Allergies")
        selected_allergies = [a for a in frozen_allergies if st.checkbox(a)]

    with right_col:
        search_input = st.text_input("Search for a product...")

        filtered = []
        if selected_allergies:
            for allergy in selected_allergies:
                for product in frozen_products:
                    if allergy in product["allergens"]:
                        filtered.append(product)

        if search_input:
            filtered = [p for p in filtered if search_input.lower() in p["name"].lower()]

        if selected_allergies or search_input:
            if filtered:
                st.markdown(f"### 🥾 Showing {len(filtered)} product(s):")
                for product in filtered:
                    st.markdown(f"#### {product['name']}")
                    st.caption(product['description'])
            else:
                st.info("❌ No matching products found.")

# ---------------------- Snacks Section ---------------------- #
elif st.session_state.page == "snacks":
    st.markdown("### 🍿 Products in Snacks")
    if st.button("🖙 Back to Home"):
        st.session_state.page = "home"

    left_col, right_col = st.columns([1, 3])
    snack_allergies = ["Gluten Allergy", "Nut Allergy", "Soy Allergy", "Dairy Allergy"]
    snack_products = [
        {"name": "Kind Dark Chocolate Nuts & Sea Salt Bar", "description": "Ingredients: Almonds, peanuts, chicory root fiber, honey, palm kernel oil, dark chocolate, sea salt\n(Gluten-Free | Contains Nuts, Dairy-Free, Soy-Free)", "allergens": ["Nut Allergy"]},
        {"name": "Glutino Pretzel Twists", "description": "Ingredients: Corn starch, potato starch, palm oil, sugar, salt, yeast, baking soda\n✔️ Nut-Free\n(Contains Gluten, Dairy-Free, Soy-Free)", "allergens": ["Gluten Allergy"]},
        {"name": "Enjoy Life Soft Baked Cookies – Chocolate Chip", "description": "Ingredients: Sorghum flour, brown rice flour, chocolate chips (dairy-free), cane sugar, palm oil, vanilla extract\n✔️ Dairy-Free\n(Gluten-Free, Nut-Free, Soy-Free)", "allergens": []},
        {"name": "Annie's Homegrown Cheddar Bunnies", "description": "Ingredients: Organic wheat flour, cheddar cheese, salt, baking soda, enzymes\n✔️ Soy-Free\n(Contains Gluten, Dairy, May Contain Nuts)", "allergens": ["Gluten Allergy", "Dairy Allergy", "Nut Allergy"]},
        {"name": "Fruit Bars (Apple + Mango)", "description": "Ingredients: Apples, mangoes\n✔️ Free from gluten, nuts, dairy, and soy", "allergens": []}
    ]

    with left_col:
        st.markdown("### 🧪 Filter by Snack Allergies")
        selected_allergies = [a for a in snack_allergies if st.checkbox(a, key=f"snack_{a}")]

    with right_col:
        search_input = st.text_input("Search for a product...", key="snack_search")

        filtered = snack_products
        if selected_allergies:
            filtered = [p for p in snack_products if not any(a in p["allergens"] for a in selected_allergies)]

        if search_input:
            filtered = [p for p in filtered if search_input.lower() in p["name"].lower()]

        if selected_allergies or search_input:
            if filtered:
                st.markdown(f"### 🥾 Showing {len(filtered)} product(s):")
                for product in filtered:
                    st.markdown(f"#### {product['name']}")
                    st.caption(product["description"])
            else:
                st.info("❌ No matching products found.")

# ---------------------- Beverages Section (NEW) ---------------------- #
elif st.session_state.page == "beverages":
    st.markdown("### 🧃 Products in Beverages")
    if st.button("🖙 Back to Home"):
        st.session_state.page = "home"

    left_col, right_col = st.columns([1, 3])
    beverage_allergies = ["Milk Allergy", "Soy Allergy", "Nut Allergy", "Gluten Allergy (Celiac Disease)"]
    beverage_products = [
        {"name": "Oatly Oat Milk", "description": "Ingredients: Water, oats, rapeseed oil, calcium carbonate, salt, vitamins (D2, B2, B12)\n✔️ Dairy-Free, Nut-Free, Soy-Free\n(Contains Gluten)", "allergens": ["Gluten Allergy (Celiac Disease)"]},
        {"name": "Redbridge Gluten-Free Beer", "description": "Ingredients: Sorghum, water, hops, yeast\n✔️ Gluten-Free", "allergens": ["Milk Allergy", "Soy Allergy", "Nut Allergy"]},
        {"name": "Rice Dream Rice Milk", "description": "Ingredients: Filtered water, partially milled brown rice, canola oil, sea salt, vitamin A palmitate, vitamin D2, vitamin B12\n✔️ Nut-Free, Dairy-Free, Soy-Free, Gluten-Free (when certified)", "allergens": []},
        {"name": "So Delicious Coconut Milk", "description": "Ingredients: Filtered water, coconut cream, calcium phosphate, guar gum, vitamin D2, vitamin B12\n✔️ Dairy-Free, Gluten-Free, Soy-Free\n(Check for nut cross-contamination)", "allergens": ["Nut Allergy"]},
        {"name": "Zico Coconut Water", "description": "Ingredients: 100% Coconut water (not from concentrate)\n✔️ Dairy-Free, Gluten-Free, Soy-Free, Nut-Free", "allergens": []}
    ]

    with left_col:
        st.markdown("### 🧪 Filter by Beverage Allergies")
        selected_allergies = [a for a in beverage_allergies if st.checkbox(a, key=f"bev_{a}")]

    with right_col:
        search_input = st.text_input("Search for a product...", key="bev_search")

        filtered = beverage_products
        if selected_allergies:
            filtered = [p for p in beverage_products if not any(a in p["allergens"] for a in selected_allergies)]

        if search_input:
            filtered = [p for p in filtered if search_input.lower() in p["name"].lower()]

        if selected_allergies or search_input:
            if filtered:
                st.markdown(f"### 🥾 Showing {len(filtered)} product(s):")
                for product in filtered:
                    st.markdown(f"#### {product['name']}")
                    st.caption(product["description"])
            else:
                st.info("❌ No matching products found.")

# ---------------------- Default ---------------------- #
else:
    st.markdown(f"### 🏍️ Products in {st.session_state.subcategory.capitalize()} (Coming Soon!)")
    if st.button("🖙 Back to Home"):
        st.session_state.page = "home"
