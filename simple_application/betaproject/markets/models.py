from django.db import models

# Create your models here.
class Market(models.Model):
    timestamp = models.CharField(max_length=255) #UNIX timestamp of when the market was opened
    transactionhash = models.CharField(max_length=255) #The transaction hash that opened the market
    address = models.CharField(max_length=255) #The address of the market opened, represented as a string
    
    def __str__(self):
        return f"{self.timestamp} {self.transactionhash} {self.address}"


