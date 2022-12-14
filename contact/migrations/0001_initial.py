# Generated by Django 4.1.3 on 2022-11-18 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('relationship', models.CharField(choices=[('family', 'Family'), ('friend', 'Friend'), ('work', 'Work'), ('other', 'Other')], max_length=200)),
            ],
        ),
    ]
