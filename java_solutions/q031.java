package java_solutions;

public class q031 {
  public static void main(String[] args) {
    System.out.println(new q031().compute());
  }

  public int compute() {
    int target = 200;
    int[] coins = {1, 2, 5, 10, 20, 50, 100, 200};
    int[] dp = new int[target + 1];
    dp[0] = 1;

    for (int i = 0; i < coins.length; i++) {
      for (int j = coins[i]; j <= target; j++) {
        dp[j] += dp[j - coins[i]];
      }
    }

    return dp[target];
  }
}
