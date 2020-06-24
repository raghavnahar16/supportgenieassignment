def agent_available(agents_ls, issue_ls):
    agent_available = False
    for i in range(len(agents_ls)):
        if agents_ls[i][0] == 'True':
            count = 0
            for issue in agents_ls[i][2]:
                if issue in issue_ls:
                    count = count+1

            if count == len(issue_ls):
                agent_available = True
                print("The issue can be presented to %d agent having the details" % (i+1))
                print("Available_since %d" % agents_ls[i][1])

    if not agent_available:
        print("None of the agents are available")


if __name__ == '__main__':
    num = int(input("Mention the number of agents"))
    agents_ls = []
    for i in range(num):
        user_details = []

        is_available = input("Is the agent available or not")
        if is_available == 'no' or is_available == '0' or is_available == 'No':
            user_details.append('False')
        else:
            user_details.append('True')

        available_since = int(input("Give input as 24 hour clock time for availability"))
        user_details.append(available_since)

        num_roles = int(input("Number of roles the agent possess"))
        roles = []
        for j in range(num_roles):
            x = input("Define the roles of the respective agents")
            roles.append(x)
        user_details.append(roles)
        agents_ls.append(user_details)

    mode = input("Enter the agent selection mode i.e. either all_available or least busy or random")

    ''' taking the issues input'''
    
    while(True):
        check = input("Do you want to enter issue(Y/N)?")
        if(check == 'Y' or check == 'y'):
            issue_num = int(input("Enter the number of issues"))
            issue_ls = []
            for i in range(issue_num):
                issue = input("Enter the %d issue "%(i+1))
                issue_ls.append(issue)
            agent_available(agents_ls, issue_ls)
        else:
            break
