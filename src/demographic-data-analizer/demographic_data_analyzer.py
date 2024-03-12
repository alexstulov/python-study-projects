import pandas as pd

def calculate_demographic_data(print_data=True):
    pd.options.mode.chained_assignment = None
    # Read data from file
    df = pd.read_csv('adult.data.csv')

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df.groupby('race').size()

    # What is the average age of men?
    average_age_men = round(df.groupby('sex').agg({
        'age': ['mean'],
        'sex': []
    })['age'].sort_values('sex', ascending=False)['mean'].iloc[0], 1)

    # What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = round(df.groupby('education').size().loc['Bachelors'] / df.shape[0] * 100,1)
    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    education_salary_group = df.groupby(['education','salary']).size().to_frame('size').reset_index()
    higher_education = education_salary_group[education_salary_group['education'].str.contains('Bachelors|Doctorate|Masters')]
    lower_education = education_salary_group[~education_salary_group['education'].str.contains('Bachelors|Doctorate|Masters')]

    # percentage with salary >50K
    higher_education_rich = round(higher_education[higher_education['salary'].str.contains('>50K')]
                                  .agg({'size': ['sum']})['size']['sum'] / 
                                  higher_education.agg({'size': ['sum']})['size']['sum'] * 100, 1)
    lower_education_rich = round(lower_education[lower_education['salary'].str.contains('>50K')]
                                 .agg({'size': ['sum']})['size']['sum'] /
                                 lower_education.agg({'size': ['sum']})['size']['sum'] * 100, 1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df.agg({'hours-per-week': ['min']})['hours-per-week']['min']

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    min_workers = df[df['hours-per-week'] == min_work_hours]

    rich_percentage = round(min_workers[min_workers['salary'] == '>50K'].shape[0] / min_workers.shape[0] * 100,1)

    # What country has the highest percentage of people that earn >50K?
    highest_earning_country = df.groupby(['native-country', 'salary']).size().to_frame('size').reset_index()
    rich_by_country = highest_earning_country[highest_earning_country['salary'] == '>50K']
    poor_by_country = highest_earning_country[highest_earning_country['salary'] == '<=50K']
    poor_by_country = poor_by_country[poor_by_country['native-country'].isin(rich_by_country['native-country'])]
    rich_by_country['ratio'] = rich_by_country['size'].values / (rich_by_country['size'].values + poor_by_country['size'].values) * 100
    countries_sorted_by_rich_ratio = rich_by_country.sort_values('ratio', ascending=False)
    highest_earning_country_row = countries_sorted_by_rich_ratio.iloc[0]
    highest_earning_country = highest_earning_country_row['native-country']
    highest_earning_country_percentage = round(highest_earning_country_row['ratio'], 1)

    # Identify the most popular occupation for those who earn >50K in India.
    people_in_india = df[df['native-country'] == 'India']
    rich_people_in_india = people_in_india[people_in_india['salary'] == '>50K']
    top_IN_occupation = rich_people_in_india.groupby('occupation').size().to_frame('size').reset_index().sort_values('size', ascending=False).iloc[0]['occupation']

    # DO NOT MODIFY BELOW THIS LINE
    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }