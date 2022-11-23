package java_solutions;

import java.math.BigInteger;

public class q020 {
    public static void main(String[] args) {
        System.out.println(new q020().compute());
    }

    public int compute() {
        String fact = factorial(100).toString();
        int sum = 0;
        for (int i = 0; i < fact.length(); i++) {
            sum += Character.getNumericValue(fact.charAt(i));
        }
        return sum;
    }

    public static BigInteger factorial(int n) {
        if (n < 0) throw new IllegalArgumentException();
        BigInteger fact = BigInteger.ONE;
        for (int i = 2; i <= n; i++) {
            fact = fact.multiply(BigInteger.valueOf(i));
        }
        return fact;
    }
}
