package leetcode.minStack;

import java.util.Deque;
import java.util.LinkedList;
import java.util.SortedMap;
import java.util.TreeMap;

public class MinStack {
    private Deque<Integer> stack = new LinkedList<>();
    private TreeMap<Integer,Integer> entries = new TreeMap<Integer,Integer>();

    private void addToEntries(int x) {
        if (entries.containsKey(x)) {
            int newValue = 1 + entries.get(x);
            entries.put(x, newValue);
        } else {
            entries.put(x, 1);
        }
    }

    private void removeFromEntries(int x) {
        if (entries.containsKey(x)) {
            int value = entries.get(x);
            if (value == 1) {
                entries.remove(x);
            } else {
                entries.put(x, value - 1);
            }
        }
    }

    /**
     * initialize your data structure here.
     */
    public MinStack() {
    }

    public void push(int x) {
        stack.push(x);
        addToEntries(x);
    }

    public void pop() {
        int value = stack.pop();
        removeFromEntries(value);
    }

    public int top() {
        return stack.peek();
    }

    public int getMin() {
        return entries.firstKey();
    }
}
