
import java.util.HashMap;
import java.util.HashSet;

import java.util.Set;

public class Faculty implements Information {
    private final String name;
    private final Institute institute;
    private HashSet<Student> students = new HashSet<>();
    private HashMap<String,Student>  map = new HashMap<>();

    public Student getStudentByMarkBook(String markBookIndex) {
        return map.get(markBookIndex);
    }


    public Faculty(String name, Institute institute, HashSet<Student> students) {
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
        students.add(student);
        map.put(student.getMarkBookIndex(),student);
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
                        "\nКоличество учеников: " +countStudents()
        );

    }
}
