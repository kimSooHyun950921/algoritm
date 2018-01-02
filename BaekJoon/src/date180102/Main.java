package date180102;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStream;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;

public class Main {

	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String inputString = br.readLine();
		ArrayList<Integer> inputNum = new ArrayList<Integer>();
		for (int i = 0; i < inputString.length(); i++) {
			inputNum.add(inputString.charAt(i)-48);
		}
		
		Sort sort = new Sort();
		Collections.sort(inputNum,sort);
		
		StringBuffer buf = new StringBuffer();
		for(int i = 0; i<inputNum.size();i++)
			buf.append(inputNum.get(i));
		
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		bw.write(buf.toString());
		bw.flush();
		bw.close();
	}

}
class Sort implements Comparator<Integer>{

	@Override
	public int compare(Integer arg0, Integer arg1) {
		// TODO Auto-generated method stub
		return arg1.compareTo(arg0);
	}
	
}
