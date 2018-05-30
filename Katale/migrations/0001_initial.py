# Generated by Django 2.0.2 on 2018-05-30 13:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Gender',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(max_length=50)),
                ('slug', models.SlugField()),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre', models.CharField(max_length=100)),
                ('slug', models.SlugField()),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=100)),
                ('size', models.CharField(blank=True, max_length=50)),
                ('description', models.TextField()),
                ('price', models.IntegerField()),
                ('date_created', models.DateField()),
                ('quantity', models.PositiveIntegerField()),
                ('image', models.ImageField(upload_to='media/')),
                ('gender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Katale.Gender')),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Katale.Genre')),
            ],
            options={
                'verbose_name_plural': 'Products',
            },
        ),
        migrations.CreateModel(
            name='ProductType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_type', models.CharField(max_length=100)),
                ('slug', models.SlugField()),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Katale.ProductType'),
        ),
    ]
