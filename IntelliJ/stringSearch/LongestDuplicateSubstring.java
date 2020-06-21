package stringSearch;

import java.lang.reflect.Array;
import java.net.Inet4Address;
import java.util.*;

public class LongestDuplicateSubstring {
    private static int startIndex;
    private static int endIndex;
    public static String getLastDuplicateSubstring(String text) {
        if (startIndex >= 0) {
            return text.substring(startIndex, endIndex);
        }
        return "\"\"";
    }

    public static String longestDuplicateSubstring(String text) {
        startIndex = endIndex = -1;

        // binary search for the largest value in range [0, text.length)
        int left = 0;
        int right = text.length();

        while (left != right - 1) {
            int median = ((right - left) / 2) + left;
            boolean duplicateSubstringExists = duplicateSubstring(text, median);
            if (duplicateSubstringExists) {
                left = median;
            } else {
                right = median;
            }
        }

        return getLastDuplicateSubstring(text);
    }

    // Side effect: stores the start and end indices of the substring in 'text' in 'startIndex' and 'endIndex'
    public static boolean duplicateSubstring(String text, int length) {
        int[] hashes = RabinKarp.hashes(text, length);
        MultiMap<Integer, Integer> hashToIndex = new MultiMap<>();

        int textLen = text.length();
        for (int i = length - 1; i < textLen; i++) {
            // hashes[i] = the hash of the window that starts at index i
            hashToIndex.put(hashes[i], i - length + 1);
        }

        for (int key : hashToIndex.keySet()) {
            List<Integer> indices = hashToIndex.get(key);
            int indicesSize = indices.size();
            for (int i = 0; i < indicesSize - 1; i++) {
                for (int j = 1; j < indicesSize; j++) {
                    int starti = indices.get(i);
                    int startj = indices.get(j);

                    if (stringCompare(text, length, starti, startj)) {
                        startIndex = starti;
                        endIndex = startIndex + length;
                        return true;
                    }
                }
            }
        }
        return false;
    }

    public static boolean stringCompare(String text, int length, int start1, int start2) {
        int i = start1, j = start2, pos = 0;
        int textLen = text.length();
        while (pos < length && i < textLen && j < textLen && text.charAt(i) == text.charAt(j)) {
            i++;
            j++;
            pos++;
        }
        return pos == length;
    }

    // todo replace this with Guava's implementation
    public static class MultiMap<K, V> {
        Map<K, List<V>> map = new HashMap<>();

        public void put(K key, V value) {
            if (!map.containsKey(key)) {
                map.put(key, new ArrayList<>());
            }
            map.get(key).add(value);
        }

        public List<V> get(K key) {
            return map.get(key);
        }

        public Set<K> keySet() {
            return map.keySet();
        }
    }
}
