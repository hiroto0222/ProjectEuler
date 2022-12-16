package java_solutions;

public class q002 {
    public static void main(String[] args) {
        System.out.println(new q002().compute2());
    }

    public int compute1() {
        int n = 4000000;
        int ans = 2;
        int f1 = 1, f2 = 2;
        int curr = f1 + f2;

        while (curr < n) {
            if (curr % 2 == 0) {
                ans += curr;
            }
            f1 = f2;
            f2 = curr;
            curr = f1 + f2;
        }

        return ans;
    }

    public int compute2() {
        // using closed form solutions
        return fibSum(fibIndex(4000000)) / 2;
    }

    static double sqrt5 = Math.sqrt(5);
    static double phi = (1 + sqrt5) / 2;
    static double psi = (1 - sqrt5) / 2;

    public static double F(int n) {
        return (Math.pow(phi, n) - Math.pow(psi, n)) / sqrt5;
    }

    public static int fibIndex(int F) {
        return (int) Math.floor(Math.log(F * sqrt5 + 0.5) / Math.log(phi));
    }

    public static int fibSum(int n) {
        return (int) F(n + 2) - 1;
    }
}
