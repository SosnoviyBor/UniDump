import java.util.ArrayList;
import java.util.OptionalDouble;
import java.util.stream.DoubleStream;

class MainA {
    public static void main(String[] args) {
        Student sasha = new Student("Sasha","Gorduz","AVB",100);
        Student oleg = new Student("Oleg","Kravets","ACB",68);
        Student misha = new Student("Misha","Radchenko","ADB",74);
        Student dima = new Student("Dima","Ochkas","DDB",87);

        Faculty ipsa = new Faculty("IPSA");
        ipsa.add(oleg); ipsa.add(misha);

        Faculty fict = new Faculty("FICT");
        fict.add(dima); fict.add(sasha);

        Institute kpi = new Institute("KPI");
        kpi.add(fict); kpi.add(ipsa);

        double instituteAverageScore = kpi.faculties.stream()
                .flatMap(x-> x.getStudents().stream())
                .flatMapToDouble(x-> DoubleStream.of(x.averageScore))
                .average()
                .orElse(0);

        System.out.println("Institute average score is "+instituteAverageScore);

        kpi.faculties.stream()
                .flatMap(x->x.getStudents().stream())
                .filter(x->x.averageScore>instituteAverageScore)
                .forEach(System.out::println);
    }
}

class Institute {
    String name;
    ArrayList<Faculty> faculties;

    public Institute(String name) {
        this.name = name;
        faculties=  new ArrayList<>();
    }

    public void add(Faculty faculty) {
        faculties.add(faculty);
    }
}

class Faculty{
    String name;
    ArrayList<Student> students;

    public Faculty(String name) {
        this.name = name;
        students = new ArrayList<>();
    }

    public void add(Student student) {
        students.add(student);
    }

    public ArrayList<Student> getStudents() {
        return students;
    }
}

class Student {
    String firstName;
    String lastName;
    String bookId;
    double averageScore;

    public Student(String firstName, String lastName, String bookId, double averageScore) {
        this.firstName = firstName;
        this.lastName = lastName;
        this.bookId = bookId;
        this.averageScore = averageScore;
    }

    public double getAverageScore() {
        return averageScore;
    }

    @Override
    public String toString() {
        return "Student{" +
                "firstName='" + firstName + '\'' +
                ", lastName='" + lastName + '\'' +
                ", averageScore=" + averageScore +
                '}';
    }
}