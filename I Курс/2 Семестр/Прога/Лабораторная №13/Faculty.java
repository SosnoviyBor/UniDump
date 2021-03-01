import java.util.HashMap;
import java.util.HashSet;

import java.util.Objects;
import java.util.Set;

public class Faculty implements Information {
    private static int MaxStudentForFaculty = 2;
    private final String name;
    private final Institute institute;
    private HashSet<Student> students = new HashSet<>();


    public Faculty(String name, Institute institute, HashSet<Student> students) {
        if (institute == null) {
            throw new NullPointerException("Нельзя создать факультет, без института");
        }
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

    public void add(Student student) throws MaxStudentsException {
        if (students.size() > MaxStudentForFaculty-1) { // .size начинаем считать от 0, а не от 1
            throw new MaxStudentsException("Нельзя добавить еще студентов, на факультете уже нету мест." +
                    " Максимум:" + MaxStudentForFaculty);
        }
        students.add(student);
    }

    public Institute getInstitute() {
        return institute;
    }

    public String getName() {
        return name;
    }

    public Set<Student> getStudents() {
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
                        "\nКоличество учеников: " + countStudents()
        );
    }


    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        Faculty faculty = (Faculty) o;
        return Objects.equals(name, faculty.name);
    }

    @Override
    public int hashCode() {
        return Objects.hash(name);
    }
}
