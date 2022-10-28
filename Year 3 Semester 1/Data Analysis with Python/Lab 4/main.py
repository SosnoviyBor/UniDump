import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df = pd.read_csv("penguins.csv")

while True:
    match input("\nВведіть завдання, яке хочете вирішити [1-4][a-c]\nДля виходу напишіть 'q'\n").lower():

        case "q":
            break


        case "1a":
            # 1A - кількість пінгвінів кожного виду
            a1 = df.groupby("species").count().reset_index()
            a1.drop(a1.columns[2:], axis=1, inplace=True)
            a1.rename(columns={"island":"count"}, inplace=True)
            sns.barplot(x = a1["species"], y = a1["count"]).set(title="Кількість пінгвінів кожного виду")
            plt.tight_layout()
            plt.show()

        case "1b":
            # 1B - мінімальну довжину дзьобу пінгвінів кожного виду
            a2 = df.groupby("species")["culmen_length_mm"].min().to_frame().reset_index()
            a2.rename(columns={"culmen_length_mm":"min_culmen_length_mm"}, inplace=True)
            sns.barplot(x = a2["species"], y = a2["min_culmen_length_mm"]).set(title="Найменша довжина дзьобу пінгвіна за видом")
            plt.tight_layout()
            plt.show()

        case "1c":
            # 1C - середню вагу пінгвінів кожного виду з розподілом за статтю
            a3 = df.groupby("sex")["body_mass_g"].mean().to_frame().reset_index()
            a3.rename(columns={"body_mass_g":"mean_body_mass_g"}, inplace=True)
            sns.barplot(x = a3["sex"], y = a3["mean_body_mass_g"]).set(title="Середня вага пінгвіна за статтю")
            plt.tight_layout()
            plt.show()


        case "2":
            # 2 - Гістограма глибини дзьобу
            sns.histplot(data=df, x="culmen_depth_mm", hue="species")
            plt.tight_layout()
            plt.show()


        case "3":
            # 3 - Діаграма розмаху довжини ласт
            sns.boxplot(data=df, x="flipper_length_mm", y="species")
            plt.tight_layout()
            plt.show()


        case "4a":
            # 4A - Діаграма розсіювання залежності між довжиною і глибиною дзьобу
            print(f"Кореляція між довжиною і глибиною дзьобу: {df['culmen_length_mm'].corr(df['culmen_depth_mm'])}")
            sns.scatterplot(x = df['culmen_length_mm'], y = df['culmen_depth_mm']).set(title = 'Залежність між довжиною і глибиною дзьобу')
            plt.tight_layout()
            plt.show()

        case "4b":
            # 4B - Діаграма розсіювання залежності між вагою і довжиною ласт
            print(f"Кореляція між вагою і довжиною ласт: {df['body_mass_g'].corr(df['flipper_length_mm'])}")
            sns.scatterplot(x = df['body_mass_g'], y = df['flipper_length_mm']).set(title = 'Залежність між вагою і довжиною ласт')
            plt.tight_layout()
            plt.show()


        case _:
            print("Ви ввели неправильне значення")
