from django.db import models

# Create your models here.

class api_data(models.Model):
    data_source = models.TextField()
    brief_description_of_data = models.TextField()
    datasets_available = models.TextField()
    brief_description_of_datasets = models.TextField()
    country = models.TextField()
    api_documentation = models.TextField()

    class Meta:
        verbose_name_plural = "api_data"