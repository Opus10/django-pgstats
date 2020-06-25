from django.core.management import call_command
import pytest

import pgstats.models


@pytest.mark.django_db
def test_snapshot_pgstats():
    """Verifies that the core management command snapshots table stats"""
    call_command('snapshot_pgstats')

    assert pgstats.models.IndexStats.objects.count() == 1
    assert pgstats.models.TableStats.objects.count() == 1

    table_stats = pgstats.models.TableStats.objects.get()
    index_stats = pgstats.models.IndexStats.objects.get()

    # We should at least have tables for the two django models in this app
    assert len(table_stats.stats) >= 2
    assert 'public.pgstats_indexstats' in table_stats.stats
    assert 'public.pgstats_tablestats' in table_stats.stats

    # We should have at least two indices for the primary keys of the two
    # django models in this app
    assert len(index_stats.stats) >= 2
    indices_from_this_app = [
        key for key in index_stats.stats if key.startswith('public.pgstats_')
    ]
    assert len(indices_from_this_app) == 2
