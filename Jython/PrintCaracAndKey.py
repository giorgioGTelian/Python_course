// DemoArgs.java

import org.python.core.*;

public class DemoArgs
{
    public static PyString __doc__ =
        new PyString("Demonstrate the use of complex arguments.");

    public String name;
    public String value;

    public DemoArgs(String newName, String newValue)
    {
        name = newName;
        value = newValue;
    }

    public static PyString __doc__set_name = new PyString(
        "Set the name attribute");
    public void set_name(PyObject[] args, String[] kwargs)
    {
        System.out.println("length(args): " +
            args.length +
            " length(kwargs): " +
            kwargs.length
            );
        ArgParser ap = new ArgParser("set_name", args, kwargs,
            new String[] {"name", "value"});
        String newName = ap.getString(0, "");
        String newValue = ap.getString(1, "<empty>");
        if (!newName.equals(""))
        {
            name = newName;
        }
        value = newValue;
    }
    public static PyString __doc__get_name = new PyString(
        "Get the name attribute");
    public String get_name()
    {
        return name;
    }

    public static PyString __doc__get_value = new PyString(
        "Get the value attribute");
    public String get_value()
    {
        return value;
    }

    public static PyString __doc__Show = new PyString(
        "Show the name and value attributes");
    public void Show()
    {
        System.out.println("My name is \"" + name +
            "\" and my value is \"" + value + "\".");
    }
}
