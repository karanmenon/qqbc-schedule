import java.util.*;
import java.io.*;

public class Scheduling
{
    String[] session1Classes;
    String[] session2Classes;
    HashMap<String, ArrayList<String>> studentPreferences;
    HashMap<String, ArrayList<String>> classEnrollment;
    HashMap<String, String[]> studentSchedule; //each array will be initialized to 4  and 3 
    //classes will be put into individual spots. The remaining empty spots for each student will become a strategy class.
    public Scheduling()
    {
        session1Classes= new String[]{"Myth and Religion", "Prose", "US History", "Chemistry", "Geography", "Poetry", "European History",
    "Biology", "Visual Art", "Drama", "World History", "Physics", "Music"};
        session2Classes= new String[]{"Prose II", "Politics", "Myth and Religion II", "Biology II", "Poetry II", "Military History",
    "Philosophy and Society", "Chemistry II", "Authors", "Monarchy", "Geography II", "Earth and Space", "Music II"};
        
        for(String str : session1Classes)
        {
            classEnrollment.put(str, new ArrayList<String>());
        }

        for(String str : session2Classes)
        {
            classEnrollment.put(str, new ArrayList<String>());
        }

    //here we will use the API to read and populate the student
        

    }
    public static void main(String [] args)
    {

    }
}
    