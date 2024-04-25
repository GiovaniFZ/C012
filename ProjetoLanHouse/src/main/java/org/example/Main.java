package org.example;

public class Main {
    public static void main(String[] args) {
        LanHouse lanHouse = new LanHouse(2, 5);
        for (int i = 0; i < 10; i++) {
            Thread thread = new Thread(() -> {
                try {
                    lanHouse.acquire();
                    System.out.println("Pessoa "+ Thread.currentThread().getName() + " está usando o computador.");
                    Thread.sleep(1000); // Simula uma operação dentro da seção crítica
                    lanHouse.release();
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
            });
            thread.start();
        }
    }
}