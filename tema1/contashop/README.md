# ContaShop – Magazin de Servicii Contabile

Aplicație web de tip e-commerce pentru achiziționarea de servicii contabile, construită cu Flask + Jinja2 + Bootstrap 5.

## Tehnologii folosite

- **Python / Flask** – server-side routing și logică
- **Jinja2** – template engine (integrat cu Flask), evitând codul duplicat
- **Bootstrap 5** + **Bootstrap Icons** – design responsive
- **CSS custom** – personalizare peste Bootstrap
- **Sesiuni Flask** – persistența coșului de cumpărături între refresh-uri
- **JSON** – salvarea comenzilor pe server

## Rulare locală

```bash
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
python3 server.py
```

Aplicația va fi disponibilă la: http://localhost:5000

## Rulare cu Docker

```bash
docker build -t iap1-tema ./
docker run -p 5000:5000 -it iap1-tema
```

## Structura proiectului

```
contashop/
├── server.py           # Entrypoint Flask, toate rutele
├── products.py         # Datele produselor (separate de logică)
├── requirements.txt
├── Dockerfile
├── README.md
├── submitted-orders/   # Comenzi salvate (JSON, create automat)
├── templates/
│   ├── base.html       # Template de bază (navbar, footer)
│   ├── index.html      # Pagina principală – catalog servicii
│   ├── cart.html       # Coș de cumpărături
│   ├── checkout.html   # Formular comandă
│   ├── order_success.html  # Confirmare comandă
│   └── contact.html    # Pagina de contact
└── static/
    ├── css/style.css   # Stiluri custom
    └── img/            # SVG-uri pentru produse
```

## Rute implementate

| Rută | Metodă | Descriere |
|------|--------|-----------|
| `/` | GET | Pagina principală cu catalog |
| `/cart` | GET | Coș cumpărături |
| `/cart/add-item?id=X` | GET | Adaugă produs în coș |
| `/cart/remove-item?id=X` | GET | Șterge produs din coș |
| `/checkout` | GET | Formular finalizare comandă |
| `/checkout` | POST | Procesare comandă |
| `/contact` | GET | Pagina de contact |

## Funcționalități

- Catalog cu 8 servicii contabile, randate dinamic din `products.py`
- Coș persistent în sesiunea browser-ului (supraviețuiește refresh-ului)
- Badge-uri pentru servicii speciale (Popular, Premium, Enterprise)
- Checkout cu validare câmpuri și 3 metode de plată
- Comenzile se salvează în `submitted-orders/` ca fișiere JSON cu timestamp
- Comenzile se printează și în consolă Flask (pentru debugging)
- Design responsiv, navbar cu counter coș, pagini de succes și contact

## Bonusuri implementate

- Design personalizat cu temă contabilitate (culori, iconuri, hero section)
- SVG-uri custom pentru fiecare produs
- Animație pe pagina de succes a comenzii
- Pagina de contact cu formular și date firmă fictive
- Salvare comenzi în format JSON structurat cu timestamp în nume fișier
- Footer complet cu link-uri

## Note implementare

Produsele sunt stocate în `products.py` ca listă de dicționare — separat față de logica Flask din `server.py`, conform bunelor practici și cerințelor de la punctajul pentru cod lizibil.

Sesiunile Flask folosesc cookies semnate criptografic pentru a stoca coșul, asigurând persistența fără a necesita o bază de date.
