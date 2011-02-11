# -*- coding: utf -*-
from django.db import models
from django.forms import ModelForm

class InputDev( models.Model ):
    dev_id = models.AutoField( primary_key=True )
    model = models.CharField( max_length=255, unique=True )
    expl_start_date = models.DateField()
    scan_mode = models.CharField( max_length=255 )

    def __unicode__( self ):
        return self.model

    class Meta:
        ordering = ['-dev_id']

class OutputDev( models.Model ):
    dev_id = models.AutoField( primary_key=True )
    model = models.CharField( max_length=255 )
    expl_start_date = models.DateField()
    cartridge_id = models.PositiveIntegerField()
    print_mode = models.CharField( max_length=255 )

<<<<<<< HEAD
    class Meta:
        ordering = ['-dev_id']

    def __unicode__( self ):
        return self.model

class Paper( models.Model ):
    dev_id = models.AutoField( primary_key=True )
    paper_type = models.CharField( max_length=255 )
    
    class Meta:
        ordering = ['-dev_id']
