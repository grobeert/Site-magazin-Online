from flask import Flask, render_template, redirect, url_for, request, session
from products import PRODUCTS, get_product_by_id
import json
import os
from datetime import datetime

app = Flask(__name__)
app.secret_key = "contashop-secret-key-2024"

ORDERS_DIR = "submitted-orders"
os.makedirs(ORDERS_DIR, exist_ok=True)


def get_cart():
    return session.get("cart", {})


def save_cart(cart):
    session["cart"] = cart


def cart_total_items():
    cart = get_cart()
    return sum(item["quantity"] for item in cart.values())


def cart_total_price():
    cart = get_cart()
    total = 0.0
    for item in cart.values():
        total += item["price"] * item["quantity"]
    return round(total, 2)


def get_cart_items(): 
    cart = get_cart()
    items = []
    for pid, item in cart.items():
        items.append({
            "id": pid,
            "name": item["name"],
            "price": item["price"],
            "quantity": item["quantity"],
            "subtotal": round(item["price"] * item["quantity"], 2),
        })
    return items


@app.context_processor
def inject_cart_count():
    return {"cart_count": cart_total_items()}


@app.route("/")
def index():
    return render_template("index.html", products=PRODUCTS)


@app.route("/cart")
def cart():
    items = get_cart_items()
    total = cart_total_price()
    return render_template("cart.html", items=items, total=total)


@app.route("/cart/add-item")
def cart_add_item():
    product_id = request.args.get("id")
    if not product_id:
        return redirect(url_for("index"))

    product = get_product_by_id(product_id)
    if not product:
        return redirect(url_for("index"))

    cart = get_cart()
    pid = str(product_id)
    if pid in cart:
        cart[pid]["quantity"] += 1
    else:
        cart[pid] = {
            "name": product["name"],
            "price": product["price"],
            "quantity": 1,
        }
    save_cart(cart)

    referer = request.referrer or url_for("index")
    return redirect(referer)


@app.route("/cart/remove-item")
def cart_remove_item():
    product_id = str(request.args.get("id", ""))
    cart = get_cart()
    if product_id in cart:
        del cart[product_id]
        save_cart(cart)
    return redirect(url_for("cart"))


@app.route("/checkout", methods=["GET", "POST"])
def checkout():
    items = get_cart_items()
    total = cart_total_price()

    if request.method == "POST":
        full_name = request.form.get("full_name", "")
        email = request.form.get("email", "")
        phone = request.form.get("phone", "")
        address = request.form.get("address", "")
        payment_method = request.form.get("payment_method", "")

        order_data = {
            "timestamp": datetime.now().isoformat(),
            "customer": {
                "full_name": full_name,
                "email": email,
                "phone": phone,
                "address": address,
                "payment_method": payment_method,
            },
            "items": items,
            "total": total,
        }

        print("\n========== COMANDĂ NOUĂ ==========")
        print(f"Data: {order_data['timestamp']}")
        print(f"Client: {full_name} | {email} | {phone}")
        print(f"Adresă: {address}")
        print(f"Plată: {payment_method}")
        print("Servicii comandate:")
        for item in items:
            print(f"  - {item['name']} x{item['quantity']} = {item['subtotal']} RON")
        print(f"TOTAL: {total} RON")
        print("===================================\n")

        filename = datetime.now().strftime("%Y%m%d_%H%M%S") + f"_{full_name.replace(' ', '_')}.json"
        filepath = os.path.join(ORDERS_DIR, filename)
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(order_data, f, ensure_ascii=False, indent=2)

        session.pop("cart", None)

        return render_template("order_success.html", order=order_data)

    if not items:
        return redirect(url_for("index"))

    return render_template("checkout.html", items=items, total=total)


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
