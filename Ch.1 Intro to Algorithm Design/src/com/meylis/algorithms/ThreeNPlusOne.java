package com.meylis.algorithms;

import java.util.ArrayList;
import java.util.Scanner;

public class ThreeNPlusOne {

    public static void main(String args[]) {
        ArrayList<String> result = new ArrayList<>();
        Scanner scanner = new Scanner(System.in);
        int a, b;

        while (true) {
            String line = scanner.nextLine();
            if (line.length() == 0) break;

            String[] numbers = line.split(" ");
            int maxCycleLength = 0;

            a = Integer.parseInt(numbers[0]);
            b = Integer.parseInt(numbers[1]);

            if (a > b) {
                int temp = b;
                b = a;
                a = temp;
            }

            for (int i=a; i<=b; i++) {
                    int localCycleLength = calculate(i, 0);
                    if (localCycleLength > maxCycleLength) maxCycleLength = localCycleLength;
            }

            result.add(numbers[0] + ' ' + numbers[1] + ' ' + maxCycleLength);
            maxCycleLength = 0;
        }

        for (String line : result) {
            System.out.println(line);
        }
    }

    private static int calculate(int n, int c) {
        if (n == 1) return c + 1;

        if (n % 2 == 0) return calculate(n / 2, c + 1);
        else            return calculate(3 * n + 1, c + 1);
    }
}
