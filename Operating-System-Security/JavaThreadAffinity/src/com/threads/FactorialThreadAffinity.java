package com.threads;

public class FactorialThreadAffinity implements Runnable{
	int[] processors;
	int n;

	public FactorialThreadAffinity(int[] processors, int n) {
		this.processors = processors;
		this.n = n;
	}
	
	public void run() {
		int f = 1; // to hold the factorial value
		
		// Create an instance of ThreadAffinity
		ThreadAffinity t = new ThreadAffinity();
		try {
			// Get an object referring to the current thread
			Thread currThread = Thread.currentThread();
			
			// Set the current thread to the cores specified in `processors`
			t.setaffinity_thread(0, this.processors.length, this.processors);
			
			for ( int i = 1; i < this.n; i++ ) {
				f *= i;
				System.out.println("computing factorial of " + this.n + " on core " + t.sched_getcpu());
			}
			System.out.println("[+] For thread " + currThread.getName() + " the cpu is " + t.sched_getcpu() + " the factorial is " + f);
		} catch (Exception e) {
			e.printStackTrace();
		}
	}
   
    public static void main(String[] args) throws InterruptedException {
		
		/* Thread "i" runs on core "i" and computes factorial of "i+1" */
		Thread[] thread_array = new Thread[8];
		for ( int i = 0 ; i < 8; i++ ) {
	    		/* Specify processors */
				int[] p1 = {i};
				thread_array[i] = new Thread(new FactorialThreadAffinity(p1, i+1), "My Thread " + i);
		}

		/* Start off all threads */
		for ( int i = 0; i < 8; i++ )
			thread_array[i].start();
		
		/* Wait for all threads to finish executing */
		for ( int i = 0; i < 8; i++ )
			thread_array[i].join();
    }
}