fn message(name: &str) -> String {
    format!("Hello from {name}.")
}

fn main() {
    println!("{}", message("Rust"));
}

#[cfg(test)]
mod tests {
    use super::message;

    #[test]
    fn returns_message() {
        assert_eq!(message("Rust"), "Hello from Rust.");
    }
}
