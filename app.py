from flask import Flask, render_template, request
import sqlite3
from flask import jsonify
from io import BytesIO
from base64 import b64encode

app = Flask(__name__)
app.static_folder = 'static'


@app.route('/', methods=['GET', 'POST'])
def index():

    conn = sqlite3.connect('mydatabase.db')
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS items (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            item_type TEXT,
            item_description TEXT,
            item_location TEXT,
            item_date TEXT,
            item_image BLOB,
            item_tag TEXT,
            item_cont TEXT
        );
    """)
    conn.commit()
    conn.close()
    if request.method == 'POST':
        # Get form data
        item_type = request.form['item-type']
        item_description = request.form['item-description']
        item_location = request.form['item-location']
        item_date = request.form['item-date']
        item_image = request.files['item-image'].read()
        item_tag = request.form['item-tag']
        item_cont = request.form['item-contact']

        # Validate form data
        if not item_type or not item_description or not item_location or not item_date or not item_tag or not item_cont:
            error_message = 'Please fill out all fields.'
            return render_template('index.html', error_message=error_message)

        # Insert data into SQLite database
        conn = sqlite3.connect('mydatabase.db')
        c = conn.cursor()
        c.execute("""
            CREATE TABLE IF NOT EXISTS items (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                item_type TEXT,
                item_description TEXT,
                item_location TEXT,
                item_date TEXT,
                item_image BLOB,
                item_tag TEXT,
                item_cont TEXT
            );
        """)

        # Commit the changes to the database
        conn.commit()
        c.execute('INSERT INTO items (item_type, item_description, item_location, item_date, item_image, item_tag, item_cont) VALUES (?, ?, ?, ?, ?, ?, ?)', (item_type, item_description, item_location, item_date, item_image, item_tag, item_cont))
        conn.commit()
        conn.close()

        # Display success message
        success_message = 'Form submitted successfully!'
        return render_template('index.html', success_message=success_message)

    # Render the template for the form
    return render_template('index.html')

@app.route('/lost_items')
def lost_items():
    # Connect to the database
    conn = sqlite3.connect('mydatabase.db')
    c = conn.cursor()

    # Query the database for all items with item_tag = 'Lost'
    c.execute("SELECT * FROM items WHERE item_tag = 'Lost'")
    items = c.fetchall()

    for i, item in enumerate(items):
        item = list(item)
        image_data = BytesIO(item[5])
        item[5] = b64encode(image_data.getvalue()).decode('utf-8')
        items[i] = tuple(item)

    # Close the connection
    conn.close()

    # Render the template with the items data
    return render_template('lost_items.html', items=items)


@app.route('/found_items')
def found_items():
    # Connect to the database
    conn = sqlite3.connect('mydatabase.db')
    c = conn.cursor()

    # Query the database for all items with item_tag = 'Lost'
    c.execute("SELECT * FROM items WHERE item_tag = 'Found'")
    items = c.fetchall()

    for i, item in enumerate(items):
        item = list(item)
        image_data = BytesIO(item[5])
        item[5] = b64encode(image_data.getvalue()).decode('utf-8')
        items[i] = tuple(item)


    # Close the connection
    conn.close()

    # Render the template with the items data
    return render_template('found_items.html', items=items)


@app.route('/buy_items')
def buy_items():
    # Connect to the database
    conn = sqlite3.connect('mydatabase.db')
    c = conn.cursor()

    # Query the database for all items with item_tag = 'Buy'
    c.execute("SELECT * FROM items WHERE item_tag = 'Buy'")
    items = c.fetchall()

    for i, item in enumerate(items):
        item = list(item)
        image_data = BytesIO(item[5])
        item[5] = b64encode(image_data.getvalue()).decode('utf-8')
        items[i] = tuple(item)

    # Close the connection
    conn.close()

    # Render the template with the items data
    return render_template('buy_items.html', items=items)


@app.route('/sell_items')
def sell_items():
    # Connect to the database
    conn = sqlite3.connect('mydatabase.db')
    c = conn.cursor()

    # Query the database for all items with item_tag = 'Lost'
    c.execute("SELECT * FROM items WHERE item_tag = 'Sell'")
    items = c.fetchall()

    for i, item in enumerate(items):
        item = list(item)
        image_data = BytesIO(item[5])
        item[5] = b64encode(image_data.getvalue()).decode('utf-8')
        items[i] = tuple(item)

    # Close the connection
    conn.close()

    # Render the template with the items data
    return render_template('sell_items.html', items=items)


@app.route('/borrow_items')
def borrow_items():
    # Connect to the database
    conn = sqlite3.connect('mydatabase.db')
    c = conn.cursor()

    # Query the database for all items with item_tag = 'Lost'
    c.execute("SELECT * FROM items WHERE item_tag = 'Borrow'")
    items = c.fetchall()

    for i, item in enumerate(items):
        item = list(item)
        image_data = BytesIO(item[5])
        item[5] = b64encode(image_data.getvalue()).decode('utf-8')
        items[i] = tuple(item)

    # Close the connection
    conn.close()

    # Render the template with the items data
    return render_template('borrow_items.html', items=items)



@app.route('/search')
def search():
    # Get the search query from the URL parameter 'q'
    query_type = request.args.get('search_type')
    query_description = request.args.get('search_description')
    
    # print(query_type)
    # print(query_description)

    if query_type and not query_description:
        query = """
        SELECT *
        FROM items
        WHERE item_type LIKE '% '||?||' %'
        OR item_type LIKE ?||' %'
        OR item_type LIKE '% '||?||''
        OR item_type = ?
        """
        conn = sqlite3.connect('mydatabase.db')
        c = conn.cursor()
        c.execute(query, (query_type, query_type, query_type, query_type))
        items = c.fetchall()

        for i, item in enumerate(items):
            item = list(item)
            image_data = BytesIO(item[5])
            item[5] = b64encode(image_data.getvalue()).decode('utf-8')
            items[i] = tuple(item)
        conn.close()

        # Render the search results template with the items data
        return render_template('search.html', items=items)
    
    elif query_type and query_description:
        query = """
        SELECT *
        FROM items
        WHERE item_description LIKE '% '||?||' %' OR item_description LIKE '%'||?||'%'
        OR item_description LIKE ?||' %'
        OR item_description LIKE '% '||?||''
        OR item_description = ?
        OR item_type LIKE '% '||?||' %'
        OR item_type LIKE ?||' %'
        OR item_type LIKE '% '||?||''
        OR item_type = ?
        """
        conn = sqlite3.connect('mydatabase.db')
        c = conn.cursor()
        c.execute(query, (query_description, query_description, query_description, query_description, query_description, query_type, query_type, query_type, query_type))
        items = c.fetchall()

        for i, item in enumerate(items):
            item = list(item)
            image_data = BytesIO(item[5])
            item[5] = b64encode(image_data.getvalue()).decode('utf-8')
            items[i] = tuple(item)
        conn.close()

        # Render the search results template with the items data
        return render_template('search.html', items=items)

    elif query_description and not query_type:
        query = """
        SELECT *
        FROM items
        WHERE item_description LIKE '% '||?||' %' OR item_description LIKE '%'||?||'%'
        OR item_description LIKE ?||' %'
        OR item_description LIKE '% '||?||''
        OR item_description = ?
        """
        conn = sqlite3.connect('mydatabase.db')
        c = conn.cursor()
        c.execute(query, (query_description, query_description, query_description, query_description, query_description))
        items = c.fetchall()

        for i, item in enumerate(items):
            item = list(item)
            image_data = BytesIO(item[5])
            item[5] = b64encode(image_data.getvalue()).decode('utf-8')
            items[i] = tuple(item)
        conn.close()

        # Render the search results template with the items data
        return render_template('search.html', items=items)

    


    # If the query is empty, render the search page without results
    elif not query_description and not query_type:
        return render_template('search.html')

    # Otherwise, connect to the database and execute the search query
    conn = sqlite3.connect('mydatabase.db')
    c = conn.cursor()
    c.execute(query, (query_description, query_description, query_description, query_description, query_description, query_type, query_type, query_type, query_type))
    items = c.fetchall()

    for i, item in enumerate(items):
        item = list(item)
        image_data = BytesIO(item[5])
        item[5] = b64encode(image_data.getvalue()).decode('utf-8')
        items[i] = tuple(item)
    conn.close()

    # Render the search results template with the items data
    return render_template('search.html', items=items)

@app.route('/about_us')
def about_us():
    return render_template('about.html')


if __name__ == '__main__':
    app.debug = True
    app.run()

