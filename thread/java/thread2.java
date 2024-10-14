class MyThread1 extends Thread {
   public MyThread1(){
        setName("MyThread1");
    }
    @Override
    public void run() {
        for (int i = 0; i < 5; i++) {
            System.out.println(getName()+" : " + i);
            try {   
                Thread.sleep(1000);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
    }
}
class MyThread2 extends Thread {
    public MyThread2(){
        setName("MyThread2");
    }
    @Override
    public void run() {
        for (int i = 0; i < 5; i++) {
            System.out.println(getName()+" : " + i);
            try {   
                Thread.sleep(1000);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
    }
}
public class thread2 {
    public static void main(String[] args) {
        Thread thread1 = new MyThread1();
        Thread thread2 = new MyThread2();
        thread1.start();
        thread2.start();
    }
}