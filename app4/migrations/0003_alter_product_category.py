# Generated by Django 5.0 on 2025-07-12 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app4', '0002_product_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('electronics', 'Electronics'), ('fashion', 'Fashion'), ('books', 'Books'), ('home', 'Home'), ('toys', 'Toys'), ('car', 'car'), ('bicycle', 'bicycle'), ('clothe', 'clothe'), ('shoe', 'shoe'), ('bag', 'bag'), ('gun', 'gun'), ('cap', 'cap'), ('house', 'house')], default='other', max_length=50),
        ),
    ]
