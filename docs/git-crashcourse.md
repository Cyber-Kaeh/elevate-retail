# Git and GitHub Crash course
[skip to commands](#commands)

The first thing we need to know is that Git and GitHub are two totally different things.  
Git is a version control system (VCS) used to track changes in computer files. You first initialize a repository in a folder, and now Git will keep track of every file added, deleted, or modified in that folder. When you `commit` a change, Git will keep track of that so you can revert your changes or `merge` your changes with a teammate's code or into the project's main codebase.  

This is a vast over-simplification but a good basis for starting as we collaborate on this project. I strongly encourage everyone who reads this to learn Git! Read the docs, watch YouTube, and take a course, but most importantly, start using it and making mistakes so you can learn from them!  

Next, we look at what GitHub is. Now that we have the basic understanding that Git is just a computer program that helps us track files and keep up with changes, we can probably start to ask questions like: what good is it to keep track of all these changes on my computer if the people I'm working with are using their computer with all their own files? That's where GitHub comes in.  

GitHub is a web-based platform that allows developers to create, store, manage, and share their code. Git is a program that runs locally on your computer, and GitHub is a cloud service that stores all those Git repositories. Developers from any location in the world can now collaborate on the same source code. GitHub also offers an incredible suite of other tools, like Codespaces, for example!, that help us develop safely and collaborate more efficiently. I'm a GitHub fan, obviously, but other providers offer similar services, such as GitLab and Bitbucket, to name a few.  

## The Basics

I'm not going to cover all the basics of getting started with Git, though I strongly advise you to learn. This guide will primarily focus on getting everyone on the same page when working on this project together.

## First Pull

After you have the project cloned on your local machine or a dev container running, you want to make sure that whatever you have is current with the remote repository. *Remote* will come up from time to time when using Git and GitHub; just remember that remote is the code that is stored on GitHub. *Origin* is another important term you will see constantly. Origin refers to the remote repository that the project was originally cloned from. So instead of saying https://github.com/etc/etc/etc... it is just referred to as origin.  

1. Get everything from the remote repository, including new changes or even branches
```bash
git fetch --all
```
2. Pull in the latest changes. (Latest in terms of your last pull)
```bash
git pull
```
3. Check the status of your repository
```bash
git status
```

If everything looks good, then continue coding and making changes. What is really cool about Git is that now at this state in your codebase, there is a sign-post right here that says, "Everything is OK!". You can go wild and make crazy changes, push your limits, try new things, or do whatever you want to do because now you can always revert back to right here. It is like a time machine for your code! Just remember you have to make `commits` to put down new sign-posts.

## First Commit

I don't actually recommend that you make huge crazy changes to the code. You can; it's fine; I just don't recommend it. I sometimes think of it as a save point in video games. I'm safe right now, the code is working, but I want to change something or try to refactor some code somewhere. It's like knowing the next screen will be a boss fight. I might not be able to beat him (i.e. make a successful refactor) but it's ok because I can just load back into my save point and try again. Or not, I could just decide to keep going, and I didn't really need that refactor/boss anyway. You could also create a new branch for a scenario where there is a large change, but for now, we will stick with commits.  

You have made changes and tested the code. Now, you want a snapshot of your code in this state.

1. Add any files that have been added

```bash
git add .
```
- Note the . (period) in the `git add` command. This says everything in this current directory.

2. Call Git commit with a brief but descriptive message
```bash
git commit -m "<your message here>"

Example:
$ git commit -m "Refactored the getAllUsers() function to use list comprehension"
```

## First Push

Ok, so far, we have pulled down the git repo with `git clone <url to repository>` or opened it directly in a dev container. Made sure it was up to date with the remote, made some changes we liked, and committed those changes. Now, you could exit your container or shut off your laptop or whatever and walk away, and Git has tracked those changes. You could come back later, make more changes, and commit to them again, creating a whole chain of tracked changes. That is awesome, and if you are working alone on the same machine all the time, this would be enough. What about your team though!?  

We want to collaborate on this project, which means every time we have a working update to the code, we want everyone else to be able to see it and use it. Or, if you have multiple machines you like to work from, like a desktop and a laptop, how are you going to keep those in sync? This is where GitHub starts to shine!  

1. You are done working on a feature, or for the day, or your laptop is about to die and you have to hurry and save where you are so you can pick back up on a different device.
```bash
git push origin <branch>

Example:
$ Git push origin development
```

That's it, one step(s). Super easy, as long as Git doesn't complain about permissions or you didn't miss a step along the way.
Example workflow from start to finish:
```bash
#Just starting for the day
git fetch --all
git pull
# Check status of repo and make sure you're on the right branch
git status
# Switch branches if not "development" for example
git checkout development
# Make sure that branch is up to date
git pull origin development
# Done working for now
git add .
git commit -m "Made some great progress on the new feature! Not finished yet, though."
git push origin development
```

## Merging & Branching

I will only briefly touch on `merging` branches here because it can be potentially destructive, and we should really be using "Pull Requests" for features.  

Let's say you have a working codebase you are happy with. Then you have an idea for some really cool new addition. You don't want to clutter up the main branch with constant commits for trying a new thing and then putting it back so the program still works. You want a whole new, fresh copy of the program you can play around with. You also want to be free to keep changing the main codebase or even try out other new features before this one is finished. It really is like branches in a tree. The trunk(main) is that stable base that doesn't change a whole lot; sturdy, dependable. The branches spread out to allow for new growth.  

Creating a new branch:

1. Always make sure you are up to date
```bash
git fetch --all
```
2. Switch to the branch you want to base the new branch on (probably main)
```bash
git checkout main
```
3. Make sure main is up to date
```bash
git pull origin main
```
4. Create and switch to new branch
```bash
git checkout -b <new-branch-name>

# Alternatively, you can create a branch and then manually change it to a new
git branch <new-branch-name>
git checkout <new-branch-name>

# Example for feature/shopping-cart
git checkout -b feature/shopping-cart

# Or

git branch feature/shopping-cart
git checkout feature/shopping cart
```
5. Make changes on the new branch and test code

6. Commit your changes
```bash
git add .
git commit -m "Added shopping cart feature!"
git push origin feature/shopping-cart
```

7. If working alone, go ahead and merge that feature branch into main
```bash
# Switch to main branch
git checkout main
git pull origin main

# Merge the new feature branch into the main branch
git merge <new-branch-name>
# Example
git merge feature/shopping-cart

# Push the updated main branch
git push origin main
```

## Pull Requests (PR)

I included the merging for completeness, or if you are working alone, so please *please* don't ever type the command `git merge` if you are on main... well, let's just say ever if working in this repository.  

I only say that because main should be treated like our production code, the single source of truth for the project that has been tested and is ready to be deployed. Collaborating in a group like this, there are safety mechanisms provided by GitHub to ensure we don't accidentally overwrite the main, break production, introduce bugs, or any other accidental nastiness that we are all likely to do. Even me. Especially me.  

Pull requests basically just automate the task of creating a new branch and then merging it back into the main, but GitHub provides additional features and layers of security so that only certain people can approve pull requests.  

There is so so, soooo much more to Git and GitHub; I highly encourage anyone to learn more about it through their extensive documentation or the many free courses available. 

Here is a free course on Microsoft Learn that also prepares you for the GitHub Foundations certification.

[GitHub Foundations](https://learn.microsoft.com/en-us/training/paths/github-foundations/)  

## Commands

Here is a quick list of commonly used Git commands:

```bash
# Stay up to date! In this order
git fetch --all
git pull
git pull <branch>
git status

# Change branch
git checkout <branch-name>

# Create branch
git <new-branch-name>

# Create && change to branch
git checkout -b <new-branch-name>

# Track new files
git add <path/to/file/>
git add .  # all files in dir

# Commit changes
git commit -m "commit description"

# Push changes to GitHub
git push origin main
git push origin <branch-name>

# Merge target branch into current branch
git merge <target-branch-name>
```

## <u>Navigation</u>
- [Home](../README.md)
- [Starting the app](./starting_the_app.md)
- [Getting Started](../README.md#getting-started)