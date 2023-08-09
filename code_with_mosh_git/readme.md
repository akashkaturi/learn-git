## GIT related

If faced any issue with denied permission delete git credentials in keychain and do ssh again.

```bash
git config --global user.name "Akash Katuri"
git config --global user.email "akashkaturi77@gmail.com"
git config --global core.editor "code --wait" (optional)
git config --global core.autocrlf input (macos)/ true (windows)
git config --global push.default matching
git config --global alias.co checkout
git config --global init.defaultBranch main

git init -b main
git remote add origin https://github.com/akashkaturi/django-crm.git
git add .
git commit -am "initial commit"
git push -u origin main
```

```bash
git config --global -e
```

#Git Ignore
If you add .gitignore file after making the first commit, i.e if you've already pushed the code into the repo.
there is a way to remove the cache files from the staging area, and permanently delete them from getting pushed.

## Here is the command

```bash
git rm --cached -r $(git ls-files -i -c -X .gitignore)
```

git ls-files -i -c -X .gitignore -> This command lists the staged files we would like to remove.
git rm --cached -r -> this will remove the files from the staging area.

# short status

```bash
git status -s
```

# to give differences between staged area and current

```bash
git diff --staged
```

```bash
git config --global diff.tool vscode (setting vscode as visual diff tool)
git config --global difftool.vscode.cmd "code --wait --diff $LOCAL $REMOTE" (check --global -e setting to see local and remote are present)
```

# History

```bash
git log
git log --oneline (short summary of the commits)
git log --oneline --reverse (with oldest commit on the top and latest at the bottom)
```

# Unstaging files

```bash
git restore --staged file1.js
```
# Discarding local changes 

```bash
git restore file1.js --> to discard the local changes of a particular file 
git restore . --> to discard all local changes (it won't be able to remove untracked files.)
git clean -fd --> it will remove all untracked files
```