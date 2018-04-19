from django.core.management.base import BaseCommand
import requests
import csv
import os
from django.core.management.base import BaseCommand
from consumption.models import Customer, Reading

class Command(BaseCommand):
    help = 'import data'

    def handle(self, *args, **options):
        with open('../data/user_data.csv') as f:
            reader = csv.DictReader(f)
            for row in reader:
                Customer.objects.update_or_create(id=row['id'], defaults=dict(
                    area=row['area'], tariff=row['tariff']
                ))

        Reading.objects.all().delete()
        for file_name in os.listdir('../data/consumption'):
            try:
                customer_id, extension = file_name.split('.')
            except ValueError:
                continue
            with open('../data/consumption/%s' % file_name) as f:
                reader = csv.DictReader(f)
                Reading.objects.bulk_create(
                    [
                        Reading(
                            customer_id=customer_id, timestamp=row['datetime'],
                            units=row['consumption']
                        ) for row in reader
                    ]
                )
    print("Implemented!")
