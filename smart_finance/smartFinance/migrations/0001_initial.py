# Generated by Django 4.0.3 on 2022-03-15 22:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ExpenseGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_name', models.CharField(max_length=200)),
                ('group_creation_date', models.DateTimeField(verbose_name='Group Creation Date')),
            ],
        ),
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('expense_name', models.CharField(max_length=200)),
                ('expense_date', models.DateTimeField(verbose_name='Expense Date')),
                ('expense_amount', models.IntegerField(default=0)),
                ('expense', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='smartFinance.expensegroup')),
            ],
        ),
    ]