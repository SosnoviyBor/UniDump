package com.example;

public class Main {
    public static void main(String[] args) {
        OrientedGraph graph;

        graph = new OrientedGraph();
        System.out.println("The graph itself:");
        graph.testFullGraph();

        System.out.println("\n\n################################################\n");

        System.out.println("Test graph with less edges:");
        graph.testGraphWithLessEdges();

        System.out.println("\n\n################################################\n");

        graph = new OrientedGraph();
        graph.customGraphGen();
        System.out.println("Test adjustment vertices to vertex 6:");
        graph.getAdjustmentVerticesFull(6).forEach(e -> System.out.print(e.number + " "));
    }
}
