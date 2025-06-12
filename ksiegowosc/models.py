from django.db import models
<<<<<<< HEAD
from django.conf import settings
from django.utils import timezone

# Create your models here.

class ActiveMod(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(deleted_at__isnull=True)

class Account(models.Model):
    ACCOUNT_TYPES = (
        ('internal', 'Internal'),
        ('external', 'External'),
    )

    name = models.CharField(max_length=300)
    account_type = models.CharField(max_length=250, choices=ACCOUNT_TYPES)
    created_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL)

    objects = models.Manager() # Default mod which includes the banished
    active = ActiveMod() # Custom mod which excludes the banished

    def soft_delete(self):
        self.deleted_at = timezone.now()
        self.save()

    def is_deleted(self):
        return self.deleted_at is not None
    
    def __str__(self):
        return self.name
    
=======

# Create your models here.

class wydatki(models.Model):
    title = models.CharField(max_length=200)
    amount = models.IntegerField()
>>>>>>> 8702e905c9eb88b49bca0485c8db1f00fd1d7221
