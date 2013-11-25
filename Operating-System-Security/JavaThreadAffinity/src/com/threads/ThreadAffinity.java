package com.threads;

import com.sun.jna.Library;
import com.sun.jna.Native;

// ThreadAffinity class for managing thread priority
public class ThreadAffinity {
	public CTest ctest;

	// ThreadAffinity constructor
	public ThreadAffinity() {
		ctest = (CTest) Native.loadLibrary("ctest", CTest.class);
	}

	// Interface for CTest
    public interface CTest extends Library {
        public void helloFromC(long i);
        public int _setaffinity_thread(int pid, int size, int[] a);
        public int _getcpu();
    }

    // Method to process the return value
    private void process_retval(int retval) throws Exception {
    	if ( retval == 0 ) { }
        	// System.out.println("DEBUG: Operation successful");
    	else if ( retval == 1 )
    		throw new Exception("Supplied memory address was invalid");
    	else if ( retval == 2 )
    		throw new Exception("cpusetsize is smaller than the size of the affinity mask used by the kernel.");
    	else if ( retval == 3 )
    		throw new Exception("The calling process does not have appropriate privileges. The caller needs an effective user ID equal to the real user ID or effective user ID of the process identified by pid, or it must possess the CAP_SYS_NICE capability.");
    	else if ( retval == 4 )
    		throw new Exception("The process whose ID is pid could not be found.");
    }

    // Method to get the current CPU
    public int sched_getcpu() throws Exception {
    	int retval = ctest._getcpu();
    	return retval;
    }

    public void setaffinity_thread(int pid, int size, int[] a) throws Exception {
    	int retval = ctest._setaffinity_thread(pid, size, a);
    	process_retval(retval);
    }
}