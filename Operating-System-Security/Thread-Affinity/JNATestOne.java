import com.sun.jna.Library;
import com.sun.jna.Native;
import com.sun.jna.Platform;
import com.sun.jna.ptr.IntByReference;  
import com.sun.jna.Pointer;  

 
public class JNATestOne 
{
    public interface CLibrary extends Library 
    {
        CLibrary INSTANCE = (CLibrary) Native.loadLibrary((Platform.isWindows() ? "msvcrt" : "c"), CLibrary.class);
        void printf(String format, Object... args);
    }
       
    public static void main(String[] args) 
    {
        final CLibrary lib = CLibrary.INSTANCE;
        lib.printf("Hello World \n");
        for (int i = 0; i < args.length; i++) 
        {
            CLibrary.INSTANCE.printf("Argument %d:%s\n",i,args[i]);
        }
        final IntByReference cpuset = new IntByReference(1);
        final int ret = lib.sched_setaffinity(0,(16),cpuset);
        System.out.println(ret);
    }   
}
