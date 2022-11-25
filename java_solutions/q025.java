package java_solutions;

import java.math.BigInteger;

public class q025 {
    public static void main(String[] args) {
        System.out.println(new q025().compute());
    }

    public int compute() {
        BigInteger f1 = BigInteger.ONE;
        BigInteger f2 = BigInteger.ONE;
        BigInteger curr = BigInteger.TWO;
        int i = 3;

        while (true) {
            if (curr.toString().length() == 1000) {
                return i;
            }

            f1 = f2;
            f2 = curr;
            curr = f1.add(f2);
            i++;
        }
    }
}