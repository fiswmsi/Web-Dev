from django.http import JsonResponse
from .models import Product, Category


def products_list(request):
    
    cat_id=request.GET.get('category',None)
    
    if cat_id:
        products = Product.objects.filter(category_id=cat_id)     
    
    products = Product.objects.all()
    
    data = []

    for product in products:
        data.append({
            'id': product.id,
            'name': product.name,
            'price': product.price,
            'description': product.description,
            'count': product.count,
            'is_active': product.is_active,
            'category': product.category.id,
            'category_name': product.category.name,
        })

    return JsonResponse(data, safe=False)


def product_detail(request, id):
    try:
        product = Product.objects.get(id=id)
        related_products = Product.objects.filter(category = product.category).exclude(id=id)
        
        product_data={
            'id': product.id,
            'name': product.name,
            'price': product.price,
            'description': product.description,
            'count': product.count,
            'is_active': product.is_active,
            'category': product.category.id,
        }
        
        related_data = []
        
        for related_product in related_products:
            related_data.append({
                'name': related_product.name,
                'id': related_product.id,
            })
            
        response_data={
            'product': product_data,
            'related_products':related_data
        }
        
        return JsonResponse(response_data)
    
    except Product.DoesNotExists:
        return JsonResponse({
            'status': 'error',
            'message': 'Product not found'
        })
        

def categories_list(request):
    categories = Category.objects.all()
    data = []

    for category in categories:
        data.append({
            'id': category.id,
            'name': category.name,
        })

    return JsonResponse(data, safe=False)


def category_detail(request, id):
    try:
        category = Category.objects.get(id=id)
        data = {
            'id': category.id,
            'name': category.name,
        }
        return JsonResponse(data)
    except Category.DoesNotExist:
        return JsonResponse({'error': 'Category not found'}, status=404)


def category_products(request, id):
    try:
        category = Category.objects.get(id=id)
        products = category.products.all()

        data = []
        for product in products:
            data.append({
                'id': product.id,
                'name': product.name,
                'price': product.price,
                'description': product.description,
                'count': product.count,
                'is_active': product.is_active,
                'category': product.category.id,
                'category_name': product.category.name,
            })

        return JsonResponse(data, safe=False)
    except Category.DoesNotExist:
        return JsonResponse({'error': 'Category not found'}, status=404)