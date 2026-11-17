"""Deploy the application to a persistent local release directory."""

import argparse
import hashlib
import json
from pathlib import Path
import shutil


def deploy(target):
    """Copy the application and record a verifiable release manifest."""
    source = Path(__file__).resolve().parent / "app.py"
    target = Path(target).resolve()
    target.mkdir(parents=True, exist_ok=True)
    destination = target / "app.py"
    shutil.copy2(source, destination)
    digest = hashlib.sha256(destination.read_bytes()).hexdigest()
    if digest != hashlib.sha256(source.read_bytes()).hexdigest():
        raise RuntimeError("Deployment checksum mismatch")
    manifest = {"application": "app.py", "sha256": digest}
    (target / "manifest.json").write_text(
        json.dumps(manifest, indent=2) + "\n", encoding="utf-8"
    )
    print(f"Deployed application to {destination}")
    print(f"SHA256: {digest}")
    return destination


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--target", required=True)
    deploy(parser.parse_args().target)
