# Generated by Django 2.1 on 2022-01-21 06:25

import ckeditor.fields
import datetime
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
            name='bennar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10000)),
                ('image', models.ImageField(upload_to='uploads/product_image')),
            ],
        ),
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='contact_table',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1000)),
                ('email', models.CharField(max_length=1000)),
                ('message', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Discount_Coupon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10000)),
                ('code', models.CharField(max_length=10000)),
                ('discount_percentage', models.IntegerField(default='0')),
                ('active_status', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='EmailConfirmed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activation_key', models.CharField(max_length=500)),
                ('email_confirmed', models.BooleanField(default=False)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'User Email-Confirmed',
            },
        ),
        migrations.CreateModel(
            name='job_post_status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_post_status', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.CharField(max_length=1000)),
                ('items_json', models.TextField()),
                ('total_bill', models.CharField(max_length=1000)),
                ('company_name', models.CharField(blank=True, default='', max_length=1000, null=True)),
                ('full_address', models.TextField()),
                ('city', models.CharField(max_length=1000)),
                ('postal_code', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=1000)),
                ('phone', models.CharField(max_length=1000)),
                ('email', models.CharField(max_length=1000)),
                ('order_date', models.DateField(blank=True, default=datetime.datetime(2022, 1, 21, 12, 25, 55, 825231))),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='posted_jobs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_title', models.CharField(blank=True, max_length=1000)),
                ('company_name', models.CharField(blank=True, default='', max_length=1000)),
                ('job_details', models.TextField(blank=True)),
                ('qualification', models.CharField(blank=True, default='', max_length=1000)),
                ('job_location', models.CharField(blank=True, max_length=1000)),
                ('job_type', models.CharField(blank=True, max_length=100)),
                ('salary', models.CharField(blank=True, max_length=1000)),
                ('phone_number', models.CharField(blank=True, max_length=1000)),
                ('post_date', models.DateField(blank=True, default=datetime.datetime(2022, 1, 21, 12, 25, 55, 824233))),
                ('email', models.CharField(blank=True, max_length=1000)),
                ('job_post_status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='medicifyapp.job_post_status')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Product_Details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=500)),
                ('price', models.IntegerField()),
                ('currency_type', models.CharField(default='ZAR', max_length=1000)),
                ('description', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, default='', null=True, upload_to='uploads/product_image')),
                ('image2', models.ImageField(blank=True, default='', null=True, upload_to='uploads/product_image')),
                ('image3', models.ImageField(blank=True, default='', null=True, upload_to='uploads/product_image')),
                ('image4', models.ImageField(blank=True, default='', null=True, upload_to='uploads/product_image')),
                ('image5', models.ImageField(blank=True, default='', null=True, upload_to='uploads/product_image')),
                ('product_status', models.CharField(choices=[('New', 'New'), ('In stock', 'In stock'), ('Out stock', 'Out stock')], default='New', max_length=20)),
                ('catalogue', models.FileField(blank=True, default='', null=True, upload_to='uploads/catalogue')),
                ('datasheets', models.FileField(blank=True, default='', null=True, upload_to='uploads/datasheets')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='medicifyapp.Categories')),
            ],
        ),
        migrations.CreateModel(
            name='Subcategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Subcategory', models.CharField(max_length=255)),
                ('Category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='medicifyapp.Categories')),
            ],
            options={
                'verbose_name_plural': 'Subcategory',
            },
        ),
        migrations.AddField(
            model_name='product_details',
            name='subcategory',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='medicifyapp.Subcategory'),
        ),
    ]
