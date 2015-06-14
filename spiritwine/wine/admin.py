from django.contrib import admin
from wine.models import *
# Register your models here.
class WineAdmin(admin.ModelAdmin):
    list_display = ('name', 'region', 'size', 'price', 'country',)
    date_hierarchy = 'produced_date'
    ordering = ('-region', 'name', 'price')
    
class MalbecAdmin(WineAdmin):
    pass

class MerlotAdmin(WineAdmin):
    pass

class CabernetSauvignonAdmin(WineAdmin):
    pass

class PinotNoirAdmin(WineAdmin):
    pass

class VodkaAdmin(WineAdmin):
    pass

class WhiskeyAdmin(WineAdmin):
    pass

class RumAdmin(WineAdmin):
    list_display = ('name', 'flavor', 'size', 'price', 'country',)

class SakeAdmin(WineAdmin):
    pass

class BrandyAdmin(WineAdmin):
    pass

class GinAdmin(WineAdmin):
    list_display = ('name', 'flavor', 'size', 'price', 'country',)

class AniseAdmin(WineAdmin):
    pass
class BlancAdmin(WineAdmin):
    pass
class BordeauxAdmin(WineAdmin):
    pass
class BurgundyAdmin(WineAdmin):
    pass
class ChardonnayAdmin(WineAdmin):
    pass
class ClaretAdmin(WineAdmin):
    pass
class CognacAdmin(WineAdmin):
    pass
class CordialAdmin(WineAdmin):
    pass
class CreamsAdmin(WineAdmin):
    pass
class SherryAdmin(WineAdmin):
    pass
class PortAdmin(WineAdmin):
    pass
class ChocolateAdmin(WineAdmin):
    pass
class MoscatoAdmin(WineAdmin):
    pass
class MarsalaAdmin(WineAdmin):
    pass
class PlumAdmin(WineAdmin):
    pass
class DessertAdmin(WineAdmin):
    pass
class FrenchAdmin(WineAdmin):
    pass
class GrenacheAdmin(WineAdmin):
    pass
class LiqueurAdmin(WineAdmin):
    pass
class PinotageAdmin(WineAdmin):
    pass
class PinotGrigioAdmin(WineAdmin):
    pass
class PiscoAdmin(WineAdmin):
    pass
class RieslingAdmin(WineAdmin):
    pass
class RoseAdmin(WineAdmin):
    pass
class SangriaAdmin(WineAdmin):
    pass
class SirahAdmin(WineAdmin):
    pass
class VermouthAdmin(WineAdmin):
    pass
class VranacAdmin(WineAdmin):
    pass
class ZinfandelAdmin(WineAdmin):
    pass
class ShirazAdmin(WineAdmin):
    pass
class ChampagneAdmin(WineAdmin):
    pass
class TequilaAdmin(WineAdmin):
    pass

admin.site.register(Malbec, MalbecAdmin)
admin.site.register(Merlot, MerlotAdmin)
admin.site.register(CabernetSauvignon, CabernetSauvignonAdmin)
admin.site.register(PinotNoir, PinotNoirAdmin)
admin.site.register(Vodka, VodkaAdmin)
admin.site.register(Whiskey, WhiskeyAdmin)
admin.site.register(Rum, RumAdmin)
admin.site.register(Sake, SakeAdmin)
admin.site.register(Brandy, BrandyAdmin)
admin.site.register(Gin, GinAdmin)
admin.site.register(Anise, AniseAdmin)
admin.site.register(Blanc, BlancAdmin)
admin.site.register(Bordeaux, BordeauxAdmin)
admin.site.register(Burgundy, BurgundyAdmin)
admin.site.register(Chardonnay, ChardonnayAdmin)
admin.site.register(Claret, ClaretAdmin)
admin.site.register(Cognac, CognacAdmin)
admin.site.register(Cordial, CordialAdmin)
admin.site.register(Creams, CreamsAdmin)
admin.site.register(Plum, PlumAdmin)
admin.site.register(Chocolate, ChocolateAdmin)
admin.site.register(Port, PortAdmin)
admin.site.register(Sherry, SherryAdmin)
admin.site.register(Marsala, MarsalaAdmin)
admin.site.register(Moscato, MoscatoAdmin)                                                                          
admin.site.register(Dessert, DessertAdmin)
admin.site.register(French, FrenchAdmin)
admin.site.register(Grenache, GrenacheAdmin)
admin.site.register(Liqueur, LiqueurAdmin)
admin.site.register(Pinotage, PinotageAdmin)
admin.site.register(PinotGrigio, PinotGrigioAdmin)
admin.site.register(Pisco, PiscoAdmin)
admin.site.register(Riesling, RieslingAdmin)
admin.site.register(Rose, RoseAdmin)
admin.site.register(Sangria, SangriaAdmin)
admin.site.register(Sirah, SirahAdmin)
admin.site.register(Vermouth, VermouthAdmin)
admin.site.register(Vranac, VranacAdmin)
admin.site.register(Zinfandel, ZinfandelAdmin)
admin.site.register(Shiraz, ShirazAdmin)
admin.site.register(Champagne, ChampagneAdmin)
admin.site.register(Tequila, TequilaAdmin)
