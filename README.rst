django-pgstats
########################################################################

``django-pgstats`` provides commands and models for tracking internal postgres
stats. Specifically, the `IndexStats` model stores stats about postgres
indices and the `TableStats` model stores stats about postgres tables.

Postgres stat tables contain global statistical information. ``django-pgstats``
is meant to be executed periodically so that one can later analyze table
and index usage. This is done by periodically calling
``python manage.py snapshot_pgstats`` using a task runner such
as [Celery](http://www.celeryproject.org/).

Stats are stored as JSON fields in the respective `IndexStats` and `TableStats`
models. Each key in the JSON field is in the format of
``{schema}.{table}`` for table stats or ``{schema}.{table}.{index}`` for index
stats.

Documentation
=============

`View the django-pgstats docs here
<https://django-pgstats.readthedocs.io/>`_.

Installation
============

Install django-pgstats with::

    pip3 install django-pgstats

After this, add ``pgstats`` to the ``INSTALLED_APPS``
setting of your Django project.

Contributing Guide
==================

For information on setting up django-pgstats for development and
contributing changes, view `CONTRIBUTING.rst <CONTRIBUTING.rst>`_.

Primary Authors
===============

- @wesleykendall (Wes Kendall)
- @tomage (Tómas Árni Jónasson)
