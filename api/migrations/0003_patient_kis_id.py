# Generated by Django 4.0.2 on 2022-02-06 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_patient_gender'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='kis_id',
            field=models.CharField(default='12345678', max_length=12),
            preserve_default=False,
        ),
    ]