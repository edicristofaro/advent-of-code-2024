#!/bin/bash

# Advent of Code Daily Challenge Setup Script
# Created with Claude. This will be the only AI-generated content for this challenge.
# No using AI to solve daily problems.

# Check if a day number is provided
if [ $# -eq 0 ]; then
    echo "Please provide a day number"
    echo "Usage: $0 <day_number>"
    exit 1
fi

# Day number from command line argument
DAY=$1

# Create day-specific directory
DAY_DIR="day${DAY}"
mkdir -p "$DAY_DIR"

# Activate virtual environment
echo "Activating virtual environment..."
source env/bin/activate

# Create Python script for the day
PYTHON_FILE="${DAY_DIR}/day${DAY}.py"
if [ ! -f "$PYTHON_FILE" ]; then
    echo "Creating ${PYTHON_FILE}..."
    cat << EOF > "$PYTHON_FILE"
def part1(input_data):
    # TODO: Implement part 1 solution
    pass

def part2(input_data):
    # TODO: Implement part 2 solution
    pass

def main():
    # Read input
    with open('input${DAY}.txt', 'r') as f:
        input_data = f.read().strip()
    
    # Solve and print results
    print("Part 1:", part1(input_data))
    print("Part 2:", part2(input_data))

if __name__ == '__main__':
    main()
EOF
    echo "Python script created."
else
    echo "${PYTHON_FILE} already exists. Skipping creation."
fi

# Create sample input file
SAMPLE_FILE="${DAY_DIR}/sample${DAY}.txt"
if [ ! -f "$SAMPLE_FILE" ]; then
    echo "Creating ${SAMPLE_FILE}..."
    touch "$SAMPLE_FILE"
    echo "Sample input file created."
else
    echo "${SAMPLE_FILE} already exists. Skipping creation."
fi

# Create actual input file
INPUT_FILE="${DAY_DIR}/input${DAY}.txt"
if [ ! -f "$INPUT_FILE" ]; then
    echo "Creating ${INPUT_FILE}..."
    touch "$INPUT_FILE"
    echo "Input file created."
else
    echo "${INPUT_FILE} already exists. Skipping creation."
fi

echo "Advent of Code setup for Day ${DAY} complete!"