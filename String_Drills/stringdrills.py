name = "  yash solanki python developer  "

print("Original String:")
print(name)


# ----------------------------
# 1. Indexing
# ----------------------------

print("\nFirst Character:")
print(name[0])

print("\nSixth Character:")
print(name[5])


# ----------------------------
# 2. Negative Indexing
# ----------------------------

print("\nLast Character:")
print(name[-1])

print("\nSecond Last Character:")
print(name[-2])


# ----------------------------
# 3. Slicing
# ----------------------------

print("\nFirst 4 Characters:")
print(name[0:4])

print("\nCharacters 5 to 11:")
print(name[5:12])

print("\nComplete String:")
print(name[:])

print("\nLast 9 Characters:")
print(name[-9:])


# ----------------------------
# 4. len()
# ----------------------------

print("\nLength:")
print(len(name))


# ----------------------------
# 5. upper()
# ----------------------------

print("\nUpper Case:")
print(name.upper())


# ----------------------------
# 6. lower()
# ----------------------------

print("\nLower Case:")
print(name.lower())


# ----------------------------
# 7. title()
# ----------------------------

print("\nTitle Case:")
print(name.title())


# ----------------------------
# 8. capitalize()
# ----------------------------

print("\nCapitalize:")
print(name.capitalize())


# ----------------------------
# 9. strip()
# ----------------------------

clean_name = name.strip()

print("\nAfter strip():")
print(clean_name)


# ----------------------------
# 10. replace()
# ----------------------------

updated_name = clean_name.replace("python", "java")

print("\nAfter replace():")
print(updated_name)


# ----------------------------
# 11. find()
# ----------------------------

print("\nFind 'developer':")
print(clean_name.find("developer"))


# ----------------------------
# 12. count()
# ----------------------------

print("\nCount of 'a':")
print(clean_name.count("a"))


# ----------------------------
# 13. startswith()
# ----------------------------

print("\nStarts with 'yash'?")
print(clean_name.startswith("yash"))


# ----------------------------
# 14. endswith()
# ----------------------------

print("\nEnds with 'developer'?")
print(clean_name.endswith("developer"))


# ----------------------------
# 15. split()
# ----------------------------

words = clean_name.split()

print("\nSplit into List:")
print(words)


# ----------------------------
# 16. join()
# ----------------------------

joined = "-".join(words)

print("\nJoin with '-':")
print(joined)


# ----------------------------
# 17. in
# ----------------------------

print("\nContains 'python'?")
print("python" in clean_name)


# ----------------------------
# 18. not in
# ----------------------------

print("\nContains 'docker'?")
print("docker" not in clean_name)
