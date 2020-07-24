package com.meylis.algorithms;

public class SpecialDivision {
    public static void main(String args[]) {
        System.out.println(divide(-10, 2));
    }

    private static int divide(int dividend, int divisor) {
        int quotient, result;
        quotient = result = 0;

        while (result + divisor <= dividend) {
            result += divisor;
            quotient++;
        }
        return quotient;
    }
}
