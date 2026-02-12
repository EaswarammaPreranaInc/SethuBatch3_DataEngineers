#!/usr/bin/env python3
"""
Daily submission report (IST) for Sri Sathya Sai Skill Development Program.

Key improvements vs original:
- Fetches ALL remote branches first (git fetch --all --prune).
- For each student, prefers local branch '<username>'; if not present, uses 'origin/<username>'.
- Works even if only remote-tracking branches exist (no local branch checkout).
- Optional overrides via environment variables:
    - TARGET_DATE_IST: YYYYMMDD or YYYY-MM-DD (report date in IST; default: yesterday IST)
    - INCLUDE_MAIN_FALLBACK: "1" to also search 'main' when the student branch is missing
    - MAIN_BRANCH_NAME: default "main"
    - VERBOSE: "1" for extra logs

Outputs:
- reports/daily_report_YYYYMMDD.md
- reports/submitted_YYYYMMDD.csv
- reports/not_submitted_YYYYMMDD.csv
- reports/late_YYYYMMDD.csv
- reports/naming_issues_YYYYMMDD.csv
"""

import os
import re
import csv
import sys
import subprocess
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo

IST = ZoneInfo("Asia/Kolkata")

SUBMISSIONS_DIR = "submissions"
REPORTS_DIR = "reports"
STUDENTS_CSV = "students.csv"

# filename like firstname_lastname_YYYYMMDD.py
FILENAME_DATE_RE = re.compile(r"^(?P<prefix>.+)_(?P<yyyymmdd>\d{8})\.py$", re.IGNORECASE)


def env_flag(name: str, default: bool = False) -> bool:
    v = os.getenv(name)
    if v is None:
        return default
    return str(v).strip() in ("1", "true", "TRUE", "yes", "YES", "on", "On")


def env_str(name: str, default: str) -> str:
    v = os.getenv(name)
    return v if v is not None else default


def verbose(msg: str):
    if env_flag("VERBOSE", False):
        print(f"[VERBOSE] {msg}")


def run(cmd: list[str]) -> str:
    verbose(f"RUN: {' '.join(cmd)}")
    out = subprocess.check_output(cmd, stderr=subprocess.STDOUT)
    return out.decode("utf-8", errors="replace").strip()


def try_run(cmd: list[str]) -> tuple[bool, str]:
    try:
        return True, run(cmd)
    except subprocess.CalledProcessError as e:
        return False, e.output.decode("utf-8", errors="replace")


def ensure_dirs():
    os.makedirs(REPORTS_DIR, exist_ok=True)


def git_fetch_all():
    # Safe to run even if already up-to-date
    ok, out = try_run(["git", "fetch", "--all", "--prune", "--tags"])
    if not ok:
        print("WARNING: 'git fetch --all --prune' failed. The script may miss remote branches.", file=sys.stderr)
        verbose(out)


def ref_exists(ref: str) -> bool:
    # Verify that ref resolves to a commit
    ok, _ = try_run(["git", "rev-parse", "--verify", "--quiet", f"{ref}^{{commit}}"])
    return ok


def preferred_ref_for_student(username: str) -> tuple[str | None, str]:
    """
    Returns (ref, origin) where ref is the best reference to use for the student branch:
    - local branch '<username>' if exists
    - else remote-tracking 'origin/<username>' if exists
    - else (None, 'origin')
    """
    local_ref = username
    remote_ref = f"origin/{username}"
    if ref_exists(local_ref):
        return local_ref, "origin"
    if ref_exists(remote_ref):
        return remote_ref, "origin"
    return None, "origin"


def list_branch_files(ref: str, path: str) -> list[str]:
    """
    Return *.py file names under `path` from the given ref (branch or remote-tracking).
    """
    ok, out = try_run(["git", "ls-tree", "-r", "--name-only", ref, path])
    if not ok:
        return []
    files = [line.strip().split("/")[-1] for line in out.splitlines()
             if line.strip().lower().endswith(".py")]
    return files


def get_last_commit_iso_for_path(ref: str, file_path: str) -> str | None:
    """
    Return ISO8601 committer timestamp for the last commit that touched file_path in ref.
    """
    ok, out = try_run(["git", "log", "-1", "--format=%cI", ref, "--", file_path])
    if not ok:
        return None
    ts = out.strip()
    return ts or None


def parse_target_date_ist() -> datetime.date:
    """
    Use TARGET_DATE_IST env if provided (YYYYMMDD or YYYY-MM-DD), else yesterday in IST.
    """
    override = os.getenv("TARGET_DATE_IST")
    if override:
        s = override.strip()
        try:
            if re.fullmatch(r"\d{8}", s):
                return datetime.strptime(s, "%Y%m%d").date()
            return datetime.strptime(s, "%Y-%m-%d").date()
        except ValueError:
            print(f"WARNING: Invalid TARGET_DATE_IST={s!r}. Falling back to yesterday IST.", file=sys.stderr)
    now_ist = datetime.now(tz=IST)
    return (now_ist - timedelta(days=1)).date()


