class Project:
    def __init__(self, name, lines, salary) -> None:
        self.name = name
        self.loc = lines
        self.salary = salary
        
        # define project type
        self.p_type: ProjectType
        if self.loc < 25_000: self.p_type = ProjectType.Organic
        elif self.loc < 75_000: self.p_type = ProjectType.SemiDetached
        else: self.p_type = ProjectType.Embedded
        
        self.effort = self.p_type.AB * pow(self.loc / 1000, self.p_type.BB)
        self.cost = self.effort * salary
        self.schedule = self.p_type.CB * pow(self.effort, self.p_type.DB)
    
    def results(self):
        print(
            "\n"
            f"--- Проект {self.name} ---\n"
            f"Розмір продукту: {self.loc} строк коду\n"
            f"Зусилля: {round(self.effort, 1)} людина/місяць\n"
            f"Вартість: {round(self.cost, 2)} грн\n"
            f"Час на розробку: {round(self.schedule, 2)}"
        )


class ProjectType:
    class Organic:
        AB = 2.4
        BB = 1.05
        CB = 2.5
        DB = 0.38
        
    class SemiDetached:
        AB = 3
        BB = 1.12
        CB = 2.5
        DB = 0.35
        
    class Embedded:
        AB = 3.6
        BB = 1.2
        CB = 2.5
        DB = 0.32


if __name__ == "__main__":
    # Цифра узята з
    # https://www.work.ua/salary-junior+associate/#:~:text=%D0%92%20%D1%81%D0%B5%D1%80%D0%B5%D0%B4%D0%BD%D1%8C%D0%BE%D0%BC%D1%83%20%C2%ABJunior%20associate%C2%BB%20%D0%B2%20%D0%A3%D0%BA%D1%80%D0%B0%D1%97%D0%BD%D1%96%20%D0%B7%D0%B0%D1%80%D0%BE%D0%B1%D0%BB%D1%8F%D1%94%2013500%20%D0%B3%D1%80%D0%BD.
    AVERAGE_JUNIOR_SALARY = 13_500

    Project("Tetris", 4_900, AVERAGE_JUNIOR_SALARY).results()
    Project("Flask", 34_000, AVERAGE_JUNIOR_SALARY).results()
    Project("Django", 1_000_000, AVERAGE_JUNIOR_SALARY).results()

    # Просто для краси
    print("")