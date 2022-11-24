package java_solutions;

public class q023 {
    public static void main(String[] args) {
        System.out.println(new q023().compute());
    }

    private static final int N = 28123;
    private boolean[] isAbundant = new boolean[N + 1]; 

    public int compute() {
        for (int i = 1; i < isAbundant.length; i++) {
            isAbundant[i] = isAbundant(i);
        }
        System.out.println(isAbundant);

        int sum = 0;
        for (int n = 1; n <= N; n++) {
            if (!isSumOf2Abundants(n)) sum += n;
        }

        return sum;
    }

    private boolean isSumOf2Abundants(int n) {
        for (int i = 0; i <= n; i++) {
            if (isAbundant[i] && isAbundant[n - i]) {
                return true;
            }
        }
        return false;
    }

    private static boolean isAbundant(int n) {
        if (n < 1) {
            throw new IllegalArgumentException();
        }

        int sum = 1;
        int end = Library.sqrt(n);
        for (int i = 2; i <= end; i++) {
            if (n % i == 0) {
                sum += (i + n / i);
            }
        }
        if (end * end == n) {
            sum -= end;
        }

        return sum > n;
    }
    
}
