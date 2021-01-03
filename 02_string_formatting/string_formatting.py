name = 'Bob'
print(f"Hello, {name}")

greeting = "Hello, {}"
with_name = greeting.format('Rolf')

print(with_name)

longer_phrase = "Hello, {}. Today is {}."
formatted = longer_phrase.format('Rolf', 'Monday')
print(formatted)
