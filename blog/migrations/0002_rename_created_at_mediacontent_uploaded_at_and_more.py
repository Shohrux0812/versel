# Generated by Django 5.1.4 on 2025-01-22 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mediacontent',
            old_name='created_at',
            new_name='uploaded_at',
        ),
        migrations.RemoveField(
            model_name='mediacontent',
            name='description',
        ),
        migrations.RemoveField(
            model_name='mediacontent',
            name='media_type',
        ),
        migrations.AlterField(
            model_name='mediacontent',
            name='title',
            field=models.CharField(max_length=255),
        ),
    ]
