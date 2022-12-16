package java_solutions;

public class q005 {
    public static void main(String[] args) {
        System.out.println(new q005().compute());
    }

    public int compute() {
        // lcm recursive
        int n = 1;
        for (int i = 2; i <= 20; i++) {
            n = lcm(n, i);
        }

        return n;
    }

    public static int gcd(int a, int b) {
        if (a == 0) return b;
        return gcd(b % a, a);
    }

    public static int lcm(int a, int b) {
        return (int)(a / gcd(a, b)) * b;
    }
}
