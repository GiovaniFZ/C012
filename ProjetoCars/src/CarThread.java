import javax.security.auth.callback.TextInputCallback;
import java.util.Random;

public class CarThread extends Thread{
    boolean isRunning = true;
    public void run() {
            int distance = 0;
            while (distance <= 100) {
                Random random = new Random();
                int velocidade = random.nextInt(20);
                distance = distance + velocidade;
                System.out.println(Thread.currentThread().getName() + " andou " + velocidade + "m está à "  + (100 - distance) + "m do final!");
                try {
                    Thread.sleep(1000);
                } catch (InterruptedException e) {
                    break;
                }
            }
            isRunning = false;
    }
}
