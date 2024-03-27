import java.util.Random;

public class CarThread extends Thread {
    private int carroId;

    @Override
    public void run() {
        int distance = 0;
        while (distance < 100 && !isInterrupted()) {
            Random random = new Random();
            int velocidade = random.nextInt(21);
            distance += velocidade;
            System.out.println("Carro " + carroId + " com velocidade " + velocidade + "m/s está a " + (100 - distance) + "m do final!");
            try {
                Thread.sleep(1000);
            } catch (InterruptedException e) {
                System.out.println("Carro " + carroId + " interrompido.");
                return;
            }
        }
        if (distance >= 100) {
            Main.setVencedor(carroId);
        }
    }

    public void setId(int carroId) {
        this.carroId = carroId;
    }
}
