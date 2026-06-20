# Shopping Cart – IAP Assignment

O aplicatie web simpla de e-commerce facuta cu Flask si Bootstrap. Utilizatorul poate naviga printr-un catalog de produse, sa adauge in cos si sa plaseze o comanda.

---

## Cum rulezi

**Cu Docker (recomandat):**
```bash
docker build -t iap1-tema ./
docker run -p 5000:5000 -it iap1-tema
```

**Fara Docker:**
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python3 server.py
```

Aplicatia porneste pe `http://localhost:5000`.

---

## Structura

```
.
├── server.py
├── products.py
├── requirements.txt
├── Dockerfile
├── submitted-orders/
├── templates/
│   ├── _base.html
│   ├── index.html
│   ├── cart.html
│   ├── checkout.html
│   └── contact.html
└── static/
    ├── style.css
    └── images/
```

---

## Ce face fiecare parte

**Pagina principala (`/`)** – produsele sunt incarcate din `products.py` si randate cu Jinja2. Fiecare card are poza, nume, pret si buton de adaugare in cos.

**Cosul (`/cart`)** – stocat in sesiunea Flask ca sa nu se piarda la refresh. Se poate adauga cu `/cart/add-item?id=X` si sterge cu `/cart/remove-item?id=X`.

**Checkout (`/checkout`)** – formular cu `full_name`, `email`, `phone`, `address`, `payment_method` (card / bank_transfer / cash). La submit, comanda se printeaza in consola si se salveaza ca JSON in `submitted-orders/`.

**Contact (`/contact`)** – pagina statica cu datele firmei.

---

## Cateva alegeri pe care le-am facut

Am tinut produsele intr-un fisier separat (`products.py`) ca sa nu fie amestecate cu logica serverului. Comenzile le salvez cu timestamp in nume ca sa nu se suprascrie. Toate paginile mostenesc acelasi `_base.html` cu navbar-ul si badge-ul de cos.

---

## Dependinte

```
Flask>=2.2.2
```

---
