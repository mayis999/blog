# Generated by Django 4.2.5 on 2023-09-23 15:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentChannel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=16)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Payment Channel',
                'verbose_name_plural': 'Payment Channels',
            },
        ),
        migrations.RemoveField(
            model_name='project',
            name='insurance',
        ),
        migrations.AddField(
            model_name='project',
            name='insurance_amount',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=7),
        ),
        migrations.AddField(
            model_name='project',
            name='link',
            field=models.URLField(default=''),
        ),
        migrations.CreateModel(
            name='Refback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('login', models.CharField(max_length=256)),
                ('deposited_at', models.DateField()),
                ('deposit', models.DecimalField(decimal_places=2, max_digits=7)),
                ('wallet', models.CharField(max_length=256)),
                ('payment_channel', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='project.paymentchannel')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='project.project')),
            ],
            options={
                'verbose_name': 'Refback',
                'verbose_name_plural': 'Refbacks',
            },
        ),
        migrations.CreateModel(
            name='Insurance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('login', models.CharField(max_length=256)),
                ('withdraw', models.DecimalField(decimal_places=2, max_digits=7)),
                ('wallet', models.CharField(max_length=256)),
                ('payment_channel', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='project.paymentchannel')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='project.project')),
            ],
            options={
                'verbose_name': 'Insurance',
                'verbose_name_plural': 'Insurances',
            },
        ),
    ]
