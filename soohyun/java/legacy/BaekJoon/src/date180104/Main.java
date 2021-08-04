package date180104;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class Main {

	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine());
		String initialInput = br.readLine();
		String[] splitInput = initialInput.split(" ");
		int primeCount = 0;

		for (int i = 0; i < N; i++) {
			if (isPrime(Integer.parseInt(splitInput[i])))
				primeCount++;
		}
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		bw.write(Integer.toString(primeCount));
		bw.flush();
		bw.close();
	}
	private static boolean isPrime(int isPrimeNum) {
		if (isPrimeNum < 2)
			return false;
		if (isPrimeNum == 2)
			return true;
		else {
			for (int i = 2; i < isPrimeNum; i++) {
				if (isPrimeNum % i == 0)
					return false;
			}
		}
		return true;

	}

}
