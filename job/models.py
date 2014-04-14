from django.db import models

# Create your models here.

class Job(models.Model):

    job_id = models.CharField(verbose_name="Job ID", max_length=100, blank=False)
    status = models.CharField(verbose_name="Status", max_length=10, blank=False, default="FAILED")


