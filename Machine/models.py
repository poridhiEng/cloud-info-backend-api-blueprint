from django.db import models
import uuid

# Create your models here.
class Machine(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    cpu = models.PositiveIntegerField()
    memory = models.PositiveIntegerField()
    gpu_count = models.PositiveIntegerField()
    gpu_model = models.CharField(max_length=20, blank=False, null=False)
    credit = models.DecimalField(max_digits=10, decimal_places=4)

    class Meta:
        verbose_name = "Machine"
        verbose_name_plural = "Machines"
        db_table = 'machines'
    
    def __str__(self):
        return f"Machine {self.id}"