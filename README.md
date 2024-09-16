# concert-challenge# Concert Challenge

Welcome to the Concert Challenge! This project manages a concert booking system using SQLite and Python. It allows you to manage bands, venues, and concerts, and provides various operations and queries to interact with the database.

## Project Overview

This project includes the following components:
- **Database Setup**: Initializes the SQLite database with tables for bands, venues, and concerts.
- **Concert Methods**: Provides methods for interacting with the database, including querying and manipulating concert data.
- **Testing**: Example tests to verify the functionality of the implemented methods.

## Features

- **Get Band for Concert**: Retrieve details of the band performing at a specific concert.
- **Get Venue for Concert**: Retrieve details of the venue hosting a specific concert.
- **Get Concerts for Venue**: List all concerts happening at a specific venue.
- **Get Bands for Venue**: List all bands that have performed at a specific venue.
- **Check Hometown Show**: Determine if a concert is held in the band's hometown.
- **Get Introduction**: Retrieve a personalized introduction message for a concert.
- **Play in Venue**: Add a new concert to the database if it doesn't already exist.
- **Get All Introductions**: Retrieve all introduction messages for a specific band.
- **Get Most Performances**: Find the band with the most performances.
- **Get Concert on Date**: Retrieve details of a concert on a specific date at a specific venue.
- **Get Most Frequent Band**: Find the band with the most performances at a specific venue.

## Getting Started

### Prerequisites

- Python 3.x
- SQLite (included with Python)

### Setup

1. **Clone the Repository**

   ```sh
   git clone git@github.com:Abdul102-ux/concert-challenge.git
   cd concert-challenge
Install Dependencies

There are no external dependencies for this project. Ensure you have Python 3 and SQLite installed.

Setup the Database

Run the setup script to create the database and initialize the tables:


python3 setup_database.py

Usage
Running Tests
To test the functionalities, use the following command:


python3 test_methods.py
This script runs various test cases to verify that the methods in concert_methods.py are working as expected.

Method Descriptions
get_band_for_concert(concert_id): Retrieves the band details for the specified concert ID.
get_venue_for_concert(concert_id): Retrieves the venue details for the specified concert ID.
get_concerts_for_venue(venue_id): Lists all concerts that are scheduled at the specified venue.
get_bands_for_venue(venue_id): Lists all bands that have performed at the specified venue.
is_hometown_show(concert_id): Checks if the concert is being held in the band's hometown.
get_introduction(concert_id): Gets a personalized introduction message for the specified concert.
play_in_venue(band_name, venue_title, date): Adds a new concert entry if it does not already exist.
get_all_introductions(band_name): Retrieves all introduction messages for a specific band.
get_most_performances(): Finds the band with the most performances.
get_concert_on_date(venue_title, date): Retrieves the concert details for a specific venue and date.
get_most_frequent_band(venue_title): Finds the most frequently performing band at a specific venue.
Contributing
Contributions are welcome! If you have any suggestions or improvements, please open an issue or submit a pull request.

