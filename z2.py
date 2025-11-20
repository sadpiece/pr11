import pandas as pd
import matplotlib.pyplot as plt



def mostpopular_month(df, track_name):
    df_copy = df.copy()
    df_copy['Date'] = pd.to_datetime(df_copy['Date'], dayfirst=True)
    df_copy['Month'] = df_copy['Date'].dt.month_name()


    month_data = df_copy.groupby('Month')[track_name].sum()


    month = month_data.idxmax()
    max_count = month_data.max()

    return month, max_count


df = pd.read_csv('data.csv')

print(df.head())
print(df.info())
print(df.describe())


print("загальна статистика")



bike = []
for col in df.columns:
    if col not in ['Date', 'Unnamed: 1']:
        bike.append(col)


total = df[bike].sum().sum()
print(f"\n1. Загальна кількість велосипедистів за рік на усіх велодоріжках: {total}")
print(f"\n2. Загальна кількість велосипедистів за рік на кожній велодоріжці:")


total_per_track = df[bike].sum()

for track in bike:
    total = total_per_track[track]
    print(f"{track} : {total} велосипедистів")


print(f"\n3. найпопулярніший місяць у обраних велодоріжках")



selected_tracks = ['Berri1', 'Rachel / Papineau', 'University']

for track in selected_tracks:
    result = mostpopular_month(df, track)
    popular_month = result[0]
    cyclists_count = result[1]

    print(f"Велодоріжка '{track}':")
    print(f"  - Найпопулярніший місяць: {popular_month}")
    print(f"  - Кількість велосипедистів: {cyclists_count}")
    print()


selected_track = 'Parc'

df_copy = df.copy()
df_copy['Date'] = pd.to_datetime(df_copy['Date'], dayfirst=True)
df_copy['Month'] = df_copy['Date'].dt.month_name()


month_order = ['January', 'February', 'March', 'April', 'May', 'June',
               'July', 'August', 'September', 'October', 'November', 'December']


monthly_data = df_copy.groupby('Month')[selected_track].sum().reindex(month_order)


plt.figure(figsize=(12, 6))
monthly_data.plot(kind='line', color='blue', linewidth=2)
plt.title(f'Завантаженість велодоріжки "{selected_track}" по місяцях', fontsize=14)
plt.xlabel('Місяць', fontsize=12)
plt.ylabel('Кількість велосипедистів', fontsize=12)
plt.show()

