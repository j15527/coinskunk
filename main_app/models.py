from django.db import models
from django.conf import settings
from PIL import Image
User = settings.AUTH_USER_MODEL


class Asset(models.Model):
    name = models.CharField(max_length=50, default='')
    price = models.FloatField(default=0)
    count = models.FloatField(default=0)
    logo = models.ImageField()

    class Meta:
        verbose_name_plural = "Assets"

    def __str__(self):
        return f'{self.name}-{self.price}-{self.count}'


class Portfolio(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(default='New Portfolio', max_length=120)
    assets = models.ManyToManyField(Asset, blank=True)
    value = models.FloatField(default=0)
    date_created = models.DateTimeField(auto_now_add=True)
    principal = 0
    asset_count = {}

    def principal_sum(self):
        for i in self.assets.all():
            self. principal += i.price * i.count
        return self.principal

    def net_worth(self):
        for i in self.assets.all():
            self.value += i.price * i.count

        # self.value = self.asset.price * self.asset_count
        return self.value

    def __str__(self):
        return self.name
