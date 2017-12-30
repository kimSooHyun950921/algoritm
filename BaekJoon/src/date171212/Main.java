package date171212;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;

public class Main {

	public static void main(String[] args) throws NumberFormatException, IOException {
		// TODO Auto-generated method stub
		/*
		 * 중앙값 : 정렬 binarySearch tree에 넣으면서 정렬한다. 일단 tree에 넣어준다 넣어주면서 트리탐색을통해 같은것을 있는지
		 * 비교해준다. 같은것에있으면 노드에 count를 넣어 증가시켜준다. 넣는게 끝나면 차례로 빼면서 최대값 최소값 중앙값을 찾는다.
		 *
		 */
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine());
		ArrayList<Node> inputNums = new ArrayList<Node>();
		BinaryTree<Node> tree = new BinaryTree<Node>(new Node(Integer.parseInt(br.readLine())));
		long sum = 0;
		double sansulAvg = 0;
		int middleVal;
		int countVal;
		int range;

		for (int i = 1; i < N; i++) {
			int input = Integer.parseInt(br.readLine());
			Node inputNode = new Node(input);
			if (tree.addBST(inputNode) == null)
				tree.findTree(inputNode).count++;
			//System.out.println(input + " ok");

			sum += input;
		}

		sansulAvg = (double) sum / (double) N;
		countVal = findCount(tree);
		//System.out.println("빈도수:" + countVal);
		range = tree.maxValueBST().num - tree.minValueBST().num;
		//System.out.println("범위:" + range);
		for (int i = 0; i < N / 2; i++) {
			tree.deleteMinTree();
		}
		middleVal = tree.deleteMinTree().num;
		//System.out.println("중앙값:" + middleVal);

		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		bw.write(Math.round(sansulAvg) + "\n");
		bw.write(middleVal + "\n");
		bw.write(countVal + "\n");
		bw.write(range + "\n");
		bw.flush();
		bw.close();

	}

	private static int findCount(BinaryTree<Node> tree) {
		// TODO Auto-generated method stub
		BinaryTree<Node> mostCount = new BinaryTree<Node>();
		SearchRecursive(mostCount, tree);
		if (mostCount.size > 1) {
			mostCount.deleteMinTree();
			return mostCount.deleteMinTree().num;

		} else
			return mostCount.deleteMinTree().num;

	}

	private static boolean SearchRecursive(BinaryTree<Node> mostCount, BinaryTree<Node> tree) {
		// TODO Auto-generated method stub
		if (tree == null)
			return false;
		if (mostCount.size == 0)
			mostCount.addBST(tree.root);
		else {
			if (tree.root.count > mostCount.root.count) {
				mostCount.removeAll();
				mostCount.addBST(tree.root);
			} else if (tree.root.count == mostCount.root.count) {
				mostCount.addBST(tree.root);
			}
		}
		SearchRecursive(mostCount, tree.left);
		SearchRecursive(mostCount, tree.right);
		return true;
	}

}

class Node implements Comparable<Node> {
	int num;
	int count;

	public Node(int num) {
		this.num = num;
		this.count = 1;
	}

	public int getCount() {
		return count;
	}

	public void setCount(int count) {
		this.count = count;
	}

	@Override
	public int compareTo(Node arg0) {
		// TODO Auto-generated method stub
		int compare = 0;
		if (this.num > arg0.num)
			compare = -1;
		else if (this.num == arg0.num)
			compare = 0;
		else if (this.num < arg0.num)
			compare = 1;
		return compare;
	}

}

class BinaryTree<T extends Comparable<T>> {
	T root;
	BinaryTree<T> left;
	BinaryTree<T> right;
	int size;
	boolean isContain = false;

	public BinaryTree() {
		this.root = null;
		this.size = 0;
	}

	public BinaryTree(T root) {
		this.root = root;
		this.size = 1;

	}

	public boolean search(T value) {
		boolean isSearch = isExist(value, this);
		return isSearch;
	}

