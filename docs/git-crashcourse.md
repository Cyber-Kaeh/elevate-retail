# Git and GitHub
[skip to commands](#first-pull)

The first thing we need to know is that Git and GitHub are two totally different things.  
Git is a version control system (VCS) use to track changes in computer files. You first initialize a repository in a folder and now git will keep track of every file that is added, deleted, or modified in that folder. When you `commit` a change Git will keep track of that so you can revert your changes or `merge` your changes with a teammates code or into the projects main codebase.  

This is a vast over-simplification but a good basis to start from as we collabroate on this project. I strongly encourage everyone that reads this to learn Git! Read the docs, watch YouTube, take a course, but most importantly just start using it and making mistakes so you can learn from them!  

Next we look at what GitHub is. Now that we have the basic understanding that Git is just a computer program that helps us track files and keep up with changes, we can probably start to ask questions like; what good is it to keep track of all these changes on my computer if the people I'm working with are using their own computer with all their own files? That's where GitHub comes in.  

GitHub is a web-based platform that allows developers to create, store, manage, and share their code. Git is the program that runs locally on your computer, and GitHub is a cloud service to store all those Git repositories so now developers from any location in the world can collaborate on the same source code. GitHub also offers an incredible suite of other tools, like Codespaces for example!, that help us develop more safely and collaborate more efficiently. I'm a GitHub fan, obviously, but there are also other providers offers a similar service, such as GitLab and Bitbucket to name a few.  

## The Basics

I'm not going to cover all the basics of getting started with Git, though I strongly advise you to learn. This is primarily focused on gettings us all on the same page for working on this project together.

## First Pull

After you have the project cloned on your local machine, or a dev container running you want to make sure that whatever you have is current with the remote repository. *Remote* will come up from time to time when using Git and GitHub, just remember remote is the code that is being stored on GitHub. *Origin* is another important term you will see constantly. Origin refers to the remote repository that the project was orignally cloned from. So instead of saying https://github.com/etc/etc/etc... it is just refered to as origin.  

1. Get everything from the remote repository, including new changes or even branches
```bash
git fetch --all
```
2. Pull in the latest changes. (Latest in terms of your last pull)
```bash
git pull
```
3. Check that status of your repository
```bash
git status
```

If everything looks good then continue coding and making changes. What is really cool about Git is that now at this state in your codebase there a sign-post right here that says, "Everything is OK!". You can go wild and make crazy changes, push your limits trying new things, or whatever you want to do because now you can always revert back to right here. It like a time machine for your code! Just remember you have to make `commits` to put down new sign-posts.

## First Commit

I don't actually recommend you make huge crazy changes to the code. You can, its fine, I just don't recommend it. I think of it like a save point in a video games sometimes. I'm safe right now, the code is working, but I want to change something or try to refactor some code somewhere. It's like knowing the next screen is going to be a boss fight. I might not be able to beat him (i.e. make a successful refactor) but its ok because I can just load back into my save point and try again. Or not, just decide to keep going and I didn't really need that refactor/boss anyway. You could also create a new branch for a scenario where it is a large change, but for now we will stick with commits.  

You have made changes and tested the code. Now you want snapshot of your code in this state.

1. Add any files that have been added

```bash
git add .
```
- Note the . (period) in the `git add` command. This says everything in this current directory.

2. Call git commit with a brief but descriptive message
```bash
git commit -m "<your message here>"

Example:
$ git commit -m "Refactored the getAllUsers() function to use list comprehension"
```

## First Push

Ok, so far we have pulled down the git repo with `git clone <url to repository>` or opened it directly in a devcontainer. Made sure it was up to date with remote, made some changes we like and commited those changes. Now you could exit your container or shut of your laptop or whatever and walk away and those changes have been tracked by Git. You could come back later, make some more changes and commit it again, creating a whole chain of tracked changes. That is awesome, and if you are working alone, on the same machine all the time this would be enough. What about your team though!?  

We want to collaborate on this project which means every time we have a working update to the code we want everyone else to be able to see it and use it. Or, if you have multiple machines you like to work from, like a desktop and a laptop, how are you going to keep those in sync? This is where GitHub starts to shine!  

1. You are done working on a feature, or for the day, or your laptop is about to die and you have to hurry and save where you are so you can pick back up on a different device.
```bash
git push origin <branch>

Example:
$ git push origin development
```

Thats it, one step(s). Super easy, as long as Git doesn't complain about permissions or you didn't miss a step along the way.
Example workflow from start to finish:
```bash
#Just starting for the day
git fetch --all
git pull
# Check status of repo and make sure your on the right branch
git status
# Switch branches if not "development" for example
git checkout development
# Make sure that branch is up to date
git pull origin development
# Done working for now
git add .
git commit -m "Made some great progress on the new feature! Not finished yet though."
git push origin development
```

## Merging & Branching

I will only briefly touch on `merging` branches here because it can be potentially destructive and we should really be using "Pull Requests" for features.  

Let's say you have a working codebase you are happy with. Then you have an idea for some really cool new addition. You don't want to clutter up main branch with constant commits for trying a new thing then putting it back so the program still works. You want a whole new fresh copy of the program you can play around with. You also want to be free to keep making changes to the main codebase, or even try out other new features before this one is finished. It really is like branches in a tree. The trunk(main) is that stable base that doesn't change a whole lot; sturdy, dependable. The branches spread out to allow for new growth.  

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

# Alternatively you can create a branch then manually change to new
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

I included the merging for completeness, or if you are working alone, so please *please* dont ever type the command `git merge` if you are on main... well let's just say ever if working in this repository.  

I only say that because main should be treated like our production code, the single source of truth for the project that has been tested and is ready to be deployed. Collaborating in a group like this there are safety mechanism provided by GitHub to make sure we don't accidently overwrite main, break production, introduce bugs, or any other accidently nastiness that we are all likely to do. Even me. Especially me.  

Pull requests basically just automate the task of creating a new branch then merging it back into main, but GitHub provides additional features and layers of security so that only certain people can approve pull requests.  

There is so so, soooo much more to Git and GitHub, I highly encourage anyone to learn more about it through their extensive documentation or the many free courses available. 

Here is a free course on Microsoft Learn that also prepares you for the GitHub Foundations certification.

[GitHub Foundations]()