import pandas as pd
from datetime import datetime
from datetime import timedelta
import time


def get_city():
    '''Asks the user for a city's name and returns the filename for that city's bikeshare data.  # NOQA
    Returns:
        (str) Filename for the city's bikeshare data.
    '''
    city = ''
    while city.lower() not in ['chicago', 'new york', 'washington']:
        city = input('Would you like to see data for Chicago, New York, or Washington?\n')  # NOQA
        if city.lower() == 'chicago':
            return 'chicago.csv'
        elif city.lower() == 'new york':
            return 'new_york_city.csv'
        elif city.lower() == 'washington':
            return 'washington.csv'
        else:
            print('Sorry, that is an invalid input. Please input either Chicago, New York, or Washington.')  # NOQA


def get_time_period():
    '''Asks the user for a time period and returns the data after applying the specified filter.  # NOQA
    Returns:
        (str) Time filter for our data.
    '''
    time_period = ''
    while time_period.lower() not in ['month', 'day', 'none']:
        time_period = input('\nWould you like to filter the data by day, month, or not at all? Type "none" for no filter.\n')  # NOQA
        if time_period.lower() not in ['month', 'day', 'none']:
            print('Sorry, your query was wrong.')
    return time_period


def get_month():
    '''Asks the user for a month and returns the data from that month.
    Returns:
        (tuple) Lower limit, upper limit of month for the bikeshare data.
    '''
    month_input = ''
    months_dict = {'january': 1, 'february': 2, 'march': 3, 'april': 4,
                   'may': 5, 'june': 6}
    while month_input.lower() not in months_dict.keys():
        month_input = input('\nWhich month? January, February, March, April,'
                            ' May, or June?\n')
        if month_input.lower() not in months_dict.keys():
            print('Sorry, invalid input. Please type in a '
                  'month b/w January and June')
    month = months_dict[month_input.lower()]
    return ('2017-{}'.format(month), '2017-{}'.format(month + 1))


def get_day():
    '''Asks the user for a day and returns the specified day.
    Returns:
        (tuple) lower limit and upper limit of date for the bikeshare data.
    '''
    this_month = get_month()[0]
    month = int(this_month[5:])
    valid_date = False
    while valid_date is False:
        is_int = False
        day = input('\nWhich day? Please type the response as an integer.\n')
        while is_int is False:
            try:
                day = int(day)
                is_int = True
            except ValueError:
                print('Sorry, I can not understand your input. Please type your response as an integer.')  # NOQA
                day = input('\nWhich day? Please type your response as an integer.\n')  # NOQA
        try:
            start_date = datetime(2017, month, day)
            valid_date = True
        except ValueError as e:
            print(str(e).capitalize())
    end_date = start_date + timedelta(days=1)
    return (str(start_date), str(end_date))


def popular_month(df):
    '''Finds and prints the most popular month for requested start time.
    Args:
        bikeshare dataframe
    '''
    months = ['January', 'February', 'March', 'April', 'May', 'June']
    index = int(df['start_time'].dt.month.mode())
    most_pop_month = months[index - 1]
    print('The most popular month is {}.'.format(most_pop_month))


def popular_day(df):
    '''Finds and prints the most popular day of week for requested start time.
    Args:
        bikeshare dataframe
    '''
    days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday',
                    'Saturday', 'Sunday']
    index = int(df['start_time'].dt.dayofweek.mode())
    most_pop_day = days_of_week[index]
    print('The most popular day of week for this start time is {}.'.format(most_pop_day))  # NOQA


def popular_hour(df):
    '''Finds and prints the most popular hour of day for start time.
    Args:
        bikeshare dataframe
    '''
    most_pop_hour = int(df['start_time'].dt.hour.mode())
    if most_pop_hour == 0:
        am_pm = 'am'
        pop_hour_readable = 12
    elif 1 <= most_pop_hour < 13:
        am_pm = 'am'
        pop_hour_readable = most_pop_hour
    elif 13 <= most_pop_hour < 24:
        am_pm = 'pm'
        pop_hour_readable = most_pop_hour - 12
    print('The most popular hour of day for start time is {}{}.'.format(pop_hour_readable, am_pm))  # NOQA


def trip_duration(df):
    '''Finds and prints the total trip duration and average trip duration in hours, minutes, and seconds.  # NOQA
    Args:
        bikeshare dataframe
    '''
    total_duration = df['trip_duration'].sum()
    minute, second = divmod(total_duration, 60)
    hour, minute = divmod(minute, 60)
    print('The total trip duration is {} hours, {} minutes and {}'
          ' seconds.'.format(hour, minute, second))
    average_duration = round(df['trip_duration'].mean())
    m, s = divmod(average_duration, 60)
    if m > 60:
        h, m = divmod(m, 60)
        print('The average trip duration is {} hours, {} minutes and {}'
              ' seconds.'.format(h, m, s))
    else:
        print('The average trip duration is {} minutes and {} seconds.'.format(m, s))  # NOQA


def popular_stations(df):
    '''Finds and prints the most popular start station and most popular end station.  # NOQA
    Args:
        bikeshare dataframe
    Returns:
        none
    '''
    pop_start = df['start_station'].mode().to_string(index=False)
    pop_end = df['end_station'].mode().to_string(index=False)
    print('The most popular start station is {}.'.format(pop_start))
    print('The most popular destination station is {}.'.format(pop_end))


