import argparse
import secrets
import string


DEFAULT_LENGTH = 16


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Generate secure passwords from the terminal."
    )
    parser.add_argument(
        "--length",
        type=int,
        default=DEFAULT_LENGTH,
        help="Number of characters in each password.",
    )
    parser.add_argument(
        "--count",
        type=int,
        default=1,
        help="How many passwords to generate.",
    )
    parser.add_argument(
        "--no-symbols",
        action="store_true",
        help="Skip special characters and use only letters and numbers.",
    )
    return parser.parse_args()


def build_charset(include_symbols: bool) -> str:
    charset = string.ascii_letters + string.digits
    if include_symbols:
        charset += "!@#$%^&*()-_=+[]{}"
    return charset


def generate_password(length: int, include_symbols: bool) -> str:
    if length < 8:
        raise ValueError("Password length must be at least 8 characters.")

    pools = [
        string.ascii_lowercase,
        string.ascii_uppercase,
        string.digits,
    ]

    if include_symbols:
        pools.append("!@#$%^&*()-_=+[]{}")

    if length < len(pools):
        raise ValueError("Length is too short for the selected password rules.")

    password_chars = [secrets.choice(pool) for pool in pools]
    charset = build_charset(include_symbols)

    while len(password_chars) < length:
        password_chars.append(secrets.choice(charset))

    secrets.SystemRandom().shuffle(password_chars)
    return "".join(password_chars)


def main() -> None:
    args = parse_args()

    try:
        passwords = [
            generate_password(args.length, not args.no_symbols)
            for _ in range(max(1, args.count))
        ]
    except ValueError as error:
        print(f"Error: {error}")
        raise SystemExit(1) from error

    print("\nGenerated passwords")
    print("-------------------")
    for index, password in enumerate(passwords, start=1):
        print(f"{index}. {password}")


if __name__ == "__main__":
    main()
