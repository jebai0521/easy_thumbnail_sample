# -*- coding: utf-8 -*-
'''
Created on 2014年12月15日

@author: jebai
'''

from django.db import models
from easy_thumbnails.fields import ThumbnailerImageField

# PPT讲义
class PPT(models.Model):
    
    name = models.CharField(max_length=30, verbose_name=u"讲义标题")

    class Meta:
        verbose_name = u'讲义PPT'
        verbose_name_plural = u'讲义PPT'
        ordering = ['id']
        pass
        
    def __unicode__(self):
        return self.name

# PPT讲义图片
class PPTItem(models.Model):
    
    ppt = models.ForeignKey(PPT, verbose_name=u"讲义")
    image = ThumbnailerImageField(u"讲义图片", upload_to="./ppt")

    class Meta:
        verbose_name = u'讲义PPT图片'
        verbose_name_plural = u'讲义PPT图片'
        ordering = ['id']
        
    def __unicode__(self):
        return str(self.id)
    