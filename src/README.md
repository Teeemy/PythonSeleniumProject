Mastering Selenium Practice: Automating Web Tables with Demo Examples
Demo Webtable 1 (Static Table)
This table has 7 rows and 3 columns. So, the distribution of rows and columns is even. We can assume this table is a static or linear table. This table is easy to automate. 
Company	Contact	Country
Google	Maria Anders	Germany
Meta	Francisco Chang	Mexico
Microsoft	Roland Mendel	Austria
Island Trading	Helen Bennett	UK
Adobe	Yoshi Tannamuri	Canada
Amazon	Giovanni Rovelli	Italy

Demo Webtable 2 (Dynamic Table)
This table has an uneven distribution of rows and columns the last row has two columns only, but the other rows have 7 columns each. So, let's assume it is a dynamic table. This table is a tougher task.

Structure	Country	City	Height	Built	Rank	…
Total	4 buildings
Burj Khalifa	UAE	Dubai	829m	2010	1	
Clock Tower Hotel	Saudi Arabia	Mecca	601m	2012	2	
Taipei 101	Taiwan	Taipei	509m	2004	3	
Financial Center	China	Shanghai	492m	2008	4	

Selenium Practice Exercises for Demo Table 2 - 
Verify that there are only 4 structure values present in the table with Selenium
Verify that the 6th row of the table (Last Row) has only two columns with Selenium
Find the tallest structure in the table with Selenium

1. Introduction


In this post, we will learn how to automate web tables with Selenium Webdriver. It's always tricky to fetch data from a web table using Selenium and when the table structure keeps changing every time on the basis of data to be shown then it becomes a more challenging task to automate it. First, let's learn how to read data from a web table with Selenium.


Table of Content
1. What is Web Table?
Types of Web Table
Static Table
Dynamic Table
2. Automate Reading data from Static Web Table with Selenium
Practice Exercises for automating Static Table
Solution Code for Static Table
Code Explanation
3. Automate Handling Dynamic Web Table with Selenium
Practice Exercises for automating Dynamic Table
Solution Code for Dynamic Table
Code Explanation

2. What is a Web Table?
A web table, also known as an HTML table, is a structured grid-like representation of data on a webpage. It is created using HTML markup tags and consists of rows and columns, similar to a spreadsheet or a traditional table. Web tables are commonly used to organize and present tabular data, such as financial data, product listings, schedules, and more, in a visually organized and easily readable format.

In a web table, each cell represents a unit of data, and rows and columns determine the arrangement of the data within the table. The table structure allows for easy navigation and interpretation of information. It enables users to compare data across different rows and columns, sort the table based on specific criteria, and interact with the data within the cells.

Web tables can be interacted with using automated testing tools and frameworks, such as Selenium WebDriver. Test automation scenarios often involve locating and extracting data from web tables, performing validations, and manipulating table data dynamically. 
2.1. HTML Tags for Table:
In HTML, the <table> tag is used to define a table on a webpage. It serves as the container for all the table-related elements, including table headers, table rows, and table data cells. Here are some commonly used tags associated with HTML tables:

<table>: The main container tag that defines the start and end of the table.
<thead>: Represents the table header section. It is typically used to group the header content, which usually consists of <th> (table header) elements.
<tbody>: Represents the table body section. It contains the main data rows of the table, typically defined using <tr> (table row) elements.
<tfoot>: Represents the table footer section. It is used to group the footer content, which may include a summary or aggregation of information for the table. Footer content is often enclosed within <td> (table data) elements.
<tr>: Defines a table row. It contains one or more <td> (table data) or <th> (table header) elements that represent the cells within that row.
<th>: Defines a table header cell. It is used to represent the header content for a column or row. <th> elements are typically placed within the <thead> section.
<td>: Defines a table data cell. It represents a data entry within a table row. <td> elements are typically placed within the <tbody> section.
Here's an example demonstrating the use of these tags in a table structure:

html
Copy code
<table>
  <thead>
    <tr>
      <th>Product</th>
      <th>Price</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Item 1</td>
      <td>$10</td>
    </tr>
    <tr>
      <td>Item 2</td>
      <td>$15</td>
    </tr>
  </tbody>
  <tfoot>
    <tr>
      <td colspan="2">Total: $25</td>
    </tr>
  </tfoot>
</table>
In this example, we have a basic table structure with a header, body, and footer. The header row contains two columns: "Product" and "Price." The body section consists of two rows with corresponding product names and prices. The footer row spans across both columns using the colspan attribute and displays the total price.

Here's the table representation of the example I provided:

diff
Copy code
+---------+-------+
| Product | Price |
+---------+-------+
| Item 1  |  $10  |
| Item 2  |  $15  |
+---------+-------+
| Total:  |  $25  |
+---------+-------+
In this representation, the table is displayed using ASCII characters to create a visual representation of the table structure. The header row is separated from the body and footer rows by a horizontal line. Each cell's content is aligned within its corresponding column, and the table content is surrounded by vertical and horizontal lines to create a clear distinction between cells and rows.

2.2. Types of Web Table
Some common types of tables include:

Static Table: A static table is a basic table where the content is predefined and does not change dynamically. It is typically created using HTML and CSS, and the data is hard-coded within the table structure. Static tables are useful for displaying fixed information that doesn't require frequent updates.

Dynamic Table: A dynamic table is a table that is populated with data dynamically, often retrieved from a database or through an API. The content of a dynamic table can change based on user interactions, data updates, or other events. JavaScript frameworks like React, Angular, or Vue.js are commonly used to create dynamic tables.

Responsive Table: A responsive table is designed to adapt and display effectively on different devices and screen sizes. It adjusts its layout and behavior based on the available screen space. Responsive tables often employ techniques such as horizontal scrolling, collapsing columns, or stacking rows to maintain readability and usability on smaller screens.

Data Grid: A data grid is a more advanced type of table that provides additional functionality for sorting, filtering, and manipulating data. It typically includes features like pagination, search, sorting columns, and editing capabilities. Data grids are commonly used in applications where managing and interacting with large datasets is required.

Pivot Table: A pivot table is a specialized table that allows for multidimensional data analysis and summarization. It enables users to reorganize and aggregate data based on different dimensions and criteria. Pivot tables are commonly used in data analytics and business intelligence applications.

Comparison Table: A comparison table is used to present and compare different attributes or features of items or options. It typically lists the items or options as rows and displays their characteristics or properties as columns. Comparison tables are often used in product comparisons, pricing plans, or feature comparisons.


3. Automate Reading data from Static Web Table with Selenium
We can automate the web table using the XPath locator. With xpath locator, we can find out the no. of rows and columns present in the table. And once we got the no. of rows and columns then it gets easier for us to fetch data from every table cell by using two loops one for the row and the other for the column.

We have to prepare the custom xpath for each table cell using these loops, we replace row no. and column no. as loop variables at run time.