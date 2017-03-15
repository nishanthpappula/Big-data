import csv  # to read from csv file
import sys  # to exit the program


music=list()                  # to get the ratings given by the current user
with open('music.csv', ) as f:
    reader = csv.reader(f.read().splitlines())
    for row in reader:
        music = row[1:]
        break


input_user_id = input("Enter the id:")  # Take the input from the user

user_ratings = list()        # to get the ratings given by the current user
with open('music.csv') as f:
    reader = csv.reader(f.read().splitlines())
    for row in reader:
        if row[0] == str(input_user_id):
            for i in row[1:]:
                user_ratings.append(int(i))
            break

if user_ratings == []:   # for invalid user id
    sys.exit("user id you entered is invalid")


zero_rating_users=[]  # make a list of all the users who gave 0 as the rating for all
with open('music.csv') as f:
    reader = csv.reader(f.read().splitlines())
    for row in reader:
        flag=1
        for i in row[1:]:
            if i=='1':
                flag=0
                break
        if flag==1:
            zero_rating_users.append(row[0])


distance = dict()  # to find the distance between the current user and other users
with open('music.csv') as f:
    reader = csv.reader(f.read().splitlines())
    for row in reader:
        curr_id = row[0]
        dist = 0
        if row[0] in zero_rating_users:
            distance[curr_id] = 999  # making the distance 999 for users who haven't given any rating because they can't recommend anyway
            continue
        for i in range(1,len(row)):
            if (int(row[i]) ^ user_ratings[i-1]) == 1:
                dist += 1
        distance[curr_id] = dist


count = 0
users = list()
while count < 20:  # to get a list of users who have similar interests to recommend
    m = 999
    _id = input_user_id
    for k, v in distance.items():
        if v < m:
            m = v
            _id = k
    distance[_id] = 999
    users.append(_id)
    count += 1

num = 1
print "Here are the recommendations for the user with user id: "+str(input_user_id)
for user in users:
    with open('music.csv') as f:
        reader = csv.reader(f.read().splitlines())
        for row in reader:
            try:
                if row[0] == user:
                    for rat in range(1, len(row)):
                        if int(row[rat]) == 1 and user_ratings[rat-1] == 0:
                            print str(num)+'. '+music[rat-1]
                            num += 1
                            user_ratings[rat-1] = 1
                        if num == 11:
                            break
                    break
            except ValueError:
                continue
    if num == 11:
        break
f.close()
