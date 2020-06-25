from django.contrib.postgres.fields import JSONField
from django.core.serializers.json import DjangoJSONEncoder
from django.db import connection
from django.db import models


def dict_fetchall(cursor):
    """Returns all rows from a cursor as a dict"""
    desc = cursor.description
    return [
        dict(zip((col[0] for col in desc), row)) for row in cursor.fetchall()
    ]


class IndexStatsManager(models.Manager):
    def create_snapshot(self):
        return self.create(stats=self.get_stats())

    def get_stats(self):
        cursor = connection.cursor()
        cursor.execute(
            "select * from pg_stat_all_indexes where schemaname='public'"
        )
        rows = dict_fetchall(cursor)
        return {
            f'{row["schemaname"]}.{row["relname"]}.{row["indexrelname"]}': row
            for row in rows
        }


class IndexStats(models.Model):
    """For storing snapshots of postgres index stats"""

    created_at = models.DateTimeField(auto_now_add=True)
    stats = JSONField(encoder=DjangoJSONEncoder)

    objects = IndexStatsManager()


class TableStatsManager(models.Manager):
    def create_snapshot(self):
        return self.create(stats=self.get_stats())

    def get_stats(self):
        cursor = connection.cursor()
        cursor.execute(
            "select * from pg_stat_all_tables where schemaname='public'"
        )
        rows = dict_fetchall(cursor)
        return {f'{row["schemaname"]}.{row["relname"]}': row for row in rows}


class TableStats(models.Model):
    """For storing snapshots of postgres table stats"""

    created_at = models.DateTimeField(auto_now_add=True)
    stats = JSONField(encoder=DjangoJSONEncoder)

    objects = TableStatsManager()
