# mor-vuln-test-repo

Small multi-language sample repository for validating GitHub repository, build, lint, and CodeQL scanning workflows.

## Samples

| Path | Language | How to run locally |
| --- | --- | --- |
| `samples/csharp-console` | C# console | `dotnet run --project samples/csharp-console` |
| `samples/csharp-web` | C# web | `dotnet run --project samples/csharp-web` |
| `samples/python` | Python | `python samples/python/app.py` |
| `samples/node` | Node.js | `node samples/node/index.js` |
| `samples/java` | Java | `mvn -f samples/java/pom.xml test` |
| `samples/go` | Go | `go test ./samples/go` |
| `samples/typescript` | TypeScript | `cd samples/typescript && npm install && npm run build` |
| `samples/ruby` | Ruby | `ruby samples/ruby/app.rb` |
| `samples/rust` | Rust | `cargo test --manifest-path samples/rust/Cargo.toml` |
| `samples/cpp` | C++ | `cmake -S samples/cpp -B samples/cpp/build && cmake --build samples/cpp/build` |

## Workflows

- `.github/workflows/build.yml` builds or compiles every sample.
- `.github/workflows/lint.yml` runs lightweight syntax and formatting checks.
- `.github/workflows/codeql-analysis.yml` runs CodeQL for supported language families used in this repository.
