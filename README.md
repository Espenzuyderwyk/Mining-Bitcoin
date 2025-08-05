# 🚀 Bitcoin Vanity Address Miner

A simple Python script for brute-forcing Bitcoin private keys to find a specific address (a "vanity address").  
This script demonstrates how Bitcoin addresses are generated from private keys, allowing you to explore cryptographic key generation and address matching in Bitcoin.  
**For educational purposes only!**

---

## 📝 Description

This Python script performs a brute-force search to find a Bitcoin private key that corresponds to a specific Bitcoin address (vanity address).  
The script generates addresses from private keys within a defined range, compares each generated address with the target address, and reports if a match is found.  
It's designed to help you understand how Bitcoin addresses are created, how hashing and encoding work, and to illustrate the near-impossibility of brute-forcing someone else's private key.

---

## ⚠️ Disclaimer

> **This script is for educational and experimental use only.**  
> Attempting to find someone else's private key is mathematically infeasible and unethical.  
> Never use this script for malicious activities or to compromise real wallets/accounts.

---

## 📦 Requirements

- Python 3.x
- [ecdsa](https://pypi.org/project/ecdsa/)
- [base58](https://pypi.org/project/base58/)

Install dependencies:

```bash
pip install ecdsa base58
```

---

## 🚦 Usage

1. **Clone or download this repository.**
2. **Edit `mining.py`** to set your desired `TARGET_ADDRESS`, `START_KEY`, and `STOP_KEY` range.
3. **Run the script:**

```bash
python mining.py
```

You’ll see output like:

```
Checked: 0x400000000000000 - 1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa
Checked: 0x400000000186a0 - 1BvBMSEYstWetqTFn5Au4m4GFg7xJaNVN2
...
🎯 MATCH FOUND!
Private Key (hex): 0x...
Address: 1PWo3JeB9jrGwfHDNpdGK54CRas7fsVzXU
```

---

## 🧑‍💻 How it Works

- Uses the [SECP256k1](https://en.bitcoin.it/wiki/Secp256k1) elliptic curve for cryptography.
- Generates Bitcoin addresses using SHA-256, RIPEMD-160 hashes, and Base58Check encoding.

---

## 📚 References

- [Bitcoin Wiki: Vanity address](https://en.bitcoin.it/wiki/Vanity_address)
- [Bitcoin Wiki: Technical background of version 1 Bitcoin addresses](https://en.bitcoin.it/wiki/Technical_background_of_version_1_Bitcoin_addresses)
- [SECP256k1 Documentation (PDF)](https://www.secg.org/sec2-v2.pdf)

---

## 🙏 Support & Contributing

Pull requests are welcome for improvements, code cleanup, or documentation!

---

## 🛑 Warning

- The search space for real Bitcoin addresses is astronomically large—**brute-force approaches are virtually impossible** for real keys.
- Never use this script to attempt to steal from others.

---

**Made with ❤️ for learning cryptography and Bitcoin internals.**
