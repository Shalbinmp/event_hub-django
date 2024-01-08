# Generated by Django 3.2.23 on 2023-12-17 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Complaint',
            fields=[
                ('complaint_id', models.AutoField(primary_key=True, serialize=False)),
                ('complaint', models.CharField(max_length=45)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('reply', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'complaint',
                'managed': False,
            },
        ),
    ]
