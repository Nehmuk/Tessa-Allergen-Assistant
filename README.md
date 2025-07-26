#  Tessa – Allergy Safe Shopping Assistant

Tessa is an AI-powered shopping assistant designed to help users with food allergies make safe and confident product choices.

Built using **Python** and **Streamlit**, Tessa provides a clean, category-wise shopping experience with allergy filters and search functionality.

---

##  Features

-  Filter products by specific food allergies
-  Search products by name
-  Organized into categories: Grocery → Dairy, Snacks, Frozen, Beverages
-  Simple, responsive UI with smart recommendations
-  Visual product categories and allergen filtering

---

## Tech Stack

- **Frontend & UI:** Streamlit  
- **Language:** Python  
- **Encoding:** Base64 for background image display  
- **Assets Folder:** All images are stored in `assets/` folder

>  No external ML models are used in this version.

---

##  Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/tessa.git
cd tessa
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

> Only `streamlit` is required. `base64` is part of Python standard library.
### 3. Run the App
```bash
streamlit run app.py
```

---

##  Project Structure

```
tessa/
├── app.py
├── requirements.txt
├── README.md
├── assets/
│   ├── header.png
│   ├── grocery.png
│   ├── dairy.png
│   ├── frozen.png
│   ├── snacks.png
│   ├── beverages.png
│   ├── fashion.png
│   └── pharmacy.png
```

##  Developed by

**Neha Mukhopadhyay**   
[LinkedIn](https://www.linkedin.com/in/neha-mukhopadhyay-ba61272a3)

---

## License

This project is for academic and demo purposes. Contributions and feedback are welcome!
