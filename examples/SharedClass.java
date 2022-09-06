import java.io.*;

// Creating thread by creating the
// objects of that class
class SharedClass {
    static int i = 10;

    void increment() {
        for (int j = 0; j < 50; j++) {
            // incrementing value of i
            i = i + 1;
            System.out.println("i after increment " + i);
        }
    }

    void decrement() {
        for (int j = 0; j < 50; j++) {
            // decrementing value of i
            i = i - 1;
            System.out.println("i after decrement " + i);
        }
    }
}

class GFG {
    public static void main(String[] args) {
        final SharedClass s1 = new SharedClass();
        Thread t1 = new Thread() {
            @Override
            public void run() {
                s1.increment();
            }
        };
        Thread t2 = new Thread() {
            @Override
            public void run() {
                s1.decrement();
            }
        };
        t1.start();
        t2.start();
    }
}