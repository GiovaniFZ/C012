package org.example;

import java.util.concurrent.locks.Condition;
import java.util.concurrent.locks.Lock;
import java.util.concurrent.locks.ReentrantLock;

public class LanHouse extends Thread{
    private int lanHouseid;

    public void setName(int id) {
        this.lanHouseid = id;
    }

    @Override
    public void run() {
        System.out.println("Pessoa "+ lanHouseid + " está usando o computador.");
    }
}
