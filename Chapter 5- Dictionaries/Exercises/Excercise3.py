# Create a glossary with programming words and their meanings
glossary = {
    "Variable": "A named storage location in memory used to store data.",
    "Function": "A block of code that can be called to perform a specific task or operation.",
    "Loop": "A control structure that repeats a set of statements as long as a specified condition is met.",
    "Conditional Statement": "A statement that allows for different code to be executed depending on a condition.",
    "List": "An ordered collection of items, which can be of different data types.",
    "Dictionary": "A collection of key-value pairs that can be used to store and retrieve data.",
    "Tuple": "An ordered, immutable collection of elements.",
    "String": "A sequence of characters enclosed in single or double quotes.",
    "Boolean": "A data type that represents True or False values.",
    "Method": "A function associated with an object or data type.",
}

# Print each word and its meaning neatly formatted with a loop
for word, meaning in glossary.items():
    print(f"{word}:\n{meaning}\n")
