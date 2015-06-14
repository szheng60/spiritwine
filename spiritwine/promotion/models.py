from django.db import models
from wine.models import WineInfo
# Create your models here.

class PromotionSpecial(WineInfo):
    oldPrice = models.DecimalField(max_digits=15, decimal_places=2, default=0)
