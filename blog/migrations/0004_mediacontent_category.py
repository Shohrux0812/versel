# Generated by Django 5.1.4 on 2025-01-22 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_blog'),
    ]

    operations = [
        migrations.AddField(
            model_name='mediacontent',
            name='category',
            field=models.CharField(choices=[('lecture', 'Maruza'), ('practice', 'Amaliy ish'), ('lab', 'Laboratoriya'), ('other', 'Boshqalar')], default='other', max_length=10),
        ),
    ]
