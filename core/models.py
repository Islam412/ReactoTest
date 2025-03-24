from django.db import models
from userauths.models import User
from django.utils.translation import gettext_lazy as _
# Create your models here.

class Predictions(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    transformer_name = models.CharField(_('Transformer ID'))
    gas_h2 = models.DecimalField(_('Hydrogen (H2) '))
    gas_C2H4 = models.DecimalField(_('Ethylene (C2H4)'))
    gas_C2H2 = models.DecimalField(_('Acetylene (C2H2)'))
    gas_CO = models.DecimalField(_('Carbon Monoxide (CO)'))
    last_maintenance_date = models.DateTimeField(_("Last Maintenance Date"), blank=True,null=True)
    ambient_temp = models.FloatField(_("Ambient Temperature"))