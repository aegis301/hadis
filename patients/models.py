from email.policy import default
from tkinter import NUMERIC
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from dataforms.models import DataForm
# Create your models here.

    
class Patient(models.Model):
    last_name = models.CharField(max_length=200)
    first_name = models.CharField(max_length=200)
    date_of_birth = models.DateField()
    kis_id = models.CharField(max_length=8)
    gender = models.BooleanField()
    created_at = models.DateTimeField(default=timezone.now)
    created_by = models.ForeignKey(
        User,
        on_delete=models.DO_NOTHING,  # don't delete patients if a user is deleted
        # default=User.objects.filter(username='christian')
    )
    main_diagnosis = models.CharField(max_length=1000, blank=False)
    dataforms = models.ForeignKey(DataForm, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.first_name + " " + self.last_name

    # how to redirect after create (reverse returs string representation of the full path, not actually redirect)
    def get_absolute_url(self):
        return reverse("patient-detail", kwargs={"pk": self.pk})