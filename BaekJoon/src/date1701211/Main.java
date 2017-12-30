package date1701211;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class Main {

	public static void main(String[] args) throws NumberFormatException, IOException {
		// TODO Auto-generated method stub
		BufferedReader buff = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(buff.readLine());
		// ¼±¾ðºÎ
		int[] countNum = new int[10000001];
		int biggestNum = 0;
		int smallestNum = Integer.MAX_VALUE;

		// scan & counting
		for (int i = 0; i < N; i++) {
			int number = Integer.parseInt(buff.readLine());
			countNum[number]++;
			if (biggestNum < number)
				biggestNum = number;

			if (smallestNum > number)
				smallestNum = number;
		}
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		for (int i = smallestNum; i <= biggestNum; i++) {
			if (countNum[i] == 0)
				continue;
			for (int j = 0; j < countNum[i]; j++) {
				bw.write(i + "\n");
				
			}

		}
		bw.flush();
		bw.close();

	}

}
