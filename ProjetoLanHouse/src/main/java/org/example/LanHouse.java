package org.example;

import java.util.concurrent.locks.Condition;
import java.util.concurrent.locks.Lock;
import java.util.concurrent.locks.ReentrantLock;

public class LanHouse {
    private int count;
    private final int maxCount;
    private final Lock lock;
    private final Condition condition;

    public LanHouse(int initialCount, int maxCount) {
        this.count = initialCount;
        this.maxCount = maxCount;
        this.lock = new ReentrantLock();
        this.condition = lock.newCondition();
    }

        public void acquire() throws InterruptedException {
            lock.lock();
            try {
                while (count == 0) {
                    condition.await();
                }
                count--;
            } finally {
                lock.unlock();
            }
        }

        public void release() {
            lock.lock();
            try {
                if (count < maxCount) {
                    count++;
                    condition.signal();
                }
            } finally {
                lock.unlock();
            }
        }
}
