package com.example;

import java.util.*;

public class GraphTraversal {
    public static void setNonOriented(OrientedGraph graph) {
        for (Map.Entry<Vertex, List<Vertex>> elem : graph.getAdjVertices().entrySet()) {
            for (Vertex vertex : elem.getValue()) {
                if (!graph.getAdjVertices(vertex.number).contains(elem.getKey()))
                    graph.getAdjVertices(vertex.number).add(elem.getKey());
            }
        }
        graph.setOriented(false);
    }

    public static Set<Integer> depthFirstTraversal(OrientedGraph graph, int root) {
        if (graph.isOriented()) {
            setNonOriented(graph);
        }

        Set<Integer> visited = new LinkedHashSet<>();
        Stack<Integer> stack = new Stack<>();
        stack.push(root);
        while (!stack.isEmpty()) {
            int vertex = stack.pop();
            if (!visited.contains(vertex)) {
                visited.add(vertex);
                for (Vertex v : graph.getAdjVertices(vertex)) {
                    stack.push(v.number);
                }
            }
        }

        return visited;
    }

    public static Set<Integer> breadthFirstTraversal(OrientedGraph graph, int root) {
        if (graph.isOriented()) {
            setNonOriented(graph);
        }

        Set<Integer> visited = new LinkedHashSet<>();
        Queue<Integer> queue = new LinkedList<>();
        queue.add(root);
        visited.add(root);
        while (!queue.isEmpty()) {
            int vertex = queue.poll();
            for (Vertex v : graph.getAdjVertices(vertex)) {
                if (!visited.contains(v.number)) {
                    visited.add(v.number);
                    queue.add(v.number);
                }
            }
        }
        return visited;
    }
}
