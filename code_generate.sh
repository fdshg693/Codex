# Create the runs directory if it doesn't exist
mkdir -p runs

# Move into the working directory
cd runs || exit 1

# Find existing run_N directories
shopt -s nullglob
run_dirs=(run_[0-9]*)
shopt -u nullglob

if [ ${#run_dirs[@]} -eq 0 ]; then
  echo "There are 0 runs."
  new_run_number=1
else
  max_run_number=0
  for d in "${run_dirs[@]}"; do
    [[ "$d" =~ ^run_([0-9]+)$ ]] && (( ${BASH_REMATCH[1]} > max_run_number )) && max_run_number=${BASH_REMATCH[1]}
  done
  new_run_number=$((max_run_number + 1))
  echo "There are $max_run_number runs."
fi

# activate the virtual environment if it exists
if [ -d "../.venv" ]; then
  source ../.venv/bin/activate
  echo "Activated virtual environment."
else
  echo "No virtual environment found. Skipping activation."
fi

# Create the run directory
mkdir "run_$new_run_number"

# Check if the template directory exists and copy its contents
if [ -d "../template" ]; then
  cp -a ../template/. "run_$new_run_number"
  echo "Initialized run_$new_run_number from template/"
else
  echo "Template directory does not exist. Skipping initialization from template."
fi

cd "run_$new_run_number"

# 受け取った引数をCODEXコマンドにそのまま渡す
CODEX "$@"


