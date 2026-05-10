.. index:: Chicago Data Portal, open data; Chicago, CSV; real-world dataset,
           data pipeline; fetch-load-analyze-visualize, urllib.request; download
   ACM-IEEE CS2013; IM1 Information Management Concepts
   ACM-IEEE CS2023; IM1 Information Management Concepts
   ACM-IEEE CS2013; SDF2 Fundamental Programming Concepts
   ACM-IEEE CS2023; SDF2 Fundamental Programming Concepts
   ACM-IEEE CS2013; CN1 Introduction to Networking
   ACM-IEEE CS2023; CN1 Introduction to Networking

.. _Graffiti-Case-Study:

Case Study: Chicago 311 Graffiti Data
=======================================

.. note::
   *Source:* Adapted from `scalaworkshop
   <https://github.com/gkthiruvathukal/scalaworkshop>`_
   by George K. Thiruvathukal.  Data is published by the
   City of Chicago under the Chicago Data Portal open data licence.

The **Chicago Data Portal** (``data.cityofchicago.org``) publishes
hundreds of datasets covering city services, crime, transportation, and
more.  All are freely downloadable as CSV or JSON.  This case study
works through the entire data pipeline — fetch, load, aggregate, filter,
visualize — using the 311 Graffiti Removal dataset, which records every
public graffiti removal request submitted to the city.

The URL for the full dataset is:

.. code-block:: none

   https://data.cityofchicago.org/api/views/hec5-y4x5/rows.csv?accessType=DOWNLOAD

.. index:: urllib.request.urlretrieve; download, data fetching; CSV

Fetching the Dataset
---------------------

Python's standard library module ``urllib.request`` can download a file
from a URL directly to disk with a single call:

.. literalinclude:: ../../examples/introcs-python/internet_data/graffiti.py
   :language: python
   :start-after: # start: fetch_graffiti
   :end-before: # end: fetch_graffiti

``urlretrieve(url, filename)`` streams the remote file to ``filename``
without loading the entire response into memory first — important for
large datasets.

.. code-block:: python

   fetch_graffiti("311_graffiti.csv")

Output:

.. code-block:: none

   Downloading to 311_graffiti.csv ...
   Done.

.. index:: csv.DictReader; real data, data loading; CSV

Loading and Inspecting
-----------------------

``csv.DictReader`` turns each CSV row into a dictionary keyed by the
column headers — no index juggling required:

.. literalinclude:: ../../examples/introcs-python/internet_data/graffiti.py
   :language: python
   :start-after: # start: load_graffiti
   :end-before: # end: load_graffiti

Calling it with a small limit lets you inspect the shape of the data
before processing the whole file:

.. code-block:: python

   rows = load_graffiti("311_graffiti.csv", limit=3)
   for row in rows:
       print(row["Creation Date"], row["Status"], row["ZIP Code"])

Output (representative — actual dates depend on when the data was downloaded):

.. code-block:: none

   01/02/2024 Completed 60614
   01/02/2024 Completed 60647
   01/03/2024 Open      60618

The dataset includes columns for creation and completion dates, street
address, ZIP code, latitude/longitude, ward, and police district.

.. index:: collections.Counter; aggregation, aggregation; group-by

Aggregating by ZIP Code
------------------------

``collections.Counter`` is the natural tool for counting occurrences of
each value — here, the number of requests per ZIP code:

.. literalinclude:: ../../examples/introcs-python/internet_data/graffiti.py
   :language: python
   :start-after: # start: aggregate_graffiti
   :end-before: # end: aggregate_graffiti

``counter.most_common(top)`` returns pairs sorted by count descending,
so the busiest ZIP codes appear first:

.. code-block:: python

   for zip_code, count in aggregate_graffiti("311_graffiti.csv", top=5):
       print(f"{zip_code:10s}  {count:6,}")

Output (representative):

.. code-block:: none

   60614       4,821
   60647       4,203
   60618       3,977
   60622       3,840
   60625       3,512

.. index:: datetime.strptime; date parsing, filtering; date range, filtering; status

Filtering by Status and Date
------------------------------

Real datasets often need filtering before analysis.  This function
returns only rows with a given status whose creation date falls within a
date range:

.. literalinclude:: ../../examples/introcs-python/internet_data/graffiti.py
   :language: python
   :start-after: # start: filter_graffiti
   :end-before: # end: filter_graffiti

The ``Creation Date`` column uses ``MM/DD/YYYY`` format, so
``datetime.strptime`` with the pattern ``"%m/%d/%Y"`` parses it.  Rows
with unparseable dates are skipped with ``continue`` rather than
crashing the program.

.. code-block:: python

   matches = filter_graffiti("311_graffiti.csv",
                              status="Completed",
                              start="2024-01-01",
                              end="2024-01-31")
   print(f"{len(matches):,} completed requests in January 2024")

Output (representative):

.. code-block:: none

   1,847 completed requests in January 2024

.. index:: matplotlib; bar chart, bar chart; monthly trend, visualization; time series

Visualizing Monthly Trends
---------------------------

Grouping by year-month and plotting a bar chart reveals seasonal
patterns in graffiti removal activity:

.. literalinclude:: ../../examples/introcs-python/internet_data/graffiti.py
   :language: python
   :start-after: # start: visualize_graffiti
   :end-before: # end: visualize_graffiti

The function groups every creation date into a ``YYYY-MM`` bucket using
``date.strftime("%Y-%m")``, sorts the months chronologically, and draws
a bar per month.  Install ``matplotlib`` first if needed:

.. code-block:: none

   pip install matplotlib

.. code-block:: python

   visualize_graffiti("311_graffiti.csv", "graffiti_trend.png")

Output:

.. code-block:: none

   Saved graffiti_trend.png

The saved chart shows request volume over time, typically with a dip in
winter months (fewer outdoor surfaces are tagged when it is cold) and
peaks in late spring and summer.

Exercises
---------

1. Modify ``aggregate_graffiti`` to group by ``"Ward"`` instead of
   ``"ZIP Code"``.  Which ward has the most graffiti removal requests?

2. Write a function ``average_completion_days(filename)`` that reads the
   dataset and returns the average number of days between
   ``"Creation Date"`` and ``"Completion Date"`` for completed requests.
   Skip rows where either date is missing or unparseable.

3. The dataset includes ``"Latitude"`` and ``"Longitude"`` columns.
   Write a function that filters rows to those within a bounding box
   (min/max lat/lon) and returns the count.  Use it to count requests
   in a neighbourhood of your choice.

4. Extend ``visualize_graffiti`` to overlay a line showing the
   12-month rolling average on top of the monthly bars.

5. Download a second Chicago dataset (for example, 311 Pothole Reports
   at ``https://data.cityofchicago.org/api/views/7as2-ds3y/rows.csv?accessType=DOWNLOAD``).
   Compare monthly request volumes for graffiti and potholes on the same
   chart using two sets of bars.
