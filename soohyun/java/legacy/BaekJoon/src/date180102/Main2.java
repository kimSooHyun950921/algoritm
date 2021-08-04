package date180102;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;

public class Main2 {

	public static void main(String[] args) throws NumberFormatException, IOException {
		// TODO Auto-generated method stub
		/*
		 * 
		 * */
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine());
		ArrayList<Node> InputWord = new ArrayList<Node>();

		for (int i = 0; i < N; i++) {
			String input = br.readLine();
			InputWord.add(new Node(input, input.length()));

		}
		Sorting sort = new Sorting();
		Collections.sort(InputWord, sort);

		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		String  result= output(InputWord);
		bw.write(result);
		bw.flush();
		bw.close();

	}

	private static String output(ArrayList<Node> inputWord) {
		// TODO Auto-generated method stub
		StringBuffer buf = new StringBuffer();
		
		String isSameWord = inputWord.get(0).getWord();
		buf.append(isSameWord+"\n");

		for (int i = 1; i<inputWord.size(); i++) {
			if(isSameWord.equals(inputWord.get(i).getWord()))
				continue;
			buf.append(inputWord.get(i).getWord()+"\n");
			isSameWord =  inputWord.get(i).getWord();
		}
		return buf.toString();
	}

}

class Node {
	private String word;
	private int numOfWord;

	public Node(String word, int numOfWord) {
		this.word = word;
		this.numOfWord = numOfWord;
	}

	public String getWord() {
		return word;
	}

	public int getNumOfWord() {
		return numOfWord;
	}

	public int compareTo(Node o2) {
		
		if(this.getNumOfWord()>o2.getNumOfWord())
			return 100;
		else if(this.getNumOfWord()==o2.getNumOfWord())
		{
			return (this.getWord().compareTo(o2.getWord()));
		}
		else
			return -100;
	}

}

class Sorting implements Comparator<Node> {

	@Override
	public int compare(Node o1, Node o2) {
		// TODO Auto-generated method stub
		return o1.compareTo(o2);
	}

	

}
