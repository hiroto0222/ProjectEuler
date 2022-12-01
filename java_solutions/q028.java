package java_solutions;

public class q028 {
    public static void main(String[] args) {
        System.out.println(new q028().compute());
    }

    public int compute() {
        int ans = 1;
        for (int i = 3; i <= 1001; i+=2) {
            int temp = i * i;
            int x = i - 1;
            ans += (temp + (temp - x) + (temp - 2 * x) + (temp - 3 * x));
        }
        return ans;
    }
}
