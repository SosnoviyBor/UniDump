import java.text.SimpleDateFormat;
import java.util.*;

 class Mai1n{
    public static void main(String[] args) {
        TreeSet<Song> list = new TreeSet<>(new Song.ComparatorByDurability());
        Song song1 = new Song("song1",2.30);
        Song song2 = new Song("song2",1.30);
        Song song3 = new Song("song3",3.30);
        list.add(song1); list.add(song2); list.add(song3);
        System.out.println(list);
        Song[] array = {song1,song2,song3};

        Arrays.sort(array, new Comparator<Song>() {
            @Override
            public int compare(Song o1, Song o2) {
                return String.CASE_INSENSITIVE_ORDER.compare(o1.songName, o2.songName);
            }
        });
        System.out.println(array);
    }
}
class Song {
     public String songName;
     public double durability;
     String text;
     String[] singers; // Певцы
     int  auditions = 0;
     String[] streamingPlace; // Сервисы где можно прослушать

    public  double getDurability() {
        return durability;
    }

    public static class ComparatorByDurability implements Comparator<Song> {
        @Override
        public int compare(Song o1, Song o2) {
            return Double.compare(o1.durability, o2.durability);
        }
    }


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

    public void setText(String text) {
        this.text = text;
    }

    public void setSingers(String[] singers) {
        this.singers = singers;
    }


    @Override
    public String toString() {
        return "Song{" +
                "songName='" + songName + '\'' +
                ", durability=" + durability +
                '}';
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