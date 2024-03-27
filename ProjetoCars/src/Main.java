import java.util.Scanner;

public class Main {
    private static int nCarros;
    private static int carroVencedor;
    private static boolean corridaFinalizada = false;

    public static void main(String[] args) {
        System.out.println("Numero de carros: ");
        Scanner sc = new Scanner(System.in);
        nCarros = sc.nextInt();

        for (int i = 1; i <= nCarros; i++) {
            CarThread carThread = new CarThread();
            carThread.setId(i);
            carThread.start();
        }
    }

    public static synchronized void setVencedor(int carroId) {
        if (!corridaFinalizada) {
            carroVencedor = carroId;
            corridaFinalizada = true;
            System.out.println("Carro " + carroVencedor + " venceu!");
            for (Thread t : Thread.getAllStackTraces().keySet()) {
                if (t instanceof CarThread && t != Thread.currentThread()) {
                    ((CarThread) t).interrupt();
                }
            }
        }
    }
}
