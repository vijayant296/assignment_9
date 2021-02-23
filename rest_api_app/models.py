from django.db import models


class Techie(models.Model):
    techie_id = models.IntegerField(primary_key=True)
    techie_name = models.CharField(max_length=200)
    techie_skill = models.CharField(max_length=20)
    techie_profile = models.CharField(max_length=50)
    techie_salary = models.IntegerField()

    def __str__(self):
        return self.techie_name




