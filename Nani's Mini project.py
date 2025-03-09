import sys
from collections import deque

# Node class for Linked List operations
class Node:
    def __init__(self, vote):
        self.vote = vote  # vote is a tuple: (voter_id, candidate_id)
        self.next = None

class VotingSystem:
    def __init__(self):
        # Arrays to store registered voters and candidates
        self.voters = []         # Array for voter IDs
        self.candidates = []     # Array for candidate IDs
        
        # Set to ensure each voter votes only once
        self.voted_voters = set()  
        
        # Different data structure representations
        self.votes_stack = []           # Stack (LIFO) of votes stored as tuples
        self.votes_queue = deque()      # Queue (FIFO) of votes stored as tuples
        self.votes_linked_list_head = None  # Head of the linked list of votes
        
        # Dictionary for tallying votes for each candidate
        self.votes_count = {}

    # ----------------- Array Operations -----------------
    def register_voter(self, voter_id):
        """Register a new voter using an array."""
        if voter_id not in self.voters:
            self.voters.append(voter_id)
            print(f"Registered voter '{voter_id}'.")
        else:
            print(f"Voter '{voter_id}' is already registered.")

    def register_candidate(self, candidate_id):
        """Register a new candidate using an array and initialize their vote counter."""
        if candidate_id not in self.candidates:
            self.candidates.append(candidate_id)
            self.votes_count[candidate_id] = 0
            print(f"Registered candidate '{candidate_id}'.")
        else:
            print(f"Candidate '{candidate_id}' is already registered.")

    # ----------------- Stack Operations -----------------
    def cast_vote_stack(self, voter_id, candidate_id):
        """Cast a vote using a stack."""
        if voter_id in self.voted_voters:
            print(f"Voter '{voter_id}' has already voted.")
            return
        if voter_id not in self.voters:
            print(f"Voter '{voter_id}' is not registered.")
            return
        if candidate_id not in self.candidates:
            print(f"Candidate '{candidate_id}' is not registered.")
            return

        # Record the vote in the stack
        self.votes_stack.append((voter_id, candidate_id))
        self.voted_voters.add(voter_id)
        self.votes_count[candidate_id] += 1
        print(f"Voter '{voter_id}' voted for candidate '{candidate_id}' using Stack.")

    # ----------------- Queue Operations -----------------
    def cast_vote_queue(self, voter_id, candidate_id):
        """Cast a vote using a queue."""
        if voter_id in self.voted_voters:
            print(f"Voter '{voter_id}' has already voted.")
            return
        if voter_id not in self.voters:
            print(f"Voter '{voter_id}' is not registered.")
            return
        if candidate_id not in self.candidates:
            print(f"Candidate '{candidate_id}' is not registered.")
            return

        # Record the vote in the queue
        self.votes_queue.append((voter_id, candidate_id))
        self.voted_voters.add(voter_id)
        self.votes_count[candidate_id] += 1
        print(f"Voter '{voter_id}' voted for candidate '{candidate_id}' using Queue.")

    # ----------------- Linked List Operations -----------------
    def cast_vote_linked_list(self, voter_id, candidate_id):
        """Cast a vote using a linked list."""
        if voter_id in self.voted_voters:
            print(f"Voter '{voter_id}' has already voted.")
            return
        if voter_id not in self.voters:
            print(f"Voter '{voter_id}' is not registered.")
            return
        if candidate_id not in self.candidates:
            print(f"Candidate '{candidate_id}' is not registered.")
            return

        # Create a new node for this vote and insert it at the head of the linked list
        new_node = Node((voter_id, candidate_id))
        new_node.next = self.votes_linked_list_head
        self.votes_linked_list_head = new_node
        self.voted_voters.add(voter_id)
        self.votes_count[candidate_id] += 1
        print(f"Voter '{voter_id}' voted for candidate '{candidate_id}' using Linked List.")

    # ----------------- Results Display -----------------
    def display_results(self):
        """Sort candidates by vote count and display the results."""
        print("\nVoting Results:")
        sorted_candidates = sorted(self.candidates, key=lambda c: self.votes_count[c], reverse=True)
        for candidate in sorted_candidates:
            print(f"Candidate '{candidate}': {self.votes_count[candidate]} votes")
        print()

# ----------------- Main loop for continuous, dynamic voting -----------------
def main():
    vs = VotingSystem()

    while True:
        print("\nSelect an option:")
        print("1. Register Voter")
        print("2. Register Candidate")
        print("3. Cast Vote")
        print("4. Display Results")
        print("5. Exit")
        
        choice = input("Enter your choice: ").strip()
        
        if choice == "1":
            voter_id = input("Enter voter ID to register: ").strip()
            vs.register_voter(voter_id)
        elif choice == "2":
            candidate_id = input("Enter candidate ID to register: ").strip()
            vs.register_candidate(candidate_id)
        elif choice == "3":
            voter_id = input("Enter your voter ID: ").strip()
            candidate_id = input("Enter candidate ID to vote for: ").strip()
            
            print("\nChoose the data structure to cast your vote:")
            print("   1. Stack")
            print("   2. Queue")
            print("   3. Linked List")
            ds_choice = input("Enter your choice: ").strip()
            
            if ds_choice == "1":
                vs.cast_vote_stack(voter_id, candidate_id)
            elif ds_choice == "2":
                vs.cast_vote_queue(voter_id, candidate_id)
            elif ds_choice == "3":
                vs.cast_vote_linked_list(voter_id, candidate_id)
            else:
                print("Invalid data structure option. Vote not cast.")
        elif choice == "4":
            vs.display_results()
        elif choice == "5":
            print("Exiting the voting system. Goodbye!")
            break
        else:
            print("Invalid option selected. Please try again.")

if __name__ == "__main__":
    main()