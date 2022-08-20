from django.core.management.base import BaseCommand

import pgstats.models


class Command(BaseCommand):
    help = "Snapshot postgres table and index stats"

    def handle(self, *args, **options):
        pgstats.models.IndexStats.objects.create_snapshot()
        pgstats.models.TableStats.objects.create_snapshot()
