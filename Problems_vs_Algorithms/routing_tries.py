# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 16:21:32 2020

@author: 17204
"""

# A RouteTrie will store our routes and their associated handlers
class RouteTrieNode:
    def __init__(self):
        # Initialize the trie with an root node and a handler, this is the root path or home page node
        self.child=dict()
        self.handler=None

    def insert(self, path):
        # Similar to our previous example you will want to recursively add nodes
        # Make sure you assign the handler to only the leaf (deepest) node of this path
        self.child[path] = RouteTrieNode()


# A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
class RouteTrie:
    def __init__(self,handler):
        # Initialize the node with children as before, plus a handler
        self.root = RouteTrieNode()
        self.handler=handler

    def insert(self,path,handler):
        # Insert the node as before
        current=self.root
        for sub_path in path:
      
            current.insert(sub_path)
            current=current.child[sub_path]
            #print(current.children)
        current.handler=handler


    def find(self, path):
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match
        current=self.root
        
        for sub_path in path:

            if sub_path not in current.child:
                return None

            current=current.child[sub_path]
                    
        return current.handler

class Router:
    def __init__(self, handler, handler_if_not_found):
        # Create a new RouteTrie for holding our routes
        # You could also add a handler for 404 page not found responses as well!
        self.root=RouteTrie(handler)
        self.handler=handler
        self.not_found=handler_if_not_found

    def add_handler(self, path, handler):
        # Add a handler for a path
        # You will need to split the path and pass the pass parts
        # as a list to the RouteTrie
        current=self.root

        splitted_path=self.split_path(path)
        current.insert(splitted_path,handler)


    def lookup(self, path):
        # lookup path (by parts) and return the associated handler
        # you can return None if it's not found or
        # return the "not found" handler if you added one
        # bonus points if a path works with and without a trailing slash
        # e.g. /about and /about/ both return the /about handler
        current=self.root
        if path=='/':
          return self.handler
        else:
          search_sub_path=self.split_path(path)

          result=current.find(search_sub_path)

          if result:
            return result
          else:
            return self.not_found

    def split_path(self, path):
        # you need to split the path into parts for 
        # both the add_handler and loopup functions,
        # so it should be placed in a function here
        return path.strip('/').split('/')



# Here are some test cases and expected outputs you can use to test your implementation

# create the router and add a route
router = Router("root handler", "not found handler") # remove the 'not found handler' if you did not implement this
router.add_handler("/home/about", "about handler")  # add a route

# some lookups with the expected output
print(router.lookup("/")) # should print 'root handler'
print(router.lookup("/home")) # should print 'not found handler' or None if you did not implement one
print(router.lookup("/home/about")) # should print 'about handler'
print(router.lookup("/home/about/")) # should print 'about handler' or None if you did not handle trailing slashes
print(router.lookup("/home/about/me")) # should print 'not found handler' or None if you did not implement one



# create the router and add a route
router = Router("root handler", "not found handler") # remove the 'not found handler' if you did not implement this
router.add_handler("/home/company","company handler")  # add a route

# some lookups with the expected output
print(router.lookup("/")) # should print 'root handler'
print(router.lookup("/home")) # should print 'not found handler' or None if you did not implement one
print(router.lookup("/home/company")) # should print 'company handler'
print(router.lookup("/home/company/")) # should print 'company handler' 
print(router.lookup("/home/company/services")) # should print 'not found handler' or None if you did not implement one









