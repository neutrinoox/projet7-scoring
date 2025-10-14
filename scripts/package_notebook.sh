#!/usr/bin/env bash
set -euo pipefail

NOTEBOOK_PATH="V_Maxime_2_notebook_modélisation_092025.ipynb"
ARCHIVE_NAME="${NOTEBOOK_PATH%.ipynb}.zip"
OUTPUT_DIR="${1:-dist}"

if ! git rev-parse --show-toplevel >/dev/null 2>&1; then
  echo "Ce script doit être exécuté depuis un dépôt Git." >&2
  exit 1
fi

repo_root="$(git rev-parse --show-toplevel)"
cd "$repo_root"

if [[ ! -f "$NOTEBOOK_PATH" ]]; then
  echo "Notebook introuvable : $NOTEBOOK_PATH" >&2
  exit 1
fi

mkdir -p "$OUTPUT_DIR"
archive_path="$OUTPUT_DIR/$ARCHIVE_NAME"

export NOTEBOOK_PATH
export ARCHIVE_PATH="$archive_path"

python3 - <<'PY'
import os
import zipfile
from pathlib import Path

notebook_path = Path(os.environ["NOTEBOOK_PATH"]).resolve()
archive_path = Path(os.environ["ARCHIVE_PATH"]).resolve()

with zipfile.ZipFile(archive_path, "w", compression=zipfile.ZIP_DEFLATED) as zf:
    zf.write(notebook_path, notebook_path.name)

print(f"Archive générée : {archive_path}")
PY

