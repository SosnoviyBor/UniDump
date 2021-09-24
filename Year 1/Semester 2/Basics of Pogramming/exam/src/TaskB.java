import java.util.ArrayList;
import java.util.List;

class MainB {
    public static void main(String[] args) {
        Enrollee sasha = new Enrollee("Sasha",100);
        Enrollee oleg = new Enrollee("Oleg",68);
        Enrollee misha = new Enrollee("Misha",74);
        Enrollee dima = new Enrollee("Dima",87);
        Enrollee ilya = new Enrollee("Ilya", 45);

        List<Enrollee> enrollees = new ArrayList<Enrollee>();
        enrollees.add(sasha);
        enrollees.add(oleg);
        enrollees.add(misha);
        enrollees.add(dima);
        enrollees.add(ilya);

        int budgetPlace = 1;
        int contractPlace = 2;

        // Список контрактников
        enrollees.stream()
                .sorted((x,y)->(-1)*Double.compare(x.getScore(),y.getScore())) //compare by score
                .filter(x->x.getScore()>=60)
                .skip(budgetPlace)
                .limit(contractPlace)
                .sorted((x,y)->x.getName().compareTo(y.getName())) //compare by name
                .forEach(System.out::println);

        // Список тих, хто маэ быльше балів за 60, але не вліз у кафедру
        enrollees.stream()
                .sorted((x,y)->(-1)*Double.compare(x.getScore(),y.getScore()))
                .filter(x->x.getScore()>=60)
                .skip(budgetPlace+contractPlace)
                .sorted((x,y)->x.getName().compareTo(y.getName())) //compare by name
                .forEach(System.out::println);

        // СПисок тих, хто не пройшов
        enrollees.stream()
                .sorted((x,y)->(-1)*Double.compare(x.getScore(),y.getScore())) //compare by score
                .filter(x->x.getScore()<60)
                .forEach(x->System.out.println(x.getName()+" "));
    }
}

class Enrollee {
    String name;
    double score;

    public Enrollee(String name, double score) {
        this.name = name;
        this.score = score;
    }

    public String getName() {
        return name;
    }

    public double getScore() {
        return score;
    }

    @Override
    public String toString() {
        return "Enrollee{" +
                "name='" + name + '\'' +
                ", score=" + score +
                '}';
    }
}
