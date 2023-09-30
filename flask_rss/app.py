# Import necessary libraries
from flask import Flask, render_template, request, redirect, url_for
import feedparser
import csv
from flask_paginate import Pagination, get_page_args


app = Flask(__name__)

# Items per page
PER_PAGE = 10



# File path for the CSV file
csv_file = 'feeds.csv'

# Function to load feeds from CSV
def load_feeds():
    try:
        with open(csv_file, 'r') as file:
            reader = csv.DictReader(file)
            return [{'name': row['name'], 'url': row['url'], 'category': row['category']} for row in reader]
    except FileNotFoundError:
        return []


# Function to save feeds to CSV
def save_feeds(feeds):
    with open(csv_file, 'w', newline='') as file:
        fieldnames = ['name', 'url', 'category']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for feed in feeds:
            writer.writerow({'name': feed['name'], 'url': feed['url'], 'category': feed['category']})

# Load feeds from CSV at startup
rss_feeds = load_feeds()

# Function to parse an RSS feed
def parse_rss_feed(url):
    feed = feedparser.parse(url)
    return feed.entries

@app.route('/add_feed', methods=['POST'])
def add_feed():
    if request.method == 'POST':
        new_feed_name = request.form['feed_name']
        new_feed_url = request.form['feed_url']
        new_feed_category = request.form['feed_category']  # Add this line
        if new_feed_name and new_feed_url and new_feed_category:  # Modify this line
            rss_feeds.append({'name': new_feed_name, 'url': new_feed_url, 'category': new_feed_category})  # Modify this line
            # Save feeds to the CSV file
            save_feeds(rss_feeds)
    return redirect(url_for('index'))

@app.route('/remove_feed/<int:index>')
def remove_feed(index):
    if 0 <= index < len(rss_feeds):
        rss_feeds.pop(index)
        # Save feeds to the CSV file after removal
        save_feeds(rss_feeds)
    return redirect(url_for('index'))

@app.route('/')
def index():
    # get page number from URL
    page = request.args.get('page', type=int, default=1)

    start = (page - 1) * PER_PAGE
    end = start + PER_PAGE

    #slice list 
    feeds_to_display = rss_feeds[start:end]

    #pagination object 
    pagination = Pagination(page=page, total=len(rss_feeds), per_page=PER_PAGE, css_framework='boostrap4')  

    return render_template('index.html', feeds=feeds_to_display, pagination=pagination)

@app.route('/feed/<int:index>')
def view_feed(index):
    if 0 <= index < len(rss_feeds):
        feed = rss_feeds[index]
        feed_items = parse_rss_feed(feed['url'])
        return render_template('feed.html', feed=feed, feed_items=feed_items)
    else:
        return "Invalid feed index"

if __name__ == '__main__':
    app.run(debug=True)
