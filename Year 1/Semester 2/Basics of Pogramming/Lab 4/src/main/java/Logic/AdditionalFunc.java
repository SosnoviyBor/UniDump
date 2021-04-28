package Logic;

import java.util.ArrayList;

public class AdditionalFunc {
    public static ArrayList<Institute> institutes = new ArrayList<>();
//    public static void init() {
//        Institute kpi = new Institute("KPI");
//        Faculty FICT = new Faculty("FICT",kpi);
//        Faculty IPSA = new Faculty("IPSA",kpi);
//        Student korol = new Student("Korol Kirill","AC555555",87.3,FICT);
//        Student bukreev = new Student("Bukreev Nikita", "AC666666",98.3,FICT);
//        Student borya = new Student("Sosnoviy Bor","AC77777777",95.6,FICT);
//        Student goncharov = new Student("Goncharov Anton","AE333333",75.3,IPSA);
//        Student ivanov = new Student("Ivanov Ivan","AE666666",95,IPSA);
//        institutes.add(kpi);
//    }
    static {
            Institute kpi = new Institute("KPI");
        Faculty FICT = new Faculty("FICT",kpi);
        Faculty IPSA = new Faculty("IPSA",kpi);
        Student korol = new Student("Korol Kirill","AC555555",87.3,FICT);
        Student bukreev = new Student("Bukreev Nikita", "AC666666",98.3,FICT);
        Student borya = new Student("Sosnoviy Bor","AC77777777",95.6,FICT);
        Student goncharov = new Student("Goncharov Anton","AE333333",75.3,IPSA);
        Student ivanov = new Student("Ivanov Ivan","AE666666",95,IPSA);
        institutes.add(kpi);
}
    public static ArrayList<Faculty> allFaculties() {
        ArrayList<Faculty> allFaculties = new ArrayList<>();
        for (Institute institute: institutes) {
            allFaculties.addAll(institute.getFaculties());
        }
        return allFaculties;
    }
    public static ArrayList<Student> allStudents() {
        ArrayList<Student> allStudents = new ArrayList<>();
        for (Faculty faculty: allFaculties()) {
            allStudents.addAll(faculty.getStudents());
        }
        return allStudents;
    }
}
