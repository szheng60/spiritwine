from django.contrib import admin
from promotion.models import *
from wine.admin import WineAdmin
# Register your models here.

class PromotionSpecialAdmin(WineAdmin):
    pass

admin.site.register(PromotionSpecial, PromotionSpecialAdmin)


