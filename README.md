# Braligne Formatter

**<center>🚧 Working In Progress...</center>**

The word *Braligne* is a combination of *Brace* and *Align*. As the name suggests, this formatter is used to align its braces in a code, for fun.

This idea comes from a meme:

*I couldn't find that meme yet, I'll upload it soon.*

## Example

**BEFORE**

```java
import java.io.InputStream;
import java.io.FileInputStream;
public class loadFiles {
    public static void main(String args[]) {
        try {
            InputStream input = new FileInputStream("input.txt");
            System.out.println("Data in the file: ");
            // Reads the first byte
            int i = input.read();
            while (i != -1) {
                System.out.print((char) i);
                // Reads next byte from the file
                i = input.read();
            }
            input.close();
        } catch (Exception e) {
            e.getStackTrace();
        }
    }
}
```

**AFTER**

```java
import java.io.InputStream                                        ;
import java.io.FileInputStream                                    ;
public class loadFiles                                            {
    public static void main(String args[])                        {
        try                                                       {
            InputStream input = new FileInputStream("input.txt")  ;
            System.out.println("Data in the file: ")              ;
            // Reads the first byte
            int i = input.read()                                  ;
            while (i != -1)                                       {
                System.out.print((char) i)                        ;
                // Reads next byte from the file
                i = input.read()                                  ;}
            input.close()                                         ;}
        catch (Exception e)                                       {
            e.getStackTrace()                                     ;}}}
```
