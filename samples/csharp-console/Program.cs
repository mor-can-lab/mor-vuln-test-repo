Console.WriteLine(Greeter.Message("C# console"));

internal static class Greeter
{
    public static string Message(string name) => $"Hello from {name}.";
}
