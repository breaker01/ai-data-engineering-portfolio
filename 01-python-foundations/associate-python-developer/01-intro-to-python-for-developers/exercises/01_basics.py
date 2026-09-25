"""
Exercise 01: Python Basics & Type Manipulation
Course: Introduction to Python for Developers
"""

def main():
    # 1. Variables and types
    username = "developer_one"
    courses_completed = 0
    progress_ratio = 0.0
    is_certified = False

    print(f"User: {username} | Completed: {courses_completed} | Certified: {is_certified}")

    # 2. String manipulation
    raw_input_email = "   User.Email@Example.COM   "
    cleaned_email = raw_input_email.strip().lower()
    print(f"Cleaned email: {cleaned_email}")

    # 3. Simple list manipulation
    skills = ["python", "git"]
    skills.append("sql")
    print(f"Skills: {skills} (Total: {len(skills)})")


if __name__ == "__main__":
    main()
