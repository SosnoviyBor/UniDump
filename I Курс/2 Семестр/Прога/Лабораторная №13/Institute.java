import java.util.ArrayList;
import java.util.HashSet;
import java.util.Iterator;
import java.util.Objects;


public class Institute implements Information{
    private HashSet<Faculty> faculties = new HashSet<>();
    private final String name;

    public Institute(String name, HashSet<Faculty> faculties) {
        this.faculties = faculties;
        this.name = name;
    }

    public Institute(String name) {
        this.name = name;
    }

    public String getName() {
        return name;
    }

    public void add(Faculty faculty) {
            faculties.add(faculty);
    }


    public int countStudents() {
        int quantity = 0;
        Iterator iterator = faculties.iterator();
        while (iterator.hasNext()) {
            quantity += ((Faculty) iterator.next()).countStudents() ;
        }
        return quantity;
    }


    public String mostStudents() {
        Faculty answer = null;
        Iterator<Faculty> iterator = faculties.iterator();
        String nullAnswer = "? ????????? ???? ??????????? ??? ?????????? ????????? ? ??????????? ????? 0";
        int tempStudents = 0;
        while (iterator.hasNext()){
            Faculty tempFaculty = iterator.next();
            if (tempFaculty.countStudents()>tempStudents) {
                tempStudents = tempFaculty.countStudents();
                answer = tempFaculty;
            }
        }
        return answer == null? nullAnswer : "??? ?????????: " + answer.getName();
    }


    private ArrayList<Student> bestStudents() {
        ArrayList<Student> bestStudents = new ArrayList<>();
        for (Faculty faculty: faculties) {
            for (Student student :faculty.getStudents()) {
                if (student.getGPA()>=95) {
                    bestStudents.add(student);
                }
            }
        }
        return bestStudents;
    }


    public String showBestStudents() {
        ArrayList<String> bestStudents = new ArrayList<>();
        for (Student student: bestStudents()) {
            bestStudents.add(student.getName());
        }
        return bestStudents.toString();
    }


    public void findStudent(String markBookIndex) {

        for (Faculty faculty: faculties) {
            for (Student student: faculty.getStudents()){
                if (student.getMarkBookIndex().equals(markBookIndex)) {
                    System.out.println("??????? ?? ???????: "+markBookIndex+" ??????. ??? ??????????:");
                    student.getInformation();
                    return;
                }
            }
        }
        System.out.println("??????? ?? ???????: "+markBookIndex+" ?? ??????");
    }

    @Override
    public void getInformation() {
        System.out.println(
                "??? ?????????? ?? ?????????:" +
                        "\n????????: " + name +
                        "\n??????????: " +getStringOfFaculties() +
                        "\n?????????? ????????: " +countStudents()
        );
    }
    private String getStringOfFaculties() {
        StringBuilder allFaculties = new StringBuilder();
        for (Faculty faculty: faculties) {
            allFaculties.append(faculty.getName()).append(" ");
        }
        return allFaculties.toString();
    }

}
