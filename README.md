                                             IIIT-H LOST AND FOUND PORTAL
                    
Welcome to the IIIT-H Lost and Found Portal! This website serves as a platform for reporting lost items, finding lost items, buying and selling items, and borrowing items within the IIIT-H community.

Summary:
    Our website contains the following pages:

    1.Home Page: Displays a form to submit information about a lost/found item, including type, description, location, date, image, contact details, and additional information.
    2.Lost Items Page: Shows a list of items that have been reported as lost by the community members.
    3.Found Items Page: Displays a list of items that have been found by community members.
    4.Buy Items Page: Shows a list of items that are available for purchase.
    5.Sell Items Page: Displays a list of items that community members want to sell.
    6.Borrow Items Page: Shows a list of items that community members are willing to lend.
    7.Search Page: Allows users to search for items based on type and description.
    8.About Us Page: Provides information about the IIIT-H Lost and Found Portal and its creators.

    The navigation bar on the website allows easy access to all the pages, and the footer contains the contact email of the creators.

    Each item's page (Lost, Found, Buy, Sell, and Borrow) includes detailed information about the item, such as its type, description, location, date, image, contact information, and status. The status indicates whether the item has been sold, found, or borrowed. Users can edit the item's status by clicking the respective button below the item's details. Additionally, the pages include a sorting feature to arrange items by date (newest first or oldest first).

    The search page enables users to find specific items based on their type and a part of the description. The search results are displayed on the same page.

Frameworks/Packages Used:
    The IIIT-H Lost and Found Portal is built using the following frameworks/packages:

    1.Flask: A Python web framework used for building web applications. It provides tools and features for routing, handling HTTP requests, rendering templates, and more.

    2.SQLite3: A built-in Python module that provides an interface to the SQLite database engine. It allows the code to interact with an SQLite database, including creating tables, executing queries, and managing data.

    3.Jinja2: A templating engine used with Flask for rendering HTML templates. It allows embedding dynamic content and logic in HTML templates using placeholders and control structures.

    4.BytesIO: A class in the 'io' module that provides a binary stream interface for in-memory data. In the code, it is used to convert binary image data to a stream for processing.

    5.base64: A module that provides functions for encoding binary data as ASCII strings using Base64 encoding. In the code, it is used to convert the binary image data to a Base64-encoded string for embedding in HTML.


Instructions to Run the Web App:
    To run the IIIT-H Lost and Found Portal web application, follow these steps:

    1.Run the app.py file.
    
    2.Copy the URL displayed in the terminal.

    3.Open a web browser and paste the copied URL.
    
    4.You will be redirected to the Home Page, where you can submit information about a lost/found item by selecting the item type, providing a description, location, date, image, and contact details.To redirect into HomePage click on the WebPage Logo on Top left Page.

    5.To navigate to different pages, you can use the links in the navigation bar or directly search for an item on the search page by providing its type and description.

    6.On each item's page (Lost, Found, Buy, Sell, and Borrow),you can view the details of the items, including their type, description, location, date, image, and contact information. The item's status, indicating whether it has been sold, found, or borrowed, will also be displayed.

    7.To update the status of an item (e.g., mark it as sold or found), simply click the corresponding button below the item's details.

    8.The search page allows you to search for items based on their type and description. Enter the desired search criteria, and the results will be displayed on the same page.

    9.The About Us page provides information about the IIIT-H Lost and Found Portal and its creators.

Contribution:
    The IIIT-H Lost and Found Portal was developed by the following team members:

    Krishna Koushik: Contributed to parts of the About Us page, added items dynamically to the Lost, Found, Buy, Sell, and Borrow pages based on item type, implemented sorting and status features.

    Abraham Paul: Created the database and implemented the storage of information in it (app.py), added the search feature to the web app, provided the main idea for the design and structure of the web app.

    Harsh Gupta: Contributed to the rest of the About Us page, designed the logo for the web app, added the navigation bar and footer to all pages, and implemented the CSS styling for each page of the website.