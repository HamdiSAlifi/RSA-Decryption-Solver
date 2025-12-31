"""
Project: RSA Decryption Solver (Exam Study Tool)
Author: HamdiSALifi
Date: 2025-12-31
Description: 
    This script solves a specific RSA decryption problem from a Discrete Mathematics exam.
    It demonstrates the mathematical process of converting ciphertext to numbers, 
    applying the RSA formula (M = C^d mod n), and converting back to text.

Acknowledgement: 
    Code logic and mathematical explanation were refined with the assistance of Gemini AI.
"""

def solve_rsa():
    # 1. Define the parameters from the problem
    # n is the modulus part of the public key (26)
    # example from my exam question, n = 26
    n = 26
    # e is the public exponent
    # in my exam question, e = 7
    e = 7
    # C_letters is the encrypted message
    # in my exam question it's 
    C_letters = ['H', 'B', 'V', 'O']

    # 2. Hardcode the Private Key Calculation, which is derived from the exam question above
    # in real scenario, my LLMs model says we need to calc this using the extended Euclidean algorithm.
    # Here we confirmed d = 7 (based on my exam question) manually.
    d = 7

    # 3. Create a helper function to convert letters to number (A = 0, B = 1, ... and so on)
    # ord(char) gets the ASCII value. ord ('A') is 65
    # So ord ('H') - 65 gives 7.
    def to_num(char):
        return ord(char) - ord('A')
    
    # 4. Create a helper function to convert numbers back to letters 
    # This reverses the process : 7 + 65 = 72, which is 'H'.
    def to_char(num):
        return chr(num + ord('A'))
    
    # 5. Perform the decryption loop
    decrypted_message = ""
    for char in C_letters:
        # Convert the current encrypted character to its number
        # Example: 'H' becomes 7
        c_num = to_num(char)

        # Apply the RSA Decryption Formula: M = (C^d) % n
        # pow(base, exp, mod) is an efficient way to calculate (base**exp) % mod
        # Example : pow(7, 7, 26) results in 19
        m_num = pow(c_num, d, n)

        # Convert the decrypted number back to a letter
        # Example : 19 becomes 'T'
        m_char = to_char(m_num)

        # Append the result to our final string
        decrypted_message += m_char

    # 6. Print the final result
    print(f"Decrypted Message : {decrypted_message}")

# Execute the function
if __name__ == "__main__":
    solve_rsa()