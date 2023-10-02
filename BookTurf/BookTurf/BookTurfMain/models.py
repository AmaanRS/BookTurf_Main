from django.db import models
from django.contrib.auth.models import User
import os
from django.db.models.signals import post_save , pre_save
from django.dispatch import receiver

# Create your models here.
# CHOICES = (
#     ('option1', 'Football'),
#     ('option2', 'Parking'),
#     ('option3', '12+ players'),
#     ('option4', '8+ players'),
# )
class Turf_Profile(models.Model):

    turf_id = models.AutoField(primary_key=True)
    turf_name = models.CharField(max_length=100,default="")
    turf_rating = models.DecimalField(max_digits=2,decimal_places=1,default=0.0)
    turf_category_1 = models.CharField(max_length=300,default="")
    turf_category_2 = models.CharField(max_length=300,default="")
    turf_category_3 = models.CharField(max_length=300,default="")
    turf_category_4 = models.CharField(max_length=300,default="")
    turf_description = models.CharField(max_length=300,default="")
    turf_rules_regulations = models.CharField(max_length=300,default="")
    turf_address = models.CharField(max_length=200,default="Please enter the address owner")
    turf_ownerContact_number = models.BigIntegerField(default=9999999991)
    # turf_reviews = models.CharField(max_length=200,default="")
    turf_price = models.IntegerField(default=9999991)
    turf_host_name = models.CharField(max_length=100,default="")
    turf_map = models.CharField(max_length=300,default="")
    turf_weekday_base = models.IntegerField(default=9999999)
    turf_weekday_peak = models.IntegerField(default=9999999)
    turf_friday_base = models.IntegerField(default=9999999)
    turf_friday_peak = models.IntegerField(default=9999999)
    turf_saturday_base = models.IntegerField(default=9999999)
    turf_saturday_peak = models.IntegerField(default=9999999)
    turf_sunday_base = models.IntegerField(default=9999999)
    turf_sunday_peak = models.IntegerField(default=9999999)
    # Make it Boolean
    # turf_field_1 = models.IntegerField(default=1)
    # turf_field_2 = models.IntegerField(default=2)
    # turf_field_3 = models.IntegerField(default=3)

    # Wase complete this
    peak_timeslot = models.JSONField(default=[])
    
    removed_timeslot = models.JSONField(default=[])
    custom_timeslot = models.JSONField(default=[
         "12-1 AM",
        "1-2 AM",
        "2-3 AM",
        "3-4 AM",
        "4-5 AM",
        "5-6 AM",
        "6-7 AM",
        "7-8 AM",
        "8-9 AM",
        "9-10 AM",
        "10-11 AM",
        "11-12 PM",
        "12-1 PM",
        "1-2 PM",
        "2-3 PM",
        "3-4 PM",
        "4-5 PM",
        "5-6 PM",
        "6-7 PM",
        "7-8 PM",
        "8-9 PM",
        "9-10 PM",
        "10-11 PM",
        "11-12 AM",
    ])
    peak_timeslot = models.JSONField(default=[
        "12-1 AM",
        "1-2 AM",
        "2-3 AM",
        "3-4 AM",
        "4-5 AM",
        "6-7 PM",
        "7-8 PM",
        "8-9 PM",
        "9-10 PM",
        "10-11 PM",
        "11-12 AM",
    ])

    def __str__(self):
        return self.turf_name

# To create new directory everytime a new Turf_Profile is created
# @receiver(post_save, sender=Turf_Profile)
# def create_turf_folder(sender, instance, created, **kwargs):
#     if created:
#         folder_path = os.path.join('media', 'BookTurf Main', str(instance.turf_id))
#         os.makedirs(folder_path, exist_ok=True)


class Turf_Pics(models.Model):
    turf_ref = models.ForeignKey(Turf_Profile, on_delete=models.CASCADE, null=True, blank=True)
    turf_picture = models.ImageField(upload_to="")

# To change the path of file stored--> Does not work!!
# @receiver(pre_save, sender=Turf_Pics)
# def change_path(sender, instance, **kwargs):
#         # arr_name = instance.turf_picture.url.split("/")
#         # instance.turf_picture.url =f"/{arr_name[1]}/{instance.turf_ref.turf_id}/{arr_name[2]}"
#
#         # current_path = sender.turf_picture.path
#         sender.turf_picture.field.upload_to = f"/media/BookTurfMain/{instance.turf_ref.turf_id}"
#         # os.makedirs(folder_path, exist_ok=True)



#
# # I want to do this because if there are many files then how to recognize which files are for which user
#     def save(self, *args, **kwargs):
#         # if self.turf_ref and self._state.adding:
#         if self.turf_ref:
#             custom_upload_path= f'BookTurfMain/{self.turf_ref.turf_id}/'
#             self.turf_picture.upload_to = custom_upload_path
#         #Can also do this
#         # super().save()
#         super(Turf_Pics, self).save(*args, **kwargs)


# def __str__(self):
#     return self.turf_picture

class Turf_Reviews(models.Model):
    Review_Turf_Profile = models.ForeignKey(Turf_Profile, on_delete=models.CASCADE, related_name='reviews')
    review_text = models.CharField(max_length=200, default="")
    rating = models.IntegerField(default=0)

    def __str__(self):
        return f"Review ID: {self.id}, Rating: {self.rating}"

# class Turf_index_profile(models.Model):
#     turf_id = models.AutoField(primary_key=True)
#     turf_name = models.CharField(max_length=100, default="")
#     turf_address = models.CharField(max_length=200, default="Please enter the address owner")
#     turf_rating = models.IntegerField(max_length=1, default=0)
#     turf_price = models.IntegerField(default=9999991)
#     turf_picture = models.ImageField(upload_to='BookTurf/BookTurfMain/media/BookTurfMain')
#     turf_new_profile = models.OneToOneField(Turf_Profile, on_delete=models.CASCADE,default="")

# def __str__(self):
#     return f"Turf name: {self.name}, ID: {self.ID}"


class addmin(models.Model):
    addmin_id = models.AutoField(primary_key=True)
    addmin_username = models.CharField(max_length=100, default="")
    addmin_password = models.CharField(max_length=100,default="")


class Turf_Booked(models.Model):
    turf_profile = models.ForeignKey(Turf_Profile,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    turf_price = models.IntegerField(default=999999999)
    turf_timeslot = models.CharField(default="timeslot...",max_length=200)
    turf_field_booked = models.IntegerField(default=999)
    # turf_transcation_id
