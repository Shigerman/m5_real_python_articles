# m5_real_python_articles
A script which signals about and saves new Real Python articles.

### instruments used
* Python for backend
* Poetry for virtual environment
* requests library
* M5Stack® Core2 ESP32 for a server and signaller

### activity algorithm
Script connects to Real Python site feed >>> checks a list of recent articles
every minute >>> if getting a new article in the feed, gives a signal and
saves the article title to a txt file.
