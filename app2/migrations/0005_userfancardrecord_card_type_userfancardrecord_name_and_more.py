# Generated by Django 5.0 on 2025-07-07 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app2', '0004_storefancard_userfancardrecord_delete_userfanscard'),
    ]

    operations = [
        migrations.AddField(
            model_name='userfancardrecord',
            name='card_type',
            field=models.CharField(default=0.9995064165844028, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userfancardrecord',
            name='name',
            field=models.CharField(default=2025, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userfancardrecord',
            name='price',
            field=models.DecimalField(decimal_places=2, default=2, max_digits=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userfancardrecord',
            name='quantity',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
