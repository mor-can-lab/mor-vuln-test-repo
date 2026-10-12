package com.example;

public final class App {
    private App() {
    }

    public static String message(String name) {
        return "Hello from " + name + ".";
    }

    public static void main(String[] args) {
        System.out.println(message("Java"));
    }
}
