import java.lang.management.ManagementFactory;
import java.lang.management.OperatingSystemMXBean;
import java.lang.reflect.Method;
import java.lang.reflect.Modifier;

public class cpuload 
{

    public static void main(String[] args)
    {
        OperatingSystemMXBean object = ManagementFactory.getOperatingSystemMXBean();
        for(Method method : object.getClass().getDeclaredMethods())
        {
            method.setAccessible(true);
            if(method.getName().startsWith("get") && Modifier.isPublic(method.getModifiers()))
            {
                Object value;
                try 
                {
                    value = method.invoke(object);
                }
                catch (Exception e)
                {
                    value = e;
                }
                System.out.println(method.getName()+"= "+value);
            }
        }
    }
}