def read_students() -> list[dict]:
    students: list[dict] = []
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
                "full_name": (row.get("full_name") or "").strip(),
            })
    return students


def ist_deadline_for_date(d: datetime.date) -> datetime:
    # Deadline: 23:59:59 IST on that date
    return datetime(d.year, d.month, d.day, 23, 59, 59, tzinfo=IST)


def main():
    ensure_dirs()

    # Always fetch branches so remote refs exist (critical on Actions and fresh clones)
    git_fetch_all()

    target_date = parse_target_date_ist()
    yyyymmdd = target_date.strftime("%Y%m%d")
    deadline_ist = ist_deadline_for_date(target_date)

    include_main_fallback = env_flag("INCLUDE_MAIN_FALLBACK", False)
    main_branch = env_str("MAIN_BRANCH_NAME", "main")

    print(f"Generating report for {target_date.isoformat()} IST (deadline {deadline_ist.strftime('%Y-%m-%d %H:%M:%S %Z')})")
    print(f"- INCLUDE_MAIN_FALLBACK = {include_main_fallback}")
    print(f"- MAIN_BRANCH_NAME = {main_branch}")

    students = read_students()

    submitted: list[tuple[str, str, str, str]] = []           # (username, full_name, file_name, commit_time_ist)
    not_submitted: list[tuple[str, str]] = []                  # (username, full_name)
    late: list[tuple[str, str, str, str]] = []                 # (username, full_name, file_name, commit_time_ist)
    naming_issues: list[tuple[str, str, str, str]] = []        # (username, full_name, issue, details)

    for s in students:
        username = s["github_username"]
        full_name = s.get("full_name", "")

        ref, _ = preferred_ref_for_student(username)

        if ref is None:
            # Branch missing: optionally fall back to main to detect merged submissions
            if include_main_fallback and ref_exists(main_branch):
                ref = main_branch
                verbose(f"{username}: no branch found; USING main fallback")
                fallback_mode = True
            else:
                not_submitted.append((username, full_name))
                verbose(f"{username}: no branch or remote-tracking branch found")
                continue
        else:
            fallback_mode = False

        files = list_branch_files(ref, SUBMISSIONS_DIR)

        # Find files matching the target yyyymmdd suffix
        matching = []
        for fn in files:
            m = FILENAME_DATE_RE.match(fn)
            if not m:
                continue
            if m.group("yyyymmdd") == yyyymmdd:
                matching.append(fn)

        if not matching:
            # No file for this date in this ref
            not_submitted.append((username, full_name))
            continue

        # If multiple, pick first for timestamp but flag duplicates
        chosen = sorted(matching)[0]
        if len(matching) > 1:
            naming_issues.append((username, full_name, "MULTIPLE_FILES", ";".join(sorted(matching))))

        # Basic prefix sanity check
        prefix = chosen.rsplit("_", 1)[0]
        if len(prefix) < 3:
            naming_issues.append((username, full_name, "SUSPICIOUS_PREFIX", chosen))

        file_path = f"{SUBMISSIONS_DIR}/{chosen}"
        commit_iso = get_last_commit_iso_for_path(ref, file_path)

        is_late = False
        commit_ist_str = ""
        if commit_iso:
            try:
                # Normalize 'Z' to +00:00 for fromisoformat
                dt = datetime.fromisoformat(commit_iso.replace("Z", "+00:00"))
                commit_ist = dt.astimezone(IST)
                commit_ist_str = commit_ist.isoformat()
                if commit_ist > deadline_ist:
                    is_late = True
            except Exception:
                naming_issues.append((username, full_name, "BAD_COMMIT_TIME", commit_iso or ""))

        submitted.append((username, full_name, chosen, commit_ist_str))

        if is_late:
            late.append((username, full_name, chosen, commit_ist_str))

        # If we had to fall back to main, annotate a warning (merge/squash can skew times)
        if fallback_mode:
            naming_issues.append(
                (username, full_name, "MAIN_FALLBACK_USED",
                 f"{chosen} scanned on {main_branch}; commit time may reflect merge/squash time.")
            )

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

    # Markdown summary
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
            f.write(f"- {label} — `{fn}`{f' — {ctime}' if ctime else ''}\n")

        f.write("\n## Not Submitted\n")
        if not_submitted:
            for u, name in not_submitted:
                label = f"{u} ({name})" if name else u
                f.write(f"- {label}\n")
        else:
            f.write("- None\n")

        f.write("\n## Late Submissions\n")
        if late:
            for u, name, fn, ctime in late:
                label = f"{u} ({name})" if name else u
                f.write(f"- {label} — `{fn}` — {ctime}\n")
        else:
            f.write("- None\n")

        f.write("\n## Naming / Duplicate / Warnings\n")
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