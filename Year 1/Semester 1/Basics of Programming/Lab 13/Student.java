import java.util.Objects;

public class Student implements Information {
    private final String name;
    private final String markBookIndex;
    private double GPA;
    private final Faculty faculty;

    public Student(String name, String markBookIndex, double GPA,Faculty faculty) throws MaxStudentsException {
        if (GPA<0) {
            throw new IllegalArgumentException("??????? ?????? ?? ????? ???? ?????? 0");
        }
        if ( faculty == null ) {
            throw new NullPointerException("You can't add student to a non-existent faculty");
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
            throw new IllegalArgumentException("??????? ?????? ?? ????? ???? ?????? 0");
        }
        this.GPA = GPA;
    }

    public Faculty getFaculty() {
        return faculty;
    }

    @Override
    public void getInformation() {
        System.out.println(
                "??? ?????????? ? ???????:" +
                        "\n???: " +this.name +
                        "\n????????: " + faculty.getInstitute().getName() +
                        "\n?????????: " + faculty.getName() +
                        "\n????? ?????????????: " + this.markBookIndex +
                        "\n??????? ???: " + this.GPA
        );
    }


}
