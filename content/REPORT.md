Report:
The plot title on the home page (summary.html) does not show.
There is a run time warning for DateTimeField when importing. Please ignore this.

Technical:
The home or summary web page shows several features. The plot, which is in total WH per day, is under the table with all the ids. Near the top is a text box that allows the user to type in one of the id numbers that can be viewed from the table. Clicking the button will send the user to a page (Individual Details) that displays an individual's total consumption per day at the bottom and that individual's id, area, and tariff number. This page has a Home link at the top to go back to the home web page.

Three tests are included. Two def tests the models and one tests the view. We test the model labels for two of the fields. We check the home URL for the view. There should be one failure when running the test ('id' != 'id_intentionalFail').

The frontend and backend solutions were split. In import.py bulk_create function is used rather than the update_or_create function for data/consumption because it is faster for larger amounts of data. For user_data.csv the update_or_create function is used. There is a warning about the DateTimeField but this does not impact the data or results.
In views.py we retrieve and aggregate the data. We use truncday to allow grouping or filtering datetimes into day. The data is split into two and the date is appended as a string. Plotly supports the string format. We use plotly because it is easy to implement and maintain. It is also interactive.

In the html files, we use data|safe to prevent html injection. This was a problem and was resolved.
