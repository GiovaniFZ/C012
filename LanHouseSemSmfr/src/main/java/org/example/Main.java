package org.example;

public class Main {
    public static void main(String[] args) {
        for (int i = 0; i < 10; i++) {
            LanHouse lanHouse = new LanHouse();
            lanHouse.setName(i);
                try {
                    lanHouse.run();
                    Thread.sleep(1000);
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
            };
        }
    }