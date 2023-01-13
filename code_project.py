from git import Repo
import datetime



def main(git_dir):
    repo = Repo(git_dir)

    # Get the active branch
    active_branch = repo.active_branch
    print("active branch:",active_branch)

    # Check if repository files have been modified
    changes= repo.is_dirty()
    print("local changes:",changes)

    # Check if the current head commit was authored in the last week
    head_commit = repo.head.commit
    head_commit_date = datetime.datetime.fromtimestamp(head_commit.committed_date)
    last_week = datetime.datetime.now() - datetime.timedelta(weeks=1)
    recent_commit = head_commit_date > last_week
    print("recent commit:",recent_commit)

    # Check if the current head commit was authored by Rufus
    blame_rufus= head_commit.author.name == "Rufus"
    print("blame Rufus:",blame_rufus)


if __name__ == "__main__":
    git_items =('/Users/thanusha/code/pronto-git-project')
    main(git_items)
