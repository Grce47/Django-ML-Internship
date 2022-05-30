from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import CharField
from django.utils.translation import gettext_lazy as _
from .constants import PaymentStatus


# Create your models here.

class pythonCode(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    codearea = models.TextField()
    output = models.TextField()
    session_key = models.TextField(null=True)
    username = models.TextField(null=True)
    added = models.DateTimeField(auto_now_add=True)

    @classmethod
    def create(cls, cur_user,cur_code,cur_output,cur_sessionkey,cur_username):
        new_code = cls(user=cur_user,codearea=cur_code,output=cur_output,session_key=cur_sessionkey,username=cur_username)
        return new_code
    
    def __str__(self):
        return self.added.strftime('%Y-%m-%d %H:%M')
    class Meta:
        ordering = ['-added']

class Order(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    amount = models.FloatField(_("Amount"), null=False, blank=False)
    status = CharField(
        _("Payment Status"),
        default=PaymentStatus.PENDING,
        max_length=254,
        blank=False,
        null=False,
    )
    provider_order_id = models.CharField(
        _("Order ID"), max_length=40, null=False, blank=False
    )
    payment_id = models.CharField(
        _("Payment ID"), max_length=36, null=False, blank=False
    )
    signature_id = models.CharField(
        _("Signature ID"), max_length=128, null=False, blank=False
    )

    def __str__(self):
        return f"{self.id}-{self.user}-{self.status}"