	public boolean isExist(T value, BinaryTree<T> tree) {
		if (tree == null)
			return false;
		if (tree.root.compareTo(value) == 0) {
			isContain = true;
			return true;
		} else if (tree.root.compareTo(value) > 0) {
			this.isExist(value, tree.left);
		} else
			this.isExist(value, tree.right);
		return isContain;
	}

	public BinaryTree<T> addBST(T value) {
		if (this.root == null) {
			this.root = value;
			size++;
			return this;
		}

		int compare = compare(this.root, value);

		if (search(value) == true)
			return null;
		else if (compare == -1) {
			if (this.left == null)
				left = new BinaryTree<T>(value);
			else
				this.left.addBST(value);
		} else if (compare == 1) {
			if (this.right == null)
				right = new BinaryTree<T>(value);
			else
				right.addBST(value);
		}
		size++;
		return this;

	}

	@SuppressWarnings("hiding")
	private <T extends Comparable<T>> int compare(T root2, T value) {
		// TODO Auto-generated method stub
		int compare = 0;
		if (root2.compareTo(value) > 0)
			compare = 1;
		else if (root2.compareTo(value) < 0)
			compare = -1;
		else if (root2.compareTo(value) == 0)
			compare = 0;
		return compare;
	}

	public T minValueBST() {
		BinaryTree<T> minValue = this;
		while (minValue.left != null) {
			minValue = minValue.left;
		}
		return minValue.root;
	}

	public T maxValueBST() {
		BinaryTree<T> maxValue = this;
		while (maxValue.right != null) {
			maxValue = maxValue.right;
		}
		return maxValue.root;
	}

	public T deleteBST(T value) {
		BinaryTree<T> deleteTree, parentTree;
		deleteTree = parentTree = this;

		while (deleteTree != null && compare(deleteTree.root, value) != 0) {
			// delete할 tree찾기
			int compareValue = compare(deleteTree.root, value);
			parentTree = deleteTree;
			if (compareValue > 0)
				deleteTree = this.right;
			else
				deleteTree = this.left;
		}
		if (deleteTree == null)
			return null;
		if (deleteTree != this && deleteTree.left == null) {
			if (deleteTree == parentTree.left)
				parentTree.left = deleteTree.right;
			else
				parentTree.right = deleteTree.right;
		} else if (deleteTree != this && deleteTree.right == null) {
			if (deleteTree == parentTree.left)
				parentTree.left = deleteTree.left;
			else
				parentTree.right = deleteTree.left;
		}

		else {
			if (deleteTree.right.left == null)
				deleteTree.right.left = deleteTree.left;
			else {
				BinaryTree<T> leftTree = deleteTree.right.left;
				while (leftTree.left != null)
					leftTree = leftTree.left;
				leftTree.left = deleteTree.left;

			}
			deleteTree.left = null;
			if (deleteTree == this) {
				deleteTree = deleteTree.right;
				this.right = deleteTree.right;
				this.left = deleteTree.left;
				this.root = deleteTree.root;
			} else {
				if (deleteTree == parentTree.left)
					parentTree.left = deleteTree.right;
				else
					parentTree.right = deleteTree.right;
			}
		}
		size--;
		return deleteTree.root;
	}

	public void removeAll() {
		while (size != 0) {
			this.deleteMaxTree();
			size--;
		}

	}

	public T findTree(T val) {
		BinaryTree<T> findTree = this;
		while (findTree != null && findTree.root.compareTo(val) != 0) {
			if (findTree.root.compareTo(val) > 1) {
				findTree = findTree.right;
			} else {
				findTree = findTree.left;
			}
		}
		if (findTree == null)
			return null;
		else
			return findTree.root;

	}

	public T deleteMinTree() {
		T rmval = this.minValueBST();
		this.deleteBST(rmval);
		size--;
		return rmval;
	}

	public T deleteMaxTree() {
		T rmval = this.maxValueBST();
		this.deleteBST(rmval);
		size--;
		return rmval;
	}
}