def popular_trip(df):
    '''Finds and prints the most popular trip.
    Args:
        bikeshare dataframe
    '''
    most_pop_trip = df['journey'].mode().to_string(index=False)
    # The 'journey' column is created in the statistics() function.
    print('The most popular trip is {}.'.format(most_pop_trip))


def users(df):
    '''Finds and prints the counts of each user type.
    Args:
        bikeshare dataframe
    '''
    subs = df.query('user_type == "Subscriber"').user_type.count()
    cust = df.query('user_type == "Customer"').user_type.count()
    print('There are {} Subscribers and {} Customers.'.format(subs, cust))


def gender(df):
    '''Finds and prints the counts of gender.
    Args:
        bikeshare dataframe
    '''
    male_count = df.query('gender == "Male"').gender.count()
    female_count = df.query('gender == "Male"').gender.count()
    print('No. of users: {} male users and {} female users'.format(male_count, female_count))  # NOQA


def birth_years(df):
    ''' Finds and prints the oldest user, youngest user, most popular birth years.  # NOQA
    Args:
        bikeshare dataframe
    '''
    earliest = int(df['birth_year'].min())
    latest = int(df['birth_year'].max())
    mode = int(df['birth_year'].mode())
    print('The oldest users are born in {}.\nThe youngest users are born in {}.'  # NOQA
          '\nThe most popular birth year is {}.'.format(earliest, latest, mode))  # NOQA


def display_data(df):
    '''Displays five lines of data if the user specifies that they would like to.
    After displaying five lines, ask the user if they would like to see five more,  # NOQA
    continuing asking until they say stop.
    Args:
        data frame
    '''
    def is_valid(display):
        if display.lower() in ['yes', 'no']:
            return True
        else:
            return False
    head = 0
    tail = 5
    valid_input = False
    while valid_input is False:
        display = input('\nWould you like to view individual trip data? '
                        'Type \'yes\' or \'no\'.\n')
        valid_input = is_valid(display)
        if valid_input is True:
            break
        else:
            print("Sorry, invalid input. Please type 'yes' or"
                  " 'no'.")
    if display.lower() == 'yes':
        print(df[df.columns[0:-1]].iloc[head:tail])
        display_more = ''
        while display_more.lower() != 'no':
            valid_input_2 = False
            while valid_input_2 is False:
                display_more = input('\nWould you like to view more'
                                     ' trip data? Type \'yes\' or \'no\'.\n')
                valid_input_2 = is_valid(display_more)
                if valid_input_2 is True:
                    break
                else:
                    print("Sorry, invalid input. Please type "
                          "'yes' or 'no'.")
            if display_more.lower() == 'yes':
                head += 5
                tail += 5
                print(df[df.columns[0:-1]].iloc[head:tail])
            elif display_more.lower() == 'no':
                break


def statistics():
    '''Calculates and prints out the descriptive statistics about a city and
    time period specified by the user via raw input.
    '''
    # Filters the data by city (Chicago, New York, Washington)
    city = get_city()
    df = pd.read_csv(city, parse_dates=['Start Time', 'End Time'])

    # change all column names in lowercase and replaces whitespaces with underscores.  # NOQA
    new_labels = []
    for col in df.columns:
        new_labels.append(col.replace(' ', '_').lower())
    df.columns = new_labels

    # increases the column width so that the long strings in the 'journey'
    # column can be displayed fully
    pd.set_option('max_colwidth', 100)

    # creates a 'journey' column that displays 'start_station' with 'end_station' for the use popular_trip() function  # NOQA
    df['journey'] = df['start_station'].str.cat(df['end_station'], sep=' to ')

    # Filter by time period (month, day, none)
    time_period = get_time_period()
    if time_period == 'none':
        df_filtered = df
    elif time_period == 'month' or time_period == 'day':
        if time_period == 'month':
            filter_lower, filter_upper = get_month()
        elif time_period == 'day':
            filter_lower, filter_upper = get_day()
        df_filtered = df[(df['start_time'] >= filter_lower) & (df['start_time'] < filter_upper)]  # NOQA

    if time_period == 'none':
        start_time = time.time()
        # most popular month for the given start time.
        popular_month(df_filtered)
    if time_period == 'none' or time_period == 'month':
        start_time = time.time()
        # the most popular day of week for given start time?
        popular_day(df_filtered)
        start_time = time.time()

    # the most popular hour of day for start time.
    popular_hour(df_filtered)
    start_time = time.time()

    # the total trip duration and average trip duration
    trip_duration(df_filtered)
    start_time = time.time()

    # the most popular start station and most popular end station.
    popular_stations(df_filtered)
    start_time = time.time()

    # the most popular trip.
    popular_trip(df_filtered)
    start_time = time.time()

    # the counts of each user type.
    users(df_filtered)

    if city == 'chicago.csv' or city == 'new_york_city.csv':
        start_time = time.time()

        # the counts of gender.
        gender(df_filtered)
        start_time = time.time()

        # the earliest, most recent, and most popular birth years.
        birth_years(df_filtered)

    # Display five lines of data at a time if user specifies that they would like to do so.  # NOQA
    display_data(df_filtered)

    # Want to start, again?
    restart = input('\nWould you like to restart? Type \'yes\' or \'no\'.\n')
    while restart.lower() not in ['yes', 'no']:
        print("Invalid input. Please type 'yes' or 'no'.")
        restart = input('\nWould you like to restart? Type \'yes\' or \'no\'.\n')  # NOQA
    if restart.lower() == 'yes':
        statistics()


if __name__ == "__main__":
    statistics()
