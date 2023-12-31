from django.urls import path
from . import views 


urlpatterns = [
    # listing of products
    path('products/all/', views.all_products, name='all_products'),
    path('brands/<slug:brand>/all/', views.brand_products, name='brand_products'),
    path('category/<slug:category>/all/', views.category_products, name='category_products'),
    
    # searching products
    path('products/search/', views.search_products, name='search_products'),
    path('seller/<int:id>/all/', views.seller_products, name='seller_products'),
    # path('seller/<int:seller_pk>/products/', SellerProductListView.as_view(), name='seller_product_list'),

    # path('seller/all/', views.seller_list, name='seller_list'),
    

    # views product details
    path('product/<slug:slug>/', views.product_detail, name='product_detail'),

]