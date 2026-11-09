# Password Generator Python

Secure password generator built with Python and the `secrets` module.

## Highlights

- Generates strong passwords from the terminal
- Supports multiple passwords in one command
- Optional symbol-free mode
- Keeps minimum security rules by mixing uppercase, lowercase, and numbers

## Stack

- Python
- `secrets`
- `string`

## Run locally

```bash
python main.py
```

Generate a longer password:

```bash
python main.py --length 24
```

Generate three passwords without symbols:

```bash
python main.py --count 3 --no-symbols
```

## Author

Becker
