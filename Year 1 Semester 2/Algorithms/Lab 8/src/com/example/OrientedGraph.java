package com.example;

import java.util.*;

public class OrientedGraph {

    public OrientedGraph() {
        adjVertices = new HashMap<>();

        for (int i = 0; i <= 22; i++) {
            this.addVertex(i);
        }
        this.addEdge(0, 2);
        this.addEdge(0, 9);
        this.addEdge(1, 2);
        this.addEdge(1, 5);
        this.addEdge(2, 5);
        this.addEdge(2, 10);
        this.addEdge(3, 1);
        this.addEdge(3, 6);
        this.addEdge(4, 3);
        this.addEdge(4, 6);
        this.addEdge(5, 4);
        this.addEdge(7, 8);
        this.addEdge(7, 10);
        this.addEdge(7, 13);
        this.addEdge(9, 11);
        this.addEdge(9, 12);
        this.addEdge(13, 14);
        this.addEdge(15, 7);
        this.addEdge(15, 11);
        this.addEdge(16, 11);
        this.addEdge(16, 15);
        this.addEdge(17, 18);
        this.addEdge(17, 22);
        this.addEdge(18, 19);
        this.addEdge(18, 21);
        this.addEdge(18, 22);
        this.addEdge(20, 19);
        this.addEdge(20, 21);
        this.addEdge(21, 19);
        this.addEdge(21, 22);
    }

    Map<Vertex, List<Vertex>> adjVertices;
    boolean isOriented = true;

    public boolean isOriented() {
        return isOriented;
    }

    public void setOriented(boolean oriented) {
        isOriented = oriented;
    }

    public Map<Vertex, List<Vertex>> getAdjVertices() {
        return adjVertices;
    }

    public void addVertex(int number) {
        adjVertices.putIfAbsent(new Vertex(number), new ArrayList<>());
    }

    public void removeVertex(int number) {
        Vertex v = new Vertex(number);
        adjVertices.values().forEach(e -> e.remove(v));
        adjVertices.remove(new Vertex(number));
    }

    public void addEdge(int from, int to) {
        Vertex v1 = new Vertex(from);
        Vertex v2 = new Vertex(to);
        adjVertices.get(v1).add(v2);
    }

    public void removeEdge(int from, int to) {
        Vertex v1 = new Vertex(from);
        Vertex v2 = new Vertex(to);
        List<Vertex> eV1 = adjVertices.get(v1);
        if (eV1 != null)
            eV1.remove(v2);
    }

    public List<Vertex> getAdjustmentVerticesFull(int number) {
        List<Vertex> adjustments = getAdjVertices(number);
        for (Map.Entry<Vertex, List<Vertex>> elem : adjVertices.entrySet()) {
            if (elem.getValue().contains(new Vertex(number))) {
                adjustments.add(elem.getKey());
            }
        }
        return adjustments;
    }

    public void getBasicInfo() {
        System.out.println("Кількість вершин: " + getVertexAmount());
        System.out.println("Кількість ребер: " + getEdgesAmount());
    }

    public int getEdgesAmount() {
        final int[] sum = new int[]{0};
        adjVertices.forEach((key, value) -> sum[0] += value.size());
        return sum[0];
    }

    public int getVertexAmount() {
        return adjVertices.size();
    }

    public List<Vertex> getAdjVertices(int number) {
        return adjVertices.get(new Vertex(number));
    }
}
