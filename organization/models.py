from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from simple_history.models import HistoricalRecords

class Organization (models.Model):
    org_id = models.CharField(max_length=10, unique=True )
    org_name = models.CharField (max_length=50)
    #history = HistoricalRecords()
    comments = models.TextField (blank=True)
    is_active = models.BooleanField(default=True)

    def __str__ (self):
        return self.org_id+ ":" +self.org_name  


class Employee (models.Model):
    class Sex (models.TextChoices):
        MALE = 'M', _('Male')
        FEMALE = 'F', _('Female')
        OTHER = 'O', _('Other')

    class EmployeeType (models.TextChoices):
        PERMANENT = 'P', _('Permanent')
        TEMPORARY = 'T', _('Temporary')
        CONTRACT = 'C', _('Contract')

    employee_id = models.CharField(max_length=20, unique=True)
    full_name = models.CharField(max_length=50)
    entry_date = models.DateField(help_text='Joining Date')
    exit_date = models.DateField()
    email = models.EmailField (null = True, blank = True)
    #TODO
    #picture = models.ImageField (upload_to='uploads/%Y/%m/')
    #MEDIA_ROOT may need to be set for uploads to work
    supervisor = models.ForeignKey (
        'self',
        limit_choices_to={'is_active':True},
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True
    )
    org = models.ForeignKey (
        'Organization', 
        on_delete=models.CASCADE,
        limit_choices_to={'is_active':True},
        null=True
    )
    org_unit = models.ForeignKey (
        'OrgUnit',
        limit_choices_to={'is_active':True},
        on_delete=models.SET_NULL, 
        null = True
    )
    time_percent = models.IntegerField('100 if Full Time')
    sex = models.CharField (max_length=1, choices= Sex.choices, blank= True)
    comments = models.TextField (blank=True,null=True)
    is_active = models.BooleanField(default=True)
    is_org_admin = models.BooleanField(default=False)
    history = HistoricalRecords()
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True, 
        blank=True
    )

    def __str__ (self):
        return self.full_name   




class OrgUnit (models.Model):
    ou_id = models.CharField(max_length=20, unique=True)
    ou_name = models.CharField (max_length=50)
    manager = models.ForeignKey(
        'Employee',
        limit_choices_to={'is_active':True},
        on_delete=models.SET_NULL,
        related_name='ou_manager',
        blank=True, 
        null=True
    )
    delegate = models.ForeignKey(
        'Employee',
        limit_choices_to={'is_active':True}, 
        on_delete=models.SET_NULL, 
        related_name='ou_delegate',
        blank=True, 
        null=True
    )
    org = models.ForeignKey (
        'Organization',
        limit_choices_to={'is_active':True}, 
        on_delete=models.CASCADE, 
        null=True
    )
    parent_ou = models.ForeignKey (
        'self', 
        limit_choices_to={'is_active':True},
        on_delete=models.SET_NULL, 
        blank=True, 
        null=True 
    )
    comments = models.TextField (blank=True,null=True)
    is_active = models.BooleanField(default=True)
    history = HistoricalRecords()
            
    def __str__ (self):
        return self.ou_name
    