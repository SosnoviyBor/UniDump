import java.util.ArrayList;
import java.util.Iterator;

public class Faculty implements Information {
    private final String name;
    private final Institute institute;
    private ArrayList<Student> students = new ArrayList<>();

    public Faculty(String name, Institute institute, ArrayList<Student> students) {
        this.name = name;
        this.institute = institute;
        this.students = students;
        institute.add(this);
    }

    public Faculty(String name, Institute institute) {
        this.name = name;
        this.institute = institute;
        institute.add(this);
    }

    public void add(Student student) {
        if (students.contains(student)) {
            System.out.println("Ошибка этот студент уже учится на этом факультете");
        }
        else {
            students.add(student);
        }
    }
    public Institute getInstitute() {
        return institute;
    }

    public String getName() {
        return name;
    }

    public ArrayList<Student> getStudents() {
        return students;
    }
    public int countStudents() {
        int quantity = 0;
        for (Student student : students) {
            quantity++;
        }
        return quantity;
    }

    @Override
    public void getInformation() {
        System.out.println(
                "Вся информация о факультете:" +
                "\nНазвание: " + name +
                        "\nКоличество учеников: " +countStudents()
        );

    }
}
