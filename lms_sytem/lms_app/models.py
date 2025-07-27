from django.db import models


class Reader(models.Model):
    refrence_id = models.CharField(max_length=10)
    reader_name = models.CharField(max_length=10, null=False)
    reader_contact = models.CharField(max_length=10, null=True)
    reader_address = models.TextField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.reader_name


from django.db import models

# Create your models here.
