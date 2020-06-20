import subprocess


def runCommand(_command):

    commandList = _command.strip().split()
    print(commandList)
    result = subprocess.run(commandList,
                            capture_output=True, text=True)

    print('output: ', result.stdout)


def addRepo():
    print('Adding repo')


def updateRepo():
    runCommand('su projects')
    runCommand('cd')

    # lets us grab repos from gitgub
    runCommand('eval `ssh-agent`')
    runCommand('ssh-add .ssh/id_rsa_gh')

    projectName = input('Name of the project: ')
    runCommand(f'cd {projectName}')

    runCommand('git pull origin master')
