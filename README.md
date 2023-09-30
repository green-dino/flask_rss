# Flask RSS Reader

The Flask RSS Reader is a simple web application built with Flask that allows you to manage and read your favorite RSS feeds. This README provides an overview of the application, its features, and how to set it up.

## Features

- **Add RSS Feeds:** You can add new RSS feeds to the reader by providing a feed name, feed URL, and category. These feeds are stored in a CSV file.

- **Remove Feeds:** If you no longer want to follow a specific RSS feed, you can easily remove it from the reader.

- **Categorize Feeds:** Organize your feeds by assigning them to custom categories.

- **Preview Feed Items:** View the latest feed items from your subscribed feeds in a user-friendly interface.

## Prerequisites

Before you can run the Flask RSS Reader, make sure you have the following prerequisites installed:

- Python 3.x
- Flask (You can install it using `pip install Flask`)

## Getting Started

Follow these steps to set up and run the Flask RSS Reader:

1. Clone this repository to your local machine:

   ```
   git clone <repository_url>
   cd flask-rss-reader
   ```

2. Create a virtual environment (recommended) to isolate the project's dependencies:

   ```
   python -m venv venv
   ```

3. Activate the virtual environment:

   - On Windows:

     ```
     venv\Scripts\activate
     ```

   - On macOS and Linux:

     ```
     source venv/bin/activate
     ```

4. Install the required Python packages:

   ```
   pip install -r requirements.txt
   ```

5. Start the Flask application:

   ```
   python app.py
   ```

6. Open your web browser and go to [http://localhost:5000](http://localhost:5000) to access the Flask RSS Reader.

## Usage

- **Adding a Feed:** On the main page, you can add a new RSS feed by providing the feed name, URL, and category (optional). Click the "Add Feed" button to subscribe to the feed.

- **Removing a Feed:** To remove a feed, click the "Remove" link next to the feed you want to unsubscribe from.

- **Viewing Feed Items:** Click the "View" link next to a feed to view the latest feed items. You can browse through the feed items and access the full content by clicking the item title.

- **Categorizing Feeds:** You can categorize feeds by providing a custom category when adding a feed. Feeds with the same category will be grouped together on the main page.

## Customization

You can customize the appearance of the Flask RSS Reader by modifying the included CSS file (`style.css`) in the "static" directory. This allows you to change colors, fonts, and other styling aspects to match your preferences.

## License

This Flask RSS Reader is open-source software released under the [MIT License](LICENSE).

---

Feel free to explore and modify the Flask RSS Reader according to your needs. If you encounter any issues or have suggestions for improvements, please don't hesitate to contribute or reach out to the project maintainers. Happy reading!