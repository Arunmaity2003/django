from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.
class ChaiVarity(models.Model):
    CHAI_TYPE_CHOISE = [
        ('ML','MASALA'),
        ('GR','GINGER'),
        ('KL','KIWI'),
        ('PL','PLAIN'),
        ('EL','ELACHI')
    ]
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    date_added = models.DateTimeField(default=timezone.now)
    type = models.CharField( max_length=100, choices = CHAI_TYPE_CHOISE )
    description = models.TextField(default='')

    def __str__(self):
        return self.name
    
# one to one
class ChaiReview(models.Model):
    chai = models.ForeignKey("ChaiVarity", on_delete=models.CASCADE,related_name = 'review')
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()
    date_added = models.DateTimeField( default=timezone.now)

    def __str__(self):
        return f'{self.user.name} reviews for {self.chai.name}'
    
#Many to many relation----------
class Store(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField( max_length=100)
    chai_varieties = models.ManyToManyField(ChaiVarity, related_name = 'stores')
   

    def __str__(self):
        return self.name
    
#one to many----------
class ChaiCertificate(models.Model):
    chai = models.OneToOneField(ChaiVarity, on_delete=models.CASCADE,related_name = 'certificate')
    certificate_number = models.CharField( max_length=100)
    issued_date = models.DateTimeField(default=timezone.now)
    valid_until = models.DateTimeField()

    def __str__(self):
        return f'certificate for {self.name.chai}'