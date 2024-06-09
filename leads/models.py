from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass

class Lead(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    state = models.CharField(max_length=20)
    phone = models.CharField(max_length=15)
    do_you_have_attorney = models.CharField(max_length=10)
    date_of_accident = models.CharField(max_length=50)
    were_your_at_fault = models.CharField(max_length=50)
    how_were_you_hurt = models.CharField(max_length=100)
    working_in_federal = models.CharField(max_length=10)
    had_medical_attention = models.CharField(max_length=10)
    brief_description = models.TextField()

    buyer = models.ForeignKey("Buyer", on_delete=models.CASCADE, default="NA")
    supplier = models.ForeignKey("Supplier", on_delete=models.CASCADE, default="NA")
    campaign = models.ForeignKey("Campaign", on_delete=models.CASCADE, default="NA")

    agent = models.ForeignKey("Agent", on_delete=models.CASCADE, default="NA")


    create_on = models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.supplier} {self.buyer} {self.campaign}"


class Campaign(models.Model):
    campaign_name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    
    added_on = models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        return self.campaign_name


class Buyer(models.Model):
    buyer_id = models.IntegerField(null=False, primary_key=True)
    buyer_name = models.CharField(max_length=50)
    buyer_firm_name = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)

    added_on = models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        return self.buyer_name    

class Supplier(models.Model):
    supplier_id = models.IntegerField(null=False, primary_key=True)
    supplier_name = models.CharField(max_length=50)
    supplier_firm_name = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)

    added_on = models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        return self.supplier_name 

class Agent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.email