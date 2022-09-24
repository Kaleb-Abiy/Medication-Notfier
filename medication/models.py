from django.db import models
from django.contrib.auth import get_user_model
import datetime 
from django.urls import reverse

User = get_user_model()


doasage_choices = (('1', 1),('2', 2), ('3', 3), ('4', 4))

class Medications(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='medications')
    med_name = models.CharField(max_length=300)
    indication = models.CharField(max_length=500)
    note = models.TextField(blank=True)
    first_time = models.TimeField()
    dosage = models.CharField(choices=doasage_choices, max_length=10)
    

    def __str__(self):
        return f'{self.user.username} - medication'


    def get_notf(self):
        if self.dosage == str(1):
            notfication_times = self.first_time
            return notfication_times
        elif self.dosage == str(2):
            notfication_times = []
            print(self.first_time)
            initial_time = self.first_time
            for d in range(0, 2):
                next_notfication = initial_time
                notfication_times.append(next_notfication)
                initial_time = (datetime.datetime.combine(datetime.date.today(), initial_time) + datetime.timedelta(hours=12)).time()
        
            return notfication_times

        elif self.dosage == str(3):
            notfication_times = []
            initial_time = self.first_time
            for d in range(0, 3):
                next_notfication = initial_time
                notfication_times.append(next_notfication)
                initial_time = (datetime.datetime.combine(datetime.date.today(), initial_time) + datetime.timedelta(hours=8)).time()

            return notfication_times
        
        elif self.dosage == str(4):
            notfication_times = []
            initial_time = self.first_time
            print(initial_time)
            for d in range(0, 4):
                next_notfication = initial_time
                notfication_times.append(next_notfication)
                initial_time = (datetime.datetime.combine(datetime.date.today(), initial_time) + datetime.timedelta(hours=6)).time()

            return notfication_times

    def get_absolute_url(self):
        return reverse('index', kwargs = {'id': self.id})   
        


        # if self.dosage == 1:
        #     next_notfication = self.first_time + timedelta(hours=24)
        #     return next_notfication
        # elif self.dosagestr(:)
        #     next_notfication = self.first_time + timedelta(hours=12)
        # elif self.dosage == 3:
        #     next_notfication = self.first_time + timedelta(hours=8)
        # elif self.dosage == 4:
        #     next_notfication = self.first_time + timedelta(hours=6)

           
