

#### Background

Electricity smart meters (in `data/consumption/<user_id>.csv`).  We want to help an energy provider view and analyse this data. One of the ways we do this is to visualise aggregated data


### The data

* `data/user_data.csv`
  * A file containing user data

id | area | tariff
---|------|-------
1 | a1 | t1
2 | a1 | t2
3 | a2 | t3
... | ... | ...

* `data/consumption/<user_id>.csv`
  * A file containing energy consumption (in Wh) in 30 minute intervals

datetime | consumption
---------|------------
2016-07-01 00:00:00 | 100.
2016-07-01 00:30:00 | 130.
2016-07-01 01:00:00 | 90.
... | ...

### Development environment

* Python 3.6 or later
* Django 1.11

