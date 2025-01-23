import java.util.Scanner;

public class solution5 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int t = scanner.nextInt();
        for (int i = 0; i < t; i++) {
            int n = scanner.nextInt();
            int k = scanner.nextInt();
            int q = scanner.nextInt();
            int[] dist = new int[k + 2]; // Increased size by 2
            int[] time = new int[k + 2]; // Increased size by 2
            dist[0] = 0;
            time[0] = 0;
            for (int j = 1; j <= k; j++) {
                dist[j] = scanner.nextInt();
            }
            for (int j = 1; j <= k; j++) {
                time[j] = scanner.nextInt();
            }
            for (int j = 0; j < q; j++) {
                int query = scanner.nextInt();
                int index = binarySearch(dist, query, k);
                if (index == k + 1) { // Adjusted condition for out of bound
                    System.out.print(time[index - 1] + " "); // Adjusted index
                } else {
                    double speed = (double) (dist[index + 1] - dist[index]) / (time[index + 1] - time[index]);
                    int req = query - dist[index];
                    System.out.print((int)(time[index] +(req / speed)) + " ");
                }
            }
            System.out.println();
        }
    }

    public static int binarySearch(int[] arr, int item, int k) {
        int low = 0;
        int high = k + 1; // Adjusted high value
        int ans = 0;
        while (low <= high) {
            int mid = (low + high) / 2;
            if (arr[mid] == item) {
                return mid;
            } else if (arr[mid] > item) {
                high = mid - 1;
            } else {
                ans = mid;
                low = mid + 1;
            }
        }
        return ans;
    }
}