from django.db import models

# Create your models here.
class WineInfo (models.Model):
    name = models.CharField(max_length=30)
    size = models.CharField(max_length=10)
    price = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    region = models.CharField(max_length = 30, blank = True, null = True)
    produced_date = models.DateField(blank = True, null = True)
    country = models.CharField(max_length = 50, blank = True, null = True)
    website = models.CharField(max_length = 100, blank = True, null = True)
    description = models.TextField(blank = True, null = True)

    def __str__(self):
        return self.name
    def get_cname(self):
        return self.__class__.__name__
    class Meta:
        abstract = True
    
class Malbec (WineInfo):
    class Meta:
        ordering = ['name']

class Merlot(WineInfo):
    pass

class CabernetSauvignon(WineInfo):
    pass

class PinotNoir(WineInfo):
    pass

class Vodka(WineInfo):
    pass

class Whiskey(WineInfo):
    pass

class Rum(WineInfo):
    flavor = models.CharField(max_length=30, blank = True, null = True)

class Sake(WineInfo):
    pass

class Brandy(WineInfo):
    pass

class Gin(WineInfo):
    flavor = models.CharField(max_length=30, blank = True, null = True)
class Anise(WineInfo):
    pass
class Blanc(WineInfo):
    pass
class Bordeaux(WineInfo):
    pass
class Burgundy(WineInfo):
    pass
class Chardonnay(WineInfo):
    pass
class Claret(WineInfo):
    pass
class Cognac(WineInfo):
    pass
class Cordial(WineInfo):
    pass
class Creams(WineInfo):
    pass
class Plum(WineInfo):
    pass
class Marsala(WineInfo):
    pass
class Sherry(WineInfo):
    pass
class Port(WineInfo):
    pass
class Moscato(WineInfo):
    pass
class Chocolate(WineInfo):
    pass
class Dessert(WineInfo):
    pass
class French(WineInfo):
    pass
class Grenache(WineInfo):
    pass
class Liqueur(WineInfo):
    pass
class Pinotage(WineInfo):
    pass
class PinotGrigio(WineInfo):
    pass
class Pisco(WineInfo):
    pass
class Riesling(WineInfo):
    pass
class Rose(WineInfo):
    pass
class Sangria(WineInfo):
    pass
class Sirah(WineInfo):
    pass
class Vermouth(WineInfo):
    pass
class Vranac(WineInfo):
    pass
class Zinfandel(WineInfo):
    pass
class Shiraz(WineInfo):
    pass
class Champagne(WineInfo):
    pass
class Tequila(WineInfo):
    pass