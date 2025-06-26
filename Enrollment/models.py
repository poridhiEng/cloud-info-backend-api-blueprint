from django.db import models
import uuid

# Create your models here.
class Enrollment(models.Model):
    PAYMENT_STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('active', 'Active'),
        ('cancel', 'Cancel'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_id = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    user_email = models.EmailField(max_length=255)
    credit = models.IntegerField(default=0)
    payment_status = models.CharField(max_length=50, choices=PAYMENT_STATUS_CHOICES, default='pending')
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'enrollment'
        ordering = ['-created_at']
        verbose_name = 'Enrollment'
        verbose_name_plural = 'Enrollments'
        
    def __str__(self):
        return f"{self.username} enrolled status {self.payment_status}"