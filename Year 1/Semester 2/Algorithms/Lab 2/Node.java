public class Node<T> {
    T key;
    Node<T> left;
    Node<T> right;
    Node<T> parent;

    public Node(T key) {
        this.key = key;
    }
}
