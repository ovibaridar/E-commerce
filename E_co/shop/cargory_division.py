# views.py

from django.shortcuts import render
from .models import product

def shophometest(request):
    all_products = product.objects.all()
    num_products_per_set = 4

    # Group the products into sets of 4
    grouped_products = [all_products[i:i + num_products_per_set] for i in
                        range(0, len(all_products), num_products_per_set)]

    # Get unique categories
    categories = product.objects.values_list('catagory', flat=True).distinct()

    # Create a dictionary to hold products grouped by category
    grouped_products_by_category = {category: [] for category in categories}
    for prod in all_products:  # Rename the variable from 'product' to 'prod'
        grouped_products_by_category[prod.catagory].append(prod)

    # Identify categories without any products
    categories_with_products = set(grouped_products_by_category.keys())
    all_categories = set(categories)
    categories_without_products = all_categories - categories_with_products

    # Create a dictionary to hold empty product lists for categories without any products
    for category in categories_without_products:
        grouped_products_by_category[category] = []

    return render(request, 'shop/catagory_division.html', {'grouped_products_by_category': grouped_products_by_category})