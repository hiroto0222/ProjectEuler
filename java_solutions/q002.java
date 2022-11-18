package java_solutions;

public class q002 {
    public static void main(String[] args) {
        System.out.println(new q002().compute());
    }

    public int compute() {
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
}
