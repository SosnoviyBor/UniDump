import java.text.SimpleDateFormat;
import java.util.*;

public class Main {
    //something
    //ssdsad
    public static void main(String[] args) {
        Song song1 = new Song("song1",3.30);
        Song song2 = new Song("song2",2.30);
        Song song3 = new Song("song3",2.25);
        Song song4 = new Song("song4",0.30);
        Song song5 = new Song("song5",1.30);
        Song song6 = new Song("song6",1.40);
        Song song7 = new Song("song7",0.30);

        // 2.1 за допомогою лямбда-виразів створити компаратор
        Comparator<Song> compareByDurability = (s1,s2) -> {
          if (s1.durability> s2.durability) return 1;
          else if (s1.durability< (s2).durability) return -1;
          else return 0;
        };
        // 2.2 Comparator.reversed() створити компаратор для сортування за обраною ознакою у зворотному порядку;
        Comparator<Song> reverseCompareByDurability = compareByDurability.reversed();
        //2.3)	за допомогою дефолтного метода Comparator.thenComparing() створити компаратор,
        //який буде порівнювати об’єкти за однією ознакою, а у разі коли вони співпадають порівнювати за іншою ознакою;\
        //  https://howtodoinjava.com/java/sort/sort-on-multiple-fields/
        Comparator<Song> mixedComporator = compareByDurability.thenComparing(
                    (o1,o2) -> String.CASE_INSENSITIVE_ORDER.compare(o1.songName,o2.songName)
                    );
        // https://www.geeksforgeeks.org/comparator-nullsfirst-method-in-java-with-examples/
        // Comparator.nullsLast() створити компаратор, який дозволить порівнювати
        // null-посилання на об’єкти з іншими об’єктами.
        Comparator<Song> nullMixedComparator = Comparator.nullsFirst(mixedComporator);
        List<Song> list = new ArrayList<>();
        list.add(song1); list.add(song2); list.add(song3); list.add(song4); list.add(song5); list.add(song6);
        list.add(song7);

        System.out.println(list);
        list.sort(compareByDurability);
        System.out.println(list);
        list.sort(reverseCompareByDurability);
        System.out.println(list);
        list.sort(mixedComporator);
        System.out.println(list);
        list.add(null);
        System.out.println(list);
        list.sort(nullMixedComparator);
        System.out.println(list);

    }
}
class Song {
    protected String songName;
    protected double durability;
    protected String text;
    protected String[] singers; // Певцы
    protected int  auditions = 0;
    protected String[] streamingPlace; // Сервисы где можно прослушать
    static String releaseDate = getDate();

    Song(String songName, double durability, String text, String[] singers) {
        this.songName = songName;
        this.durability = durability;
        this.text = text;
        this.singers = singers;
    }
    Song(String songName, double durability) {
        this.songName = songName;
        this.durability = durability;
    }

    public void sing() {
        auditions++;
    }
    public int getAuditions() {
        return auditions;
    }


    public String[] getSingers() {
        return singers;
    }

    public void setSingers(String[] singers) {
        this.singers = singers;
    }

    public String getText() {
        return text;
    }

    @Override
    public String toString() {
        return "Song{" +
                "songName='" + songName + '\'' +
                ", durability=" + durability +
                '}';
    }

    public void setText(String text) {
        this.text = text;
    }

    public String[] getStreamingPlace() {
        return streamingPlace;
    }

    public void setStreamingPlace(String... streamingPlace) {
        this.streamingPlace = streamingPlace;
    }

    public String getDurability() {
        return durability +" min";
    }

    public String getSongName() {
        return songName;
    }
    public int countSinger() {
        return singers.length;
    }
    private static String getDate() {
        SimpleDateFormat formatter= new SimpleDateFormat("yyyy-MM-dd 'at' HH:mm:ss z");
        Date date = new Date(System.currentTimeMillis());
        return formatter.format(date);
    }

    public String getReleaseDate() {
        return releaseDate;
    }

}

class VideoClip extends Song {
    protected String producer;
    protected int views = 0;
    protected boolean advertise; //присутсвует ли реклама

    VideoClip(String songName, double durability, String text,String producer, String... singers) {
        super(songName, durability, text, singers);
        this.producer = producer;
    }

    VideoClip(String songName, double durability) {
        super(songName, durability);
    }

    public void watch() {
        views++;
    }

    public String getProducer() {
        return producer;
    }

    public void setProducer(String producer) {
        this.producer = producer;
    }

    public int getViews() {
        return views;
    }

    public boolean isAdvertise() {
        return advertise;
    }

    public void setAdvertise(boolean advertise) {
        this.advertise = advertise;
    }

    @Override
    public String toString() {
        return super.toString()+" Producer: " +producer+" Advertise:" +advertise;
    }
}