# Generated by Django 5.0.6 on 2024-07-08 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0007_alter_islam_mechet_fard'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vredprivichki',
            name='telefon',
            field=models.BooleanField(),
        ),
    ]