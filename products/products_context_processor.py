from .models import Brand, Category


def get_brands(request):
    brands = Brand.objects.all()
    categories = Category.objects.all()

    return {'brand_info': brands, 'category_info':categories}



def get_favorites():
    pass