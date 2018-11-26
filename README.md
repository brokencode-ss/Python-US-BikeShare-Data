# Python-US-BikeShare-Data

This Python script is used to explore data related to bike share systems for Chicago, NYC, and Washington. It imports data from csv files and compute descriptive statistics from the data. With Udacity's permission, the files have been uploaded to the following link: https://drive.google.com/open?id=1tmZPans5NN7Nj2m6XSdFCf5Ooh5_n4Ez

## Running the script
You can run the script using a Python integrated development environment (IDE). This script is written in Python 3, so you will need the Python 3.x version of the IDE.

## Datasets
The datasets used for this script contain bike share data for the first six months of 2017.

The data is provided by [Motivate](https://www.motivateco.com/), which is a bike share system provider for many cities in the United States. The data files for all three cities contain the same six columns:
* Start Time
* End Time
* Trip Duration (in seconds)
* Start Station
* End Station
* User Type

## Questions explored
The script answers the following questions about the bike share data:
* What is the most popular month for start time?
* What is the most popular day of week (Monday, Tuesday, etc.) for start time?
* What is the most popular hour of day for start time?
* What is the total trip duration and average trip duration?
* What is the most popular start station and most popular end station?
* What is the most popular trip?
* What are the counts of each user type?
* What are the counts of gender?
* What are the earliest (i.e. oldest person), most recent (i.e. youngest person), and most popular birth years?

## Statistics Computed
The code can provide the following information:

#1 Popular times of travel (i.e., occurs most often in the start time)

most common month
most common day of week
most common hour of day

#2 Popular stations and trip

most common start station
most common end station
most common trip from start to end (i.e., most frequent combination of start station and end station)

#3 Trip duration

total travel time
average travel time

#4 User info

counts of each user type
counts of each gender (only available for NYC and Chicago)
earliest, most recent, most common year of birth (only available for NYC and Chicago)
