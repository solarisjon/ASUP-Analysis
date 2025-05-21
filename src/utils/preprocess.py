import re

def count_leading_whitespace(line):
    """
    Counts the number of leading whitespace characters (spaces and tabs) in a line.
    Returns the count of spaces and tabs separately.
    """
    spaces = 0
    tabs = 0
    for character in line:
        if character == ' ':
            spaces += 1
        elif character == '\t':
            tabs += 1
        else:
            break
    return spaces, tabs

def normalize_indentation(input_file_path, output_file_path, spaces_per_tab=4):
    """
    Reads the input file, normalizes indentation so each level is one tab deeper than its parent,
    and writes the result to the output file.
    """
    with open(input_file_path, 'r') as input_file:
        lines = input_file.readlines()

    # This stack will keep track of the indentation levels seen so far
    indentation_levels = [0]  # The root is always at 0
    normalized_lines = []

    for line in lines:
        # Skip empty lines
        if not line.strip():
            normalized_lines.append('\n')
            continue

        # Count leading whitespace
        spaces, tabs = count_leading_whitespace(line)
        total_leading = tabs * spaces_per_tab + spaces

        # Find the correct level for this line
        # If this indentation is new, add it to the stack
        if total_leading > indentation_levels[-1]:
            indentation_levels.append(total_leading)
            current_level = len(indentation_levels) - 1
        else:
            # Find the closest existing indentation level
            while indentation_levels and total_leading < indentation_levels[-1]:
                indentation_levels.pop()
            current_level = len(indentation_levels) - 1

        # Remove all leading whitespace and add normalized tabs
        stripped_line = line.lstrip(' \t')
        normalized_line = '\t' * current_level + stripped_line
        normalized_lines.append(normalized_line)

    # Write the normalized lines to the output file
    with open(output_file_path, 'w') as output_file:
        output_file.writelines(normalized_lines)

if __name__ == "__main__":
    input_path = "data/SmartSolve_SYSCONFIG-A_Asupid_2025051316060195.txt"
    output_path = "data/SmartSolve_SYSCONFIG-A_Asupid_2025051316060195_normalized.txt"
    normalize_indentation(input_path, output_path)
    print(f"Normalized file written to {output_path}")