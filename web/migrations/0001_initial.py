# Generated by Django 4.0.2 on 2022-04-19 09:17

from django.db import migrations, models
import versatileimagefield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='about',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('about banana divine', 'about banana divine'), ('why banana divine', 'why banana divine'), ('vision', 'vision'), ('mission', 'mission')], max_length=50, unique=True)),
                ('content', models.TextField(max_length=2000)),
            ],
        ),
        migrations.CreateModel(
            name='about_banana_divine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=70)),
                ('bold_content', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='background_image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_one', versatileimagefield.fields.VersatileImageField(blank=True, upload_to='background_image')),
                ('image_ppoi_one', versatileimagefield.fields.PPOIField(default='0.5x0.5', editable=False, max_length=20)),
                ('image_two', versatileimagefield.fields.VersatileImageField(blank=True, upload_to='background_image')),
                ('image_ppoi_two', versatileimagefield.fields.PPOIField(default='0.5x0.5', editable=False, max_length=20)),
                ('image_three', versatileimagefield.fields.VersatileImageField(blank=True, upload_to='background_image')),
                ('image_ppoi_three', versatileimagefield.fields.PPOIField(default='0.5x0.5', editable=False, max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='banner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(max_length=100)),
                ('content', models.TextField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(max_length=100)),
                ('image', versatileimagefield.fields.VersatileImageField(upload_to='blog')),
                ('image_ppoi', versatileimagefield.fields.PPOIField(default='0.5x0.5', editable=False, max_length=20)),
                ('date', models.DateField(auto_now=True)),
                ('category', models.CharField(blank=True, max_length=50, null=True)),
                ('content', models.TextField(max_length=10000)),
            ],
        ),
        migrations.CreateModel(
            name='CheckProcess',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content', models.CharField(max_length=250)),
                ('video', models.FileField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='CompanyDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=250)),
                ('mailid', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=15)),
                ('location', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=50)),
                ('subject', models.CharField(max_length=200)),
                ('message', models.TextField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', versatileimagefield.fields.VersatileImageField(upload_to='gallery')),
                ('image_ppoi', versatileimagefield.fields.PPOIField(default='0.5x0.5', editable=False, max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('price', models.CharField(max_length=50)),
                ('description', models.TextField(max_length=300)),
                ('image', models.ImageField(upload_to='Product')),
            ],
        ),
        migrations.CreateModel(
            name='Progress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('summary', models.CharField(max_length=250)),
                ('count1', models.CharField(max_length=50)),
                ('discription1', models.CharField(max_length=100)),
                ('count2', models.CharField(max_length=50)),
                ('discription2', models.CharField(max_length=100)),
                ('count3', models.CharField(max_length=50)),
                ('discription3', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='social_media',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('social_media', models.CharField(choices=[('facebook', 'facebook'), ('instagramme', 'instagramme'), ('snapchat', 'snapchat'), ('twiter', 'twiter'), ('youtube', 'youtube')], max_length=70, unique=True)),
                ('link', models.URLField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='team')),
                ('description', models.TextField(max_length=300)),
                ('facebook', models.URLField(blank=True, max_length=100, null=True)),
                ('twiter', models.URLField(blank=True, max_length=100, null=True)),
                ('instagram', models.URLField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField(max_length=300)),
                ('image', models.ImageField(upload_to='testimonial')),
                ('destination', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Testimonial_Heading',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(max_length=60)),
                ('content', models.CharField(max_length=100)),
            ],
        ),
    ]
