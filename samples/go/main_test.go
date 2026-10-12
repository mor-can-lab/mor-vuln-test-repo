package main

import "testing"

func TestMessage(t *testing.T) {
	want := "Hello from Go."
	if got := message("Go"); got != want {
		t.Fatalf("message() = %q, want %q", got, want)
	}
}
