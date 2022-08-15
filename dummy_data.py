import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')


import django
django.setup()



from faker import Faker
import random
from products.models import Product, Brand, Category

def seed_brand(n):
    fake = Faker()

    for _ in range(n):
        name = fake.name()
        image = f"brand/({random.randint(1,10)}).jpg"

        Brand.objects.create(
            name=name,
            image=image
        )
    print(f"Seed {n} Brands")


def seed_category(n):
    fake = Faker()

    for _ in range(n):
        name = fake.name()
        image = f"category/({random.randint(1,10)}).jpg"

        Category.objects.create(
            name=name,
            image=image
        )

    print(f"Seed {n} Categories")


def seed_products(n):
    fake = Faker()

    flag_type = ['New', 'Feature']

    for _ in range(n):
        name = fake.name()
        sku = random.randint(1, 100000)
        brand = Brand.objects.get(id=random.randint(1, 20))
        price = round(random.uniform(20.99, 99.99), 2)
        desc = fake.text(max_nb_chars=1000)
        flag = random.choice(flag_type)
        category = Category.objects.get(id=random.randint(43, 62))
        image = f"product/({random.randint(1, 86)}).jpg"

        Product.objects.create(
            name=name,
            sku=sku,
            brand=brand,
            price=price,
            desc=desc,
            flag=flag,
            category=category,
            image=image
        )

    print(f"Seed {n} products")


#seed_brand(20)
#seed_category(20)
seed_products(1000)
