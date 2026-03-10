import heapq
import os
from collections import Counter


class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq


def build_huffman_tree(text):
    frequency = Counter(text)
    heap = [Node(char, freq) for char, freq in frequency.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        n1 = heapq.heappop(heap)
        n2 = heapq.heappop(heap)
        merged = Node(None, n1.freq + n2.freq)
        merged.left, merged.right = n1, n2
        heapq.heappush(heap, merged)
    return heap[0]


def generate_codes(node, current_code, codes):
    if node:
        if node.char is not None:
            codes[node.char] = current_code
        generate_codes(node.left, current_code + "0", codes)
        generate_codes(node.right, current_code + "1", codes)


def compress_file(input_path, output_path):
    with open(input_path, 'r') as f:
        text = f.read()

    root = build_huffman_tree(text)
    codes = {}
    generate_codes(root, "", codes)

    encoded_text = "".join(codes[char] for char in text)

    with open(output_path, 'w') as f:
        f.write(encoded_text)

    original_size = os.path.getsize(input_path) * 8
    compressed_size = len(encoded_text.encode())

    saving = (1 - (compressed_size / original_size)) * 100

    print(f"File saved to {output_path}")
    print("Original size:", original_size)
    print("Compressed size:", compressed_size)
    print(f"Minimum Space Saved: {saving:.4f}%")

    def decompress_text(encoded_text, root):
        decoded_output = []
        current_node = root

        for bit in encoded_text:
            if bit == '0':
                current_node = current_node.left
            else:
                current_node = current_node.right

            if current_node.char is not None:
                decoded_output.append(current_node.char)
                current_node = root

        return "".join(decoded_output)

    original_text = decompress_text(encoded_text, root)
    print(f"Decoded Text: {original_text}")

if __name__ == "__main__":
    text = ""
    with open("input.txt", "w") as f:
        f.write("""Lorem ipsum dolor sit amet consectetur adipisicing elit. Porro praesentium ullam est, voluptatibus amet quaerat! A illum laboriosam aliquam obcaecati sint. Quasi reprehenderit dicta porro fugit deleniti doloremque, sapiente fuga.""")
    compress_file("input.txt", "compressed.txt")

