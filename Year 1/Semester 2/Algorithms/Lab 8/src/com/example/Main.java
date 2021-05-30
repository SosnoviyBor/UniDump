package com.example;

import java.util.HashSet;
import java.util.Set;

public class Main {
    public static void main(String[] args) {
        OrientedGraph graph = new OrientedGraph();

        System.out.println("");
        testFullGraph(graph);

        System.out.println("\n\n################################################\n");

        graph = new OrientedGraph();
        System.out.println("Список вершин, що пов'язані із вершиною 18:");
        graph.getAdjustmentVerticesFull(18).forEach(e -> System.out.print(e.number + " "));
        System.out.println("");
    }



    public static void testFullGraph(OrientedGraph graph){
        graph.getBasicInfo();
        GraphTraversal.setNonOriented(graph);
        Set<Integer> integers = new HashSet<>();

        long ms = System.currentTimeMillis();
        for (int i = 0; i < 1000; i++) {
            integers = GraphTraversal.depthFirstTraversal(graph, 0);
        }
        ms = System.currentTimeMillis() - ms;
        System.out.println("Пошук depth first зайняв " +
                ms + " мс");
        integers.forEach(e -> System.out.print(e + " "));
    }
}
