# Generated by Django 4.2.1 on 2023-06-04 11:13

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
            name='Korisnik',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ime', models.CharField(blank=True, max_length=255, null=True)),
                ('prezime', models.CharField(blank=True, max_length=255, null=True)),
                ('fotografija', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('interesi', models.CharField(blank=True, max_length=255, null=True)),
                ('veshtini', models.CharField(blank=True, max_length=255, null=True)),
                ('profesija', models.CharField(blank=True, max_length=255, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Objava',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('naslov', models.CharField(max_length=255)),
                ('sodrzina', models.TextField()),
                ('files', models.FileField(blank=True, null=True, upload_to='files/')),
                ('datum_kreiranje', models.DateTimeField()),
                ('posledna_promena', models.DateTimeField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.korisnik')),
            ],
        ),
        migrations.CreateModel(
            name='Komentar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sodrzina', models.TextField()),
                ('datum', models.DateTimeField()),
                ('objava', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.objava')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.korisnik')),
            ],
        ),
        migrations.CreateModel(
            name='Blokiran',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blokiral', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blokiran', to='app.korisnik')),
                ('blokiran', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blokiral', to='app.korisnik')),
            ],
        ),
    ]
