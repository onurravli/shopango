from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=50)
    desc = models.TextField(max_length=255)
    img = models.CharField(max_length=255)
    stock = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

    def to_json(self):
        return {
            "id": self.id,
            "desc": self.desc,
            "img": self.img,
            "stock": self.stock,
            "price": self.price,
        }
