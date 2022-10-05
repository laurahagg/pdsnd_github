# import the neccessary tools and third-party-packages

import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': "C:/Users/laura/Desktop/Lau/Udacity/Python/all-project-files/chicago.csv",
              'new york city': "C:/Users/laura/Desktop/Lau/Udacity/Python/all-project-files/new_york_city.csv",
              'washington': "C:/Users/laura/Desktop/Lau/Udacity/Python/all-project-files/washington.csv"}

# provide lists with the options for cities, months and days
cities = ["chicago", "new york city", "washington"]
months = ["all", "january", "february", "march", "april", "may", "june"]
days = ["all", "monday", "tuesday", "wednesday", "thirsday", "friday", "saturday", "sunday"]


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')

    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input("Would you like to see the data for Chicago, New York City or Washington?\n").lower()
        if city in cities:
            break
        else:
            print("You made a typing error. Please enter the right City.")




    # get user input for month (all, january, february, ... , june)
    while True:
        month = input("Would you like to filter by month?  \n Your Options are: 'all' for no filters, January, February, March, April, May or June. \n").lower()
        if month in months:
            break
        else:
            print("You made a typing error. Please enter the right Month.")


    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("Would you like to filter by day? \n Your Options are: 'all' for no filters, Monday, Tuesday, Wednesday, Thrisday, Friday, Saturday or Sunday. \n").lower()
        if day in days:
            break
        else:
            print("You made a typing error. Please enter the right Day.")

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
    df["Start Time"] = pd.to_datetime(df["Start Time"])

     # extract month and day of week from Start Time to create new columns
    df["month"] = df["Start Time"].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()


     # filter by month if applicable
    if month != 'all':
         # use the index of the months list to get the corresponding int
         months = ['january', 'february', 'march', 'april', 'may', 'june']
         month = months.index(month) + 1

         # filter by month to create the new dataframe
         df = df[df["month"] == month]

     # filter by day of week if applicable
    if day != 'all':
         # filter by day of week to create the new dataframe
         df = df[df["day_of_week"] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    print("\nWhat are the most frequent times of travel?")


    # display the most common month
    df["month"] = df["Start Time"].dt.month
    popular_month = df["month"].mode()[0]
    print('Most Popular Month:', popular_month)



    # display the most common day of week
    df["day_of_week"] = df["Start Time"].dt.day_name()
    popular_day = df["day_of_week"].mode()[0]
    print('Most Popular Day of the Week:', popular_day)


    # display the most common start hour
    df["hour"] = df["Start Time"].dt.hour
    popular_hour = df["hour"].mode()[0]
    print('Most Popular Hour:', popular_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    return df

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    print("\nWhat are the most popular stations and trips?")

    # display most commonly used start station
    start_station = df["Start Station"].value_counts().idxmax()
    print("The most popular Start Station: ", start_station)

        # display most commonly used end station
    end_station = df["End Station"].value_counts().idxmax()
    print("The most popular End Station: ", end_station)


    # display most frequent combination of start station and end station trip
    start_to_end_station = df[['Start Station', 'End Station']].mode().loc[0]
    print('Most Frequent Combination of Start Station and End Station trip : {}, {}'.format(start_to_end_station[0], start_to_end_station[1]))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    return df


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    print("\nHow long are the people traveling?")

    # display total travel time
    total_travel_time = df["Trip Duration"].sum()
    print("The total travel time is {} seconds.".format(total_travel_time))


    # display mean travel time
    mean_travel_time = df["Trip Duration"].mean()
    print("The mean Travel Time is {} seconds.".format(mean_travel_time))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    return df


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    print("\nHere are some statistics about the Bikeshare Users:")

    # Display counts of user types
    user_types = df["User Type"].value_counts()
    print("The counts of the User Types are \n", user_types)


    # Display counts of gender
    while True:
        if "Gender" in df.columns:
            gender = df["Gender"].value_counts()
            print("The counts of the gender are \n", gender)
            break
        else:
            print("There is no data about the Genders available for your city.")
            break


    # Display earliest, most recent, and most common year of birth
    while True:
        if "Birth Year" in df.columns:
            earliest_birth_year = df["Birth Year"].min()
            print("The oldest User was born in ", earliest_birth_year)

            recent_birth_year = df["Birth Year"].max()
            print("The youngest User was born in ", recent_birth_year)

            common_birth_year = df["Birth Year"].mode()[0]
            print("Most of the Users are born in ", common_birth_year)
            break
        else:
            print("There is no data about the Birth Years available for you city.")
            break

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    return df

def raw_data(df):
    """Displays raw data about the bikeshare project"""
    print('\nCalculating Raw Data...\n')
    start_time = time.time()

    # ask the user if he wants to get raw data or not
    # if yes: five lines of the raw data


    data_lines = 0
    raw_data_input = input("\nDo you want to see the Raw Data? Enter yes or no.\n").lower()

    while True:
        if raw_data_input.lower() == "yes":
            data_lines += 5
            raw_data = df.iloc[data_lines: data_lines+5]
            print("\nHere are five lines of the raw data: \n ", raw_data)
    # ask the user if he wants to contintue:
            more_data = input("\nDo you want to see the next five lines of the raw data? Enter yes or no.\n").lower()
            if more_data != "yes":
                break
    # if no: go further to the next question
        else:
            print("\nYou don't want to see the raw data.\n")
            break

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    return df


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
