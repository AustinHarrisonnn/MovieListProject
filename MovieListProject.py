

# Dictionaries of my 5 favorite movies
m1 = {'Genre': 'Action', 'Title': 'Dark Knight Rises', 'Director': 'Christopher N', 'Investments': '25,000,000',
      'Revenue': '1,081,000,000', 'Duration': '2:45:00'}
m2 = {'Genre': 'Action', 'Title': 'Captain Phillips', 'Director': 'Paul G', 'Investments': '55,000,000',
      'Revenue': '220,600,000', 'Duration': '2:14:00'}
m3 = {'Genre': 'Musical', 'Title': 'La La Land', 'Director': 'Damien C', 'Investments': '30,000,000',
      'Revenue': '472,000,000', 'Duration': '2:08:00'}
m4 = {'Genre': 'Fantasy', 'Title': 'Spirited Away', 'Director': 'Hayao M', 'Investments': '19,000,000',
      'Revenue': '395,580,000', 'Duration': '2:05:00'}
m5 = {'Genre': 'Drama', 'Title': 'Forest Gump', 'Director': 'Robert Z', 'Investments': '55,000,000',
      'Revenue': '678,200,000', 'Duration': '2:22:00'}
# List of dictionaries, and flagging my favorite movie out of the 5
movie_list = [m1, m2, m3, m4, m5]
favorite_movie = movie_list[0]
# Printing the header and catagories
print('MY FAVORITE MOVIES')
print('-' * 113)
print(f"{'Genre': <15} {'Title' : <15} {'Director' : <15} {'Investments ' : <15} {' Revenue' : <15} {'Duration' : <15}")
print('-' * 113)
# Calculation of the total movie durations by adding all movie times together and formatting them as an hour:minute format
total_minutes = 0
for movie in movie_list:
    duration = movie['Duration']
    hours = int(duration.split(':')[0])
    minutes = int(duration.split(':')[1])
    total_minutes = total_minutes + hours * 60 + minutes
    if movie['Title'] == favorite_movie:
        flag = '*'
    else:
        flag = ''
# flagging favorite movie by adding * around the title
for movie in movie_list:
    flag = '*' if movie == favorite_movie else ''
    print(
        f"{movie['Genre']:<15} {(flag + movie['Title'] + flag):<20} {movie['Director']:<20} {movie['Investments']:<20} {movie['Revenue']:<19}  {movie['Duration']:<20}")

    total_minutes = total_minutes + hours + minutes

total_hours = int(total_minutes / 60)
fractioned_minutes = int((total_minutes / 60 - total_hours) * 60)

avg_hours = int(total_hours / 5)
average_minutes = int(total_minutes / 60)
# Calculations for total investments
investment_money = 0
for i in movie_list:
    investment = i['Investments'].split(',')[0] + i['Investments'].split(',')[1] + i['Investments'].split(',')[2]
    investment_money = investment_money + int(investment)
total_investment = '{:,}'.format(investment_money)
# Calculations for total revenue
revenue_money = 0
for i in movie_list:
    revenue = i['Revenue'].split(',')[0] + i['Revenue'].split(',')[1] + i['Revenue'].split(',')[2]
    revenue_money = revenue_money + int(revenue)
total_revenue = '{:,}'.format(revenue_money)
# Printing the results of the calculations
print('-' * 113)
print(f"The total movie duration is: {total_hours} hours and {fractioned_minutes} minutes.")
print(f"The average movie duration is: {avg_hours} hours and {average_minutes} minutes.")
print(f"The total investments of these movies was: ${total_investment}.")
print(f"The sum of total revenue for these movies was: ${total_revenue}.")
print('-' * 113)