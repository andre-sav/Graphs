import random

class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)

class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME
        
        # Add users
        for i in range(0, num_users):
            self.add_user(f"User {i+1}")

        # Create friendships
        possible_friendships = []

        for user_id in self.users:
            for friend_id in range(user_id+1, self.last_id+1):
                possible_friendships.append((user_id, friend_id))

        random.shuffle(possible_friendships)

        for i in range(num_users * avg_friendships // 2):
            friendship = possible_friendships[i]
            self.add_friendship(friendship[0], friendship[1])

        # * Hint 1: To create N random friendships, you could create a
        # list with all possible friendship combinations, shuffle the
        # list, then grab the first N elements from the list. You will
        # need to `import random` to get shuffle.
        # * Hint 2: `add_friendship(1, 2)` is the same as
        # `add_friendship(2, 1)`. You should avoid calling one after
        # the other since it will do nothing but print a warning. You
        # can avoid this by only creating friendships where user1 < user2.

    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
       
        # !!!! IMPLEMENT ME

        # "shortest" keyword tells us we must go breadth first, hence Queue
        # "extended network" - traversal, connected component

        # planning
        # start at input UID, do breadth first traversal, return path to each friend

        # instantiate queue with user_id as first addition
        qq = Queue()
        qq.enqueue([user_id])

        # while queue is not empty, loop
        while qq.size() > 0:
            # assigns queue - last element to path
            path = qq.dequeue()
            # assigns uid at the end of path to var uid
            uid = path[-1]
            # checks if the current uid has been visited, if not, assigns path as value to uid key in visited dictionary
            if uid not in visited:
                visited[uid] = path
                # loops through edges (friendly neighbors) of current uid 
                for friend in self.friendships[uid]:
                    # checks if given edge has been visited by looking at dict keys
                    if friend not in visited:
                        # if it is not present in our dict, update the path with the edge and enqueue it
                        u_path = path.copy()
                        u_path.append(friend)
                        qq.enqueue(u_path)
        return visited

    def get_all_social_paths_recursive(self, user_id, visited=None, path=None):
        if visited == None:
            visited = {}
        if path == None:
            path = [user_id]
        # base case

        uid = path[-1]
        path.pop()
        if uid not in visited:
            visited[uid] = path
            for friend in self.friendships[uid]:
                if friend not in visited:
                    new_path = list(path)
                    new_path.append(friend)
                    self.get_all_social_paths(uid, visited, new_path)
        



if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(10, 2)
    print(sg.friendships)
    connections = sg.get_all_social_paths(1)
    print(connections)
