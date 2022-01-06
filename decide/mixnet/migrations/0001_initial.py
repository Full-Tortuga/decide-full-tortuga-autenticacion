# Generated by Django 2.2.5 on 2022-01-06 16:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mixnet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('voting_id', models.PositiveIntegerField()),
                ('auth_position', models.PositiveIntegerField(default=0)),
                ('type', models.CharField(choices=[('V', 'Voting'), ('BV', 'BinaryVoting'), ('MV', 'MultipleVoting'), ('SV', 'ScoreVoting')], default='V', max_length=2)),
                ('auths', models.ManyToManyField(related_name='mixnets', to='base.Auth')),
                ('key', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='mixnets', to='base.Key')),
                ('pubkey', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='mixnets_pub', to='base.Key')),
            ],
        ),
    ]
