from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class Buyer(models.Model):
    user = models.OneToOneField(User)
    birthday = models.DateField()
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name

#create our user object to attach to our buyer object
#def create_buyer_user_callback(sender, instance, **kwargs):
    #buyer, new = Buyer.objects.get_or_create(user=instance)
    #post_save.connect(create_buyer_user_callback(), User)