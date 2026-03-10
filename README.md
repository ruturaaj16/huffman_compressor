# Huffman Coding Text Compressor 📄✂️

A high-performance, lossless data compression utility built in **Python**. [cite_start]This project implements the **Huffman Coding algorithm** to compress raw text files, leveraging greedy logic and optimal binary prefix trees to reduce file sizes significantly without any data loss.

---

## 🚀 Performance & Impact
* [cite_start]**Space Efficiency:** Achieved a measurable space-saving of **30-50%** on standard text datasets.
* [cite_start]**Algorithmic Complexity:** Optimized for **$O(N \log K)$** time complexity using a Min-Heap (Priority Queue)[cite: 16].
* [cite_start]**Data Integrity:** Guaranteed 100% reconstruction of original data through bi-directional processing (encoding and decoding).

---

## 🛠️ How It Works
The compressor follows a structured algorithmic pipeline:

1. **Frequency Analysis:** Scans the input text to calculate the frequency of each unique character.
2. [cite_start]**Greedy Tree Construction:** Utilizes a **Min-Heap** to repeatedly merge the two least frequent nodes until a single **Huffman Tree** root remains.
3. [cite_start]**Prefix-Free Encoding:** Traverses the tree to assign unique binary codes (0 for left, 1 for right), ensuring no code is a prefix of another.
4. **Bitstream Generation:** Replaces characters with their new bit-level shorthand to create a compact binary file.



---

## 💻 Usage

### Prerequisites
- Python 3.14.2

### Compression
To compress a text file into a binary format:
```bash
python huffman.py
