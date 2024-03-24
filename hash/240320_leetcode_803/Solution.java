import java.lang.reflect.Array;
import java.util.ArrayList;
import java.util.Arrays;

class Solution {
  public int uniqueMorseRepresentations(String[] words) {
    String[] morseCodesOfAlphabet = new String[] {
        ".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..",
        "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."
    };

    Set<String> uniqueMorseCodes = new HashSet<>();

    for (String word : words) {
      StringBuilder morseCode = new StringBuilder();

      for (char alphabetChar : word.toCharArray()) {
        // get index of alphabetChar in the alphabet
        int index = alphabetChar - 'a';
        morseCode.append(morseCodesOfAlphabet[index]);
      }
      uniqueMorseCodes.add(morseCode.toString());
    }
    return uniqueMorseCodes.size();
  }
}
