package com.threads;

public class ThreadAffinityBasicUser implements Runnable{
	int[] processors;

	public ThreadAffinityBasicUser(int[] processors) {
		this.processors = processors;
	}
	
	public void run() {
		ThreadAffinity t = new ThreadAffinity();
		try {
			Thread currThread = Thread.currentThread();
			t.setaffinity_thread(0, this.processors.length, this.processors);
			System.out.println("[+] For thread " + currThread.getName() + " the cpu is " + t.sched_getcpu());
		} catch (Exception e) {
			e.printStackTrace();
		}
	}
   
    public static void main(String[] args) throws InterruptedException {
    	/* Specify processors */
		int[] p1 = {0, 1};
		int[] p2 = {2, 3};
		
		/* Create two threads with processors as arguments */
		Thread t1 = new Thread(new ThreadAffinityBasicUser(p1), "My Thread One");
		Thread t2 = new Thread(new ThreadAffinityBasicUser(p2), "My Thread Two");

		/* Start the first thread and wait for it to join */
		t1.start(); t1.join();
		/* Start the second thread and wait for it to join */
		t2.start(); t2.join();         
    }
}