// Temperature Analyzer

// Массив температур за неделю
// Найти среднюю, максимальную, минимальную
// Сколько дней было выше среднего
// Применяет: массивы, циклы, методы

public class TemperatureAnalyzer {
    public static void main(String[] args) {
        double[] weekTemperatures = {32.4, 35.2, 28.0, 25.9, 30.3, 31.4, 33.0};
        double sumTemp = 0;
        double maxTemp = weekTemperatures[0];
        double minTemp = weekTemperatures[0];
        int greaterThanMean = 0;

        for (double dayTemp : weekTemperatures) {
            if (dayTemp > maxTemp) {
                maxTemp = dayTemp;
            }
            if (dayTemp < minTemp) {
                minTemp = dayTemp;
            }
            sumTemp += dayTemp;
        }

        for (double dayTemp : weekTemperatures) {
            if (dayTemp > sumTemp / weekTemperatures.length) {
                greaterThanMean += 1;
            }
        }

        System.out.printf("Min temp for a week is: %s\n", minTemp);
        System.out.printf("Max temp for a week is: %s\n\n", maxTemp);
        System.out.printf("Mean temp for a week is: %s\n", sumTemp / weekTemperatures.length);
        System.out.printf("How many days were above average? %d\n", greaterThanMean);
    }
}
