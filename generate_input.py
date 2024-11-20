# input_generator.py
import random
import string

def generate_input(size, output_file):
    """Generate random strings of given size and save to file."""
    try:
        # Generate two random strings of equal length
        S1 = ''.join(random.choices(string.ascii_lowercase, k=size))
        S2 = ''.join(random.choices(string.ascii_lowercase, k=size))
        
        # Write to file in the required format
        with open(output_file, 'w') as f:
            f.write(f"{size} {size}\n")
            f.write(f"{S1}\n")
            f.write(f"{S2}\n")
        
        print(f"Successfully generated input file: {output_file}")
        return True
    except Exception as e:
        print(f"Error generating input file {output_file}: {str(e)}")
        return False

if __name__ == "__main__":
    # Generate inputs for different sizes
    sizes = [8, 50, 100, 1000, 10000, 50000, 100000]
    
    for size in sizes:
        input_file = f"input{size}.txt"
        generate_input(size, input_file)