import sys
import urllib.parse

def encode_file(input_file, output_file):
    try:
        with open(input_file, 'r', encoding='utf-8', errors='ignore') as infile, \
             open(output_file, 'w', encoding='utf-8') as outfile:

            for line in infile:
                encoded_line = urllib.parse.quote_plus(line.rstrip())
                outfile.write(encoded_line + '\n')
        
        print(f"URL-encoded contents have been written to '{output_file}'")
    except FileNotFoundError:
        print(f"Error: The file '{input_file}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    if len(sys.argv) == 2:
        input_file = sys.argv[1]
        output_file = 'encoded_' + input_file
        encode_file(input_file, output_file)
    else:
        print("Usage: python3 urlencode.py <inputfile>")
        sys.exit(1)

if __name__ == "__main__":
    main()

