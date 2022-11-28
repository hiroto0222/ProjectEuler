package java_solutions;

import java.util.Map;
import java.util.HashMap;


public class q026 {
    public static void main(String[] args) {
        System.out.println(new q026().compute());
    }

    public int compute() {
        int ans = 0;
        int maxLength = 0;
        for (int i = 1; i <= 1000; i++) {
            int currLen = getReciprocalCycleLength(i);
            if (currLen > maxLength) {
                ans = i;
                maxLength = currLen;
            }
        }

        return ans;
    }

    public static int getReciprocalCycleLength(int n) {
        Map<Integer, Integer> seen = new HashMap<>();
        int x = 1;
        for (int i = 0; ; i++) {
            if (seen.containsKey(x)) {
                return i - seen.get(x);
            } else {
                seen.put(x, i);
                x = x * 10 % n;
            }
        }
    }
}
