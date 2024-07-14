from django.db import models

class Company(models.Model):
    company_name = models.CharField(max_length=45)
    company_registration_number = models.CharField(max_length=45)
    portal_url = models.CharField(max_length=45)
    phone_number = models.IntegerField()
    address = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'company'