import java.text.ParseException;
import java.util.StringTokenizer;

import com.sun.jna.*;
import com.sun.jna.ptr.LongByReference;
//import net.jcip.annotations.Immutable;

class Tester {
  static final String LIBRARY_NAME = Platform.isWindows() ? "msvcrt" : "ctest";

  private interface CLibrary extends Library {
    public static final CLibrary INSTANCE = (CLibrary)
      Native.loadLibrary(LIBRARY_NAME, CLibrary.class);
    public int sched_setaffinity(final int pid,
        final int cpusetsize,
        final PointerType cpuset) throws LastErrorException;
    public int sched_getaffinity(final int pid,
        final int cpusetsize,
        final PointerType cpuset) throws LastErrorException;
  }

  public long getAffinity() {
    final CLibrary lib = CLibrary.INSTANCE;
    final LongByReference cpuset = new LongByReference(0L);
    try {
      final int ret = lib.sched_getaffinity(0, Long.SIZE / 8, cpuset);
      if (ret < 0)
        throw new IllegalStateException("sched_getaffinity((" + Long.SIZE / 8 + ") , &(" + cpuset + ") ) return " + ret);
      return cpuset.getValue();
    }
    catch (LastErrorException e) {
      throw new IllegalStateException("sched_getaffinity((" + Long.SIZE / 8 + ") , &(" + cpuset + ") ) errorNo=" + e.getErrorCode(), e);
    }
  }
}



public class AffinityTest {
  public static void main(String[] args) {
    Tester t = new Tester();
    System.out.println(t.getAffinity());
    System.out.println("asdf");
  }
}
