import boto3
import json
import sys
class aws_operations:
        
    def user_creation(self):
        abc=int(input("enter how many user want to create="))
        for i in range(1,abc+1):
            print("user ",i)
            username=input("enter user name=")
            def create_user(username):
        
                iam = boto3.client("iam")
                response = iam.create_user(UserName=username)
                print(response)
            create_user(username)

    def attach_policy_to_user(self):
        a2=int(input("enter how many policies you want to attach the iam user="))
        username=input("enter user=")
        for i in range(1,a2+1):
            print("policy ",i)
            policy_arn=input("enter policy ARN=")
            def attach_user_policy(policy_arn):
                iam = boto3.client("iam")
                response = iam.attach_user_policy(
                        UserName=username,
                        PolicyArn=policy_arn
                        ) 
                print(response)
            attach_user_policy(policy_arn=policy_arn)


    def custom_policy(self):
        print("custom policy creation...!" )
        def create_iam_policy():
            iam = boto3.client('iam')

            policy_name=input("enter policy name what want you create=")
            my_managed_policy = eval(input("enter policy structure in json formate="))
            response = iam.create_policy(
                PolicyName=policy_name,
                PolicyDocument=json.dumps(my_managed_policy)
                )
            print(response)

        create_iam_policy()

    def create_group(self,group_name):
        self.group_name=group_name
        iam=boto3.client("iam")
        responce=iam.create_group(GroupName=self.group_name)
        print(responce)

    def attach_policies_to_group(self):
        a=int(input("how many policies you want to attach into group:"))
        group_name=input("enter group name=")
        for i in range(a):
            policy_arn=input("enter policy ARN=")
            def attach_group_policy(policy_arn):
                iam = boto3.client("iam")
                response = iam.attach_group_policy(
                    GroupName=group_name,
                    PolicyArn=policy_arn
                )
                print(response)
            attach_group_policy(policy_arn)

    def add_users_into_existinggroup(self):
        a=int(input("enter how users many you want to add into group:"))
        group_name=input("enter existing Group name=")
        for i in range(1,a+1):
            print("user ",i)
            a1=input("enter user name:")
            def add_user_to_group(a1):
                iam = boto3.client('iam') # IAM low level client object
                response = iam.add_user_to_group(
                        UserName=a1,
                        GroupName=group_name
                    )
                print(response)

            add_user_to_group(a1)



    def list_users(self):
        iam = boto3.client("iam")
        paginator = iam.get_paginator('list_users')
        for response in paginator.paginate():
            for user in response["Users"]:
                print(f"Username: {user['UserName']}, Arn: {user['Arn']}")
    
    def list_groups(self):
        iam = boto3.client("iam")
        paginator = iam.get_paginator('list_groups')
        for response in paginator.paginate():
            for user in response["Groups"]:
                print(f"Groupname: {user['GroupName']}, Arn: {user['Arn']}")
    
    def list_custom_policies(self):
        iam = boto3.client("iam")
        paginator = iam.get_paginator('list_policies')
        for response in paginator.paginate(Scope="Local"):
            for policy in response["Policies"]:
                print(f"Policy Name: {policy['PolicyName']} ARN: {policy['Arn']}")
    
    def list_aws_policies(self):
        iam = boto3.client("iam")
        paginator = iam.get_paginator('list_policies')
        for response in paginator.paginate(Scope="AWS"):
            for policy in response["Policies"]:
                print(f"Policy Name: {policy['PolicyName']} ARN: {policy['Arn']}")

    def remove_user_from_group(self):
        x1=int(input("enter how many users remove from group="))
        group_name=input("enter group name=")
        for i in range(1,x1+1):
            print("user ",i)
            username=input("enter user name to remove=")
            def remove_user_group(username):
                iam = boto3.resource("iam")
                group = iam.Group(group_name)
                response = group.remove_user(
                            UserName=username
                                )

                print(response)
            remove_user_group(username)        
sai=aws_operations()

print("choose the below operations for aws...!")

while True:
    print("options------->Description")
    print("option:=create------>Create Iam User\noption:=CreatePolicy------>Create the custom Policy\noption:=CreateGroup------>create a new group")
    print("option:=Add users to Group------>add the number of users to group")
    print("option:=Remove User------>to remove iam users from group")
    print("option:=AttachPolicy To User------>attach polices to the user\noption:=AttachPolicy to Group------>attached the policies to the existing group")
    print("option:=UsersList------>list out all iam users\noption:=GroupsList------>list out all groups")
    print("option:=CustomPoliciesList1------>list out all iam Custom policies\noption:=Aws Policies List------>list out all aws policies")
    print("Exit------>exit the current program")
    print()
    option=input(("enter your option:\n"))
    option1=option.lower()
    option2=option1.replace(" ","")
    if  option2=="create":   
        sai.user_creation()
        print()
    elif option2=="attachpolicytouser":
        sai.attach_policy_to_user()
        print()
    elif option2=="createpolicy":
        sai.custom_policy()
        print()
    elif option2=="creategroup":
        group_name=input("enter group name what want you create=")
        sai.create_group(group_name)
        print()
    elif option2=="attachpolicytogroup":
        sai.attach_policies_to_group()
        print()
    elif option2=="adduserstogroup":
        sai.add_users_into_existinggroup()
        print()
    elif option2=="userslist":
        sai.list_users()
        print()
    elif option2=="groupslist":
        sai.list_groups()
        print()
    elif option2=="custompolicieslist":
        sai.list_custom_policies()
        print()
    elif option2=="awspolicieslist":
        sai.list_aws_policies()
        print()
    elif option2=='removeuser':
        sai.remove_user_from_group()
        print()
    elif option2=="exit":
        print("Thanks for Using aws Services.")
        sys.exit()
    else:
        print("Wrong option you have entered.Please Enter correct option.")
        print()
