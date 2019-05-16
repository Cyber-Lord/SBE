from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

class Bank(models.Model):
    bankName = models.CharField(max_length=100, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    phoneNumber = models.IntegerField()
    contactMail = models.EmailField()
    about = models.TextField()

    def __str__(self):
        return self.bankName

class LoanCritereia(models.Model):
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE)
    criteria = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = 'criterias'

    def __str__(self):
        return self.bank.bankName

class Feature(models.Model):
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE)
    feature = models.CharField(max_length=500)

    def __str__(self):
        return self.bank.bankName

class Benefit(models.Model):
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE)
    benefit = models.CharField(max_length=500)

    def __str__(self):
        return self.bank.bankName

class Branch(models.Model):
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE)
    branchName = models.CharField(max_length=100, unique=True)
    sortCode = models.IntegerField()
    swiftCode = models.TextField()
    loanManager = models.ForeignKey(User, on_delete=models.CASCADE)
    contactAddress = models.CharField(max_length=200)

    def __str__(self):
        return self.bank.bankName + ' ' + self.branchName

class AppForm(models.Model):
    fName = models.CharField(max_length=15)
    lName = models.CharField(max_length=15)
    oName = models.CharField(max_length=15)
    phoneNumber = models.IntegerField()
    homeAddress = models.TextField(max_length=200)
    busName = models.CharField(max_length=50)
    busAddress = models.CharField(max_length=200)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=20)

    def __str__(self):
        return self.fName + ' '+ self.lName


