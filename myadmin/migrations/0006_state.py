# Generated by Django 4.1.7 on 2023-03-29 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myadmin', '0005_delete_company'),
    ]

    operations = [
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('states', models.CharField(max_length=150)),
            ],
            options={
                'db_table': 'state',
            },
        ),
    ]