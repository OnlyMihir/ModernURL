# Generated by Django 2.1.5 on 2019-09-22 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='shortenedurl',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('sh_url', models.CharField(max_length=50)),
                ('desc', models.CharField(max_length=50)),
                ('org_url', models.CharField(max_length=50)),
                ('is_ent_user', models.BooleanField(default=False)),
            ],
        ),
    ]
