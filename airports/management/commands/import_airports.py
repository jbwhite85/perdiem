import csv
import decimal
from django.core.management.base import BaseCommand
from airports.models import Airport


class Command(BaseCommand):
    def add_arguments(self, parser):
            parser.add_argument('csvfile', type=str)

    def handle(self, *args, **kwargs):
        filename = kwargs['csvfile']
        try:
            f = open(filename, 'r')
        except FileNotFoundError:
            print(f'File: "{filename}" not found')
            return

        csv_data = csv.DictReader(f)
        for row in csv_data:

            fields = {
                'name': row['name'],
                'latitude': decimal.Decimal(row['latitude_deg']),
                'longitude': decimal.Decimal(row['longitude_deg']),
                'country': row['iso_country'],
                'region': row['iso_region'].split('-', 1)[1],
                'municipality': row['municipality']
            }

            airport, created = Airport.objects.get_or_create(
                identifier=row['ident'],
                defaults=fields)

            if not created:
                for field, value in fields.items():
                    setattr(airport, field, value)
                airport.save()

        print('Data Imported Successfully')
