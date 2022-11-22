// # A palindromic number reads the same both ways.
// # The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
// # Find the largest palindrome made from the product of two 3-digit numbers.

// # intuition:
// # largest possible number -> 999 x 999 = 998001
// # smallest possible number -> 100 x 100 = 100000
// # largest possible palindromes -> 100001, 

package java_solutions;

public class q004 {
    public static void main(String[] args) {
        System.out.println(new q004().compute());
    }

    public int compute() {
        int maxPalin = -1;
        for (int i = 100; i < 1000; i++) {
            for (int j = 100; j < 1000; j++) {
                int prod = i * j;
                if (Library.isPalindrome(String.valueOf(prod))) {
                    maxPalin = prod;
                }
            }
        }
        return maxPalin;
    }
}
