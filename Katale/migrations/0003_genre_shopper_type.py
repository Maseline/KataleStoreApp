# Generated by Django 2.0.2 on 2018-05-30 14:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Katale', '0002_genre_product_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='genre',
            name='shopper_type',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Katale.Gender'),
            preserve_default=False,
        ),
    ]
