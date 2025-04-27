from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.utils import timezone
class Type_leave(models.Model):
    name = models.CharField(max_length=200)
    no_days = models.PositiveIntegerField(default=0)
    def __str__(self):
        return self.name        #optional, but useful for admin interface
class LeaveBalance(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    leave_type = models.ForeignKey(Type_leave, on_delete=models.CASCADE)
    year = models.PositiveIntegerField(default=timezone.now().year)
    balance = models.IntegerField(default=0)
    class Meta:
        unique_together = ('user', 'leave_type', 'year')

    def __str__(self):
        return f"{self.user.username} - {self.leave_type.name} - {self.balance} days"
class LeaveApplication(models.Model):
    STATUS_PENDING = 'Pending'
    STATUS_APPROVED = 'Approved'
    STATUS_REJECTED = 'Rejected'
    STATUS_CHOICES = [
        (STATUS_PENDING, 'Pending'),
        (STATUS_APPROVED, 'Approved'),
        (STATUS_REJECTED, 'Rejected'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name = 'leave_applications')
    leave_type = models.ForeignKey(Type_leave, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    reason = models.TextField()
    status = models.CharField(max_length=30, choices=STATUS_CHOICES, default=STATUS_PENDING)
    #created_at = models.DateTimeField(auto_now_add=True)
    #updated_at = models.DateTimeField(auto_now=True)
    def duration(self):
        """Calculate the duration of the leave in days."""
        return (self.end_date - self.start_date).days + 1  # Include both start and end dates