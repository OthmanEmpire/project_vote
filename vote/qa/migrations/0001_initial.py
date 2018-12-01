# Generated by Django 2.1.3 on 2018-12-01 20:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MAC',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mac_address', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='MCQ',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField(default='')),
                ('open_for_voting', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='MCQOption',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('option', models.TextField(default='')),
                ('totalVotes', models.IntegerField(default=0)),
                ('MCQ_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='qa.MCQ')),
            ],
        ),
        migrations.CreateModel(
            name='OptionVoting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unique', models.IntegerField(default=0)),
                ('MCQ_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='qa.MCQ')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField(default='')),
                ('votes', models.IntegerField(default=0)),
                ('isAppropriate', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='QuestionVoting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unique', models.CharField(default='0.0.0.0', max_length=15)),
                ('question_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='qa.Question')),
            ],
        ),
    ]