Relations
on_delete : - CASCADE - SET_NULL - Protect - Set default

---

null : db
blank : form

---

Signal : 2 events related
5 types : - Pre init save - Post init save - m2m_changed

            Pre-init
            Pre-save

---

Aggregaion & Annotaion:
------
from django.db.models.aggregates import Count, Max, Min, Sum, Avg
from django.db import F, Value
from django.db.models.functions import Concat
from django.db.models import CharField
------

    Product.objects.aggregate(Sum('price'), Avg('price'))
    Product.objects.aggregate(mysum = Sum('price'))


    Product.objects.annonate(price_tax=F(price)*0.8)
    Product.objects.annonate(
        full_name = Concat('name', 'sku', output_field=CharField())
        )

---

-login_required:
-orders
-add to favorties

<!-- orders(statuschoices = in progress) -->

-Auto calculate price-order detail
----------------------------------------------------------------------------

Translations:
-------------

django-admin makemessages -l ar





