PRODUCTS = [
    {
        "id": 1,
        "name": "Pachet Start-up",
        "description": "Ideal pentru firme nou-înființate. Include înregistrare contabilă lunară, declarații fiscale și consultanță inițială.",
        "price": 299.00,
        "image": "startup.svg",
        "badge": "Popular",
    },
    {
        "id": 2,
        "name": "Pachet IMM",
        "description": "Soluție completă pentru întreprinderi mici și mijlocii. Contabilitate lunară, salarii până la 10 angajați și raportări trimestriale.",
        "price": 599.00,
        "image": "imm.svg",
        "badge": None,
    },
    {
        "id": 3,
        "name": "Declarații Fiscale",
        "description": "Pregătirea și depunerea tuturor declarațiilor fiscale obligatorii: D100, D112, D300, D394 și altele.",
        "price": 149.00,
        "image": "declaratii.svg",
        "badge": None,
    },
    {
        "id": 4,
        "name": "Audit Financiar Anual",
        "description": "Audit complet al situațiilor financiare anuale, conform standardelor ISA. Raport detaliat și recomandări.",
        "price": 1299.00,
        "image": "audit.svg",
        "badge": "Premium",
    },
    {
        "id": 5,
        "name": "Administrare Salarii",
        "description": "Calcul salarii, generare fluturași, declarații REVISAL și gestiunea contractelor de muncă. Până la 25 angajați.",
        "price": 399.00,
        "image": "salarii.svg",
        "badge": None,
    },
    {
        "id": 6,
        "name": "Consultanță Fiscală",
        "description": "Sesiune de consultanță fiscală personalizată de 2 ore cu un expert contabil certificat CECCAR.",
        "price": 199.00,
        "image": "consultanta.svg",
        "badge": None,
    },
    {
        "id": 7,
        "name": "Recuperare TVA",
        "description": "Serviciu specializat de analiză și recuperare TVA de la bugetul de stat. Include documentație completă.",
        "price": 449.00,
        "image": "tva.svg",
        "badge": None,
    },
    {
        "id": 8,
        "name": "Pachet Corporate",
        "description": "Soluție enterprise pentru companii mari. Contabilitate, audit, salarii nelimitate, consultanță fiscală și juridică.",
        "price": 1999.00,
        "image": "corporate.svg",
        "badge": "Enterprise",
    },
]

def get_product_by_id(product_id):
    for p in PRODUCTS:
        if p["id"] == int(product_id):
            return p
    return None
