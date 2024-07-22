import os
def format_size(size):
    if size >= 1024 * 1024:
        return f" {size / (1024 * 1024):.1f} M5"
    elif size >= 1024:
        return f"{size / 1024:.1f} КБ"
    else:
        return f" {size} 5"

directory = ("/")
files_with_sizes = []

for filename in os.listdir(directory):
        size = os.path.getsize(os.path.join(directory, filename))
        files_with_sizes.append((filename, size))

files_with_sizes.sort(key=lambda x: x[1], reverse=True)

print("Список файлов:")
for i, (filename, size) in enumerate(files_with_sizes, start=1):
    print(f"{i}. {filename} - {format_size(size)}")