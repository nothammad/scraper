# GitHub Machine Learning Projects Scraper

This Python script scrapes the [GitHub Machine Learning Collection](https://github.com/collections/machine-learning) using Selenium and extracts the names and URLs of popular machine learning repositories.

## Features

- Uses Selenium WebDriver to handle dynamic JavaScript rendering
- Extracts project names and repository links
- Saves data as a clean CSV file (`project_list.csv`)
- Works with Chrome in incognito mode (optional headless)

## Requirements

- Python 3.x
- Google Chrome
- ChromeDriver (version must match your Chrome browser)
- Selenium
- Pandas

Install dependencies:

```bash
pip install selenium pandas
