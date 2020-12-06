import java.lang.reflect.Field;

public class Main {
    public static void main(String[] args) {

        Institute kpi = new Institute("KPI");
        Faculty FICT = new Faculty("FICT",kpi);
        Faculty IPSA = new Faculty("IPSA",kpi);
        Student korol = new Student("Korol Kirill","AC555555",87.3,FICT);
        Student bukreev = new Student("Bukreev Nikita", "AC666666",98.3,FICT);
        Student borya = new Student("Sosnoviy Bor","AC77777777",95.6,FICT);
        Student goncharov = new Student("Goncharov Anton","AE333333",75.3,IPSA);
        Student ivanov = new Student("Ivanov Ivan","AE666666",95,IPSA);

        //System.out.println(kpi.showBestStudents());
        //System.out.println(kpi.countStudents());
        //System.out.println(kpi.mostStudents());
        //    kpi.findStudent("AE333333");

        goncharov.getInformation();
        System.out.println();
        FICT.getInformation();
        System.out.println();
        kpi.getInformation();
    }
}
