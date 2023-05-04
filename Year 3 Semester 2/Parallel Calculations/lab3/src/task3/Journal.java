package task3;

import java.util.*;
import java.util.stream.Collectors;

public class Journal {
    private final Map<Student, List<Integer>> grades;

    public Journal(Set<Student> students) {
        this.grades = students
                .stream()
                .collect(Collectors.toMap(
                        student -> student,
                        student -> new ArrayList<>()));
    }

    public synchronized void addGradeForStudent(Student student, Integer grade) {
        final List<Integer> studentsGrades = grades.get(student);
        if (studentsGrades == null) throw new IllegalArgumentException("Unknown student: " + student.getName());
        else studentsGrades.add(grade);
    }

    public Map<Student, List<Integer>> getGrades() {
        return grades;
    }
}
