import subprocess
import sys


def run_command(cmd: list[str], description: str) -> bool:
    print(f"\n--- Running {description} ---")
    result = subprocess.run(cmd, capture_output=True, text=True)
    print(result.stdout)
    if result.stderr:
        print(result.stderr, file=sys.stderr)
    return result.returncode == 0


def main() -> None:
    format_ok = run_command(["ruff", "format", "--check", "."], "Ruff Format Check")
    lint_ok = run_command(["ruff", "check", "."], "Ruff Linter")
    mypy_ok = run_command(["mypy", "src/"], "Mypy Type-Checker")

    if format_ok and lint_ok and mypy_ok:
        print("\nAll local CI checks passed successfully!")
        sys.exit(0)
    else:
        print("\nSome checks failed. Please fix the reported errors above.", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
