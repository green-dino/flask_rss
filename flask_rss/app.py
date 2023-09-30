# Import necessary libraries
from flask import Flask, render_template, request, redirect, url_for
import feedparser
import csv

app = Flask(__name__)

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
    return render_template('flask_rss/templates/index.html', feeds=rss_feeds)

@app.route('/feed/<int:index>')
def view_feed(index):
    if 0 <= index < len(rss_feeds):
        feed = rss_feeds[index]
        feed_items = parse_rss_feed(feed['url'])
        return render_template('flask_rss/templates/feed.html', feed=feed, feed_items=feed_items)
    else:
        return "Invalid feed index"

if __name__ == '__main__':
    app.run(debug=True)
