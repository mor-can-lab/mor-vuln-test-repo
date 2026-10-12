#include <iostream>
#include <string>

std::string message(const std::string& name)
{
    return "Hello from " + name + ".";
}

int main()
{
    std::cout << message("C++") << '\n';
    return 0;
}
