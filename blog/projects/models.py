from django.db import models

class Customer(models.Model):
    username = models.CharField(max_length=100,verbose_name='ID : ', null=True)
    first_name = models.CharField(max_length=100,verbose_name="Name : ", null=True)
    last_name = models.CharField(max_length=100,verbose_name='Surname : ', null=True)
    password = models.CharField(max_length=100,verbose_name='Password : ', null=True)
    created_date = models.DateTimeField(auto_now_add=True,verbose_name='Login Date : ', null=True)
    balance = models.IntegerField(verbose_name='Balance : ', null=True)

    def __str__(self):
        return str(self.username)
    def __str__(self):
        return str(self.first_name)
    def __str__(self):
        return str(self.last_name)
    def __str__(self):
        return str(self.balance)
