import pandas as pd

def calculate_demographic_data(print_data=True):
    # Lecture des données
    df = pd.read_csv('adult.data.csv')
    
    # Comptage des races
    race_count = df['race'].value_counts()

    # Âge moyen des hommes
    average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)

    # Pourcentage de personnes ayant un diplôme de Bachelors
    percentage_bachelors = round(
        (df[df['education'] == 'Bachelors'].shape[0] / df.shape[0]) * 100, 1
    )

    # Richesse et éducation
    higher_education = df[df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    lower_education = df[~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]

    higher_education_rich = round(
        (higher_education[higher_education['salary'] == '>50K'].shape[0] / higher_education.shape[0]) * 100, 1
    )
    lower_education_rich = round(
        (lower_education[lower_education['salary'] == '>50K'].shape[0] / lower_education.shape[0]) * 100, 1
    )

    # Temps de travail minimum
    min_work_hours = df['hours-per-week'].min()

    # Richesse parmi ceux qui travaillent le moins
    num_min_workers = df[df['hours-per-week'] == min_work_hours]
    rich_percentage = round(
        (num_min_workers[num_min_workers['salary'] == '>50K'].shape[0] / num_min_workers.shape[0]) * 100, 1
    )

    # Pays avec le plus haut pourcentage de richesse
    country_earnings = df[df['salary'] == '>50K']['native-country'].value_counts()
    country_counts = df['native-country'].value_counts()
    rich_percentage_country = (country_earnings / country_counts * 100).round(1)
    highest_earning_country = rich_percentage_country.idxmax()
    highest_earning_country_percentage = rich_percentage_country.max()

    # Occupation la plus populaire en Inde pour >50K
    india_occupation = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]['occupation']
    top_IN_occupation = india_occupation.value_counts().idxmax()

    if print_data:
        print("Number of each race:", race_count)
        print("Average age of men:", average_age_men)
        print("Percentage with Bachelors degrees:", percentage_bachelors)
        print("Percentage with higher education that earn >50K:", higher_education_rich)
        print("Percentage without higher education that earn >50K:", lower_education_rich)
        print("Min work time:", min_work_hours, "hours/week")
        print("Percentage of rich among those who work fewest hours:", rich_percentage)
        print("Country with highest percentage of rich:", highest_earning_country)
        print("Highest percentage of rich people in country:", highest_earning_country_percentage)
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
        'highest_earning_country_percentage': highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
