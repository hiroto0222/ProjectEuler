// If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
// Find the sum of all the multiples of 3 or 5 below 1000.

// 3*n < 1000
// 5*n < 1000

package java_solutions;

public class q001 {
	public static void main(String[] args) {
        System.out.println(new q001().compute2());
	}
	
	public int compute1() {
        // brute force
		int sum = 0;
        for (int i = 0; i < 1000; i++) {
            if (i % 3 == 0 || i % 5 == 0) {
                sum += i;
            }
        }
        
        return sum;
	}

    public int compute2() {
        // using Gauss's summation formula
        int x = Math.floorDiv(999, 3);
        int y = Math.floorDiv(999, 5);
        int z = Math.floorDiv(999, 15);

        double ans = 0.5 * (
            3 * x * (x + 1) +
            5 * y * (y + 1) -
            15 * z * (z + 1)
        );

        return (int) ans;
    }
}