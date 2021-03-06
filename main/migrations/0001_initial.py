# Generated by Django 3.2.7 on 2021-10-02 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PANCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pan', models.CharField(max_length=15)),
                ('name', models.CharField(max_length=255)),
                ('fname', models.CharField(max_length=255)),
                ('birth', models.DateField()),
                ('photo', models.ImageField(upload_to='pan/photos/')),
                ('sign', models.ImageField(upload_to='pan/signs/')),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('razorpay_order_id', models.CharField(max_length=255)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('paid', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Voter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('epic', models.CharField(max_length=20)),
                ('name1', models.CharField(max_length=100)),
                ('name2', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('blck1', models.CharField(max_length=100)),
                ('blck2', models.CharField(default='', max_length=100)),
                ('subblock', models.CharField(max_length=100)),
                ('address1', models.CharField(blank=True, max_length=250, null=True)),
                ('address2', models.CharField(blank=True, max_length=250, null=True)),
                ('gender', models.CharField(max_length=100)),
                ('birth', models.DateField(blank=True, null=True)),
                ('gname1', models.CharField(max_length=100)),
                ('gname2', models.CharField(max_length=100)),
                ('partno', models.CharField(max_length=100)),
                ('partname1', models.CharField(max_length=100)),
                ('partname2', models.CharField(default='', max_length=100)),
                ('serialno', models.CharField(max_length=100)),
                ('guardian_title', models.CharField(max_length=100)),
                ('photo', models.ImageField(default='voter.png', upload_to='photos/')),
                ('barcode', models.ImageField(blank=True, null=True, upload_to='barcodes/')),
            ],
        ),
    ]
