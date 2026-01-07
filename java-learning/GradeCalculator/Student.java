// Student Grade Calculator

// Класс Student (имя, оценки)
// Средний балл, лучшая/худшая оценка
// Список студентов, найти отличников
// Применяет: объекты, ArrayList, методы

import java.util.ArrayList;
import java.util.Arrays;

public class Student {
    String name;
    ArrayList<Integer> grades;

    public Student(String name, ArrayList<Integer> grades) {
        this.name = name;
        this.grades = grades;
    }

    public static void main(String[] args) {
        Student bek = new Student("Bek", new ArrayList<>(Arrays.asList(5, 5, 5, 5)));
        Student azat = new Student("Azat", new ArrayList<>(Arrays.asList(5, 2, 5, 3)));
        Student uluk = new Student("Uluk", new ArrayList<>(Arrays.asList(4, 3, 3, 5)));
        Student[] students = {bek, azat, uluk};
        ArrayList<Student> topStudents = new ArrayList<>();


        for (Student stud : students) {
            System.out.printf("%s's greatest grade's %d, lowest one's %d, mean grade %s\n\n", stud.name, stud.getGreatestGrade(), stud.getLowestGrade(), stud.getMeanGrade());
            if (stud.getMeanGrade() == 5) {
                topStudents.add(stud);
            }
        }
        System.out.println("Top students: ");
        for (Student s : topStudents) {
            System.out.println(s.name);
        }
    }

    public double getMeanGrade() {
        double sumOfGrades = 0;
        for (int grade : this.grades) {
            sumOfGrades += grade;
        }
        return sumOfGrades / this.grades.size();
    }

    public int getGreatestGrade() {
        int greatestGrade = this.grades.get(0);
        for (int grade : this.grades) {
            if (greatestGrade < grade) {
                greatestGrade = grade;
            }
        }
        return greatestGrade;
    }

    public int getLowestGrade() {
        int lowestGrade = this.grades.get(0);
        for (int grade : this.grades) {
            if (lowestGrade > grade) {
                lowestGrade = grade;
            }
        }
        return lowestGrade;
    }
}
