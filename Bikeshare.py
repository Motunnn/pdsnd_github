
# coding: utf-8

# In[ ]:


#!/usr/bin/env python
# coding: utf-8

#                                 
#                                 Project: Exploring the bike share data
#                                 Name: Motun Adesina
#                                 Programming for data science Nanodegree 
# 
# 

# In[1]:


import time
import pandas as pd
import numpy as np


# The data uses three csv file from three cities for and the end users have the opportunity to filter to a city fo chouce

# In[2]:


CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }


# In[ ]:





# In[3]:


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
    
    city = input('Bike share is now available in three cities. Type in which of these three cities you are interested in: Chicago, New York City, Washington----').lower()
    if city not in CITY_DATA.keys():
        print("\nYou can only explore the cities listed above. Please try again\n")
        city = input('Bike share is now available in three cities. Type in which of thse three cities you are interested in: Chicago, New York City, Washington').lower() 
    else:
        print("\nGreat! Let's go ahead and explore your chosen city\n which is:", city)
            
            
# TO DO: get user input for month (all, january, february, ... , june)
    
# First I ask how they want to view the data
    date_filter = input('Type in how you would like to filter the data : month or day or both-->  ')
    if date_filter not in (['month', 'day', 'both']):
        print('You have entered an invalid filter option. Try month, day or both')
        date_filter = input('Type in how you would like to filter : month or day or both-->  ')
    else:
        print(f"\nCool!! You have chosen to filter the data by {date_filter.title()}")

#Then I check which month they are interested in
    months = ['january', 'february', 'march', 'april', 'may', 'june']
    if date_filter == 'month' or date_filter == 'both':
        month = input('Which month are you interested in? January, February, March, April, May, or June-->  ').lower()
        while month not in months:
            print("\nSorry, you can only filter by the following months: January, February, March, April, May, or June \n")
            month= input("Enter again the month you want to filter by  =").lower()
    else:
        month ='all'

      
    #TO DO: get user input for day of week (all, monday, tuesday, ... sunday)  
    days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']
    if date_filter == 'day' or date_filter == 'both':
        day = input('Type in which day you want to see - monday, tuesday, wednesday, thursday, friday, saturday, sunday or all? ').lower()
        while day not in days:
            print('"\nSorry, you can only filter by the following days listed above')
            day = input('Retry entering a day in the format above --> ').lower()
    else:
          day = 'all'
          
          
    print('-'*40)

    print('Thanks for your selection. Here is what you have selected')
    print("City  ->", city.title())
    if date_filter == 'month': 
        print("Month ->",  month.title())
    elif date_filter =='day':
        print("Day -> " , day.title())
    else: 
        print('month & day filter')
    
    return city, month, day


# In[ ]:





# In[4]:


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
    # This loads the data into the data frame, which selecting the chosen city
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # Creates a new column for the month and weekday
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()


    # If the month filter is chosen, use it, else all
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # New data fram based on the month
        df = df[df['month'] == month]

    # If the day filter is chosen then filter by the day
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


# In[5]:


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    months = ['january', 'february', 'march', 'april', 'may', 'june']
    most_common_month = df['month'].mode()[0]
    print("The most common month is:", months[most_common_month-1])


    # TO DO: display the most common day of week
    most_common_day = df['day_of_week'].mode()[0]
    print("The most common day of week is:", most_common_day)


    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_start_hour = df['hour'].mode()[0]
    print(f'The most common start hour is: {common_start_hour}')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    


# In[6]:


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_popular_station = df['Start Station'].mode()[0]
    print(f"The most commonly used start station: {most_popular_station}")


    # TO DO: display most commonly used end station
    most_common_end_station = df['End Station'].mode()[0]
    print(f"\nThe most commonly used end station: {most_common_end_station}")

    # TO DO: display most frequent combination of start station and end station trip
    df['station_combination'] = df['Start Station'] + 'to ' + df['End Station']
    most_common_combination = df['station_combination'].mode()[0]
    print("The most frequesnt combination of start and end station trip is from", most_common_combination.upper())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


# In[7]:


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print("The total travel time covered by bikes is", total_travel_time , "seconds")

    # TO DO: display mean travel time
    avg_travel_time = df['Trip Duration'].mean()
    print("The aevrage travel time is", avg_travel_time, "seconds")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


# In[8]:



def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print("The number of user types are:", user_types)

    # TO DO: Display counts of gender
    if 'Gender' in df:
        gender = df['Gender'].value_counts()
        print(gender)
    else:
        print("The city you have selected does not have a gender information")


    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        earliest = df['Birth Year'].min()
        print("The earliest best year is", earliest)
        oldest = df['Birth Year'].max()
        print("The most recent birth year is", oldest)
        most_common_birth = df['Birth Year'].mode()[0]
        print("The most common birthyear is", most_common_birth)
    else:
        print("The city you selected does not have a birth information")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


# In[ ]:





# In[9]:



    
def view_data_function(df):
    view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n')
    if view_data.lower() == 'yes':
        start_loc = 0
        while True:
            print(df.iloc[start_loc: start_loc+5])
            start_loc += 5
            view_data = input("Do you wish to continue?: ").lower()
            if view_data.lower() == 'no':
                break


# In[ ]:





# In[ ]:


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        view_data_function(df)
       
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
    main()


# In[ ]:





# # References
# 1. https://www.w3resource.com/python/python-print-statement.php - How to return a variable and string
# 2. https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.month_name.html - How to use dt.
# 3. https://github.com/Aritra96/bikeshare-project/blob/master/bikeshare.py - Compared results and ready through the code for improvements on my code
# 4. https://www.w3schools.com/python/ref_string_upper.asp - String methods
# 5. https://github.com/ipython/ipython/issues/11027 - issues with blank output
# 6. https://stackoverflow.com/questions/53680913/typeerror-cannot-unpack-non-iterable-nonetype-object/53681554

# In[ ]:



