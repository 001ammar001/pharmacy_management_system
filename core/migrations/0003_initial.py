# Generated by Django 4.1.7 on 2023-05-14 14:20

from django.db import migrations

def apply_migration(apps, schema_editor):
    Role = apps.get_model('core', 'Role')
    Role.objects.bulk_create([
        Role(name=u'saller'),
        Role(name=u'purcher'),
        Role(name=u'pharmacy_manager'),
        Role(name=u'manager'),
    ])

def revert_migration(apps, schema_editor):
    Role = apps.get_model('core', 'Role')
    Role.objects.filter(
        name__in=[
            u'saller',
            u'purcher',
            u'pharmacy_manager',
            u'manager',
        ]
    ).delete()

class Migration(migrations.Migration):

    dependencies = [
        ('custom', '0001_initial'),
        ('core', '0001_initial'),
        ('core', '0002_initial'),
    ]

    operations = [
        migrations.RunPython(apply_migration, revert_migration)
    ]

