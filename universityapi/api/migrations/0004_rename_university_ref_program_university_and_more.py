# Generated by Django 4.2.2 on 2023-08-22 19:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_rename_university_program_university_ref_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='program',
            old_name='university_ref',
            new_name='university',
        ),
        migrations.RemoveField(
            model_name='student',
            name='program_ref',
        ),
    ]
