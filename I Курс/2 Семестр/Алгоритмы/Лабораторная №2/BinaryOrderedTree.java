import java.util.Objects;

public class BinaryOrderedTree<T> {

    public Node<T> root= null;

    //Workds only if key is Int// Работает только если Node key Integer type !!!!!!
    private long sumOfTree = 0;
    public long findSum () throws Exception {
        if (root==null) {
            return 0;
        }
        if (root.key.getClass() == Integer.class) {
            sumOfTree = 0;
            findSumByRecursion(root);
            return sumOfTree;
        }
        else {
            throw new Exception("Поиск суммы рабоатет только если как ключ мы храним число,\n" +
                    "иначе реализация не продумана.");
        }

    }

    private void findSumByRecursion(Node<T> node) {
        sumOfTree += (Integer) node.key;
        if (node.right!=null) {
            findSumByRecursion(node.right);
        }
        if (node.left!=null) {
            findSumByRecursion(node.left);
        }
    }
    public void delete(T t) throws Exception {
        root = deleteByRecursion(root,t);
    }
    public void inorder() {
        printInorder(root);
    }

    private void printInorder(Node<T> root) {
        if (root != null) {
            printInorder(root.left);
            System.out.print(root.key + " ");
            printInorder(root.right);
        }
    }
    private Node<T> deleteByRecursion(Node<T> root, T key) throws Exception {
        if (root == null)
            return root;

        if (compareTwoValues(root.key,key) == 1)
            root.left = deleteByRecursion(root.left, key);
        else if (compareTwoValues(root.key,key) ==-1)
            root.right = deleteByRecursion(root.right, key);
        else  {
            // node contains only one child
            if (root.left == null)
                return root.right;
            else if (root.right == null)
                return root.left;
            root.key = minValue(root.right);
            root.right = deleteByRecursion(root.right, root.key);
        }
        return root;
    }
    private T minValue(Node<T> root) {
        //initially minval = root
        T minval = root.key;
        //find minval
        while (root.left != null) {
            minval = root.left.key;
            root = root.left;
        }
        return minval;
    }

        @Deprecated
    private Node<T> next(Node<T> x) {
        if (x.right != null)
            return minimum(x.right);
        Node<T> y = x.parent;
        while (y != null && x ==y.right) {
            x = y;
            y = y.parent;
        }
        return y;
    }
        @Deprecated
    private Node<T> minimum(Node<T> x) {
        if (x.left == null)
            return x;
        return minimum(x.left);
    }

    public Node<T> searchByValue(T t) throws Exception {
        return searchByValue(root,t);
    }

    private Node<T> searchByValue(Node<T> current,T value) throws Exception {
        if (current == null) {
            return null;
        }
            if (value == current.key) {
            return current;
        }
        return compareTwoValues(current.key,value)==1
                ? searchByValue(current.left, value)
                : searchByValue(current.right, value);
    }


    public void insert(T t) throws Exception {
        root = addRecursive(root, t);
    }
    private Node<T> addRecursive(Node<T> current, T value) throws Exception {
        if (current == null) {
            return new Node<T>(value);
        }
        if (compareTwoValues(current.key,value)==1) {
            current.left = addRecursive(current.left, value);
        } else if (compareTwoValues(current.key,value)==-1) {
            current.right = addRecursive(current.right, value);
        } else {
            // value already exists
            return current;
        }

        return current;
    }
        @Deprecated
    private void insert(Node<T> node, Node<T> newNode ) throws Exception {
        if (root ==null) {
            root = newNode;
        }
        else {
            while (node != null) {
                if (compareTwoValues(newNode.key,node.key) == 1) {
                    if (node.right != null)
                        node.right = newNode;
                    else {
                        newNode.parent = node;
                        node.right = newNode;
                        break;
                    }
                }
                else {
                    if (node.left!=null)
                        node = node.left;
                    else {
                        newNode.parent = node;
                        node.left = newNode;
                        break;
                    }
                }
            }
        }
    }


    private int compareTwoValues(T t, T d) throws Exception {
        if (t ==null |d ==null) {
            throw new Exception("Не могу сравнить объекты у которых нету ключей");
        }
        else if ( t.getClass() == String.class && d.getClass()==String.class) {
            if (((String) t).length() > ((String) d).length()) {
                return 1;
            }
            else if ((((String) t).length() < ((String) d).length())){
                return -1;
            }
            else
                return 0;
        }
        else if (t.getClass()==Integer.class && d.getClass()==Integer.class) {
            if ((Integer) t > (Integer) d) {
                return 1;
            }
            else if  ( (Integer) t < (Integer) d) {
                return -1;
            }
            else {
                return 0;
            }
        }
        else {
            throw new Exception("Something went Wrong");
        }

    }
}
