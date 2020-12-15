# this is my first attempt at CICD

This repository sits on AWS CodeCommit!


To clone a repository click on 'Clone URL'.
In the Terminal type 'git clone URL NAME'
Use files on Visual Code
Once you are ready to upload changes


To commit code to CodeCommit
```
'git add .'
'git commit -m "MESSAGE"'
'git push'
```

To update code on your machine
```
git pull
```
another change!

To branch type 
'git checkout -b my-feature'

This will create a new branch on master
You can treat them as separate entities until you are ready to merge


Another item added to this was to trigger a Lambda function to send info to CloudWatch Logs whenever there is a commit. Make sure the Lambda function has access to CodeCommit.

# finish