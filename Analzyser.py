def check_files(files):
    score = 100
    problems = []
    if "main.py" not in files:
        problems.append("Missing main file")
        score -= 20
    if "README.md" not in files:
        problems.append("Missing README")
        score -= 20
    return score, problems

def check_readme(text):
    score = 100
    problems = []
    if len(text) < 20:
        problems.append("README too short")
        score -= 20
    return score, problems

def check_commits(commits):
    score = 100
    problems = []
    for commit in commits:
        if len(commit) < 10:
            problems.append("Too short commits")
            score -= 10
        if commit.lower() in ["fix", "asdf", "temp", "update", "update main.py"]:
            problems.append("Useless commit message")
            score -= 15
        if not commit[0].isupper():
            problems.append("Bad formatting")
            score -= 5
    return score, problems

def analyze_repo(files, readme_text, commits):
    total_score = 0
    all_problems = []
    s1, p1 = check_files(files)
    total_score += s1
    all_problems.extend(p1)
    s2, p2 = check_readme(readme_text)
    total_score += s2
    all_problems.extend(p2)
    s3, p3 = check_commits(commits)
    total_score += s3
    all_problems.extend(p3)
    final_score = total_score / 3
    report = ", ".join(all_problems) if all_problems else "All good"
    print(f"Final Score: {final_score}% - Issues: {report}")
    return final_score

files = ["main.py", "README.md"]
readme_text = "# My Awesome Project - This does cool stuff"
commits = ["Added login feature", "Fixed bug in payment", "Updated documentation"]
analyze_repo(files, readme_text, commits)