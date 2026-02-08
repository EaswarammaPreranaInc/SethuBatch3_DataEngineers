import os
import re
import csv
import sys
import json
import subprocess
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo

IST = ZoneInfo("Asia/Kolkata")

SUBMISSIONS_DIR = "submissions"
REPORTS_DIR = "reports"
STUDENTS_CSV = "students.csv"

FILENAME_DATE_RE = re.compile(r"^(?P<prefix>.+)_(?P<yyyymmdd>\d{8})\.py$", re.IGNORECASE)

def run(cmd: list[str]) -> str:
    out = subprocess.check_output(cmd, stderr=subprocess.STDOUT)
    return out.decode("utf-8", errors="replace").strip()

def ensure_dirs():
    os.makedirs(REPORTS_DIR, exist_ok=True)

def read_students():
    students = []
    with open(STUDENTS_CSV, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        if "github_username" not in reader.fieldnames:
            raise ValueError("students.csv must contain a 'github_username' column.")
        for row in reader:
            username = (row.get("github_username") or "").strip()
            if not username:
                continue
            students.append({
                "github_username": username,
                "full_name": (row.get("full_name") or "").strip()
            })
    return students

def list_branch_files(branch: str, path: str) -> list[str]:
    """
    Return file names (not full paths) under `path` in the given branch.
    """
    # If folder doesn't exist, git will error; handle gracefully.
    try:
        out = run(["git", "ls-tree", "-r", "--name-only", branch, path])
        files = [line.split("/")[-1] for line in out.splitlines() if line.strip().lower().endswith(".py")]
        return files
    except subprocess.CalledProcessError:
        return []

def get_last_commit_iso_for_path(branch: str, file_path: str) -> str | None:
    """
    Return ISO timestamp for last commit that touched file_path in branch.
    """
    try:
        out = run(["git", "log", "-1", "--format=%cI", branch, "--", file_path])
        return out.strip() or None
    except subprocess.CalledProcessError:
        return None

def ist_day_to_check(now_ist: datetime) -> datetime.date:
    """
    We run at ~00:10 IST and report on the previous IST day (the day that just ended).
    """
    return (now_ist - timedelta(days=1)).date()

def main():
    ensure_dirs()

    now_ist = datetime.now(tz=IST)
    target_date = ist_day_to_check(now_ist)
    yyyymmdd = target_date.strftime("%Y%m%d")

    students = read_students()

    submitted = []
    not_submitted = []
    late = []
    naming_issues = []

    # Deadline: 23:59:59 IST on target_date
    deadline_ist = datetime(
        year=target_date.year,
        month=target_date.month,
        day=target_date.day,
        hour=23, minute=59, second=59,
        tzinfo=IST
    )

    for s in students:
        branch = s["github_username"]
        full_name = s.get("full_name", "")
        files = list_branch_files(branch, SUBMISSIONS_DIR)

        # Find files with matching date suffix
        matching = []
        for fn in files:
            m = FILENAME_DATE_RE.match(fn)
            if not m:
                continue
            if m.group("yyyymmdd") == yyyymmdd:
                matching.append(fn)

        if not matching:
            not_submitted.append((branch, full_name))
            continue

        # If multiple matches, treat as submitted, but flag naming/duplicate
        # Choose the first for timestamp evaluation
        chosen = sorted(matching)[0]
        if len(matching) > 1:
            naming_issues.append((branch, full_name, "MULTIPLE_FILES", ";".join(sorted(matching))))

        # Validate naming prefix is present (best-effort; we can't fully validate names)
        # We only enforce the *_YYYYMMDD.py pattern, but still warn if prefix is too short.
        prefix = chosen.rsplit("_", 1)[0]
        if len(prefix) < 3:
            naming_issues.append((branch, full_name, "SUSPICIOUS_PREFIX", chosen))

        file_path = f"{SUBMISSIONS_DIR}/{chosen}"
        commit_iso = get_last_commit_iso_for_path(branch, file_path)

        is_late = False
        commit_ist = None
        if commit_iso:
            try:
                commit_dt = datetime.fromisoformat(commit_iso.replace("Z", "+00:00"))
                commit_ist = commit_dt.astimezone(IST)
                if commit_ist > deadline_ist:
                    is_late = True
            except Exception:
                naming_issues.append((branch, full_name, "BAD_COMMIT_TIME", commit_iso or ""))

        submitted.append((branch, full_name, chosen, commit_ist.isoformat() if commit_ist else ""))

        if is_late:
            late.append((branch, full_name, chosen, commit_ist.isoformat() if commit_ist else ""))

    # Write CSVs
    submitted_csv = os.path.join(REPORTS_DIR, f"submitted_{yyyymmdd}.csv")
    not_submitted_csv = os.path.join(REPORTS_DIR, f"not_submitted_{yyyymmdd}.csv")
    late_csv = os.path.join(REPORTS_DIR, f"late_{yyyymmdd}.csv")
    naming_csv = os.path.join(REPORTS_DIR, f"naming_issues_{yyyymmdd}.csv")
    md_report = os.path.join(REPORTS_DIR, f"daily_report_{yyyymmdd}.md")

    with open(submitted_csv, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["github_username", "full_name", "file_name", "commit_time_ist"])
        w.writerows(submitted)

    with open(not_submitted_csv, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["github_username", "full_name"])
        w.writerows(not_submitted)

    with open(late_csv, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["github_username", "full_name", "file_name", "commit_time_ist"])
        w.writerows(late)

    with open(naming_csv, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["github_username", "full_name", "issue", "details"])
        w.writerows(naming_issues)

    # Write Markdown summary
    with open(md_report, "w", encoding="utf-8") as f:
        f.write(f"# Daily Submission Report - {target_date.isoformat()} (IST)\n\n")
        f.write(f"**Deadline:** {deadline_ist.strftime('%Y-%m-%d %H:%M:%S %Z')}\n\n")
        f.write(f"## Summary\n")
        f.write(f"- Total students: **{len(students)}**\n")
        f.write(f"- Submitted: **{len(submitted)}**\n")
        f.write(f"- Not submitted: **{len(not_submitted)}**\n")
        f.write(f"- Late submissions: **{len(late)}**\n")
        f.write(f"- Naming/duplicate issues: **{len(naming_issues)}**\n\n")

        f.write("## Submitted\n")
        for u, name, fn, ctime in submitted:
            label = f"{u} ({name})" if name else u
            f.write(f"- {label} — `{fn}` {f'— {ctime}' if ctime else ''}\n")
        f.write("\n## Not Submitted\n")
        for u, name in not_submitted:
            label = f"{u} ({name})" if name else u
            f.write(f"- {label}\n")

        f.write("\n## Late Submissions\n")
        if late:
            for u, name, fn, ctime in late:
                label = f"{u} ({name})" if name else u
                f.write(f"- {label} — `{fn}` — {ctime}\n")
        else:
            f.write("- None\n")

        f.write("\n## Naming / Duplicate Issues\n")
        if naming_issues:
            for u, name, issue, details in naming_issues:
                label = f"{u} ({name})" if name else u
                f.write(f"- {label} — **{issue}** — {details}\n")
        else:
            f.write("- None\n")

    print(f"Generated reports for {target_date.isoformat()} IST:")
    print(f"- {md_report}")
    print(f"- {submitted_csv}")
    print(f"- {not_submitted_csv}")
    print(f"- {late_csv}")
    print(f"- {naming_csv}")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"ERROR: {e}", file=sys.stderr)
        sys.exit(1)
