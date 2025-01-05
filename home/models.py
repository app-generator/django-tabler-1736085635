# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Project(models.Model):

    #__Project_FIELDS__
    name = models.CharField(max_length=255, null=True, blank=True)

    #__Project_FIELDS__END

    class Meta:
        verbose_name        = _("Project")
        verbose_name_plural = _("Project")


class Jujucontroller(models.Model):

    #__Jujucontroller_FIELDS__
    name = models.CharField(max_length=255, null=True, blank=True)
    juju_version = models.ForeignKey(JujuVersion, on_delete=models.CASCADE)

    #__Jujucontroller_FIELDS__END

    class Meta:
        verbose_name        = _("Jujucontroller")
        verbose_name_plural = _("Jujucontroller")


class Jujuversion(models.Model):

    #__Jujuversion_FIELDS__
    display = models.CharField(max_length=255, null=True, blank=True)

    #__Jujuversion_FIELDS__END

    class Meta:
        verbose_name        = _("Jujuversion")
        verbose_name_plural = _("Jujuversion")



#__MODELS__END
