from django.db import migrations

def copy_profiles_data(apps, schema_editor):
    # Accès aux anciens et nouveaux modèles via apps.get_model
    OldProfile = apps.get_model('oc_lettings_site', 'Profile')
    NewProfile = apps.get_model('profiles', 'Profile')
    User = apps.get_model('auth', 'User')

    for old_profile in OldProfile.objects.all():
        NewProfile.objects.create(
            user=old_profile.user,
            favorite_city=old_profile.favorite_city
        )

class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(copy_profiles_data),
    ]
