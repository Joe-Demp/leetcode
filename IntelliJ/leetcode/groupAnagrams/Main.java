package leetcode.groupAnagrams;

import java.util.Collection;
import java.util.Collections;
import java.util.List;

public class Main {
    public static void main(String[] args) {
        String[] words = new String[]{"eat", "tea", "tan", "ate", "nat", "bat"};
        List<List<String>> sortedWords = new GroupAnagrams().groupAnagrams(words);
        printList(sortedWords);
    }

    public static <T> void printList(List<T> list) {
        System.out.println("{");
        for (T item : list) {
            if (item instanceof List) {
                printList((List) item);
            } else {
                System.out.printf("%s,", item);
            }
            System.out.println();
        }
        System.out.println("}");
    }
}
