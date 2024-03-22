public class CarThreadAux extends Thread{
    CarThread carro1;
    CarThread carro2;
    CarThread carro3;
    public void instanciarCarros(){
        carro1 = new CarThread();
        carro2 = new CarThread();
        carro3 = new CarThread();
        carro1.start();
        carro2.start();
        carro3.start();
    }
    @Override
    public void run() {
        while(carro1.isRunning && carro2.isRunning && carro3.isRunning){
            try {
                Thread.sleep(30);
            } catch (InterruptedException e) {
                throw new RuntimeException(e);
            }
        }
        if(!carro1.isRunning){
            System.out.println("VENCEDOR: CARRO 1");
        }
        if(!carro2.isRunning){
            System.out.println("VENCEDOR: CARRO 2");
        }
        if(!carro3.isRunning){
            System.out.println("VENCEDOR: CARRO 3");
        }
        while(carro1.isRunning || carro2.isRunning || carro3.isRunning){
            carro1.interrupt();
            carro2.interrupt();
            carro3.interrupt();
        }
    }
}
