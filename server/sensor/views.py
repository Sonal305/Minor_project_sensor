from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework import viewsets, permissions,generics
from rest_framework.views import APIView
from django.db.models.signals import post_save
from django.dispatch import receiver
from .sms import send_sms
# Create your views here.




class homeListView(generics.ListCreateAPIView):
    queryset = Home.objects.all()
    serializer_class = HomeSerializer

class homeDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Home.objects.all()
    serializer_class = HomeSerializer

class damageListView(generics.ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class damageDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class DamageHomeListView(APIView):
    def get(self, request, home_add):
         getHome=Home.objects.get(home_add=home_add)
         getDamage=Sensor.objects.filter(home_add=getHome)
         damages=[]

         for d in getDamage:
             damages.append(d.id)

         return Response({'damages':damages})



@receiver(post_save, sender=Sensor)
def send_msg_PSP(sender,instance, **kwargs):
    critical=['FIRE','GAS','BURG']
    curr=instance.type
    if curr in critical:
        format={'FIRE':'Reporting Fire','GAS':'Reporting Gas Leakage ','BURG':'Reporting Burglary '}

        msg=format[curr]

        message1=''
        message2=''
        contact= ContactPSP.objects.get(type=curr).contact

        getHome=Home.objects.get(home_add=instance.home_add)
        owner=str(getHome.name)
        contactno=str(getHome.contact)
        address=str(getHome.address)

        message1+="Name : " +owner +"\\n"+"Contact : " + contactno+"\\n"+"Address: "+address+"\\n"+curr+""

        message2+=curr+" at your house ( "+address+" )."+"\\n"+"Reported to respected department."+"\\n"+"Contact : "+contact+" \\n"+"Stay Safe! "

        #send_sms(contact,message1) #msg to psp
        #send_sms(contactno,message2) #msg to owner
        instance.resolved=True

        print("msg sent")
