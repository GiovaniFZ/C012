import java.util.Scanner;

public class Main {
    public static void main(String[] args) throws InterruptedException {
        CarThreadAux carThreadAux = new CarThreadAux();
        carThreadAux.instanciarCarros();
        carThreadAux.start();
        //System.out.println("Numero de carros: ");
        //Scanner sc = new Scanner(System.in);
        //nCarros = sc.nextInt();
    }
}