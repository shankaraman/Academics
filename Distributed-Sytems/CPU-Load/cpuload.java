import java.lang.management.ManagementFactory;
import java.lang.management.OperatingSystemMXBean;
public class cpuload 
{

    public static void main(String[] args)
    {
        OperatingSystemMXBean osBean=(OperatingSystemMXBean) ManagementFactory.getOperatingSystemMXBean();
        System.out.println(osBean.getSystemLoadAverage());
    }
}

