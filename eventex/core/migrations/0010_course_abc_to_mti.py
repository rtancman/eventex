# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-29 15:04
from __future__ import unicode_literals

from django.db import migrations


def copy_src_to_dst(Source, Destination):
    for src in Source.objects.all():
        dst = Destination(
            title=src.title,
            start=src.start,
            description=src.description,
            slots=src.slots
        )
        dst.save()
        dst.speakers.set(src.speakers.all())
        src.delete()

def forward_course_abd_to_dst(apps, schema_editor):
    """
    para cada src, instanciar um dst com todos os atributos
    salvar o dst
    associar os speakers do src no dst
    deletar src
    """
    copy_src_to_dst(
        apps.get_model('core', 'CourseOld'),
        apps.get_model('core', 'Course')
    )

def backward_course_abd_to_dst(apps, schema_editor):
    """
    para cada src, instanciar um dst com todos os atributos
    salvar o dst
    associar os speakers do src no dst
    deletar src
    """
    copy_src_to_dst(
        apps.get_model('core', 'CourseOld'),
        apps.get_model('core', 'Course')
    )


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_course'),
    ]

    operations = [
        migrations.RunPython(forward_course_abd_to_dst,
                             backward_course_abd_to_dst)
    ]
