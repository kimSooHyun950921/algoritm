package date180106;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int inputs = 0;
		int PrimeNum;
		BufferedWriter bw= new BufferedWriter(new OutputStreamWriter(System.out));;
		while(true) {
			inputs = Integer.parseInt(br.readLine());
			if(inputs==0)break;
			PrimeNum = findPrimeNum(inputs);
			bw.write(Integer.toString(PrimeNum)+"\n");
			bw.flush();
		} 
		bw.close();

	}

	private static int findPrimeNum(int inputs) {
		int count = 0;
		boolean isPrime = true;
		for (int i = inputs + 1; i <= 2 * inputs; i++) {
			if(i==2) isPrime = true;
			for (int j = 2; j < i; j++) {
				if (i % j == 0) {
					isPrime = false;
					break;
				}
			}
			if(isPrime)
				count++;
			isPrime = true;
		}
		return count;
	}

}
