import pytz
import random
import os
from datetime import datetime

# Dynamic content generators
def get_greeting():
    hour = datetime.now().hour
    if 5 <= hour < 12: return "Good morning"
    elif 12 <= hour < 18: return "Good afternoon"
    return "Good evening"

def get_tip():
    tips = [
        "Use git commit --amend to rewrite history",
        "Prefer atomic commits",
        "Review your diffs before pushing",
        "Write meaningful commit messages",
        "Use feature branches for new work",
        "Keep your dependencies updated",
        "Document your code as you write it",
        "Test your code before committing",
        "Use conventional commit messages",
        "Regularly sync your fork with upstream",
        "Write self-documenting code",
        "Use meaningful variable names",
        "Follow the DRY principle",
        "Practice code review regularly",
        "Learn one new technology each month",
        "Contribute to open source projects",
        "Write unit tests for critical functions",
        "Use TypeScript for better type safety",
        "Optimize your development workflow",
        "Stay updated with latest tech trends"
    ]
    return random.choice(tips)

def get_activity():
    # Fetch latest activity from GitHub API (simplified)
    activities = [
        "• Working on new features",
        "• Code review and improvements",
        "• Learning new technologies",
        "• Contributing to open source",
        "• Building side projects",
        "• Writing documentation",
        "• Optimizing performance",
        "• Fixing bugs and issues",
        "• Refactoring legacy code",
        "• Setting up CI/CD pipelines",
        "• Learning advanced React patterns",
        "• Exploring cloud technologies",
        "• Contributing to community projects",
        "• Writing technical blog posts",
        "• Mentoring junior developers",
        "• Attending tech conferences",
        "• Building microservices",
        "• Implementing best practices",
        "• Creating reusable components",
        "• Improving code quality"
    ]
    return random.choice(activities)

def get_quote():
    quotes = [
        "Code is like humor. When you have to explain it, it's bad. - Cory House",
        "Any fool can write code that a computer can understand. Good programmers write code that humans can understand. - Martin Fowler",
        "First, solve the problem. Then, write the code. - John Johnson",
        "Code never lies, comments sometimes do. - Ron Jeffries",
        "It's not a bug – it's an undocumented feature. - Anonymous",
        "The best error message is the one that never shows up. - Thomas Fuchs",
        "Make it work, make it right, make it fast. - Kent Beck",
        "Programming isn't about what you know; it's about what you can figure out. - Chris Pine",
        "The only way to learn a new programming language is by writing programs in it. - Dennis Ritchie",
        "Sometimes it pays to stay in bed on Monday, rather than spending the rest of the week debugging Monday's code. - Dan Salomon"
    ]
    return random.choice(quotes)

# Get the correct paths
script_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.dirname(script_dir)
template_path = os.path.join(project_dir, 'template.md')
readme_path = os.path.join(project_dir, 'README.md')

# Process template
with open(template_path) as f:
    template = f.read()

content = template.replace("{{ greeting }}", get_greeting()) \
                 .replace("{{ date }}", datetime.now().strftime("%Y-%m-%d")) \
                 .replace("{{ time }}", datetime.now(pytz.UTC).strftime("%H:%M")) \
                 .replace("{{ tip }}", get_tip()) \
                 .replace("{{ activity }}", get_activity())

# Write to README.md
with open(readme_path, 'w') as f:
    f.write(content)

print("✅ README updated successfully!")
print(f"📅 Date: {datetime.now().strftime('%Y-%m-%d')}")
print(f"⏰ Time: {datetime.now(pytz.UTC).strftime('%H:%M')} UTC")
print(f"💡 Tip: {get_tip()}")
print(f"🎯 Activity: {get_activity()}")
print(f"💭 Quote: {get_quote()}")