# Generated by Django 4.0 on 2021-12-27 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yaho_app', '0004_alter_application_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='nation',
            field=models.CharField(db_column='nation', default='kor', max_length=40),
        ),
    ]