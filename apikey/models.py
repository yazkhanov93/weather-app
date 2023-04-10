from django.db import models


class ApiKey(models.Model):
    key = models.CharField(max_length=200, verbose_name="api key")

    class Meta:
        verbose_name_plural = "Api Key"
    
    def __str__(self):
        return self.key