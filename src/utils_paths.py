# --- src/utils_paths.py ---
from pathlib import Path

def get_project_paths():
    """
    Detects whether running in Local, Colab, or Google Drive environment.
    Returns dictionary of standard project paths.
    """
    drive_path = Path("/content/drive/MyDrive/Loan_Repayment_Behaviour_Analytics")
    colab_path = Path("/content/Loan_Repayment_Behaviour_Analytics")
    local_path = Path.cwd().resolve()

    if drive_path.exists():
        ROOT = drive_path
        env = "Google Drive"
    elif colab_path.exists():
        ROOT = colab_path
        env = "Colab"
    else:
        ROOT = local_path
        env = "Local"

    DATA_RAW = ROOT / "data" / "raw"
    DATA_INTERIM = ROOT / "data" / "interim"
    DATA_PROCESSED = ROOT / "data" / "processed"
    IMAGES = ROOT / "images"
    REPORTS = ROOT / "reports"

    # ensure folders exist
    for f in [DATA_RAW, DATA_INTERIM, DATA_PROCESSED, IMAGES, REPORTS]:
        f.mkdir(parents=True, exist_ok=True)

    return {
        "env": env,
        "ROOT": ROOT,
        "DATA_RAW": DATA_RAW,
        "DATA_INTERIM": DATA_INTERIM,
        "DATA_PROCESSED": DATA_PROCESSED,
        "IMAGES": IMAGES,
        "REPORTS": REPORTS
    }
