# Generated by Django 4.0.1 on 2022-02-03 15:00

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coefficient',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=2)),
                ('count', models.DecimalField(decimal_places=2, max_digits=3)),
            ],
        ),
        migrations.CreateModel(
            name='Coefficients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Entrants',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('priority', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)])),
                ('point', models.DecimalField(decimal_places=3, max_digits=6)),
                ('type', models.CharField(max_length=1)),
                ('submited_docs', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Marks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Points',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('count', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name='Quota',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('quota', models.CharField(max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='Quotas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('subject_name', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='SubjectPoints',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('point', models.DecimalField(decimal_places=2, max_digits=2)),
            ],
        ),
        migrations.CreateModel(
            name='University',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('university_name', models.TextField()),
                ('faculty_name', models.TextField()),
                ('speciality_name', models.TextField()),
                ('edu_program', models.TextField()),
                ('degree', models.CharField(max_length=32)),
                ('year', models.DateField(auto_now=True)),
            ],
        ),
        migrations.AddIndex(
            model_name='university',
            index=models.Index(fields=['university_name'], name='DB_universi_univers_58c878_idx'),
        ),
        migrations.AddField(
            model_name='subjectpoints',
            name='subject_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='DB.subject'),
        ),
        migrations.AddField(
            model_name='subjectpoints',
            name='university_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='DB.university'),
        ),
        migrations.AddIndex(
            model_name='subject',
            index=models.Index(fields=['subject_name'], name='DB_subject_subject_5bc157_idx'),
        ),
        migrations.AddField(
            model_name='quotas',
            name='entrants_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='DB.entrants'),
        ),
        migrations.AddField(
            model_name='quotas',
            name='quota_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='DB.quota'),
        ),
        migrations.AddIndex(
            model_name='quota',
            index=models.Index(fields=['quota'], name='DB_quota_quota_c2b4c3_idx'),
        ),
        migrations.AddField(
            model_name='marks',
            name='entrants_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='DB.entrants'),
        ),
        migrations.AddField(
            model_name='marks',
            name='point_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='DB.points'),
        ),
        migrations.AddField(
            model_name='marks',
            name='subject_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='DB.subject'),
        ),
        migrations.AddField(
            model_name='entrants',
            name='university_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='DB.university'),
        ),
        migrations.AddField(
            model_name='coefficients',
            name='coefficient_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='DB.coefficient'),
        ),
        migrations.AddField(
            model_name='coefficients',
            name='entrants_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='DB.entrants'),
        ),
        migrations.AddIndex(
            model_name='coefficient',
            index=models.Index(fields=['name'], name='DB_coeffici_name_355f84_idx'),
        ),
    ]