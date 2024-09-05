# RediPy

**RediPy** is a lightweight, Redis-like key-value store implemented in Python. It provides basic functionality similar to Redis, including in-memory storage, key expiration, and persistence to disk. This project is an educational tool designed to mimic some of the core features of Redis.

## Features

- **In-Memory Storage**: Fast key-value storage in memory.
- **Key Expiration**: Set time-based expiration for keys.
- **Persistence**: Save and load data to/from disk using Python's `pickle`.
- **Basic Commands**: Supports commands like `SET`, `GET`, `DEL`, `EXPIRE`, `KEYS`, and `PERSIST`.

## Usage

To run the RediPy interactive session:

1. **Start the database:**
   ```bash
   python main.py
   ```

2. **Interactive Prompt:**
   In the interactive prompt, you can use commands like:
   - `SET key value` – Store a value under a key.
   - `GET key` – Retrieve the value for a key.
   - `DEL key` – Delete a key from the store.
   - `EXPIRE key ttl` – Set a time-to-live (TTL) for a key.
   - `KEYS` – List all keys in the store.
   - `PERSIST key` – Remove the expiration for a given key.

   **Example:**
   ```
   >> SET name Alice
   OK
   >> GET name
   Alice
   >> EXPIRE name 10
   1
   >> GET name
   Alice
   ```

3. **Exit the Session:**
   Type `EXIT` and press Enter.

## Testing

To run the unit tests for RediPy, use the following command:
```bash
python -m unittest discover -s tests
```

## File Structure

- **core.py**: Handles in-memory data storage and expiration.
- **commands.py**: Command handling logic.
- **persistence.py**: Data persistence functionality.
- **config.py**: Configuration constants.
- **tests/**: Unit tests for RediPy.
  - **test_core.py**: Tests for core functionality.
  - **test_commands.py**: Tests for command handling.
- **main.py**: Entry point for running the interactive session.

## Contributing

Contributions are welcome Please open an issue or a pull request if you have suggestions or improvements.

**Steps to Contribute:**

1. **Fork the repository.**
2. **Create a new branch:**
   ```bash
   git checkout -b feature-branch
   ```
3. **Commit your changes:**
   ```bash
   git commit -am 'Add new feature'
   ```
4. **Push to the branch:**
   ```bash
   git push origin feature-branch
   ```
5. **Open a pull request.**

## Acknowledgements

- **Redis:** For inspiring the core functionality of this project.