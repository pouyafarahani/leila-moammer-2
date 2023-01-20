from django.db import models
from django.shortcuts import reverse
from django_jalali.db import models as jmodels


class MyTeamModel(models.Model):
    name = models.CharField(max_length=80, null=True, blank=True)
    image = models.ImageField(blank=True, null=True)
    work = models.CharField(max_length=70, null=True, blank=True)
    description_me = models.TextField(null=True, blank=True)
    darbare_majmoee = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=40, null=True, blank=True)
    specialty = models.CharField(max_length=40, null=True, blank=True)
    description_short = models.TextField(null=True, blank=True)

    price1 = models.CharField(max_length=30, null=True, blank=True)
    price2 = models.CharField(max_length=30, null=True, blank=True)
    price3 = models.CharField(max_length=30, null=True, blank=True)
    price4 = models.CharField(max_length=30, null=True, blank=True)
    price5 = models.CharField(max_length=30, null=True, blank=True)

    image1 = models.ImageField(null=True, blank=True)
    image2 = models.ImageField(null=True, blank=True)
    image3 = models.ImageField(null=True, blank=True)
    image4 = models.ImageField(null=True, blank=True)
    image5 = models.ImageField(null=True, blank=True)
    image6 = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('my_team:user_detail', args=[self.pk])


class UserOstadModel(models.Model):
    name = models.CharField(max_length=80, null=True, blank=True)
    image = models.ImageField(blank=True, null=True)
    work = models.CharField(max_length=70, null=True, blank=True)
    description_me = models.TextField(null=True, blank=True)
    darbare_majmoee = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=40, null=True, blank=True)
    specialty = models.CharField(max_length=40, null=True, blank=True)
    description_short = models.TextField(null=True, blank=True)
    phone = models.CharField(max_length=12, null=True, blank=True)
    telegram = models.TextField(null=True, blank=True)
    instagram = models.TextField(null=True, blank=True)
    whatsapp = models.TextField(null=True, blank=True)

    price1 = models.CharField(max_length=30, null=True, blank=True)
    price2 = models.CharField(max_length=30, null=True, blank=True)
    price3 = models.CharField(max_length=30, null=True, blank=True)
    price4 = models.CharField(max_length=30, null=True, blank=True)
    price5 = models.CharField(max_length=30, null=True, blank=True)
    price6 = models.CharField(max_length=30, null=True, blank=True)
    price7 = models.CharField(max_length=30, null=True, blank=True)

    image1 = models.ImageField(null=True, blank=True)
    image2 = models.ImageField(null=True, blank=True)
    image3 = models.ImageField(null=True, blank=True)
    image4 = models.ImageField(null=True, blank=True)
    image5 = models.ImageField(null=True, blank=True)
    image6 = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('my_team:ostad_detail', args=[self.pk])


class DateTeamModel(models.Model):
    team = models.ForeignKey(MyTeamModel, on_delete=models.CASCADE, related_name='teams')
    time = models.TimeField()
    date = models.DateField()
    is_rezerv = models.BooleanField(default=False)

    def __str__(self):
        return self.team.name


class RezervTeamModel(models.Model):
    user = models.ForeignKey(MyTeamModel, on_delete=models.CASCADE)
    is_rezerv = models.BooleanField(default=False)

    date = models.CharField(max_length=100)
    time = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=11)
    khadamat = models.CharField(max_length=100)
    authority = models.CharField(max_length=120, null=True, blank=True)


class DateOstadModel(models.Model):
    user = models.ForeignKey(UserOstadModel, on_delete=models.CASCADE, related_name='ostads')
    time = models.TimeField()
    date = models.DateField()
    is_rezerv = models.BooleanField(default=False)

    def __str__(self):
        return self.user.name


class RezervOstadModel(models.Model):
    is_rezerv = models.BooleanField(default=False)

    date = models.CharField(max_length=100)
    time = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=11)
    khadamat = models.CharField(max_length=100)
    authority = models.CharField(max_length=120, null=True, blank=True)

    def __str__(self):
        return self.last_name


#Mohammad

class BokingDate(models.Model):
    date = jmodels.jDateField()
    employ = models.ForeignKey(UserOstadModel, on_delete=models.CASCADE)

    time1 = models.BooleanField(default=False)
    time2 = models.BooleanField(default=False)
    time3 = models.BooleanField(default=False)

    user1 = models.CharField(max_length=100, null=True)
    user2 = models.CharField(max_length=100, null=True)
    user3 = models.CharField(max_length=100, null=True)

    phone1 = models.CharField(max_length=100, null=True)
    phone2 = models.CharField(max_length=100, null=True)
    phone3 = models.CharField(max_length=100, null=True)

    service1 = models.CharField(max_length=100, null=True)
    service2 = models.CharField(max_length=100, null=True)
    service3 = models.CharField(max_length=100, null=True)

class BokingDate_MyTeam(models.Model):
    date = jmodels.jDateField()
    employ = models.ForeignKey(MyTeamModel, on_delete=models.CASCADE)

    time1 = models.BooleanField(default=False)
    time2 = models.BooleanField(default=False)
    time3 = models.BooleanField(default=False)

    user1 = models.CharField(max_length=100, null=True)
    user2 = models.CharField(max_length=100, null=True)
    user3 = models.CharField(max_length=100, null=True)

    phone1 = models.CharField(max_length=100, null=True)
    phone2 = models.CharField(max_length=100, null=True)
    phone3 = models.CharField(max_length=100, null=True)

    service1 = models.CharField(max_length=100, null=True)
    service2 = models.CharField(max_length=100, null=True)
    service3 = models.CharField(max_length=100, null=True)