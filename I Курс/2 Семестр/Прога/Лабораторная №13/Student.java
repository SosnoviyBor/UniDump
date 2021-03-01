import java.util.Objects;

public class Student implements Information {
    private final String name; // ім’я, прізвище
    private final String markBookIndex; // номер залікової книжки
    private double GPA; //середній бал
    private final Faculty faculty;

    public Student(String name, String markBookIndex, double GPA,Faculty faculty) throws MaxStudentsException {
        if (GPA<0) {
            throw new IllegalArgumentException("Средняя оценка не может быть меньше 0");
        }
        if ( faculty == null ) {
            throw new NullPointerException("Нельзя добавить студента в несуществующий факультет.");
        }
        this.name = name;
        this.markBookIndex = markBookIndex;
        this.GPA = GPA;
        this.faculty = faculty;
        faculty.add(this);
    }


    public String getName() {
        return name;
    }

    public double getGPA() {
        return GPA;
    }

    public String getMarkBookIndex() {
        return markBookIndex;
    }

    public void setGPA(double GPA) {
        if (GPA<0) {
            throw new IllegalArgumentException("Средняя оценка не может быть меньше 0");
        }
        this.GPA = GPA;
    }

    public Faculty getFaculty() {
        return faculty;
    }

    @Override
    public void getInformation() {
        System.out.println(
                "Вся информация о студенте:" +
                        "\nФИО: " +this.name +
                        "\nИнститут: " + faculty.getInstitute().getName() +
                        "\nФакультет: " + faculty.getName() +
                        "\nНомер студенческого: " + this.markBookIndex +
                        "\nСредний бал: " + this.GPA

        );
    }


}
