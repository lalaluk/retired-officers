# Generated by Django 5.0.2 on 2024-03-05 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_alter_activity_score_label_and_more'),
        ('user', '0002_student_activity_student_graduated_school'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='user',
            managers=[
            ],
        ),
        migrations.AlterField(
            model_name='student',
            name='activity',
            field=models.ManyToManyField(related_name='student', to='myapp.activity'),
        ),
    ]