# Generated by Django 5.0.4 on 2024-05-03 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_bookmodel_created_at_bookmodel_updated_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookmodel',
            name='image',
            field=models.ImageField(null=True, upload_to='books-images'),
        ),
    ]
