from .models import Brand


def get_brands(request):
    brands = Brand.objects.all()

    return {'brand_info': brands}



def get_favorites():
    pass