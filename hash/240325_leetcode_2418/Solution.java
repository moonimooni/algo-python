import java.lang.reflect.Array;
import java.util.Arrays;


// https://leetcode.com/problems/sort-the-people/description/
class Solution {
  public String[] sortPeople(String[] names, int[] heights) {
    Person[] people = new Person[names.length];

    for (int i = 0; i < names.length; i++) {
      people[i] = new Person(names[i], heights[i]);
    }

    return Arrays.stream(people)
        .sorted()
        .map(Person::getName)
        .toArray(String[]::new);

  }

  class Person implements Comparable<Person> {
    private String name;
    private int height;

    public Person(String name, int height) {
      this.name = name;
      this.height = height;
    }

    @Override
    public int compareTo(Person person) {
      return person.height - this.height;
    }

    public String getName() {
      return name;
    }
  }
}