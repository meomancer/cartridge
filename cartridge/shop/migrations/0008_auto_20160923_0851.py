# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import cartridge.shop.fields


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_auto_20150921_2323'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='billing_detail_company',
            field=models.CharField(max_length=100, verbose_name='Company', blank=True),
        ),
        migrations.AddField(
            model_name='order',
            name='billing_detail_vat_number',
            field=models.CharField(max_length=24, verbose_name='VAT No.', blank=True),
        ),
        migrations.AlterField(
            model_name='productoption',
            name='type',
            field=models.IntegerField(verbose_name='Type', choices=[(1, b'Course date'), (2, b'Course venue')]),
        ),
        migrations.AlterField(
            model_name='productvariation',
            name='option1',
            field=cartridge.shop.fields.OptionField(max_length=50, null=True, verbose_name=b'Course date'),
        ),
        migrations.AlterField(
            model_name='productvariation',
            name='option2',
            field=cartridge.shop.fields.OptionField(max_length=50, null=True, verbose_name=b'Course venue'),
        ),
    ]
