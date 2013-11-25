package com.threads;

public class ThreadAffinityMultiUser implements Runnable{
	int[] processors;

	public ThreadAffinityMultiUser(int[] processors) {
		this.processors = processors;
	}
	
	public void run() {
		ThreadAffinity t = new ThreadAffinity();
		try {
			Thread currThread = Thread.currentThread();
			t.setaffinity_thread(0, this.processors.length, this.processors);
			for ( int i = 0; i < 5; i++ ) {
				System.out.println("[+] For thread " + currThread.getName() + " the cpu is " + t.sched_getcpu());
				Thread.sleep(4);
			}
		} catch (Exception e) {
			e.printStackTrace();
		}
	}
   
    public static void main(String[] args) throws InterruptedException {
    	/* Specify processors */
		int[] p1 = {0, 1, 2, 3};
		int[] p2 = {4, 5, 6, 7};
		
		/* Create 10 threads with processors as arguments */
		Thread[] thread_array = new Thread[10];
		for ( int i = 0 ; i < 10; i++ ) {
			if ( i % 2 == 0 )
				thread_array[i] = new Thread(new ThreadAffinityMultiUser(p1), "My Thread " + i);
			else
				thread_array[i] = new Thread(new ThreadAffinityMultiUser(p2), "My Thread " + i);
		}

		/* Start off all threads */
		for ( int i = 0; i < 10; i++ )
			thread_array[i].start();
		
		for ( int i = 0; i < 10; i++ )
			thread_array[i].join();
    }
}