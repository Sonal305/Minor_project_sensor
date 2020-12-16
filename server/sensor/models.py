from django.db import models

# Create your models here.
class Home(models.Model):
    home_add=models.CharField(max_length=256)
    name=models.CharField(max_length=200)
    contact=models.CharField(max_length=200)
    address=models.CharField(max_length=200)


    def __str__(self):
        return self.home_add

class Sensor(models.Model):
    name=models.CharField(max_length=10)
    home_add=models.ForeignKey(Home,on_delete=models.CASCADE, related_name='home')
    ins_add=models.CharField(max_length=256,blank=True,null=True)
    inves_add=models.CharField(max_length=256,blank=True,null=True)
    supp_add=models.CharField(max_length=256,blank=True,null=True)

    CHOICES1=(
                ('KIT','Kitchen'),
                ('HAL','Hall'),
                ('GAR', 'Garden'),
                ('BAT','Bathroom'),
    )

    CHOICES2=(
            ('FIRE','Fire'),
            ('GAS','Gas Leakage'),
            ('WAT','Water Leakage'),
            ('BURG','Burglary'),
    )
    area=models.CharField(max_length=3,choices=CHOICES1,null=True)
    type=models.CharField(max_length=4,choices=CHOICES2)

    resolved=models.BooleanField(default=False)


    def __str__(self):
        return self.name+' '+str(self.home_add)


class ContactPSP(models.Model):
    CHOICES=(
            ('FIRE','Fire'),
            ('GAS','Gas Leakage'),
            ('BURG','Burglary'),
    )
    type=models.CharField(max_length=200,choices=CHOICES)
    contact=models.CharField(max_length=10)

    def __str__(self):
        return self.type
