# Changelog

## 1.2.0 (2023-10-08)

### Feature

  - Add Python 3.12 support and use Mkdocs for documentation [Wesley Kendall, b7ba5f7]

    Python 3.12 and Postgres 16 are supported now, along with having revamped docs using Mkdocs and the Material theme.

    Python 3.7 support was dropped.

## 1.1.0 (2023-06-09)

### Feature

  - Added Python 3.11, Django 4.2, and Psycopg 3 support [Wesley Kendall, 8552e39]

    Adds Python 3.11, Django 4.2, and Psycopg 3 support along with tests for multiple Postgres versions. Drops support for Django 2.2.

## 1.0.8 (2022-10-14)

### Trivial

  - Update with latest Django template [Wesley Kendall, 181b90d]
  - Fix JSONField deprecation warnings with Django 4. [Omen Apps, 614cb0a]

## 1.0.7 (2022-08-26)

### Trivial

  - Test against Django 4.1 and other CI improvements [Wes Kendall, a79dd28]

## 1.0.6 (2022-08-24)

### Trivial

  - Fix ReadTheDocs builds [Wes Kendall, a30b183]

## 1.0.5 (2022-08-20)

### Trivial

  - Updated with latest Django template [Wes Kendall, 2c47ac7]

## 1.0.4 (2022-08-20)

### Trivial

  - Fix release note rendering and code formatting changes [Wes Kendall, 08f2691]

## 1.0.3 (2022-07-31)

### Trivial

  - Updated with latest Django template, fixing doc builds [Wes Kendall, ef15173]

## 1.0.2 (2021-06-06)

### Trivial

  - Updated with the latest Django template [Wes Kendall, 7000d5d]

## 1.0.1 (2020-06-29)

### Trivial

  - Added more information to the README [Wes Kendall, acee174]

## 1.0.0 (2020-06-25)

### Api-Break

  - Initial release of django-pgstats [Wes Kendall, 7933b73]

    Version one of django-pgstats provides models for tracking table and index
    stats. Along with that, it provides management commands to sync these
    stats.
