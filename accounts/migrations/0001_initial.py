# Generated by Django 2.2.14 on 2020-08-29 03:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profesion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='profesion')),
                ('abbreviation', models.CharField(max_length=10, verbose_name='abreviatura')),
            ],
            options={
                'verbose_name': 'profesion',
                'verbose_name_plural': 'profesiones',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Profesional',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email_prof', models.EmailField(max_length=254, unique=True)),
                ('matricula', models.IntegerField(default=0)),
                ('servicio', models.TextField(blank=True, null=True)),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Profesionales',
                'ordering': ['usuario__last_name'],
            },
        ),
        migrations.CreateModel(
            name='Especialidad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='especialidad')),
                ('info', models.CharField(blank=True, max_length=100, null=True, verbose_name='detalle')),
                ('profesion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Profesion')),
            ],
            options={
                'verbose_name_plural': 'especialidades',
                'ordering': ['profesion', 'name'],
            },
        ),
        migrations.AddConstraint(
            model_name='especialidad',
            constraint=models.UniqueConstraint(fields=('profesion', 'name'), name='profesion - especialidad'),
        ),
    ]
