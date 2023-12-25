# Generated by Django 4.2.8 on 2023-12-24 19:45

from django.db import migrations, models
import django.db.models.deletion
import stdimage.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('schoolApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Conductor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('phoneNumber', models.CharField(blank=True, max_length=10, null=True)),
                ('experience', models.CharField(blank=True, max_length=200, null=True)),
                ('address', models.CharField(blank=True, max_length=500, null=True)),
                ('photo', stdimage.models.StdImageField(blank=True, force_min_size=False, null=True, upload_to='StudentImage', variations={'thumbnail': {'height': 250, 'width': 250}})),
                ('datetime', models.DateTimeField(auto_now_add=True)),
                ('lastUpdatedOn', models.DateTimeField(auto_now=True)),
                ('isDeleted', models.BooleanField(default=False)),
                ('schoolID', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='schoolApp.schooldetail')),
                ('sessionID', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='schoolApp.schoolsession')),
            ],
        ),
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('phoneNumber', models.CharField(blank=True, max_length=10, null=True)),
                ('experience', models.CharField(blank=True, max_length=200, null=True)),
                ('address', models.CharField(blank=True, max_length=500, null=True)),
                ('photo', stdimage.models.StdImageField(blank=True, force_min_size=False, null=True, upload_to='StudentImage', variations={'thumbnail': {'height': 250, 'width': 250}})),
                ('datetime', models.DateTimeField(auto_now_add=True)),
                ('lastUpdatedOn', models.DateTimeField(auto_now=True)),
                ('isDeleted', models.BooleanField(default=False)),
                ('schoolID', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='schoolApp.schooldetail')),
                ('sessionID', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='schoolApp.schoolsession')),
            ],
        ),
        migrations.CreateModel(
            name='StudentVehicleAssign',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fee', models.CharField(blank=True, max_length=100, null=True)),
                ('description', models.CharField(blank=True, max_length=500, null=True)),
                ('startDate', models.DateField(blank=True, null=True)),
                ('datetime', models.DateTimeField(auto_now_add=True)),
                ('lastUpdatedOn', models.DateTimeField(auto_now=True)),
                ('isDeleted', models.BooleanField(default=False)),
                ('schoolID', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='schoolApp.schooldetail')),
                ('sessionID', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='schoolApp.schoolsession')),
                ('studentID', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='schoolApp.studentdetail')),
            ],
        ),
        migrations.CreateModel(
            name='VehicleDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('number', models.CharField(blank=True, max_length=10, null=True)),
                ('terminal', models.CharField(blank=True, max_length=200, null=True)),
                ('seatCapacity', models.CharField(blank=True, max_length=100, null=True)),
                ('datetime', models.DateTimeField(auto_now_add=True)),
                ('lastUpdatedOn', models.DateTimeField(auto_now=True)),
                ('isDeleted', models.BooleanField(default=False)),
                ('conductorID', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Transport.conductor')),
                ('driverID', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Transport.driver')),
                ('schoolID', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='schoolApp.schooldetail')),
                ('sessionID', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='schoolApp.schoolsession')),
            ],
        ),
        migrations.CreateModel(
            name='VehicleExpenses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cost', models.CharField(blank=True, max_length=100, null=True)),
                ('expenseType', models.CharField(blank=True, max_length=100, null=True)),
                ('description', models.CharField(blank=True, max_length=500, null=True)),
                ('expenseDate', models.DateField(blank=True, null=True)),
                ('datetime', models.DateTimeField(auto_now_add=True)),
                ('lastUpdatedOn', models.DateTimeField(auto_now=True)),
                ('isDeleted', models.BooleanField(default=False)),
                ('schoolID', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='schoolApp.schooldetail')),
                ('sessionID', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='schoolApp.schoolsession')),
                ('vehicleID', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Transport.vehicledetail')),
            ],
        ),
        migrations.CreateModel(
            name='StudentVehicleFee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('month', models.CharField(blank=True, max_length=100, null=True)),
                ('note', models.TextField(blank=True, null=True)),
                ('payDate', models.DateField(blank=True, null=True)),
                ('isPaid', models.BooleanField(default=False)),
                ('datetime', models.DateTimeField(auto_now_add=True)),
                ('lastUpdatedOn', models.DateTimeField(auto_now=True)),
                ('isDeleted', models.BooleanField(default=False)),
                ('schoolID', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='schoolApp.schooldetail')),
                ('sessionID', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='schoolApp.schoolsession')),
                ('studentID', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='schoolApp.studentdetail')),
                ('studentVehicleAssignID', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Transport.studentvehicleassign')),
            ],
        ),
        migrations.AddField(
            model_name='studentvehicleassign',
            name='vehicleID',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Transport.vehicledetail'),
        ),
    ]