import commands


taskNumber = input('1. Add a new repo, 2. Update a repo:')

if int(taskNumber) == 1:
    commands.addRepo()
elif int(taskNumber) == 2:
    commands.updateRepo()
else:
    print('Invalid input')
