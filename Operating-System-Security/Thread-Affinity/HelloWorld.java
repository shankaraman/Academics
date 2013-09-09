import com.sun.jna.Library;
import com.sun.jna.Native;

public class HelloWorld {
  public interface CTest extends Library {
    public void helloFromC(final int blah);
  }

  public interface CLibrary extends Library {
    public static final CLibrary INSTANCE = ( CLibrary )
      Native.loadLibrary(  "c" ,
          CLibrary.class );

    public void printf( final String format,
        final Object... args );
  }

    /*
    public int sched_setaffinity( final int     pid,
        final int cpusetsize,
        final IntByReference cpuset );
  }
  */
  static public void main(String argv[]) {
    final CLibrary lib = CLibrary.INSTANCE;
    CLibrary.INSTANCE.printf( "Argument %d: %s\n", 0, "asdf" );
    CTest ctest = (CTest) Native.loadLibrary("ctest", CTest.class);
    ctest.helloFromC(10);
  }
}
