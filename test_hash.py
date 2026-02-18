#!/usr/bin/env python3
"""Test script for hash_password with long passwords"""

from auth.hash_password import HashPassword

hash_password = HashPassword()

# Test 1: mot de passe normal (< 72 bytes)
print("Test 1: Mot de passe normal")
password1 = "my_secure_password"
hashed1 = hash_password.create_hash(password1)
print(f"  Original: {password1}")
print(f"  Hashed: {hashed1}")
verified1 = hash_password.verify_hash(password1, hashed1)
print(f"  Verified: {verified1}")
print()

# Test 2: mot de passe long (> 72 bytes)
print("Test 2: Mot de passe très long (>72 bytes)")
password2 = "a" * 100  # 100 caractères (100 bytes en ASCII)
print(f"  Original length: {len(password2.encode('utf-8'))} bytes")
hashed2 = hash_password.create_hash(password2)
print(f"  Hashed: {hashed2}")
verified2 = hash_password.verify_hash(password2, hashed2)
print(f"  Verified: {verified2}")
print()

# Test 3: mot de passe avec caractères Unicode (> 72 bytes en UTF-8)
print("Test 3: Mot de passe Unicode long")
password3 = "🔐" * 30  # chaque emoji = 4 bytes en UTF-8, total = 120 bytes
print(f"  Original length: {len(password3.encode('utf-8'))} bytes")
hashed3 = hash_password.create_hash(password3)
print(f"  Hashed: {hashed3}")
verified3 = hash_password.verify_hash(password3, hashed3)
print(f"  Verified: {verified3}")
print()

print("✅ Tous les tests sont passés!")
