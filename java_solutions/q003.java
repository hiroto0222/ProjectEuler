// # The prime factors of 13195 are 5, 7, 13 and 29.
// # What is the largest prime factor of the number 600851475143 ?

// # intuition:
// # every integer n > 1 has a unique factorization as product of primes
// # by dividing n repeatedly by its smallest factor (which is prime)
// # then the last factor we divide out must be largest prime factor of n
// # 71 * 839 * 1471 * 6857 <-

package java_solutions;

public class q003 {
	public static void main(String[] args) {
        System.out.println(new q003().compute());
	}

    public static long smallestPrimeFactor(long n) {
        if (n <= 1) {
            throw new IllegalArgumentException();
        }
        for (long i = 2; i <= Math.sqrt(n); i++) {
            if (n % i == 0) {
                return i;
            }
        }
        return n;
    }
	
	public long compute() {
		long n = 600851475143L;
        while (true) {
            long p = smallestPrimeFactor(n);
            if (p < n) {
                n /= p;
            } else {
                return n;
            }
        }
	}
}