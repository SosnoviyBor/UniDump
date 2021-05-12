public class Main {
    public static void main(String[] args) {
        String date = "11.22.3333";

        Integer day = Integer.parseInt(date.substring(0,2));
        Integer month = Integer.parseInt(date.substring(3,5));
        Integer year = Integer.parseInt(date.substring(6,10));

        System.out.println(day);
        System.out.println(month);
        System.out.println(year);
    }
}
