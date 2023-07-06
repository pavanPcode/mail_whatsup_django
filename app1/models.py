from django.db import models

# Create your models here.


# class Messagesdetails(models.Model):
#     customerid = models.CharField(db_column='Customerid', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     customernmae = models.CharField(db_column='CustomerNmae', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     mobile = models.CharField(max_length=10, blank=True, null=True)
#     email = models.CharField(max_length=255, blank=True, null=True)
#     message = models.CharField(db_column='Message', max_length=1500, blank=True, null=True)  # Field name made lowercase.
#     sendingtime = models.DateTimeField(db_column='sendingTime', blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'messagesdetails'
#
#
#
#
# class Customer(models.Model):
#     customernmae = models.CharField(db_column='CustomerNmae', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     mobile = models.CharField(max_length=50, blank=True, null=True)
#     email = models.CharField(max_length=255, blank=True, null=True)
#     adress = models.CharField(db_column='Adress', max_length=255, blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'customer'