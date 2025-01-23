def calculate_demographic_data(print_data=True):
    import pandas as pd

    # Load data
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

    # 1. Average age of men
    average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)

    # 2. Percentage with Bachelors
    percentage_bachelors = round(len(df[df['education'] == 'Bachelors']) / len(df) * 100, 1)

    # 3. Higher education
    higher_education = df[df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    lower_education = df[~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]

    higher_education_rich = round(len(higher_education[higher_education['salary'] == '>50K']) / len(higher_education) * 100, 1)
    lower_education_rich = round(len(lower_education[lower_education['salary'] == '>50K']) / len(lower_education) * 100, 1)

    # 4. Min work hours and rich percentage
    min_work_hours = df['hours-per-week'].min()
    num_min_workers = df[df['hours-per-week'] == min_work_hours]
    rich_percentage = round(len(num_min_workers[num_min_workers['salary'] == '>50K']) / len(num_min_workers) * 100, 1)

    # 5. Country with highest percentage of rich
    country_salary = df.groupby('native-country')['salary'].value_counts().unstack().fillna(0)
    country_salary['total'] = country_salary['>50K'] + country_salary['<=50K']
    highest_earning_country = (country_salary['>50K'] / country_salary['total']).idxmax()
    highest_earning_country_percentage = round((country_salary['>50K'] / country_salary['total']).max() * 100, 1)

    # 6. Top occupation in India
    india_data = df[df['native-country'] == 'India']
    top_IN_occupation = india_data[india_data['salary'] == '>50K']['occupation'].value_counts().idxmax()

    # Results
    if print_data:
        print(f"Average age of men: {average_age_men}")
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print(f"Country with highest percentage of rich: {highest_earning_country}")
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print(f"Top occupations in India: {top_IN_occupation}")

    return {
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
