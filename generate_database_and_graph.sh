#!/bin/bash

# Define the base directory
BASE_DIR=$(pwd)

# Define the paths for the input data and output images
DATA_DIR="$BASE_DIR/databases"
RESULTS_DIR="$BASE_DIR/images"

# Define paths to the commands
DATABASE_CREATION_DIR="$BASE_DIR/commands/database_creation"
GRAPH_CREATION_DIR="$BASE_DIR/commands/graph_creation"

# Check if required directories exist
if [ ! -d "$DATA_DIR" ]; then
  echo "Error: Data directory not found: $DATA_DIR"
  exit 1
fi

if [ ! -d "$RESULTS_DIR" ]; then
  echo "Creating results directory: $RESULTS_DIR"
  mkdir -p "$RESULTS_DIR"
fi

# Step 1: Create Database (assuming there is a database creation process in the database_creation folder)
echo "Step 1: Creating database..."

# Run database creation commands (e.g., CSV processing or database setup)
if [ -d "$DATABASE_CREATION_DIR" ]; then
  # Assuming there's a script inside the `database_creation` folder to process the data or generate the database
  for script in "$DATABASE_CREATION_DIR"/*.py; do
    echo "Running $script..."
    python3 "$script"
    if [ $? -ne 0 ]; then
      echo "Error during database creation in $script"
      exit 1
    fi
  done
else
  echo "Error: Database creation directory not found."
  exit 1
fi

# Step 2: Generate Graphs from the data
echo "Step 2: Generating graphs..."

# Run graph creation commands (e.g., plotting scripts)
if [ -d "$GRAPH_CREATION_DIR" ]; then
  # Assuming there are Python scripts in the `graph_creation` folder to generate the graphs
  for script in "$GRAPH_CREATION_DIR"/*.py; do
    echo "Running $script..."
    python3 "$script"
    if [ $? -ne 0 ]; then
      echo "Error during graph creation in $script"
      exit 1
    fi
  done
else
  echo "Error: Graph creation directory not found."
  exit 1
fi

# Step 3: Provide feedback to the user
echo "Process completed successfully! The graphs have been generated and saved to the $RESULTS_DIR directory."

# End of script
