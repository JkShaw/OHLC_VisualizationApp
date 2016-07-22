Stock Chart Visualization web application
-----------------------------------------
Project Name: financeMetric
Application Name: finAnalytics

Introduction:
-------------
This application generates a stock chart that takes stock records in excel format and store it in the database programmatically, Once the records is loaded in the db. The index page of the application lets user to select the stock movements of a stock through dropdown menu, on selecting 
th corresponding stock's behaviour is displayed.


Input: 
Excel file containing Stock related records namely date, open, high, low, close, adj_close, volume and stock

Output:
------
Securities OHLC(Open high low close) chart that clearly shows the opening, high, low and closing prices for a security.often used by technical analysts to spot trends and view stock movements.

Technologies Used:
------------------
- Django
- AngularJS
- Sqlite

Libraries used:
---------------
- Django-excel (for excel import/export)
- Angular-nvd3 (for chart creation)
