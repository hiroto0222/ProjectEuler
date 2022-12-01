package java_solutions;

import java.math.BigInteger;
import java.util.Set;
import java.util.HashSet;

public class q029 {
    public static void main(String[] args) {
        System.out.println(new q029().compute());
    }

    public int compute() {
        Set<BigInteger> seen = new HashSet<>();
        for (int a = 2; a <= 100; a++) {
            for (int b = 2; b <= 100; b++) {
                seen.add(BigInteger.valueOf(a).pow(b));
            }
        }
        return seen.size();
    }
}
