# Generated by Django 5.0.3 on 2024-04-12 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skin_treatment', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agemodel',
            name='age',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='reacttonewproductsmodel',
            name='react_to_new_products',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='sensitivemodel',
            name='senstive',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='skincaretexturemodel',
            name='skin_texture',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='skinconernmodel',
            name='skin_concern',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='skintypemodel',
            name='skin_type',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='sleepcyclemodel',
            name='sleep_cycle',
            field=models.CharField(max_length=55),
        ),
        migrations.AlterField(
            model_name='treatmentmodel',
            name='treatment',
            field=models.CharField(max_length=255),
        ),
    ]