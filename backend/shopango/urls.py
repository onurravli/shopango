from .views import get_product, create_product, get_all_products, delete_product
from django.urls import path

urlpatterns = [
    path("get_product/<int:id>/", get_product, name="get_product"),
    path("get_all_products", get_all_products, name="get_all_products"),
    path("create_product/", create_product, name="create_product"),
    path("delete_product/<int:id>/", delete_product, name="delete_product"),
]
