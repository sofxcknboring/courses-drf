import stripe

from config.settings import STRIPE_API_KEY
from users.models import Payment

stripe.api_key = STRIPE_API_KEY


def create_stripe_price(amount, product_id):
    """
    Создаем цену в Stripe.
    """
    return stripe.Price.create(
        currency="RUB",
        unit_amount=amount * 100,
        product_data={"name": product_id},
    )

def create_stripe_product(prd: Payment):
    """Создаем продукт в Stripe"""
    product = prd.course if prd.course else prd.lesson
    stripe_product = stripe.Product.create(name=product)
    return stripe_product.get('id')

def create_stripe_session(price):
    """
    Создаем сессию на оплату в Stripe.
    """
    session = stripe.checkout.Session.create(
        success_url="http://127.0.0.1:8000/",
        line_items=[{"price": price.get("id"), "quantity": 1}],
        mode="payment",
    )
    return session.get("id"), session.get("url")