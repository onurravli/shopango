from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse, HttpRequest
from .models import Product
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist


def get_product(request: HttpRequest, id: int) -> JsonResponse:
    try:
        product = get_object_or_404(Product, id=id)
        return JsonResponse(
            product.to_json(),
            status=200,
        )
    except ObjectDoesNotExist as odne:
        return JsonResponse(
            {
                "error": "Product not found.",
            },
            status=404,
        )
    except Exception as e:
        return JsonResponse(
            {
                "error": "An error occurred.",
            },
            status=500,
        )


def get_all_products(request: HttpRequest) -> JsonResponse:
    products = [
        dict(
            id=product.id,
            name=product.name,
            desc=product.desc,
            img=product.img,
            stock=product.stock,
            price=product.price,
        )
        for product in Product.objects.all()
    ]
    return JsonResponse(
        products,
        status=200,
        safe=False,
    )


@csrf_exempt
def create_product(request: HttpRequest) -> JsonResponse:
    body = request.POST
    name = body.get("name")
    desc = body.get("desc")
    img = body.get("img")
    stock = body.get("stock")
    price = body.get("price")
    if not name or not desc or not img or not stock or not price:
        return JsonResponse(
            {
                "error": "Required fields missing.",
            },
            status=400,
        )
    try:
        Product.objects.all().create(
            name=name, desc=desc, img=img, stock=stock, price=price
        )
        return JsonResponse(
            {
                "message": "Product created.",
            },
            status=201,
        )
    except Exception as e:
        return JsonResponse(
            {
                "error": e.__str__(),
            },
            status=500,
        )


@csrf_exempt
def delete_product(request: HttpRequest, id: int) -> JsonResponse:
    product = get_object_or_404(Product, id=id)
    if product != None:
        product.delete()
        return JsonResponse(
            {
                "message": f"Product with ID {id} deleted.",
            },
            status=200,
        )
    else:
        return JsonResponse(
            {
                "error": "Product doesn't exist.",
            },
            status=404,
        )
