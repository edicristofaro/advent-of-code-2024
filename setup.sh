#!/bin/bash

# Advent of Code Daily Challenge Setup Script

# Path to session cookie file. Don't check this into github.
SESSION_FILE="${HOME}/.config/aoc_session"

# Day number from command line argument
if [ $# -eq 0 ]; then
    echo "Please provide a day number"
    echo "Usage: $0 <day_number>"
    exit 1
fi

# Day number and current year
DAY=$1
YEAR=$(date +%Y)

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
        input_data = f.readlines()
    
    input_data = [i.replace("\n","") for i in input_data]
    
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
SAMPLE_FILE="${DAY_DIR}/sample.txt"
if [ ! -f "$SAMPLE_FILE" ]; then
    echo "Creating ${SAMPLE_FILE}..."
    touch "$SAMPLE_FILE"
    echo "Sample input file created."
else
    echo "${SAMPLE_FILE} already exists. Skipping creation."
fi

# Create a notes file
NOTES_FILE="${DAY_DIR}/notes.md"
if [ ! -f "$NOTES_FILE" ]; then
    echo "Creating ${NOTES_FILE}..."
    touch "$NOTES_FILE"
    echo "Notes markdown file created."
else
    echo "${NOTES_FILE} already exists. Skipping creation."
fi

# Fetch input data (if session cookie exists)
INPUT_FILE="${DAY_DIR}/input.txt"
if [ -f "$SESSION_FILE" ]; then
    # Read session cookie, trimming any whitespace
    AOC_SESSION=$(tr -d '[:space:]' < "$SESSION_FILE")

    # Only attempt download if session cookie is not empty
    if [ ! -z "$AOC_SESSION" ] && [ ! -f "$INPUT_FILE" ] || [ ! -s "$INPUT_FILE" ]; then
        echo "Fetching input data for Day ${DAY}..."
        curl "https://adventofcode.com/${YEAR}/day/${DAY}/input" \
            --compressed \
            -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:132.0) Gecko/20100101 Firefox/132.0" \
            -H "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8" \
            -H "Accept-Language: en-US,en;q=0.5" \
            -H "Accept-Encoding: gzip, deflate, br, zstd" \
            -H "Referer: https://adventofcode.com/${YEAR}/day/${DAY}" \
            -H "DNT: 1" \
            -H "Connection: keep-alive" \
            -H "Cookie: session=${AOC_SESSION}" \
            -H "Upgrade-Insecure-Requests: 1" \
            -H "Sec-Fetch-Dest: document" \
            -H "Sec-Fetch-Mode: navigate" \
            -H "Sec-Fetch-Site: same-origin" \
            -H "Priority: u=0, i" \
            -H "TE: trailers" \
            -o "$INPUT_FILE"
        
        # Check if input was successfully downloaded
        if [ $? -eq 0 ] && [ -s "$INPUT_FILE" ]; then
            echo "Input data downloaded successfully."
        else
            echo "Failed to download input data."
            rm -f "$INPUT_FILE"
            touch "$INPUT_FILE"
        fi
    else
        if [ -f "$INPUT_FILE" ]; then
            echo "Input file already exists. Skipping download."
        else
            echo "No session cookie found. Skipping input data download."
        fi
    fi
else
    echo "No session cookie file found. Skipping input data download."
    # Create an empty input file if it doesn't exist
    touch "$INPUT_FILE"
fi

echo "Advent of Code setup for Day ${DAY} complete!"