from django.db import models
from django.utils.translation import gettext_lazy as _

from base.utils.models.standard_models import StandardModel

# Create your models here.

class TodoList(StandardModel):
    """
    Model representing a TodoList.
    """
    
    class Meta:
        verbose_name = _("TodoList")
        verbose_name_plural = _("TodoLists")
      
    name = models.CharField(max_length=255, verbose_name=_("Name"))
        
    def __str__(self):
        return self.name
