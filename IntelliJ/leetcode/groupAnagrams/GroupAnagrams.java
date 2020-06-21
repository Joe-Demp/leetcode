package leetcode.groupAnagrams;

import java.util.*;

public class GroupAnagrams {
    public List<List<String>> groupAnagrams(String[] strs) {
        List<List<String>> answer = new ArrayList<>();
        List<String[]> stringPairs = new ArrayList<>(strs.length);

        // map to pairs
        for (String str : strs) {
            stringPairs.add(new String[]{str, sortString(str)});
        }

        // sort the pairs
        stringPairs.sort(Comparator.comparing(arr -> arr[1]));

        for (int i = 0; i < stringPairs.size(); i++) {
            String currentAnagram = stringPairs.get(i)[1];
            List<String> stringsWithAnagram = new LinkedList<>();

            int j;
            for (j = i;
                 j < stringPairs.size() && stringPairs.get(j)[1].equals(currentAnagram);
                 j++) {
                stringsWithAnagram.add(stringPairs.get(j)[0]);
            }
            answer.add(stringsWithAnagram);
            i = j-1;
        }

        return answer;
    }

    public String sortString(String str) {
        char[] characters = str.toCharArray();
        Arrays.sort(characters);
        return String.valueOf(characters);
    }
}
