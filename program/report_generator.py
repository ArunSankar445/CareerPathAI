def save_report(role, score, matched, missing, advice, questions):
    """
    Saves a markdown file with skill gap analysis, learning advice, and mock interview questions.
    """

    output_path = "outputs/gap_report.md"

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(f"# 📄 Gap Report for **{role}**\n\n")
        f.write(f"**🧮 Match Score:** `{round(score * 100)}%`\n\n")

        f.write("## ✅ Matched Skills\n")
        if matched:
            for skill in matched:
                f.write(f"- {skill}\n")
        else:
            f.write("- None matched\n")
        f.write("\n")

        f.write("## ❌ Missing Skills\n")
        if missing:
            for skill in missing:
                f.write(f"- {skill}\n")
        else:
            f.write("- None missing\n")
        f.write("\n")

        f.write("## 📚 Learning Advice\n")
        f.write(f"{advice.strip()}\n\n")

        f.write("## 🎤 Mock Interview Questions\n")
        f.write(f"{questions.strip()}\n")

    print(f"📁 Report saved successfully at: {output_path}")
