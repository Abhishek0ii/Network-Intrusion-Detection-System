import os
import random
from datetime import datetime, timedelta

def random_backup_activity(total_days=176, max_commits_per_day=3):
    today = datetime.now()

    # Choose 176 unique days within the last 180 days
    commit_days = sorted(random.sample(range(180), total_days))

    for day_offset in commit_days:
        commit_date = today - timedelta(days=day_offset)
        commit_base_time = commit_date.replace(hour=9, minute=0)

        # 1 to max_commits_per_day commits for this date
        commits_today = random.randint(1, max_commits_per_day)

        for commit_num in range(commits_today):
            commit_time = commit_base_time + timedelta(minutes=commit_num * 30)
            formatted_time = commit_time.strftime('%Y-%m-%dT%H:%M:%S')

            # Log simulated backup
            with open("backup_log.txt", "a") as f:
                f.write(f"System backup updated at {formatted_time}\n")

            os.system("git add .")
            os.system(f'GIT_AUTHOR_DATE="{formatted_time}" GIT_COMMITTER_DATE="{formatted_time}" git commit -m "Automated system backup - {formatted_time}"')

random_backup_activity()

