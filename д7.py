import pandas as pd


df = pd.DataFrame({
    "Student": ["Prikhodko", "Kropyvnytskyi", "Romanenko", "Derizemlya", "Zhuk",
                "Kuryanov", "Dubovets", "Stroganov", "Nikolaenko", "Dron"],
    "Phone": ["+38033620350010", "+38011467044811", "+38053094916898", "+3801323021338",
              "+38023043222562", "+3800173846270", "+38031726476940", "+380724515698",
              "+3801156096502", "+380514527074"],
    "Scholarship": [2000, 2890, 2000, 2000, 2890, 2000, 2890, 2890, 2000, 2000],
    "Month_Expenses": [1800, 2200, 1500, 1700, 2500, 1600, 2100, 2800, 1650, 1750]
})


print("Вміст DataFrame:")
print(df)

print("Перші 3 рядки:")
print(df.head(3))

print("Типи даних:")
print(df.dtypes)


print(f"Розмір DataFrame: {df.shape}")
print(f"Кількість рядків: {df.shape[0]}")
print(f"Кількість стовпців: {df.shape[1]}")

print("Описова статистика:")
print(df.describe())


df['Balance'] = df['Scholarship'] - df['Month_Expenses']
print("DataFrame з новим стовпцем 'Balance':")
print(df)



positive_balance = df[df['Balance'] > 350]
print("Студенти з балансом > 350:")
print(positive_balance)



increased_scholarship = df[df['Scholarship'] == 2890]
print("Студенти з підвищеною стипендією:")
print(increased_scholarship)


df_sorted = df.sort_values('Balance')
print("Сортування за балансом:")
print(df_sorted)

df_grouped = df.groupby('Scholarship')['Month_Expenses'].mean()
print("Середні місячні витрати за типом стипендії:")
print(df_grouped)


max_balance = df['Balance'].max()
max_expenses = df['Month_Expenses'].max()


print(f"Максимальний баланс студента: {max_balance} грн")
print(f"Максимальні місячні витрати студента: {max_expenses} грн")
print("\n")


print("Статистика:")
print(f"Кількість студентів з позитивним балансом: {len(df[df['Balance'] > 0])}")
print(f"Кількість студентів з негативним балансом: {len(df[df['Balance'] < 0])}")
print(f"Кількість студентів з нульовим балансом: {len(df[df['Balance'] == 0])}")
print(f"Загальна сума стипендій: {df['Scholarship'].sum()} грн")
print(f"Загальна сума витрат: {df['Month_Expenses'].sum()} грн")
print(f"Загальний баланс всіх студентів: {df['Balance'].sum()} грн")