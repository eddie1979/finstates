from django.db import models

# Create your models here.
class Company(models.Model):
  name = models.CharField("会社名", max_lenght = 30, blank = false)


    def __str__(self):
      return str(self.name)

#----ここまで----