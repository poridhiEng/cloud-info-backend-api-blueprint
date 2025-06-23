from django.db import models
import uuid

# Create your models here.
class PricePlan(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    price = models.CharField(max_length=6, blank=False, null=False)
    credit = models.PositiveSmallIntegerField(blank=False, null=False)
    gpu_hours = models.CharField(max_length=6, blank=False, null=False)

    class Meta:
        verbose_name = "Price Plan"
        verbose_name_plural = "Price Plans"
        ordering = ['name']
        db_table = 'price_plans'
    
    def __str__(self):
        return self.name
    