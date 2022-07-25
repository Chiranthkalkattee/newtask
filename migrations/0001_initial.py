# Generated by Django 4.0.6 on 2022-07-22 06:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Candidate_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(choices=[('male', 'male'), ('Female', 'Female')], default='fill', max_length=25)),
                ('skills', models.CharField(choices=[('python', 'python'), ('java', 'java'), ('c', 'c')], default='fill the skills', max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='skill_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_skills', models.CharField(choices=[('django', 'django'), ('nodejs', 'nodejs'), ('express', 'express')], default='fill', max_length=200)),
                ('level', models.IntegerField(default=0)),
                ('skill_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='skill', to='flexibeecandidate.candidate_details')),
            ],
        ),
    ]
