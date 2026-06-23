# E-Commerce

A simple e-commerce web application built with Django.

## Features

- Product catalog with categories
- Add to cart / remove from cart (session-based)
- PayPal checkout integration
- Order management via Django admin
- Responsive design

## Tech Stack

- **Backend:** Django 6.0
- **Database:** MySQL (Railway)
- **Payments:** PayPal (django-paypal)
- **Static Files:** WhiteNoise
- **Server:** Gunicorn

## Project Structure

```text
E-Commerce/
├── mystore/           # Django project settings
├── shop/              # Product catalog
├── cart/              # Shopping cart logic
├── payment/           # Payment processing
├── templates/         # HTML templates
├── static/            # CSS, JS, images
├── manage.py
├── requirements.txt


```

1.Installation

Clone the repository:

git clone https://github.com/manojpatra-dev1/E-Commerce.git
cd E-Commerce

2.Create and activate a virtual environment:
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate

3.Install dependencies:
pip install -r requirements.txt

4.Run migrations:
python manage.py migrate

6.Create a superuser (optional, for admin access):

python manage.py createsuperuser

7.Run the development server:

python manage.py runserver

Open http://127.0.0.1:8000/ in your browser.

Environment Variables
Create a .env file in the root directory and add:

SECRET_KEY=your-django-secret-key
DEBUG=True
DATABASE_URL=your-database-url
PAYPAL_RECEIVER_EMAIL=your-paypal-business-email
PAYPAL_TEST=True

Author
Manoj Patra
GitHub: @manojpatra-dev1
