import time
import pandas as pd
import numpy as np
import calendar

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input('Would you like to see data for Chicago, New York, or Washington? ').lower() #using .lower() to make the user input lowercase
                if city not in CITY_DATA:
            print("Please choose a correct city name!")
        else:
            break


    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input("Please enter a munth from january to june, or type 'all' to display all months: ").lower()
        months = ['january', 'february', 'march', 'april', 'may','june']
        if month != 'all' and month not in months:
            print("Please choose a munth from january to june!")
        else:
            break
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input('Please enter a dey of the week, or type "all" to display all days: ').lower()
        days = ['saturday', 'sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday']
        if day != 'all' and day not in days:
            print("Please choose a day from saturday to friday!")
        else:
            break

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
 # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])


    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()


    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df

def display_row_data(df):
    """
    displays subsequent rows of data according to user answer
    Args:
         df - Pandas DataFrame containing city data filtered by month and day returned from load_data function above
    """
    i = 0
    answer = input("Would you like to display the first 5 rows of data? yes/no: ").lower() #convert the user input to lower case usin .lower() function
    pd.set_option("display.max_columns",None) # "None" sets the number of displayed columns to max
    while True:
        if answer == "no":
            break
        else:
            print(df[i:i+5]) #at first will display 5 rows(i = 0 to i = 5) then if user input "yes" then display next 5 rows
            answer = input("Would you like to display the next 5 rows of data? yes/no: ").lower()
            i += 5 #add 5 to i to show the next 5 rows if user choose 'yes'


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['month'].mode()[0] #returns a month number
    print('Most Common Month: ', calendar.month_name[common_month]) # use calendar to get month name from month number

    # TO DO: display the most common day of week
    common_day = df['day_of_week'].mode()[0]
    print('Most Common Day: ', common_day)

    # TO DO: display the most common start hour
    #create an hour column
    df['hour'] = df['Start Time'].dt.hour

    common_hour = df['hour'].mode()[0]
    print('Most Common Start Hour: ', common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start = df['Start Station'].mode()[0]
    print('Most Commonly Used Start Station: ', common_start)


    # TO DO: display most commonly used end station
    common_end = df['End Station'].mode()[0]
    print('Most Commonly Used End Station: ', common_end)

    # TO DO: display most frequent combination of start station and end station trip
    common_start_end = (df['Start Station'] + ' - ' + df['End Station']).mode()[0]
    print('Most Frequent Combination of Start and End Station: ', common_start_end)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_time = df['Trip Duration'].sum()
    print('Total Travel Duration: ', total_time, ' seconds, or ', total_time/3600, ' hours')

    # TO DO: display mean travel time
    avg_time = df['Trip Duration'].mean()
    print('Average Travel Time: ', avg_time, ' seconds, or ', avg_time/3600, ' hours')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('Counts of User Types:\n', df['User Type'].value_counts())

    # TO DO: Display counts of gender
    if 'Gender' in df: #avoid errors because washington data set has no 'gender' column
        print('\n Counts of Gender:\n', df['Gender'].value_counts())

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        earliest_birth_year = int(df['Birth Year'].min())
        print('\n Earliest Year of Birth:\n', earliest_birth_year)
        recent_birth_year = int(df['Birth Year'].max())
        print('\n Most Recent Year of Birth:\n', recent_birth_year)
        common_birth_year = int(df['Birth Year'].mode()[0])
        print('\n Most Common Year of Birth:\n', common_birth_year)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        display_row_data(df)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
