// Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
// If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

// For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284.
// The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

// Evaluate the sum of all the amicable numbers under 10000.


package java_solutions;

public class q021 {
    public static void main(String[] args) {
        System.out.println(new q021().compute());
    }

    public int compute() {
        int ans = 0;
        for (int i = 1; i < 10000; i++) {
            if (isAmicable(i)) ans += i;
        }
        return ans;
    }

    public static boolean isAmicable(int n) {
        int m = divisorSum(n);
        return m != n && divisorSum(m) == n;
    }

    public static int divisorSum(int n) {
        int sum = 1;
        for (int i = 2; i <= Math.ceil(Math.sqrt(n)); i++) {
            if (n % i == 0) {
                sum += i + n / i;
            }
        }
        return sum;
    }
}
