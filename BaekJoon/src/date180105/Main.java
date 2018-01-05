package date180105;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class Main {

	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int M = Integer.parseInt(br.readLine());
		int N = Integer.parseInt(br.readLine());
		int[] resultArray = calPrime(M, N);
		int smallestPrime = resultArray[0];
		int addPrime = resultArray[1];
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		bw.write(Integer.toString(addPrime) + "\n");
		if (smallestPrime != 0)
			bw.write(Integer.toString(smallestPrime) + "\n");
		
		bw.flush();
		bw.close();
	}

	private static int[] calPrime(int M, int N) {
		int[] result = new int[2];
		int totalSum = 0;
		int isFirst = 0;
		if (M == 1)
			M += 1;
		for (int i = M; i <= N; i++) {
			int isPrime = 0;
			for (int j = 2; j < i; j++) {
				if (i % j == 0) {
					isPrime = -1;
					break;
				}
			}
			if (isPrime < 0)
				continue;
			if (isFirst == 0) {
				result[0] = i;
				isFirst = 1;

			}
			totalSum += i;

		}
		if (totalSum == 0)
			totalSum = -1;
		result[1] = totalSum;

		return result;
	}

}
