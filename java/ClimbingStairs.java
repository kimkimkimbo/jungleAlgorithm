public class ClimbingStairs {
    // climbStairs 함수: n번째 계단까지 도달하는 경우의 수를 계산
    public static int climbStairs(int n) {
        // 계단이 1개일 경우 경우의 수는 1가지
        if (n == 1) {
            return 1;
        }

        // 계단이 2개일 경우 경우의 수는 2가지 (1+1 또는 2)
        if (n == 2) {
            return 2;
        }

        // dp 배열 생성: dp[i]는 i번째 계단까지 도달할 수 있는 방법의 수
        // n번째 계단까지 계산해야 하므로 크기는 n+1로 설정
        int[] dp = new int[n + 1];

        // 초기 조건 설정
        dp[1] = 1; // 1번째 계단까지 도달하는 방법은 1가지
        dp[2] = 2; // 2번째 계단까지 도달하는 방법은 2가지

        // 점화식 적용: 3번째 계단부터 n번째 계단까지 경우의 수 계산
        // dp[i] = dp[i-1] + dp[i-2]
        for (int i = 3; i <= n; i++) {
            dp[i] = dp[i - 1] + dp[i - 2];
        }

        // 최종적으로 n번째 계단까지 도달하는 경우의 수 반환
        return dp[n];
    }

    // main 함수: 테스트용 실행 진입점
    public static void main(String[] args) {
        // 예시: 4번째 계단까지 도달하는 경우의 수 출력
        System.out.println(climbStairs(4)); // 출력값: 5
    }
}
