# Generated by Django 4.2.1 on 2023-05-16 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0004_alter_student_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='gender',
            field=models.CharField(max_length=6, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='level',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='mobile',
            field=models.CharField(max_length=11, null=True),
        ),
    ]
