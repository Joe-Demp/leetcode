package leetcode.RansomNote;

public class RansomNote {
    public static final int LETTERS_IN_ALPHABET = 26;

    public boolean canConstruct(String ransomNote, String magazine) {
        int ransomNoteLen = ransomNote.length();
        int[] letterCounts = new int[LETTERS_IN_ALPHABET];
        for (int i = 0; i < ransomNoteLen; i++) {
            letterCounts[ransomNote.charAt(i) - 'a']++;
        }

        int magazineLen = magazine.length();
        for (int i = 0; ransomNoteLen > 0 && i < magazineLen; i++) {
            int current = magazine.charAt(i) - 'a';
            if (letterCounts[current] > 0) {
                letterCounts[current]--;
                ransomNoteLen--;
            }
        }
        return ransomNoteLen == 0;
    }
}
