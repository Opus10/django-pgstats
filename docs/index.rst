django-pgstats
==============

``django-pgstats`` provides commands and models for tracking internal postgres
stats. Specifically, the `IndexStats` model stores stats about postgres
indices and the `TableStats` model stores stats about postgres tables.

Usage
-----

Postgres stat tables contain global statistical information. ``django-pgstats``
is meant to be executed periodically so that one can later analyze table
and index usage. This is done by periodically calling
``python manage.py snapshot_pgstats`` using a task runner such
as [Celery](http://www.celeryproject.org/).

Stats are stored as JSON fields in the respective `IndexStats` and `TableStats`
models. Each key in the JSON field is in the format of
``{schema}.{table}`` for table stats or ``{schema}.{table}.{index}`` for index
stats.

Compatibility
-------------

``django-pgstats`` is compatible with Python 3.7 -- 3.11, Django 3.2 -- 4.2, Psycopg 2 -- 3 and Postgres 12 -- 15.
